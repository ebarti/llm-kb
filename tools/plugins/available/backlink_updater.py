#!/usr/bin/env python3
"""
Backlink updater plugin — rescans all wiki files to rebuild the link graph.

Hook: post_compile
Ensures wiki/_meta/links.md is accurate and detects orphan pages.
"""

import os
import re
from collections import defaultdict


def register():
    return {"post_compile": run_post_compile}


def extract_wikilinks(content):
    """Extract all [[wikilink]] targets from content."""
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", content)


def run_post_compile(root, *args):
    """Rescan all wiki files and rebuild the link graph."""
    wiki_dir = os.path.join(root, "wiki")
    meta_dir = os.path.join(wiki_dir, "_meta")
    os.makedirs(meta_dir, exist_ok=True)

    # Collect all articles and their outgoing links
    articles = {}  # relpath (no .md) -> set of link targets
    all_pages = set()

    for dirpath, _, filenames in os.walk(wiki_dir):
        # Skip _meta
        rel_dir = os.path.relpath(dirpath, wiki_dir)
        if rel_dir.startswith("_meta"):
            continue
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(fpath, wiki_dir)
            page_id = relpath.replace(".md", "")
            all_pages.add(page_id)

            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue

            links = extract_wikilinks(content)
            articles[page_id] = set(links)

    # Build incoming links (backlinks)
    incoming = defaultdict(set)
    for page_id, targets in articles.items():
        for target in targets:
            incoming[target].add(page_id)

    # Find orphan pages (no incoming links and not an index/meta page)
    index_pages = {"_index", "Dashboard", "Tags", "Queries", "Graph",
                   "Glossary", "Reading-List", "Changelog", "log"}
    orphans = []
    for page in sorted(all_pages):
        if page in index_pages:
            continue
        if page not in incoming or len(incoming[page]) == 0:
            orphans.append(page)

    # Generate links.md
    lines = [
        "---",
        'title: "Link Graph"',
        "type: meta",
        f"last_updated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}",
        "---",
        "",
        "# Link Graph",
        "",
        "Backlink map of all wiki articles.",
        "",
    ]

    for page_id in sorted(articles.keys()):
        outgoing = articles[page_id]
        inc = incoming.get(page_id, set())

        lines.append(f"## {page_id}")
        if inc:
            inc_links = ", ".join(f"[[{p}]]" for p in sorted(inc))
            lines.append(f"\u2190 {inc_links}")
        else:
            lines.append("\u2190 (no incoming wikilinks from other sources)")
        if outgoing:
            out_links = ", ".join(f"[[{t}]]" for t in sorted(outgoing))
            lines.append(f"\u2192 {out_links}")
        else:
            lines.append("\u2192 (no outgoing links)")
        lines.append("")

    # Add orphan pages section
    if orphans:
        lines.append("## Orphan Pages")
        lines.append("")
        lines.append("Pages with no incoming links:")
        lines.append("")
        for page in orphans:
            lines.append(f"- [[{page}]]")
        lines.append("")

    links_path = os.path.join(meta_dir, "links.md")
    with open(links_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  [backlink_updater] Scanned {len(articles)} pages, "
          f"found {sum(len(v) for v in articles.values())} links")
    if orphans:
        print(f"  [backlink_updater] Orphan pages ({len(orphans)}): "
              f"{', '.join(orphans[:10])}")
    else:
        print(f"  [backlink_updater] No orphan pages detected.")
