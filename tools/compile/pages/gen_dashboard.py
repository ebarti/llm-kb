#!/usr/bin/env python3
"""Generate wiki/Dashboard.md — the KB status dashboard.

Computes everything from the current wiki state: counts by type, top-connected
("hub") articles, orphan articles, and a quick-links section. Writes a fresh
`last_compiled` timestamp so the page is never stale.

Usage:
    python3 tools/compile/pages/gen_dashboard.py
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from _common import (
    ARTICLE_DIRS,
    ROOT,
    WIKI,
    article_rel_path,
    collect_wikilinks,
    iter_articles,
    today,
    write_page,
)


def _count_raw_files() -> int:
    raw_dir = ROOT / "raw"
    if not raw_dir.is_dir():
        return 0
    return sum(1 for p in raw_dir.iterdir() if p.suffix == ".md")


def _build_link_graph():
    """Return (all_articles, outgoing, incoming) where each value is a set."""
    all_articles = set()
    outgoing = defaultdict(set)
    for path, _meta, body in iter_articles():
        rel = article_rel_path(path)
        all_articles.add(rel)
        for link in collect_wikilinks(body):
            # Only count links that point to wiki article paths
            if "/" in link and not link.startswith("raw/"):
                outgoing[rel].add(link)
    incoming = defaultdict(set)
    for src, targets in outgoing.items():
        for t in targets:
            incoming[t].add(src)
    return all_articles, outgoing, incoming


def _counts_by_type() -> dict[str, int]:
    counts = {d: 0 for d in ARTICLE_DIRS}
    for subdir in ARTICLE_DIRS:
        dir_path = WIKI / subdir
        if dir_path.is_dir():
            counts[subdir] = sum(1 for _ in dir_path.glob("*.md"))
    return counts


def _top_hubs(all_articles, outgoing, incoming, n: int = 10):
    rows = []
    for art in all_articles:
        inc = len(incoming.get(art, ()))
        out = len(outgoing.get(art, ()))
        rows.append((art, inc, out, inc + out))
    rows.sort(key=lambda r: (-r[3], r[0]))
    return rows[:n]


def _orphans(all_articles, incoming):
    return sorted(a for a in all_articles if not incoming.get(a))


def _recent_activity(limit: int = 10):
    """Walk all wiki article files and sort by mtime, descending."""
    entries = []
    for subdir in ARTICLE_DIRS:
        dir_path = WIKI / subdir
        if not dir_path.is_dir():
            continue
        for p in dir_path.glob("*.md"):
            try:
                mtime = p.stat().st_mtime
            except OSError:
                continue
            entries.append((mtime, article_rel_path(p)))
    entries.sort(key=lambda e: (-e[0], e[1]))
    return entries[:limit]


def _navigation_rows() -> list[tuple[str, str]]:
    """Return dashboard navigation rows whose wikilinks should resolve.

    Some tests and partial workspaces run decoration generation without the
    usual seeded ``_index.md``/``log.md``/``_meta`` files. Keep those optional,
    but always include pages produced by this decoration batch.
    """
    generated_pages = {
        "Graph": "Link-graph analysis",
        "Tags": "Tag cloud",
        "Glossary": "Glossary of defined terms",
        "Changelog": "Wiki changelog from git",
    }
    optional_pages = {
        "_index": "Master index of every article",
        "_meta/summaries": "One-line summary per article",
        "_meta/links": "Backlink graph",
        "_meta/manifest": "Compilation tracking",
        "_meta/queries": "Pre-built Dataview queries",
        "log": "Append-only activity log",
    }

    rows: list[tuple[str, str]] = []
    for target, description in optional_pages.items():
        if (WIKI / f"{target}.md").exists():
            rows.append((target, description))
    rows.extend(generated_pages.items())
    return rows


def generate() -> Path:
    counts = _counts_by_type()
    total_articles = sum(counts.values())
    raw_count = _count_raw_files()
    sources_count = counts["sources"]

    all_articles, outgoing, incoming = _build_link_graph()
    hubs = _top_hubs(all_articles, outgoing, incoming, n=10)
    orphan_list = _orphans(all_articles, incoming)
    recent = _recent_activity(limit=10)

    # Average links per node
    total_edges = sum(len(t) for t in outgoing.values())
    avg_deg = (total_edges / len(all_articles)) if all_articles else 0.0

    lines: list[str] = []
    lines.append("# LLM Knowledge Base Dashboard")
    lines.append("")
    lines.append(f"_Auto-generated on {today()} by `tools/compile/pages/gen_dashboard.py`._")
    lines.append("")

    # --- Quick stats ---
    lines.append("## Quick Stats")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Sources | {counts['sources']} |")
    lines.append(f"| Concepts | {counts['concepts']} |")
    lines.append(f"| Entities | {counts['entities']} |")
    lines.append(f"| Comparisons | {counts['comparisons']} |")
    lines.append(f"| Total articles | {total_articles} |")
    lines.append(f"| Raw files | {raw_count} |")
    lines.append(f"| Raw files compiled | {sources_count} / {raw_count} |")
    lines.append(f"| Total wikilinks | {total_edges} |")
    lines.append(f"| Avg links per article | {avg_deg:.1f} |")
    lines.append(f"| Orphan articles | {len(orphan_list)} |")
    lines.append("")

    # --- Top hubs ---
    lines.append("## Top Connected Articles (Hub Nodes)")
    lines.append("")
    if hubs:
        lines.append("The most connected articles in the wiki, ranked by incoming + outgoing wikilinks.")
        lines.append("")
        lines.append("| Article | Incoming | Outgoing | Total |")
        lines.append("|---------|---------:|---------:|------:|")
        for art, inc, out, tot in hubs:
            lines.append(f"| [[{art}]] | {inc} | {out} | {tot} |")
    else:
        lines.append("_No articles yet._")
    lines.append("")

    # --- Recently modified ---
    lines.append("## Recently Modified")
    lines.append("")
    if recent:
        for _mtime, rel in recent:
            lines.append(f"- [[{rel}]]")
    else:
        lines.append("_No articles yet._")
    lines.append("")

    # --- Orphans ---
    lines.append("## Orphan Watch")
    lines.append("")
    lines.append("Articles with no incoming links from other wiki pages.")
    lines.append("")
    if orphan_list:
        for o in orphan_list[:25]:
            lines.append(f"- [[{o}]]")
        if len(orphan_list) > 25:
            lines.append(f"- _...and {len(orphan_list) - 25} more_")
    else:
        lines.append("_None — every article is reachable._")
    lines.append("")

    # --- Quick actions / links ---
    lines.append("## Navigation")
    lines.append("")
    lines.append("| Page | Description |")
    lines.append("|------|-------------|")
    for target, description in _navigation_rows():
        lines.append(f"| [[{target}]] | {description} |")
    lines.append("")

    body = "\n".join(lines)
    frontmatter = {
        "title": "Dashboard",
        "type": "dashboard",
        "summary": "Auto-generated KB status dashboard: counts, top hubs, orphans, and navigation links.",
    }

    out_path = WIKI / "Dashboard.md"
    write_page(out_path, frontmatter, body)
    return out_path


def main() -> int:
    out = generate()
    print(f"  [dashboard] Written to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
