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

   These override any heuristic match. Provenance is logged as
   `frontmatter:edges` (or `frontmatter:manual` when keyed under `manual:`).

2. **Structural frontmatter fields** — `source`, `sources`, `subjects` are
   interpreted as typed:

        source / sources  -> predicate = cites      (provenance='frontmatter:sources')
        subjects          -> predicate = compares   (provenance='frontmatter:subjects')

3. **Heuristic patterns** over a ±50-char window around each `[[link]]` in
   the body. See `PREDICATE_PATTERNS` below for the exact regexes. The
   first matching pattern wins; patterns are ordered from most specific
   to most generic.

4. **Default** — if nothing matches, the predicate is `mentions` with
   provenance `'default'`.

## Patterns

Each pattern fires when a trigger verb or phrase appears within ~50 chars
BEFORE the wikilink (with the link allowed to carry a display name after
`|`). Matching is case-insensitive. The window also includes a few chars
AFTER the link to catch constructions like "X is a part of [[Y]]" vs.
"[[X]] is part of Y" — the patterns are written with directional
awareness.

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
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator, Optional


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
    ("cites", re.compile(
        r"\b("
        r"cites?|cited|citing|"
        r"references?|referenced|referencing|"
        r"as\s+shown\s+in|as\s+described\s+in|as\s+noted\s+in|"
        r"see\s+also|"
        r"per\s+|according\s+to"
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
                    })
                    continue
                # Shorthand: - concepts/rag:extends
                short = re.match(r"\"?([^\":]+)\"?\s*:\s*([a-z_]+)\s*$", body)
                if short:
                    overrides.append({
                        "to": short.group(1).strip(),
                        "predicate": short.group(2).strip(),
                    })
                    continue
                # Opens a key: value block (e.g. `- to: concepts/rag`).
                # Process remainder of the line as a key: value pair.
                kv = re.match(r"(\w+)\s*:\s*\"?([^\"]*?)\"?\s*$", body)
                if kv:
                    pending[kv.group(1)] = kv.group(2).strip()
                continue
            # Continuation lines inside an active `- ` entry.
            kv = re.match(r"(\w+)\s*:\s*\"?([^\"]*?)\"?\s*$", stripped)
            if kv:
                pending[kv.group(1)] = kv.group(2).strip()
        if pending:
            overrides.append(pending)

    # Keep only valid-looking entries.
    clean: list[dict] = []
    for o in overrides:
        to = o.get("to", "").strip()
        pred = o.get("predicate", "").strip()
        # Unwrap wikilink in `to`.
        wm = re.match(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]\s*$", to)
        if wm:
            to = wm.group(1).strip()
        if to and pred:
            clean.append({"to": to, "predicate": pred})
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


def _iter_wiki_files(wiki_dir: Path) -> Iterator[Path]:
    """Yield markdown files that should be treated as graph nodes.

    Skips `_meta/`, `_index.md`, `log.md`, and anything starting with `_`.
    """
    for path in wiki_dir.rglob("*.md"):
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


def extract_nodes_and_edges(
    wiki_dir: str | Path,
    raw_dir: Optional[str | Path] = None,
) -> tuple[list[Node], list[Edge]]:
    """Walk the wiki and return typed nodes + edges.

    Edge resolution:

    1. Frontmatter ``edges:`` / ``manual:`` override everything.
    2. Frontmatter list fields (``source``, ``sources``, ``subjects``) map to
       ``cites`` (for sources) and ``compares`` (for subjects).
    3. Body wikilinks are classified by heuristic, defaulting to ``mentions``.

    Edges whose target doesn't resolve to an existing node are still emitted
    (so that dangling links are visible in the graph) — but only if the
    target is well-formed. Targets under `raw/` are auto-added as nodes of
    type `raw` when the file exists on disk.
    """
    wiki_dir = Path(wiki_dir).resolve()
    raw_dir = Path(raw_dir).resolve() if raw_dir else wiki_dir.parent / "raw"

    nodes: dict[str, Node] = {}
    edges: list[Edge] = []
    overrides_per_src: dict[str, set[tuple[str, str]]] = {}

    # Pass 1: collect all nodes so self-links and cross-refs resolve.
    files = list(_iter_wiki_files(wiki_dir))
    parsed: dict[str, tuple[Node, str, str]] = {}
    for path in files:
        node, fm_block, body = _node_from_file(path, wiki_dir)
        parsed[node.id] = (node, fm_block, body)
        nodes[node.id] = node

    # Pass 2: emit edges.
    for node_id, (node, fm_block, body) in parsed.items():
        # --- 1. Manual / edges frontmatter overrides ---
        override_keys: set[tuple[str, str]] = set()
        for entry in _extract_edges_override(fm_block):
            target = _normalise_link(entry["to"])
            pred = entry["predicate"]
            if not target or target == node_id:
                continue
            if target.startswith("raw/"):
                _add_raw_node(target, raw_dir, nodes)
            edges.append(Edge(
                src=node_id,
                dst=target,
                predicate=pred,
                provenance="frontmatter:manual",
            ))
            override_keys.add((target, pred))
        overrides_per_src[node_id] = override_keys

        # --- 2. Structural frontmatter lists ---
        # `source` (scalar) and `sources` (list) both imply `cites`.
        scalar_source = _extract_scalar(fm_block, "source")
        if scalar_source:
            target = _normalise_link(scalar_source)
            if target and target != node_id:
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
            if target.startswith("raw/"):
                _add_raw_node(target, raw_dir, nodes)
            left = body[: m.start()]
            predicate, provenance = detect_predicate(left)
            if (target, predicate) not in override_keys:
                edges.append(Edge(
                    src=node_id,
                    dst=target,
                    predicate=predicate,
                    provenance=provenance,
                ))

    return list(nodes.values()), edges


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
