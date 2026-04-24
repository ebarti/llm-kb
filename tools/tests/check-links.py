#!/usr/bin/env python3
"""
Link Graph Validator
Builds the actual link graph from scanning all wiki files and validates it.

Checks:
  - Compares actual graph against wiki/_meta/links.md
  - Finds orphan articles (no incoming links)
  - Finds dead links (pointing to nonexistent files)
  - Finds self-links
  - Computes graph metrics: density, avg degree, connected components

Usage: python3 tools/tests/check-links.py [--json]
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"
LINKS_FILE = WIKI_DIR / "_meta" / "links.md"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")


def collect_wiki_files():
    """Collect all .md article files from wiki subdirectories."""
    files = []
    for subdir in ["concepts", "sources", "comparisons", "entities"]:
        dirpath = WIKI_DIR / subdir
        if dirpath.is_dir():
            for f in sorted(dirpath.iterdir()):
                if f.suffix == ".md":
                    files.append(f)
    return files


def get_rel(filepath):
    return str(filepath.relative_to(WIKI_DIR)).replace(".md", "")


def build_actual_graph(files):
    """Scan all files and extract wikilinks to build the actual graph."""
    # outgoing[article] = set of targets
    outgoing = defaultdict(set)
    all_articles = set()

    for f in files:
        rel = get_rel(f)
        all_articles.add(rel)
        text = f.read_text(encoding="utf-8", errors="replace")
        links = WIKILINK_RE.findall(text)
        for link in links:
            link = link.strip()
            if link.endswith(".md"):
                link = link[:-3]
            # Only count links that point to wiki article paths
            if "/" in link and not link.startswith("raw/"):
                outgoing[rel].add(link)

    # Compute incoming
    incoming = defaultdict(set)
    for src, targets in outgoing.items():
        for t in targets:
            incoming[t].add(src)

    return all_articles, outgoing, incoming


def parse_links_md():
    """Parse wiki/_meta/links.md to extract the declared graph."""
    if not LINKS_FILE.exists():
        return None, None

    text = LINKS_FILE.read_text(encoding="utf-8", errors="replace")
    declared_outgoing = defaultdict(set)
    declared_incoming = defaultdict(set)

    current_article = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("## ") and not line.startswith("## Sources") and not line.startswith("## Concepts"):
            current_article = line[3:].strip()
        elif current_article and line.startswith("→"):
            links = WIKILINK_RE.findall(line)
            for link in links:
                declared_outgoing[current_article].add(link.strip())
        elif current_article and line.startswith("←"):
            links = WIKILINK_RE.findall(line)
            for link in links:
                declared_incoming[current_article].add(link.strip())

    return declared_outgoing, declared_incoming


def find_connected_components(articles, outgoing):
    """Find connected components in the undirected version of the graph."""
    # Build adjacency (undirected)
    adj = defaultdict(set)
    for src, targets in outgoing.items():
        for t in targets:
            if t in articles:
                adj[src].add(t)
                adj[t].add(src)

    visited = set()
    components = []

    for article in articles:
        if article in visited:
            continue
        # BFS
        component = set()
        queue = [article]
        while queue:
            node = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        components.append(component)

    return components


def run_checks():
    files = collect_wiki_files()
    all_articles, outgoing, incoming = build_actual_graph(files)

    issues = []
    results = {
        "dead_links": [],
        "self_links": [],
        "orphans": [],
        "metrics": {
            "total_articles": 0,
            "total_edges": 0,
            "density": 0,
            "avg_out_degree": 0,
            "avg_in_degree": 0,
            "connected_components": 0,
            "largest_component_size": 0,
        },
        "links_md_stale": [],
        "links_md_missing": [],
        "issues": [],
        "ok": True,
    }

    if not files:
        return results

    # --- Dead links ---
    dead_links = []
    for src, targets in outgoing.items():
        for t in targets:
            if t not in all_articles:
                dead_links.append({"from": src, "to": t})
    results["dead_links"] = dead_links
    if dead_links:
        issues.append(f"{len(dead_links)} dead link(s) found")

    # --- Self-links ---
    self_links = []
    for src, targets in outgoing.items():
        if src in targets:
            self_links.append(src)
    results["self_links"] = self_links
    if self_links:
        issues.append(f"{len(self_links)} self-link(s) found")

    # --- Orphan articles (no incoming links from other articles) ---
    orphans = []
    for article in sorted(all_articles):
        if not incoming.get(article):
            orphans.append(article)
    results["orphans"] = orphans
    if orphans:
        issues.append(f"{len(orphans)} orphan article(s) with no incoming links")

    # --- Graph metrics ---
    total_edges = sum(len(t) for t in outgoing.values())
    n = len(all_articles)
    max_edges = n * (n - 1) if n > 1 else 1
    density = total_edges / max_edges if max_edges > 0 else 0
    avg_out = total_edges / n if n > 0 else 0
    avg_in = sum(len(s) for s in incoming.values()) / n if n > 0 else 0

    components = find_connected_components(all_articles, outgoing)

    results["metrics"] = {
        "total_articles": n,
        "total_edges": total_edges,
        "density": round(density, 4),
        "avg_out_degree": round(avg_out, 2),
        "avg_in_degree": round(avg_in, 2),
        "connected_components": len(components),
        "largest_component_size": max(len(c) for c in components) if components else 0,
    }

    # --- Compare with links.md ---
    declared_out, declared_in = parse_links_md()
    stale_entries = []
    missing_entries = []

    if declared_out is not None:
        # Check for entries in links.md that don't match actual
        all_declared_articles = set(declared_out.keys()) | set(declared_in.keys()) if declared_in else set(declared_out.keys())

        for article in all_articles:
            actual_out = outgoing.get(article, set())
            declared = declared_out.get(article, set())
            # Links in actual but not in declared
            for link in actual_out - declared:
                if link in all_articles:  # only flag if target exists
                    missing_entries.append({"article": article, "link": link, "direction": "outgoing"})
            # Links in declared but not in actual
            for link in declared - actual_out:
                stale_entries.append({"article": article, "link": link, "direction": "outgoing"})

        results["links_md_stale"] = stale_entries
        results["links_md_missing"] = missing_entries
        if stale_entries:
            issues.append(f"{len(stale_entries)} stale entry/entries in links.md")
        if missing_entries:
            issues.append(f"{len(missing_entries)} missing entry/entries from links.md")
    else:
        results["links_md_stale"] = []
        results["links_md_missing"] = []
        issues.append("links.md not found or could not be parsed")

    results["issues"] = issues
    results["ok"] = len(issues) == 0

    return results


def print_report(result):
    print("=" * 60)
    print("  Link Graph Validator")
    print("=" * 60)

    m = result["metrics"]
    print(f"\nArticles: {m['total_articles']}")
    print(f"Edges: {m['total_edges']}")
    print(f"Density: {m['density']}")
    print(f"Avg out-degree: {m['avg_out_degree']}")
    print(f"Avg in-degree: {m['avg_in_degree']}")
    print(f"Connected components: {m['connected_components']}")
    print(f"Largest component: {m['largest_component_size']}")

    if result["dead_links"]:
        print(f"\n\033[31mDead links ({len(result['dead_links'])}):\033[0m")
        for dl in result["dead_links"]:
            print(f"  {dl['from']} -> {dl['to']}")

    if result["self_links"]:
        print(f"\n\033[33mSelf-links ({len(result['self_links'])}):\033[0m")
        for sl in result["self_links"]:
            print(f"  {sl}")

    if result["orphans"]:
        print(f"\n\033[33mOrphans ({len(result['orphans'])}):\033[0m")
        for o in result["orphans"]:
            print(f"  {o}")

    if result.get("links_md_stale"):
        print(f"\n\033[33mStale entries in links.md ({len(result['links_md_stale'])}):\033[0m")
        for e in result["links_md_stale"][:20]:
            print(f"  {e['article']}: {e['direction']} -> {e['link']}")

    if result.get("links_md_missing"):
        print(f"\n\033[33mMissing from links.md ({len(result['links_md_missing'])}):\033[0m")
        for e in result["links_md_missing"][:20]:
            print(f"  {e['article']}: {e['direction']} -> {e['link']}")

    print()
    if result["ok"]:
        print("\033[32mAll checks passed.\033[0m")
    else:
        print(f"\033[31mIssues found: {', '.join(result['issues'])}\033[0m")
    print()


def main():
    parser = argparse.ArgumentParser(description="Link Graph Validator")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    result = run_checks()

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    sys.exit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
