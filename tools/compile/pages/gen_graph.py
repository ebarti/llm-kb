#!/usr/bin/env python3
"""Generate wiki/Graph.md — static analysis of the wiki link graph.

Produces overview metrics, a hub-node table, orphan list, and leaf-node
list. Always stamps a fresh `last_compiled` so the page is never stale.

Usage:
    python3 tools/compile/pages/gen_graph.py
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


def _build_link_graph():
    all_articles: set[str] = set()
    outgoing: dict[str, set[str]] = defaultdict(set)
    for path, _meta, body in iter_articles():
        rel = article_rel_path(path)
        all_articles.add(rel)
        for link in collect_wikilinks(body):
            if "/" in link and not link.startswith("raw/"):
                outgoing[rel].add(link)
    incoming: dict[str, set[str]] = defaultdict(set)
    for src, targets in outgoing.items():
        for t in targets:
            incoming[t].add(src)
    return all_articles, outgoing, incoming


def _counts_per_dir():
    counts = {d: 0 for d in ARTICLE_DIRS}
    for d in ARTICLE_DIRS:
        dir_path = WIKI / d
        if dir_path.is_dir():
            counts[d] = sum(1 for _ in dir_path.glob("*.md"))
    return counts


def generate() -> Path:
    all_articles, outgoing, incoming = _build_link_graph()
    counts = _counts_per_dir()

    total_edges = sum(len(v) for v in outgoing.values())
    n = len(all_articles)
    avg_deg = (total_edges / n) if n else 0.0

    # Per-article degree
    rows = []
    for art in all_articles:
        inc = len(incoming.get(art, ()))
        out = len(outgoing.get(art, ()))
        rows.append((art, inc, out, inc + out))

    hubs = sorted(rows, key=lambda r: (-r[3], r[0]))[:15]
    leaves = sorted(rows, key=lambda r: (r[3], r[0]))[:15]
    orphans = sorted(a for a in all_articles if not incoming.get(a))
    dead_links = sorted(
        {t for src, targets in outgoing.items() for t in targets if t not in all_articles}
    )

    lines: list[str] = []
    lines.append("# Graph Analysis")
    lines.append("")
    lines.append(
        f"_Auto-generated on {today()} by `tools/compile/pages/gen_graph.py`. "
        "Computed directly from wikilinks in `wiki/{sources,concepts,entities,comparisons}`._"
    )
    lines.append("")

    # --- Overview ---
    lines.append("## Overview")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Total nodes (articles) | {n} |")
    lines.append(f"| Source nodes | {counts['sources']} |")
    lines.append(f"| Concept nodes | {counts['concepts']} |")
    lines.append(f"| Entity nodes | {counts['entities']} |")
    lines.append(f"| Comparison nodes | {counts['comparisons']} |")
    lines.append(f"| Total directed edges | {total_edges} |")
    lines.append(f"| Average connections per node | {avg_deg:.2f} |")
    lines.append(f"| Orphan articles | {len(orphans)} |")
    lines.append(f"| Dead-link targets | {len(dead_links)} |")
    lines.append("")

    # --- Hubs ---
    lines.append("## Hub Nodes (Most Connected)")
    lines.append("")
    if hubs:
        lines.append("Articles with the highest combined incoming + outgoing link count.")
        lines.append("")
        lines.append("| Rank | Article | Incoming | Outgoing | Total |")
        lines.append("|-----:|---------|---------:|---------:|------:|")
        for i, (art, inc, out, tot) in enumerate(hubs, start=1):
            lines.append(f"| {i} | [[{art}]] | {inc} | {out} | {tot} |")
    else:
        lines.append("_No articles yet._")
    lines.append("")

    # --- Leaves ---
    lines.append("## Leaf Nodes (Fewest Connections)")
    lines.append("")
    if leaves:
        lines.append("| Article | Incoming | Outgoing | Total |")
        lines.append("|---------|---------:|---------:|------:|")
        for art, inc, out, tot in leaves:
            lines.append(f"| [[{art}]] | {inc} | {out} | {tot} |")
    else:
        lines.append("_No articles yet._")
    lines.append("")

    # --- Orphans ---
    lines.append("## Orphan Articles")
    lines.append("")
    if orphans:
        for o in orphans[:30]:
            lines.append(f"- [[{o}]]")
        if len(orphans) > 30:
            lines.append(f"- _...and {len(orphans) - 30} more_")
    else:
        lines.append("_No orphan articles._")
    lines.append("")

    # --- Dead links ---
    lines.append("## Dead Wikilink Targets")
    lines.append("")
    if dead_links:
        for d in dead_links[:30]:
            lines.append(f"- `{d}`")
        if len(dead_links) > 30:
            lines.append(f"- _...and {len(dead_links) - 30} more_")
    else:
        lines.append("_All wikilink targets resolve to real articles._")
    lines.append("")

    body = "\n".join(lines)
    frontmatter = {
        "title": "Graph Analysis",
        "type": "meta",
        "summary": "Auto-generated link-graph analysis: overview metrics, hubs, leaves, orphans, dead links.",
    }

    out_path = WIKI / "Graph.md"
    write_page(out_path, frontmatter, body)
    return out_path


def main() -> int:
    out = generate()
    print(f"  [graph] Written to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
