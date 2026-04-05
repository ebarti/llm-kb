#!/usr/bin/env python3
"""
CLI for the LLM Knowledge Base SDK.

Provides command-line access to search, stats, articles, links,
orphans, hubs, tags, and JSON export.

Usage:
    python3 tools/sdk/cli.py search "knowledge graph"
    python3 tools/sdk/cli.py stats
    python3 tools/sdk/cli.py article "concepts/llm-knowledge-base"
    python3 tools/sdk/cli.py links "concepts/llm-knowledge-base"
    python3 tools/sdk/cli.py orphans
    python3 tools/sdk/cli.py hubs
    python3 tools/sdk/cli.py tags
    python3 tools/sdk/cli.py export-json

    Add --json to any command for JSON output.
"""

import sys
import os
import json
import argparse
import textwrap

# Allow running from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb import KnowledgeBase


def fmt_table(rows: list[list[str]], headers: list[str]) -> str:
    """Format a simple text table."""
    all_rows = [headers] + rows
    widths = [max(len(str(cell)) for cell in col) for col in zip(*all_rows)]
    lines = []
    header_line = "  ".join(str(h).ljust(w) for h, w in zip(headers, widths))
    lines.append(header_line)
    lines.append("  ".join("-" * w for w in widths))
    for row in rows:
        lines.append("  ".join(str(c).ljust(w) for c, w in zip(row, widths)))
    return "\n".join(lines)


def cmd_search(kb: KnowledgeBase, args: argparse.Namespace):
    """Search the knowledge base."""
    results = kb.search(args.query, type=args.type, top_k=args.top_k)
    if args.json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print("No results found.")
        return

    print(f"Search results for: \"{args.query}\"\n")
    rows = []
    for r in results:
        rows.append([str(r["score"]), r["type"], r["path"], r["summary"][:80]])
    print(fmt_table(rows, ["Score", "Type", "Path", "Summary"]))


def cmd_stats(kb: KnowledgeBase, args: argparse.Namespace):
    """Show knowledge base statistics."""
    stats = kb.get_stats()
    if args.json:
        print(json.dumps(stats, indent=2))
        return

    print("Knowledge Base Statistics")
    print("=" * 40)
    print(f"Total articles:       {stats['total_articles']}")
    print(f"Total words:          {stats['total_words']:,}")
    print(f"Avg words/article:    {stats['avg_words_per_article']:,}")
    print(f"Total links:          {stats['total_links']}")
    print(f"Orphan articles:      {stats['orphan_count']}")
    print(f"Raw source files:     {stats['raw_files']}")
    print()
    print("Articles by type:")
    for t, count in sorted(stats["by_type"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {t:25s} {count}")


def cmd_article(kb: KnowledgeBase, args: argparse.Namespace):
    """Show a single article."""
    try:
        article = kb.get_article(args.path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(article, indent=2))
        return

    fm = article["frontmatter"]
    print(f"Title: {fm.get('title', article['path'])}")
    print(f"Type:  {fm.get('type', 'unknown')}")
    if fm.get("summary"):
        print(f"Summary: {fm['summary']}")
    if article["links"]:
        print(f"Links: {', '.join(article['links'][:10])}")
        if len(article["links"]) > 10:
            print(f"  ... and {len(article['links']) - 10} more")
    print()
    print(article["content"])


def cmd_links(kb: KnowledgeBase, args: argparse.Namespace):
    """Show links for an article."""
    links = kb.get_links(args.article)
    if args.json:
        print(json.dumps(links, indent=2))
        return

    print(f"Links for: {args.article}\n")
    print("Outgoing:")
    for link in links.get("outgoing", []):
        print(f"  -> {link}")
    if not links.get("outgoing"):
        print("  (none)")

    print("\nIncoming (backlinks):")
    for link in links.get("incoming", []):
        print(f"  <- {link}")
    if not links.get("incoming"):
        print("  (none)")


def cmd_orphans(kb: KnowledgeBase, args: argparse.Namespace):
    """Find orphan articles."""
    orphans = kb.get_orphans()
    if args.json:
        print(json.dumps(orphans, indent=2))
        return

    if not orphans:
        print("No orphan articles found.")
        return

    print(f"Orphan articles ({len(orphans)}):\n")
    for o in orphans:
        print(f"  {o}")


def cmd_hubs(kb: KnowledgeBase, args: argparse.Namespace):
    """Find hub articles."""
    hubs = kb.get_hubs(top_k=args.top_k)
    if args.json:
        print(json.dumps(hubs, indent=2))
        return

    print(f"Top {len(hubs)} hub articles:\n")
    rows = []
    for h in hubs:
        rows.append([h["path"], str(h["incoming"]), str(h["outgoing"]), str(h["total"])])
    print(fmt_table(rows, ["Path", "In", "Out", "Total"]))


def cmd_tags(kb: KnowledgeBase, args: argparse.Namespace):
    """Show tag cloud."""
    tags = kb.get_tag_cloud()
    if args.json:
        print(json.dumps(tags, indent=2))
        return

    if not tags:
        print("No tags found. Articles may not use frontmatter tags or inline #tags yet.")
        return

    print("Tag Cloud:\n")
    for tag, count in tags.items():
        bar = "#" * count
        print(f"  {tag:30s} {count:3d}  {bar}")


def cmd_export_json(kb: KnowledgeBase, args: argparse.Namespace):
    """Export entire wiki as JSON."""
    data = kb.export_all()

    output_dir = kb.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "wiki-export.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(data['articles'])} articles to {out_path}")
    print(f"  Links: {data['stats']['total_links']}")
    print(f"  Words: {data['stats']['total_words']:,}")
    print(f"  Size:  {out_path.stat().st_size / 1024:.1f} KB")


def cmd_log(kb: KnowledgeBase, args: argparse.Namespace):
    """Show recent activity log."""
    entries = kb.get_log(n=args.n)
    if args.json:
        print(json.dumps(entries, indent=2))
        return

    if not entries:
        print("No log entries found.")
        return

    print(f"Recent activity ({len(entries)} entries):\n")
    for entry in entries:
        print(f"[{entry['date']}] {entry['action']} | {entry['description']}")
        for detail in entry["details"]:
            print(f"  - {detail}")
        print()


def main():
    parser = argparse.ArgumentParser(
        prog="kb",
        description="CLI for the LLM Knowledge Base SDK",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              python3 tools/sdk/cli.py search "knowledge graph"
              python3 tools/sdk/cli.py stats --json
              python3 tools/sdk/cli.py article "concepts/llm-knowledge-base"
              python3 tools/sdk/cli.py links "concepts/llm-knowledge-base"
              python3 tools/sdk/cli.py orphans
              python3 tools/sdk/cli.py hubs --top-k 5
              python3 tools/sdk/cli.py tags
              python3 tools/sdk/cli.py log --n 5
              python3 tools/sdk/cli.py export-json
        """),
    )
    parser.add_argument("--kb-path", default="/Users/eloibarti/Desktop/agentic-ai",
                        help="Path to the knowledge base root")

    # Shared flags available on every subcommand
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--json", action="store_true", help="Output as JSON")

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # search
    p_search = subparsers.add_parser("search", parents=[shared], help="Search the knowledge base")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--type", help="Filter by article type")
    p_search.add_argument("--top-k", type=int, default=10, help="Max results")

    # stats
    subparsers.add_parser("stats", parents=[shared], help="Show statistics")

    # article
    p_article = subparsers.add_parser("article", parents=[shared], help="Show a single article")
    p_article.add_argument("path", help="Article path (e.g. concepts/llm-knowledge-base)")

    # links
    p_links = subparsers.add_parser("links", parents=[shared], help="Show links for an article")
    p_links.add_argument("article", help="Article path")

    # orphans
    subparsers.add_parser("orphans", parents=[shared], help="Find orphan articles")

    # hubs
    p_hubs = subparsers.add_parser("hubs", parents=[shared], help="Find hub articles")
    p_hubs.add_argument("--top-k", type=int, default=10, help="Number of hubs")

    # tags
    subparsers.add_parser("tags", parents=[shared], help="Show tag cloud")

    # log
    p_log = subparsers.add_parser("log", parents=[shared], help="Show activity log")
    p_log.add_argument("--n", type=int, default=10, help="Number of entries")

    # export-json
    subparsers.add_parser("export-json", parents=[shared], help="Export wiki as JSON")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    kb = KnowledgeBase(path=args.kb_path)

    commands = {
        "search": cmd_search,
        "stats": cmd_stats,
        "article": cmd_article,
        "links": cmd_links,
        "orphans": cmd_orphans,
        "hubs": cmd_hubs,
        "tags": cmd_tags,
        "log": cmd_log,
        "export-json": cmd_export_json,
    }

    commands[args.command](kb, args)


if __name__ == "__main__":
    main()
