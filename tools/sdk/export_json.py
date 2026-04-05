#!/usr/bin/env python3
"""
Export the entire LLM Knowledge Base as a single JSON file.

Includes all articles (frontmatter + content + links), the full
link graph, statistics, and summaries.

Output: output/wiki-export.json

Usage:
    python3 tools/sdk/export_json.py
    python3 tools/sdk/export_json.py --output /path/to/output.json
    python3 tools/sdk/export_json.py --kb-path /path/to/kb
"""

import sys
import os
import json
import argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb import KnowledgeBase


def main():
    parser = argparse.ArgumentParser(description="Export KB as JSON")
    parser.add_argument("--kb-path", default="/Users/eloibarti/Desktop/agentic-ai",
                        help="Path to the knowledge base root")
    parser.add_argument("--output", default=None,
                        help="Output file path (default: output/wiki-export.json)")
    parser.add_argument("--compact", action="store_true",
                        help="Compact JSON (no indentation)")
    args = parser.parse_args()

    kb = KnowledgeBase(path=args.kb_path)

    print("Exporting knowledge base...")
    data = kb.export_all()

    # Determine output path
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = kb.output_dir / "wiki-export.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)

    indent = None if args.compact else 2
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

    size_kb = out_path.stat().st_size / 1024

    print(f"\nExport complete!")
    print(f"  Output:     {out_path}")
    print(f"  Articles:   {len(data['articles'])}")
    print(f"  Links:      {data['stats']['total_links']}")
    print(f"  Words:      {data['stats']['total_words']:,}")
    print(f"  File size:  {size_kb:.1f} KB")

    # Summary by type
    print(f"\n  By type:")
    for t, count in sorted(data["stats"]["by_type"].items(), key=lambda x: x[1], reverse=True):
        print(f"    {t:25s} {count}")


if __name__ == "__main__":
    main()
