#!/usr/bin/env python3
"""Shared helpers for the decoration-page generators in tools/compile/pages/.

Every generator writes a top-level wiki/*.md file with fresh frontmatter
(including last_compiled) so no navigation page is ever stamped with
"unknown" or a stale manual date.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Iterator, Tuple

# tools/compile/pages/_common.py -> .../<repo>
ROOT = Path(__file__).resolve().parents[3]
WIKI = ROOT / "wiki"

ARTICLE_DIRS = ("sources", "concepts", "entities", "comparisons")


def today() -> str:
    """ISO 8601 date string for the `last_compiled` frontmatter field."""
    return datetime.now().strftime("%Y-%m-%d")


def _parse_inline_list(raw: str) -> list[str]:
    """Parse a single-line YAML-ish list with quoted or bare scalar items."""
    inner = raw.strip()
    if not (inner.startswith("[") and inner.endswith("]")):
        return []
    inner = inner[1:-1].strip()
    if not inner:
        return []

    items: list[str] = []
    current: list[str] = []
    quote: str | None = None

    for ch in inner:
        if quote:
            if ch == quote:
                quote = None
            else:
                current.append(ch)
            continue
        if ch in ('"', "'"):
            quote = ch
            continue
        if ch == ",":
            item = "".join(current).strip()
            if item:
                items.append(item)
            current = []
            continue
        current.append(ch)

    item = "".join(current).strip()
    if item:
        items.append(item)
    return items


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    """Parse YAML-ish frontmatter. Returns (metadata_dict, body).

    Handles scalar values, quoted strings, and simple `["a", "b"]` lists.
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    meta: Dict[str, object] = {}
    for line in yaml_block.split("\n"):
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s*(\w[\w_-]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith('"') and raw.endswith('"'):
            meta[key] = raw[1:-1]
        elif raw.startswith("'") and raw.endswith("'"):
            meta[key] = raw[1:-1]
        elif raw.startswith("["):
            meta[key] = _parse_inline_list(raw)
        else:
            meta[key] = raw
    return meta, body


def iter_articles(wiki_dir: Path = WIKI) -> Iterator[Tuple[Path, Dict[str, object], str]]:
    """Yield (path, frontmatter, body) for every article under the four canonical dirs."""
    for subdir in ARTICLE_DIRS:
        dir_path = wiki_dir / subdir
        if not dir_path.is_dir():
            continue
        for md in sorted(dir_path.glob("*.md")):
            try:
                text = md.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta, body = parse_frontmatter(text)
            yield md, meta, body


def article_rel_path(path: Path, wiki_dir: Path = WIKI) -> str:
    """wiki/concepts/foo.md -> concepts/foo"""
    rel = path.relative_to(wiki_dir).with_suffix("")
    return str(rel)


def render_frontmatter(meta: Dict[str, object]) -> str:
    """Render a minimal YAML frontmatter block for a generated page.

    Values are stringified with basic quoting; numbers and bare identifiers
    stay unquoted. Lists are written as `["a", "b"]`.
    """
    lines = ["---"]
    for key, val in meta.items():
        lines.append(f"{key}: {_format_value(val)}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _format_value(val: object) -> str:
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, list):
        items = ", ".join(f'"{str(v)}"' for v in val)
        return f"[{items}]"
    s = str(val)
    # Quote if it looks risky (contains colon/hash/leading special chars)
    if re.search(r"[:#]", s) or s.strip() != s:
        s_escaped = s.replace('"', r"\"")
        return f'"{s_escaped}"'
    return f'"{s}"'


def write_page(output_path: Path, frontmatter: Dict[str, object], body: str) -> None:
    """Write a wiki page with fresh frontmatter (always stamps last_compiled=today())."""
    fm = dict(frontmatter)
    fm["last_compiled"] = today()
    text = render_frontmatter(fm) + body.rstrip() + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")


def collect_wikilinks(body: str) -> list[str]:
    """Return a list of wikilink targets (normalized, no .md suffix)."""
    out = []
    for m in WIKILINK_RE.findall(body):
        link = m.strip()
        if link.endswith(".md"):
            link = link[:-3]
        out.append(link)
    return out
