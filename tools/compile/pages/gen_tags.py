#!/usr/bin/env python3
"""Generate wiki/Tags.md — the tag cloud page.

Reads `tags:` (YAML list) and `#inline-tags` from every article, groups them
alphabetically, and lists the articles under each tag. Always stamps a fresh
`last_compiled` so the page is never "unknown".

Usage:
    python3 tools/compile/pages/gen_tags.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from _common import (
    ROOT,
    WIKI,
    article_rel_path,
    iter_articles,
    today,
    write_page,
)

# Inline tag pattern — `#word-with-dashes`, not inside a wikilink or URL.
INLINE_TAG_RE = re.compile(r"(?<![\w#/])#([a-zA-Z][\w\-]{1,40})")
# Filter out likely hex colors (3-8 hex digits with no non-hex letter).
HEX_COLOR_RE = re.compile(r"^[0-9a-fA-F]{3,8}$")


def _normalize_tag(tag: str) -> str:
    """Canonicalize tag form: lowercase, no leading '#'."""
    t = tag.strip().lstrip("#")
    return t.lower()


def _tags_from_frontmatter(meta) -> list[str]:
    raw = meta.get("tags")
    if not raw:
        return []
    if isinstance(raw, list):
        return [_normalize_tag(t) for t in raw if t]
    # String form: could be `[a, b]`, `"a, b"`, etc.
    s = str(raw).strip()
    # Split on common delimiters
    parts = re.split(r"[,\s]+", s.strip("[]"))
    return [_normalize_tag(p) for p in parts if p]


def _tags_from_body(body: str) -> list[str]:
    out: list[str] = []
    for m in INLINE_TAG_RE.findall(body):
        tag = _normalize_tag(m)
        # Drop hex-color-looking captures like `#fcb32c`.
        if HEX_COLOR_RE.match(tag):
            continue
        out.append(tag)
    return out


def _collect_tags():
    """Return dict[tag] -> sorted list[article_rel_path]."""
    tag_map: dict[str, set[str]] = defaultdict(set)
    total_articles = 0
    for path, meta, body in iter_articles():
        total_articles += 1
        rel = article_rel_path(path)
        all_tags = set(_tags_from_frontmatter(meta)) | set(_tags_from_body(body))
        for tag in all_tags:
            if not tag:
                continue
            tag_map[tag].add(rel)
    return tag_map, total_articles


def generate() -> Path:
    tag_map, total_articles = _collect_tags()

    # Group tags by first letter
    by_letter: dict[str, list[tuple[str, list[str]]]] = defaultdict(list)
    for tag in sorted(tag_map.keys()):
        letter = tag[0].upper() if tag else "#"
        articles = sorted(tag_map[tag])
        by_letter[letter].append((tag, articles))

    lines: list[str] = []
    lines.append("# Tag Index")
    lines.append("")
    lines.append(
        f"_Auto-generated on {today()} by `tools/compile/pages/gen_tags.py`. "
        "Covers `tags:` frontmatter and inline `#tags` across the wiki._"
    )
    lines.append("")

    # --- Summary table ---
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Unique tags: **{len(tag_map)}**")
    lines.append(f"- Articles scanned: **{total_articles}**")
    total_usages = sum(len(v) for v in tag_map.values())
    lines.append(f"- Total tag usages: **{total_usages}**")
    lines.append("")

    # --- Tag cloud ranked by count ---
    if tag_map:
        lines.append("## Tag Cloud (by count)")
        lines.append("")
        ranked = sorted(tag_map.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        lines.append("| Tag | Articles |")
        lines.append("|-----|---------:|")
        for tag, articles in ranked:
            lines.append(f"| `#{tag}` | {len(articles)} |")
        lines.append("")
    else:
        lines.append("_No tags found yet. Add `tags: [\"foo\", \"bar\"]` to article frontmatter "
                     "or use inline `#foo` tags in the body._")
        lines.append("")

    # --- Tag index (alphabetical) ---
    if by_letter:
        lines.append("## Tag Index")
        lines.append("")
        for letter in sorted(by_letter.keys()):
            lines.append(f"### {letter}")
            lines.append("")
            for tag, articles in by_letter[letter]:
                lines.append(f"- **`#{tag}`** ({len(articles)})")
                for art in articles:
                    lines.append(f"  - [[{art}]]")
            lines.append("")

    body = "\n".join(lines)
    frontmatter = {
        "title": "Tags",
        "type": "meta",
        "summary": "Auto-generated tag cloud pulled from frontmatter `tags:` and inline `#tags`.",
    }

    out_path = WIKI / "Tags.md"
    write_page(out_path, frontmatter, body)
    return out_path


def main() -> int:
    out = generate()
    print(f"  [tags] Written to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
