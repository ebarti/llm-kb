#!/usr/bin/env python3
"""Generate wiki/Glossary.md — an alphabetical list of entities + concepts.

Each entry is keyed on the article title with its `summary:` field as the
definition. Entities are annotated with their `entity_type` when available.
Always stamps a fresh `last_compiled` so the page is never "unknown".

Usage:
    python3 tools/compile/pages/gen_glossary.py
"""

from __future__ import annotations

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


def _first_letter(term: str) -> str:
    for ch in term:
        if ch.isalpha():
            return ch.upper()
        if ch.isdigit():
            return "0-9"
    return "Other"


def _display_title(meta, fallback: str) -> str:
    title = str(meta.get("title") or "").strip()
    if title:
        return title
    return fallback


def _entity_type(meta) -> str | None:
    val = meta.get("entity_type")
    if not val:
        return None
    return str(val).strip() or None


def _collect_entries():
    """Yield glossary entries for entities and concepts."""
    entries = []
    for path, meta, _body in iter_articles():
        rel = article_rel_path(path)
        category = rel.split("/", 1)[0]
        if category not in ("entities", "concepts"):
            continue
        stem = path.stem
        title = _display_title(meta, stem.replace("-", " ").title())
        summary = str(meta.get("summary") or "").strip()
        entries.append({
            "category": category,
            "title": title,
            "summary": summary,
            "entity_type": _entity_type(meta) if category == "entities" else None,
            "link": rel,
        })
    return entries


def generate() -> Path:
    entries = _collect_entries()

    # Group by first letter of title
    by_letter: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_letter[_first_letter(e["title"])].append(e)
    for letter in by_letter:
        by_letter[letter].sort(key=lambda e: (e["title"].lower(), e["link"]))

    n_entities = sum(1 for e in entries if e["category"] == "entities")
    n_concepts = sum(1 for e in entries if e["category"] == "concepts")

    lines: list[str] = []
    lines.append("# Glossary")
    lines.append("")
    lines.append(
        f"_Auto-generated on {today()} by `tools/compile/pages/gen_glossary.py`. "
        "Entries are the titles of entity and concept articles; definitions are the "
        "`summary:` field from each article's frontmatter._"
    )
    lines.append("")
    lines.append(f"- Concepts: **{n_concepts}**")
    lines.append(f"- Entities: **{n_entities}**")
    lines.append(f"- Total entries: **{len(entries)}**")
    lines.append("")

    if not entries:
        lines.append("_No concept or entity articles found yet._")
        body = "\n".join(lines)
    else:
        for letter in sorted(by_letter.keys()):
            lines.append(f"## {letter}")
            lines.append("")
            for e in by_letter[letter]:
                prefix = ""
                if e["category"] == "entities":
                    etype = e["entity_type"]
                    prefix = f" _(entity{': ' + etype if etype else ''})_"
                else:
                    prefix = " _(concept)_"
                summary = e["summary"] or "_no summary yet_"
                lines.append(f"**{e['title']}**{prefix}")
                lines.append(f": {summary}")
                lines.append(f": See [[{e['link']}]]")
                lines.append("")
        body = "\n".join(lines)

    frontmatter = {
        "title": "Glossary",
        "type": "meta",
        "entries": len(entries),
        "summary": "Auto-generated alphabetical glossary of concepts and entities with their summaries.",
    }

    out_path = WIKI / "Glossary.md"
    write_page(out_path, frontmatter, body)
    return out_path


def main() -> int:
    out = generate()
    print(f"  [glossary] Written to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
