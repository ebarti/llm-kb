"""Wiki scanning and heuristic predicate extraction.

Given a wiki directory, yields `nodes` (one per article file) and `edges`
(one per resolved wikilink) with a predicate chosen from:

    cites | mentions | compares | implements | extends
    contradicts | refutes | part_of | instance_of

## Resolution order for each edge's predicate

1. **Frontmatter override (`manual`)** — highest priority. An article may
   declare explicit typed edges in its YAML frontmatter:

        edges:
          - to: "concepts/rag"
            predicate: "extends"
          - to: "entities/openai"
            predicate: "cites"

   These override any heuristic match. Regardless of whether the entries are
   keyed under ``edges:`` or ``manual:``, provenance is logged as
   ``frontmatter:manual``.

2. **Structural frontmatter fields** — `source`, `sources`, `subjects` are
   interpreted as typed:

        source            -> predicate = cites      (provenance='frontmatter:source')
        sources           -> predicate = cites      (provenance='frontmatter:sources')
        subjects          -> predicate = compares   (provenance='frontmatter:subjects')

3. **Heuristic patterns** over the ~50 chars of *left context* immediately
   preceding each `[[link]]` in the body. See `PREDICATE_PATTERNS` below
   for the exact regexes. The first matching pattern wins; patterns are
   ordered from most specific to most generic.

4. **Default** — if nothing matches, the predicate is `mentions` with
   provenance `'default'`.

## Patterns

Each pattern fires when a trigger verb or phrase appears within ~50 chars
BEFORE the wikilink (with the link allowed to carry a display name after
`|`). Matching is case-insensitive. Only the left-context is inspected;
patterns such as "[[X]] is part of Y" where the trigger appears AFTER the
link intentionally fall through to the `mentions` default — this keeps
extraction cheap and predictable. Author-supplied `edges:` / `manual:`
overrides in frontmatter provide an escape hatch when the heuristic
misclassifies a right-context case.

    contradicts  — "contradicts", "disagrees with", "disputes"
    refutes      — "refutes", "debunks", "disproves"
    extends      — "extends", "builds on", "builds upon", "generalizes"
    implements   — "implements", "realizes", "based on the … of"
                   (NB: "based on" on its own is too weak; we require the
                   verb "implements" / "realizes")
    cites        — "cites", "citing", "reference[sd]?", "as shown in",
                   "see also", "per ", "according to"
    compares     — "compares", "compared with", "compared to", "vs\\.", "versus"
    part_of      — "part of", "subset of", "component of", "belongs to"
    instance_of  — "instance of", "example of", "is a …"
                   (the generic "is a" only fires when it directly
                   precedes the link, not mid-sentence)

The default `mentions` covers generic wikilinks and prose references.
"""

from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Iterator, Optional

from .store import PREDICATES


# ---------------------------------------------------------------------- #
#  Wikilink regex
# ---------------------------------------------------------------------- #
# Matches [[target]] or [[target|display]]. Target may contain / and -.
_WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]")


# Directories inside wiki/ that correspond to a node `type`.
_DIR_TYPE_MAP = {
    "concepts": "concept",
    "sources": "source-summary",
    "entities": "entity",
    "comparisons": "comparison",
}


# ---------------------------------------------------------------------- #
#  Heuristic predicate patterns
# ---------------------------------------------------------------------- #
# Each entry is (predicate, compiled_regex). The regex is anchored to
# run against a *left-context* string — the ~50 chars preceding the link.
# The first match (in order) wins.
#
# NOTE: patterns end with `\s*$` when they need to directly precede the
# link; more forgiving patterns use plain `$` (i.e. anywhere in the window).
PREDICATE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    # Most specific: contradicts / refutes — disambiguate carefully.
    ("refutes", re.compile(
        r"\b(refutes?|refuted|debunks?|disproves?)\b[^.?!]*$",
        re.IGNORECASE,
    )),
    ("contradicts", re.compile(
        r"\b(contradicts?|contradicted|disagrees?\s+with|disputes?)\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Intellectual lineage: extends / builds on.
    ("extends", re.compile(
        r"\b(extends?|extended|builds?\s+(?:on|upon)|generali[sz]es?)\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Instantiation / realization.
    ("implements", re.compile(
        r"\b(implements?|implemented|reali[sz]es?|reali[sz]ed|realization\s+of)\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Citations.
    # NB: ``per`` uses a ``(?=\s)`` lookahead so the trailing ``\b`` after
    # the alternation group still anchors on a word boundary — the bare
    # ``per\s+`` form would end in whitespace and the final ``\b`` could
    # never match (no word/non-word transition after the spaces).
    ("cites", re.compile(
        r"\b("
        r"cites?|cited|citing|"
        r"references?|referenced|referencing|"
        r"as\s+shown\s+in|as\s+described\s+in|as\s+noted\s+in|"
        r"see\s+also|"
        r"per(?=\s)|according\s+to"
        r")\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Explicit comparison language.
    ("compares", re.compile(
        r"\b(compares?|compared\s+(?:with|to|against)|versus|vs\.?)\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Part-of relationships.
    ("part_of", re.compile(
        r"\b("
        r"part\s+of|subset\s+of|component\s+of|"
        r"belongs?\s+to|sub-?topic\s+of"
        r")\b[^.?!]*$",
        re.IGNORECASE,
    )),
    # Instance-of / example-of. "is a" alone is too noisy, so we require
    # it to directly precede the link (end-of-window anchor).
    ("instance_of", re.compile(
        r"\b("
        r"instance\s+of|example\s+of|"
        r"(?:is|are)\s+an?\s+(?:kind|type|form|instance|example)\s+of|"
        r"(?:is|are)\s+an?"
        r")\s*$",
        re.IGNORECASE,
    )),
)


WINDOW_CHARS = 50


def _validate_predicate(predicate: str, *, source: str) -> str:
    """Reject predicates outside the canonical graph vocabulary."""
    if predicate not in PREDICATES:
        raise ValueError(
            f"invalid predicate {predicate!r}; expected one of {PREDICATES}; source={source}"
        )
    return predicate


# ---------------------------------------------------------------------- #
#  Frontmatter parsing (minimal, stdlib-only)
# ---------------------------------------------------------------------- #
def _split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body). Either may be empty."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[4:end], text[end + 4:]


def _extract_list(fm_block: str, key: str) -> list[str]:
    """Extract a flow-style YAML list value for `key`, returning wikilink targets.

    Handles both flow style `key: ["[[a]]", "[[b]]"]` and block style:

        key:
          - "[[a]]"
          - "[[b]]"

    Only the wikilink *target* (inside `[[...]]`) is returned, with any
    display-name portion stripped.
    """
    out: list[str] = []
    # Flow style on the same line as the key.
    m = re.search(
        rf"(?m)^{re.escape(key)}\s*:\s*\[(.*?)\]\s*$",
        fm_block,
    )
    if m:
        for raw in re.findall(r'"([^"]*)"|\'([^\']*)\'', m.group(1)):
            token = raw[0] or raw[1]
            if token:
                out.append(token)
    else:
        # Block style: look for lines indented under `key:`.
        block_m = re.search(
            rf"(?m)^{re.escape(key)}\s*:\s*$",
            fm_block,
        )
        if block_m:
            tail = fm_block[block_m.end():]
            for line in tail.splitlines():
                sline = line.strip()
                if not sline:
                    continue
                if not sline.startswith("-"):
                    # First non-indented, non-list line ends the block.
                    break
                token = sline.lstrip("-").strip().strip('"').strip("'")
                if token:
                    out.append(token)

    # Extract just the wikilink target from `[[x|y]]` forms.
    cleaned: list[str] = []
    for token in out:
        wm = re.match(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]\s*$", token.strip())
        cleaned.append(wm.group(1).strip() if wm else token.strip())
    return cleaned


def _split_flow_list(value: str) -> list[str]:
    """Parse a small YAML-ish flow list into scalar strings."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    if not value.strip():
        return []

    out: list[str] = []
    token = ""
    quote = ""
    escape = False
    for ch in value:
        if escape:
            token += ch
            escape = False
            continue
        if ch == "\\" and quote:
            escape = True
            continue
        if quote:
            if ch == quote:
                quote = ""
            else:
                token += ch
            continue
        if ch in ("'", '"'):
            quote = ch
            continue
        if ch == ",":
            item = token.strip()
            if item:
                out.append(item)
            token = ""
            continue
        token += ch
    item = token.strip()
    if item:
        out.append(item)
    return [x.strip().strip('"').strip("'") for x in out if x.strip()]


def _extract_string_list(fm_block: str, key: str) -> list[str]:
    """Extract a scalar/list frontmatter field as plain strings.

    This intentionally supports only the small YAML subset used in wiki
    frontmatter: scalar, flow list, and block list.
    """
    out: list[str] = []
    m = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.*?)\s*$", fm_block)
    if m and m.group(1).strip():
        raw_value = m.group(1).strip()
        if raw_value.startswith("["):
            out.extend(_split_flow_list(raw_value))
        else:
            out.append(raw_value.strip().strip('"').strip("'"))
        return [x for x in out if x]

    block_m = re.search(rf"(?m)^{re.escape(key)}\s*:\s*$", fm_block)
    if not block_m:
        return []
    tail = fm_block[block_m.end():]
    for line in tail.splitlines():
        sline = line.strip()
        if not sline:
            continue
        if not sline.startswith("-"):
            break
        token = sline.lstrip("-").strip().strip('"').strip("'")
        if token:
            out.append(token)
    return out


def _extract_scalar(fm_block: str, key: str) -> str:
    """Extract a single-line scalar field, with quotes stripped."""
    m = re.search(
        rf'(?m)^{re.escape(key)}\s*:\s*(.+?)\s*$',
        fm_block,
    )
    if not m:
        return ""
    val = m.group(1).strip()
    # Strip one layer of quotes.
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        val = val[1:-1]
    # Scalar source may be `"[[raw/foo]]"` — unwrap wikilink.
    wm = re.match(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]\s*$", val)
    return wm.group(1).strip() if wm else val


def _slugify_entity_id(value: str) -> str:
    """Convert a title/path/manual ID into a stable canonical entity ID."""
    raw = _normalise_link(value) or value.strip()
    if raw.startswith("entities/"):
        raw = raw[len("entities/") :]
    raw = raw.rsplit("/", 1)[-1]
    raw = raw.lower()
    raw = re.sub(r"[^a-z0-9]+", "-", raw)
    return raw.strip("-")


def _display_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-") if part)


def _clean_fact_value(value: str) -> str:
    value = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^\]|]+)\]\]", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", value)
    value = re.sub(r"\s+", " ", value).strip(" .;:,")
    # Keep heuristic facts short enough to be useful in generated pages.
    return value[:120].strip(" .;:,")


def _parse_inline_mapping(text: str) -> dict[str, str]:
    """Parse a tiny `{key: value, ...}` frontmatter mapping."""
    body = text.strip()
    if body.startswith("{") and body.endswith("}"):
        body = body[1:-1]
    out: dict[str, str] = {}
    for part in _split_flow_list(body):
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def _extract_fact_overrides(fm_block: str) -> list[dict[str, str]]:
    """Extract manual facts from frontmatter.

    Supported forms:

        facts:
          - {attribute: "role", value: "AI educator"}
          - attribute: affiliation
            value: OpenAI
          - role: AI educator
    """
    block_m = re.search(r"(?m)^facts\s*:\s*$", fm_block)
    if not block_m:
        return []

    entries: list[dict[str, str]] = []
    pending: dict[str, str] = {}
    tail = fm_block[block_m.end():]
    for line in tail.splitlines():
        sline = line.rstrip()
        if not sline:
            continue
        if not (sline.startswith("  ") or sline.startswith("\t") or sline.lstrip().startswith("-")):
            break
        stripped = sline.strip()
        if stripped.startswith("- "):
            if pending:
                entries.append(pending)
                pending = {}
            body = stripped[2:].strip()
            if body.startswith("{"):
                entries.append(_parse_inline_mapping(body))
                continue
            if ":" in body:
                key, value = body.split(":", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key in {"attribute", "value", "source"}:
                    pending[key] = value
                else:
                    entries.append({"attribute": key, "value": value})
                continue
        elif ":" in stripped:
            key, value = stripped.split(":", 1)
            pending[key.strip()] = value.strip().strip('"').strip("'")
    if pending:
        entries.append(pending)

    clean: list[dict[str, str]] = []
    for entry in entries:
        attr = entry.get("attribute", "").strip()
        value = entry.get("value", "").strip()
        source = entry.get("source", "").strip()
        if attr and value:
            clean.append({"attribute": attr, "value": value, "source": source})
    return clean


def _extract_edges_override(fm_block: str) -> list[dict]:
    """Parse explicit edge overrides from frontmatter.

    Supports both ``edges:`` and ``manual:`` as top-level keys. Each entry
    may be either:

        - {to: "concepts/rag", predicate: "extends"}
        - "concepts/rag:extends"           # shorthand

    Returns a list of dicts with keys `to`, `predicate`.
    """
    overrides: list[dict] = []
    for key in ("edges", "manual"):
        block_m = re.search(rf"(?m)^{key}\s*:\s*$", fm_block)
        if not block_m:
            continue
        tail = fm_block[block_m.end():]
        pending: dict[str, str] = {}
        for line in tail.splitlines():
            sline = line.rstrip()
            if not sline:
                # Empty line inside the block is tolerated.
                continue
            if not (sline.startswith("  ") or sline.startswith("\t") or sline.lstrip().startswith("-")):
                # De-indented — the block is over.
                break
            stripped = sline.strip()
            if stripped.startswith("- "):
                # Flush any pending dict from the previous `-`.
                if pending:
                    overrides.append(pending)
                    pending = {}
                body = stripped[2:].strip()
                # Inline object: - {to: "x", predicate: "y"}
                inline = re.match(
                    r"\{\s*to\s*:\s*\"?([^\",]+)\"?\s*,\s*predicate\s*:\s*\"?([^\"}\s]+)\"?\s*\}",
                    body,
                )
                if inline:
                    overrides.append({
                        "to": inline.group(1).strip(),
                        "predicate": inline.group(2).strip(),
                        "_source_key": key,
                    })
                    continue
                # Shorthand: - concepts/rag:extends
                short = re.match(r"\"?([^\":]+)\"?\s*:\s*([a-z_]+)\s*$", body)
                if short:
                    overrides.append({
                        "to": short.group(1).strip(),
                        "predicate": short.group(2).strip(),
                        "_source_key": key,
                    })
                    continue
                # Opens a key: value block (e.g. `- to: concepts/rag`).
                # Process remainder of the line as a key: value pair.
                kv = re.match(r"(\w+)\s*:\s*\"?([^\"]*?)\"?\s*$", body)
                if kv:
                    pending["_source_key"] = key
                    pending[kv.group(1)] = kv.group(2).strip()
                continue
            # Continuation lines inside an active `- ` entry.
            kv = re.match(r"(\w+)\s*:\s*\"?([^\"]*?)\"?\s*$", stripped)
            if kv:
                pending.setdefault("_source_key", key)
                pending[kv.group(1)] = kv.group(2).strip()
        if pending:
            overrides.append(pending)

    # Keep only valid-looking entries.
    clean: list[dict] = []
    for o in overrides:
        to = o.get("to", "").strip()
        pred = o.get("predicate", "").strip()
        source_key = o.get("_source_key", "manual").strip() or "manual"
        # Unwrap wikilink in `to`.
        wm = re.match(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]\s*$", to)
        if wm:
            to = wm.group(1).strip()
        if to and pred:
            clean.append({
                "to": to,
                "predicate": _validate_predicate(
                    pred,
                    source=f"frontmatter:{source_key}",
                ),
            })
    return clean


# ---------------------------------------------------------------------- #
#  Core extraction
# ---------------------------------------------------------------------- #
@dataclass
class Node:
    id: str
    type: str = ""
    title: str = ""
    path: str = ""
    summary: str = ""


@dataclass
class Edge:
    src: str
    dst: str
    predicate: str
    provenance: str = ""


@dataclass
class EntityAlias:
    canonical_id: str
    alias: str


@dataclass
class Fact:
    entity_id: str
    attribute: str
    value: str
    source: str


@dataclass
class GraphExtraction:
    nodes: list[Node]
    edges: list[Edge]
    entity_aliases: list[EntityAlias]
    facts: list[Fact]


def _normalise_link(target: str) -> Optional[str]:
    """Normalise a wikilink target to a canonical node id, or None to skip."""
    if not target:
        return None
    t = target.strip()
    # Strip ".md" if someone wrote [[concepts/rag.md]].
    if t.endswith(".md"):
        t = t[:-3]
    # Obsidian allows `wiki/concepts/rag` — normalise.
    if t.startswith("wiki/"):
        t = t[5:]
    # Ignore in-article anchors: [[#Heading]] or [[page#Section]].
    t = t.split("#", 1)[0].strip()
    if not t:
        return None
    return t


def detect_predicate(left_context: str) -> tuple[str, str]:
    """Choose a predicate for a wikilink based on its left context.

    Returns (predicate, provenance). Provenance is either
    `"heuristic:<predicate>"` or `"default"` for the fallback.

    `left_context` should be up to WINDOW_CHARS of text immediately
    preceding the `[[`.
    """
    window = left_context[-WINDOW_CHARS:] if left_context else ""
    for predicate, pattern in PREDICATE_PATTERNS:
        if pattern.search(window):
            return predicate, f"heuristic:{predicate}"
    return "mentions", "default"


def iter_wiki_files(wiki_dir: Path) -> Iterator[Path]:
    """Yield markdown files that should be treated as graph nodes.

    Skips `_meta/`, `_index.md`, `log.md`, and anything starting with `_`.
    """
    for path in sorted(wiki_dir.rglob("*.md"), key=lambda p: p.as_posix()):
        rel = path.relative_to(wiki_dir)
        # Skip meta paths.
        top = rel.parts[0]
        if top.startswith("_"):
            continue
        name = rel.stem
        if name in ("log", "_index"):
            continue
        if name.startswith("_"):
            continue
        # Top-level files like Changelog.md / Dashboard.md are allowed so
        # that hub pages can still participate, but their type is 'meta'.
        yield path


# Backward-compatible alias for any internal callers still using the old name.
_iter_wiki_files = iter_wiki_files


def _node_from_file(path: Path, wiki_dir: Path) -> tuple[Node, str, str]:
    """Return (Node, frontmatter_block, body) for a wiki file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm_block, body = _split_frontmatter(text)
    rel = path.relative_to(wiki_dir)
    node_id = str(rel).replace("\\", "/")[:-3]  # strip ".md"
    parent = rel.parts[0] if len(rel.parts) > 1 else ""
    node_type = (
        _extract_scalar(fm_block, "type")
        or _DIR_TYPE_MAP.get(parent, "meta" if not parent else parent)
    )
    title = _extract_scalar(fm_block, "title") or rel.stem
    summary = _extract_scalar(fm_block, "summary")
    return (
        Node(
            id=node_id,
            type=node_type,
            title=title,
            path=str(path),
            summary=summary,
        ),
        fm_block,
        body,
    )


def _add_raw_node(
    raw_id: str, raw_dir: Path, nodes: dict[str, Node]
) -> None:
    """Register a `raw/<slug>` node if the file exists and it's not yet recorded."""
    if raw_id in nodes:
        return
    slug = raw_id[len("raw/") :]
    raw_file = raw_dir / f"{slug}.md"
    title = slug.replace("-", " ")
    path = ""
    summary = ""
    if raw_file.exists():
        text = raw_file.read_text(encoding="utf-8", errors="replace")
        fm_block, _ = _split_frontmatter(text)
        title = _extract_scalar(fm_block, "title") or title
        summary = _extract_scalar(fm_block, "summary")
        path = str(raw_file)
    nodes[raw_id] = Node(
        id=raw_id, type="raw", title=title, path=path, summary=summary
    )


def _source_ref(node_id: str, provenance: str) -> str:
    return f"{node_id}#{provenance}" if provenance else node_id


def _is_graph_generated_frontmatter(fm_block: str) -> bool:
    return _extract_scalar(fm_block, "generated_by") == "graph"


def _canonical_entity_id(node: Node, fm_block: str) -> str:
    manual = _extract_scalar(fm_block, "canonical_id")
    if manual:
        return _slugify_entity_id(manual)
    if node.id.startswith("entities/"):
        return _slugify_entity_id(node.id[len("entities/") :])
    return _slugify_entity_id(node.id)


def _entity_aliases_for(
    node: Node,
    fm_block: str,
    canonical_id: str,
) -> list[EntityAlias]:
    raw_aliases = [
        canonical_id,
        _display_from_slug(canonical_id),
        node.title,
        _display_from_slug(node.id.rsplit("/", 1)[-1]),
    ]
    raw_aliases.extend(_extract_string_list(fm_block, "alias"))
    raw_aliases.extend(_extract_string_list(fm_block, "aliases"))

    entity_type = _extract_scalar(fm_block, "entity_type").lower()
    if entity_type == "person":
        title_bits = [x for x in re.split(r"\s+", node.title.strip()) if x]
        if len(title_bits) > 1:
            raw_aliases.append(title_bits[-1])

    aliases: list[EntityAlias] = []
    seen: set[str] = set()
    for alias in raw_aliases:
        clean = _clean_fact_value(alias)
        if not clean:
            continue
        if clean in seen:
            continue
        seen.add(clean)
        aliases.append(EntityAlias(canonical_id=canonical_id, alias=clean))
    return aliases


def _entity_facts_for(
    node: Node,
    fm_block: str,
    canonical_id: str,
) -> list[Fact]:
    facts: list[Fact] = []

    def add(attribute: str, value: str, provenance: str) -> None:
        clean = _clean_fact_value(value)
        if clean:
            facts.append(Fact(
                entity_id=canonical_id,
                attribute=attribute,
                value=clean,
                source=_source_ref(node.id, provenance),
            ))

    add("name", node.title, "frontmatter:title")
    for key in (
        "entity_type",
        "summary",
        "role",
        "affiliation",
        "url",
        "website",
        "notable_for",
    ):
        value = _extract_scalar(fm_block, key)
        if value:
            add(key, value, f"frontmatter:{key}")

    for entry in _extract_fact_overrides(fm_block):
        source = entry.get("source") or f"frontmatter:facts:{entry['attribute']}"
        add(entry["attribute"], entry["value"], source)

    return facts


def _resolve_entity_target(
    target: str,
    entity_node_to_canonical: dict[str, str],
) -> str:
    if target.startswith("entities/"):
        canonical = entity_node_to_canonical.get(target)
        if canonical:
            return f"entities/{canonical}"
        return f"entities/{_slugify_entity_id(target)}"
    return target


def _ensure_canonical_entity_nodes(
    wiki_dir: Path,
    nodes: dict[str, Node],
    aliases: Iterable[EntityAlias],
    facts: Iterable[Fact],
) -> None:
    titles: dict[str, str] = {}
    summaries: dict[str, str] = {}
    for fact in facts:
        if fact.attribute == "name":
            titles.setdefault(fact.entity_id, fact.value)
        elif fact.attribute == "summary":
            summaries.setdefault(fact.entity_id, fact.value)
    for alias in aliases:
        titles.setdefault(alias.canonical_id, alias.alias)

    for canonical_id in sorted(titles):
        node_id = f"entities/{canonical_id}"
        existing = nodes.get(node_id)
        title = titles.get(canonical_id) or _display_from_slug(canonical_id)
        summary = summaries.get(canonical_id) or f"Entity profile for {title}."
        path = str(wiki_dir / "entities" / f"{canonical_id}.md")
        if existing is None:
            nodes[node_id] = Node(
                id=node_id,
                type="entity",
                title=title,
                path=path,
                summary=summary,
            )
        else:
            existing.type = existing.type or "entity"
            existing.title = existing.title or title
            existing.path = existing.path or path
            existing.summary = existing.summary or summary


def _sentence_around(text: str, start: int, end: int) -> str:
    left = max(text.rfind(".", 0, start), text.rfind("\n", 0, start))
    right_dot = text.find(".", end)
    right_newline = text.find("\n", end)
    candidates = [x for x in (right_dot, right_newline) if x != -1]
    right = min(candidates) if candidates else len(text)
    return text[left + 1:right]


def _extract_mention_attribute_facts(
    sentence: str,
    alias: str,
    canonical_id: str,
    source_ref: str,
) -> list[Fact]:
    facts: list[Fact] = []
    escaped = re.escape(alias)
    patterns = [
        (
            re.compile(
                rf"\b{escaped}\b\s+(?:is|was)\s+(?:an?\s+|the\s+)?"
                rf"(?P<role>[A-Za-z][^.,;\n]{{2,80}}?)\s+"
                rf"(?:at|with|for)\s+(?P<affiliation>[A-Z][A-Za-z0-9&.' -]{{1,80}})",
                re.IGNORECASE,
            ),
            ("role", "affiliation"),
        ),
        (
            re.compile(
                rf"\b{escaped}\b\s+(?:is|was)\s+(?:an?\s+|the\s+)?"
                rf"(?P<role>[A-Za-z][^.,;\n]{{2,80}})",
                re.IGNORECASE,
            ),
            ("role",),
        ),
        (
            re.compile(
                rf"\b{escaped}\b\s+(?:works|worked)\s+(?:at|for)\s+"
                rf"(?P<affiliation>[A-Z][A-Za-z0-9&.' -]{{1,80}})",
                re.IGNORECASE,
            ),
            ("affiliation",),
        ),
        (
            re.compile(
                rf"\b{escaped}\b\s+(?:is|was)\s+affiliated\s+with\s+"
                rf"(?P<affiliation>[A-Z][A-Za-z0-9&.' -]{{1,80}})",
                re.IGNORECASE,
            ),
            ("affiliation",),
        ),
    ]
    for pattern, attributes in patterns:
        match = pattern.search(sentence)
        if not match:
            continue
        for attribute in attributes:
            value = _clean_fact_value(match.group(attribute))
            if value:
                facts.append(Fact(
                    entity_id=canonical_id,
                    attribute=attribute,
                    value=value,
                    source=source_ref,
                ))
        break
    return facts


def _dedupe_nodes(nodes: Iterable[Node]) -> list[Node]:
    return sorted(nodes, key=lambda n: n.id)


def _dedupe_edges(edges: Iterable[Edge]) -> list[Edge]:
    seen: dict[tuple[str, str, str], Edge] = {}
    for edge in edges:
        seen[(edge.src, edge.dst, edge.predicate)] = edge
    return sorted(seen.values(), key=lambda e: (e.src, e.predicate, e.dst))


def _dedupe_aliases(aliases: Iterable[EntityAlias]) -> list[EntityAlias]:
    seen: dict[str, EntityAlias] = {}
    for alias in aliases:
        if alias.canonical_id and alias.alias:
            seen[alias.alias] = alias
    return sorted(
        seen.values(),
        key=lambda a: (a.canonical_id, a.alias.casefold(), a.alias),
    )


def _dedupe_facts(facts: Iterable[Fact]) -> list[Fact]:
    seen: dict[tuple[str, str, str, str], Fact] = {}
    for fact in facts:
        key = (fact.entity_id, fact.attribute, fact.value, fact.source)
        if all(key):
            seen[key] = fact
    return sorted(
        seen.values(),
        key=lambda f: (f.entity_id, f.attribute, f.value, f.source),
    )


def extract_graph(
    wiki_dir: str | Path,
    raw_dir: Optional[str | Path] = None,
) -> GraphExtraction:
    """Walk the wiki and return typed graph rows plus entity facts.

    Edge resolution:

    1. Frontmatter ``edges:`` / ``manual:`` override everything.
    2. Frontmatter list fields (``source``, ``sources``, ``subjects``) map to
       ``cites`` (for sources) and ``compares`` (for subjects).
    3. Body wikilinks are classified by heuristic, defaulting to ``mentions``.

    Edges whose target doesn't resolve to an existing node are still emitted
    (so that dangling links are visible in the graph) — but only if the
    target is well-formed. Targets under `raw/` are auto-added as nodes of
    type `raw` when the file exists on disk.

    Entity pages seed alias and fact rows. References to entity pages are
    normalized to ``entities/<canonical_id>``; bare alias mentions in
    non-entity articles also emit ``mentions`` edges and mention facts.
    """
    wiki_dir = Path(wiki_dir).resolve()
    raw_dir = Path(raw_dir).resolve() if raw_dir else wiki_dir.parent / "raw"

    nodes: dict[str, Node] = {}
    edges: list[Edge] = []
    entity_aliases: list[EntityAlias] = []
    facts: list[Fact] = []
    entity_node_to_canonical: dict[str, str] = {}
    # Pass 1: collect all nodes so self-links and cross-refs resolve.
    files = list(iter_wiki_files(wiki_dir))
    parsed: dict[str, tuple[Node, str, str]] = {}
    for path in files:
        node, fm_block, body = _node_from_file(path, wiki_dir)
        parsed[node.id] = (node, fm_block, body)
        nodes[node.id] = node
        if (
            node.id.startswith("entities/")
            and not _is_graph_generated_frontmatter(fm_block)
        ):
            canonical_id = _canonical_entity_id(node, fm_block)
            if canonical_id:
                entity_node_to_canonical[node.id] = canonical_id
                entity_node_to_canonical[f"entities/{canonical_id}"] = canonical_id
                entity_aliases.extend(
                    _entity_aliases_for(node, fm_block, canonical_id)
                )
                facts.extend(_entity_facts_for(node, fm_block, canonical_id))

    _ensure_canonical_entity_nodes(wiki_dir, nodes, entity_aliases, facts)

    alias_patterns = sorted(
        (
            (alias, canonical_id)
            for alias, canonical_id in (
                (a.alias, a.canonical_id) for a in _dedupe_aliases(entity_aliases)
            )
            if len(alias) >= 3
        ),
        key=lambda item: (-len(item[0]), item[0].casefold(), item[1]),
    )

    # Pass 2: emit edges.
    for node_id, (node, fm_block, body) in parsed.items():
        if (
            node.id.startswith("entities/")
            and _is_graph_generated_frontmatter(fm_block)
        ):
            continue

        # --- 1. Manual / edges frontmatter overrides ---
        override_keys: set[tuple[str, str]] = set()
        for entry in _extract_edges_override(fm_block):
            target = _normalise_link(entry["to"])
            pred = entry["predicate"]
            if not target or target == node_id:
                continue
            target = _resolve_entity_target(target, entity_node_to_canonical)
            if target.startswith("raw/"):
                _add_raw_node(target, raw_dir, nodes)
            edges.append(Edge(
                src=node_id,
                dst=target,
                predicate=pred,
                provenance="frontmatter:manual",
            ))
            override_keys.add((target, pred))
        # --- 2. Structural frontmatter lists ---
        # `source` (scalar) and `sources` (list) both imply `cites`.
        scalar_source = _extract_scalar(fm_block, "source")
        if scalar_source:
            target = _normalise_link(scalar_source)
            if target and target != node_id:
                target = _resolve_entity_target(target, entity_node_to_canonical)
                if target.startswith("raw/"):
                    _add_raw_node(target, raw_dir, nodes)
                if (target, "cites") not in override_keys:
                    edges.append(Edge(
                        src=node_id,
                        dst=target,
                        predicate="cites",
                        provenance="frontmatter:source",
                    ))

        for t in _extract_list(fm_block, "sources"):
            target = _normalise_link(t)
            if not target or target == node_id:
                continue
            target = _resolve_entity_target(target, entity_node_to_canonical)
            if target.startswith("raw/"):
                _add_raw_node(target, raw_dir, nodes)
            if (target, "cites") not in override_keys:
                edges.append(Edge(
                    src=node_id,
                    dst=target,
                    predicate="cites",
                    provenance="frontmatter:sources",
                ))

        for t in _extract_list(fm_block, "subjects"):
            target = _normalise_link(t)
            if not target or target == node_id:
                continue
            target = _resolve_entity_target(target, entity_node_to_canonical)
            if (target, "compares") not in override_keys:
                edges.append(Edge(
                    src=node_id,
                    dst=target,
                    predicate="compares",
                    provenance="frontmatter:subjects",
                ))

        # --- 3. Body wikilinks with heuristic predicates ---
        for m in _WIKILINK_RE.finditer(body):
            target = _normalise_link(m.group(1))
            if not target or target == node_id:
                continue
            original_target = target
            target = _resolve_entity_target(target, entity_node_to_canonical)
            if target.startswith("raw/"):
                _add_raw_node(target, raw_dir, nodes)
            left = body[max(0, m.start() - WINDOW_CHARS): m.start()]
            predicate, provenance = detect_predicate(left)
            if (target, predicate) not in override_keys:
                edges.append(Edge(
                    src=node_id,
                    dst=target,
                    predicate=predicate,
                    provenance=provenance,
                ))
            if original_target.startswith("entities/"):
                canonical_id = target[len("entities/") :]
                alias = m.group(2) or m.group(1).rsplit("/", 1)[-1]
                facts.append(Fact(
                    entity_id=canonical_id,
                    attribute="mention",
                    value=_clean_fact_value(alias),
                    source=_source_ref(node_id, "wikilink"),
                ))

        # --- 4. Bare alias mentions in non-entity articles ---
        if node.type != "entity":
            seen_mentions: set[tuple[str, str]] = set()
            for alias, canonical_id in alias_patterns:
                pattern = re.compile(
                    rf"(?<![A-Za-z0-9_/-]){re.escape(alias)}(?![A-Za-z0-9_/-])",
                    re.IGNORECASE,
                )
                for match in pattern.finditer(body):
                    mention_key = (canonical_id, alias.casefold())
                    if mention_key in seen_mentions:
                        continue
                    seen_mentions.add(mention_key)
                    dst = f"entities/{canonical_id}"
                    edges.append(Edge(
                        src=node_id,
                        dst=dst,
                        predicate="mentions",
                        provenance=f"entity_mention:{alias}",
                    ))
                    source = _source_ref(node_id, f"mention:{alias}")
                    facts.append(Fact(
                        entity_id=canonical_id,
                        attribute="mention",
                        value=body[match.start():match.end()],
                        source=source,
                    ))
                    sentence = _sentence_around(body, match.start(), match.end())
                    facts.extend(
                        _extract_mention_attribute_facts(
                            sentence,
                            body[match.start():match.end()],
                            canonical_id,
                            source,
                        )
                    )

    return GraphExtraction(
        nodes=_dedupe_nodes(nodes.values()),
        edges=_dedupe_edges(edges),
        entity_aliases=_dedupe_aliases(entity_aliases),
        facts=_dedupe_facts(facts),
    )


def extract_nodes_and_edges(
    wiki_dir: str | Path,
    raw_dir: Optional[str | Path] = None,
) -> tuple[list[Node], list[Edge]]:
    """Backward-compatible typed node/edge extraction API."""
    result = extract_graph(wiki_dir, raw_dir=raw_dir)
    return result.nodes, result.edges


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _source_article(source: str) -> tuple[str, str]:
    article, sep, provenance = source.partition("#")
    return article, provenance if sep else ""


def _is_generated_entity_page(path: Path) -> bool:
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    fm_block, _ = _split_frontmatter(text)
    return _extract_scalar(fm_block, "generated_by") == "graph"


def _facts_by_entity(facts: Iterable[Fact]) -> dict[str, list[Fact]]:
    grouped: dict[str, list[Fact]] = {}
    for fact in facts:
        grouped.setdefault(fact.entity_id, []).append(fact)
    for entity_id in grouped:
        grouped[entity_id] = sorted(
            grouped[entity_id],
            key=lambda f: (f.attribute, f.value, f.source),
        )
    return grouped


def _aliases_by_entity(aliases: Iterable[EntityAlias]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for alias in aliases:
        grouped.setdefault(alias.canonical_id, []).append(alias.alias)
    for entity_id, values in grouped.items():
        deduped = sorted(set(values), key=lambda x: (x.casefold(), x))
        grouped[entity_id] = deduped
    return grouped


def _first_fact(facts: list[Fact], attribute: str) -> str:
    for fact in facts:
        if fact.attribute == attribute:
            return fact.value
    return ""


def _render_entity_page(
    canonical_id: str,
    aliases: list[str],
    facts: list[Fact],
    today: str,
) -> str:
    title = _first_fact(facts, "name") or (aliases[0] if aliases else "")
    if not title:
        title = _display_from_slug(canonical_id)
    entity_type = _first_fact(facts, "entity_type") or "unknown"
    summary = (
        _first_fact(facts, "summary")
        or f"Auto-generated entity profile for {title}."
    )

    aliases = sorted(set([canonical_id, *aliases]), key=lambda x: (x.casefold(), x))
    alias_yaml = "[" + ", ".join(_yaml_quote(a) for a in aliases) + "]"

    lines = [
        "---",
        f"title: {_yaml_quote(title)}",
        "type: entity",
        f"entity_type: {_yaml_quote(entity_type)}",
        f"canonical_id: {_yaml_quote(canonical_id)}",
        f"aliases: {alias_yaml}",
        "generated_by: graph",
        f"last_compiled: {today}",
        f"summary: {_yaml_quote(summary)}",
        "---",
        "",
        "## Overview",
        "",
        summary,
        "",
        "## Key Facts",
        "",
    ]

    excluded = {"name", "entity_type", "summary", "mention"}
    fact_rows = [f for f in facts if f.attribute not in excluded]
    if fact_rows:
        lines.extend([
            "| Attribute | Value | Source |",
            "|-----------|-------|--------|",
        ])
        for fact in fact_rows:
            article, provenance = _source_article(fact.source)
            source_link = f"[[{article}]]"
            source_text = (
                f"{source_link} ({provenance})" if provenance else source_link
            )
            lines.append(
                f"| {fact.attribute} | {fact.value} | {source_text} |"
            )
    else:
        lines.append("- No attributes recorded yet.")

    lines.extend(["", "## Mentions", ""])
    mention_rows = [f for f in facts if f.attribute == "mention"]
    if mention_rows:
        seen: set[tuple[str, str, str]] = set()
        for fact in mention_rows:
            article, provenance = _source_article(fact.source)
            key = (article, fact.value, provenance)
            if key in seen:
                continue
            seen.add(key)
            suffix = f" ({provenance})" if provenance else ""
            lines.append(f"- [[{article}]] - {fact.value}{suffix}")
    else:
        lines.append("- No source mentions recorded yet.")

    lines.append("")
    return "\n".join(lines)


def rebuild_entity_pages(
    wiki_dir: str | Path,
    extraction: GraphExtraction,
    *,
    today: str | None = None,
) -> list[Path]:
    """Create/update graph-generated canonical entity pages.

    Existing hand-authored pages are not overwritten. A page is considered
    graph-owned only when its frontmatter has ``generated_by: graph``.
    """
    wiki_dir = Path(wiki_dir).resolve()
    entities_dir = wiki_dir / "entities"
    if not wiki_dir.exists() or not wiki_dir.is_dir():
        return []

    today_value = today or os.environ.get("KB_TODAY") or date.today().isoformat()
    aliases = _aliases_by_entity(extraction.entity_aliases)
    facts = _facts_by_entity(extraction.facts)
    entity_ids = sorted(set(aliases) | set(facts))
    written: list[Path] = []

    for canonical_id in entity_ids:
        page = entities_dir / f"{canonical_id}.md"
        if not _is_generated_entity_page(page):
            continue
        content = _render_entity_page(
            canonical_id,
            aliases.get(canonical_id, []),
            facts.get(canonical_id, []),
            today_value,
        )
        page.parent.mkdir(parents=True, exist_ok=True)
        old = page.read_text(encoding="utf-8") if page.exists() else None
        if old != content:
            page.write_text(content, encoding="utf-8")
            written.append(page)
    return written


# ---------------------------------------------------------------------- #
#  Convenience
# ---------------------------------------------------------------------- #
def fingerprint(nodes: list[Node], edges: list[Edge]) -> str:
    """Stable hash of nodes+edges — useful for cache invalidation tests."""
    h = hashlib.sha256()
    for n in sorted(nodes, key=lambda x: x.id):
        h.update(n.id.encode())
        h.update(n.type.encode())
    for e in sorted(edges, key=lambda x: (x.src, x.predicate, x.dst)):
        h.update(e.src.encode())
        h.update(e.predicate.encode())
        h.update(e.dst.encode())
    return h.hexdigest()[:16]
