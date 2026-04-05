#!/usr/bin/env python3
"""Snapshot Tool — creates and compares point-in-time wiki statistics snapshots."""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
SNAPSHOTS_DIR = Path(__file__).resolve().parent / ".snapshots"


def gather_stats():
    """Walk the wiki directory and gather comprehensive statistics."""
    stats = {
        "timestamp": datetime.now().isoformat(),
        "files": {
            "total": 0,
            "concepts": 0,
            "sources": 0,
            "entities": 0,
            "comparisons": 0,
            "meta": 0,
            "other": 0,
        },
        "words": {
            "total": 0,
            "concepts": 0,
            "sources": 0,
            "entities": 0,
            "comparisons": 0,
            "other": 0,
        },
        "lines": {
            "total": 0,
        },
        "links": {
            "total": 0,
            "unique_targets": 0,
        },
        "tags": {},
        "file_list": [],
    }

    all_links = []
    tag_counts = defaultdict(int)

    for md in sorted(WIKI.rglob("*.md")):
        rel = str(md.relative_to(WIKI))
        text = md.read_text(errors="ignore")
        words = len(text.split())
        lines = text.count("\n")
        links = re.findall(r'\[\[(.+?)\]\]', text)

        stats["files"]["total"] += 1
        stats["words"]["total"] += words
        stats["lines"]["total"] += lines
        stats["links"]["total"] += len(links)
        all_links.extend(links)

        # Classify
        if rel.startswith("concepts/"):
            cat = "concepts"
        elif rel.startswith("sources/"):
            cat = "sources"
        elif rel.startswith("entities/"):
            cat = "entities"
        elif rel.startswith("comparisons/"):
            cat = "comparisons"
        elif rel.startswith("_meta/"):
            cat = "meta"
        else:
            cat = "other"

        stats["files"][cat] = stats["files"].get(cat, 0) + 1
        if cat in stats["words"]:
            stats["words"][cat] += words

        # Extract tags from frontmatter
        tag_match = re.findall(r'^tags:\s*\[(.+?)\]', text, re.MULTILINE)
        if tag_match:
            for tag_str in tag_match:
                for tag in re.findall(r'["\']?([^"\'`,]+)["\']?', tag_str):
                    tag = tag.strip()
                    if tag:
                        tag_counts[tag] += 1

        # Extract type from frontmatter
        type_match = re.search(r'^type:\s*(.+)$', text, re.MULTILINE)
        ftype = type_match.group(1).strip().strip('"\'') if type_match else "unknown"

        stats["file_list"].append({
            "path": rel,
            "category": cat,
            "type": ftype,
            "words": words,
            "links": len(links),
        })

    stats["links"]["unique_targets"] = len(set(all_links))
    stats["tags"] = dict(tag_counts)

    return stats


def save_snapshot(date_str=None):
    """Save a snapshot to disk."""
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    stats = gather_stats()

    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    path = SNAPSHOTS_DIR / f"{date_str}.json"
    with open(path, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Snapshot saved to {path}")
    print(f"  Files: {stats['files']['total']} "
          f"(concepts={stats['files']['concepts']}, sources={stats['files']['sources']}, "
          f"entities={stats['files']['entities']}, comparisons={stats['files']['comparisons']})")
    print(f"  Words: {stats['words']['total']:,}")
    print(f"  Lines: {stats['lines']['total']:,}")
    print(f"  Links: {stats['links']['total']} ({stats['links']['unique_targets']} unique targets)")
    if stats["tags"]:
        top_tags = sorted(stats["tags"].items(), key=lambda x: -x[1])[:10]
        print(f"  Top tags: {', '.join(f'{t}({c})' for t, c in top_tags)}")
    return stats


def load_snapshot(date_str):
    """Load a snapshot from disk."""
    path = SNAPSHOTS_DIR / f"{date_str}.json"
    if not path.exists():
        print(f"Snapshot not found: {path}")
        return None
    with open(path) as f:
        return json.load(f)


def compare_snapshots(date1, date2):
    """Compare two snapshots and print differences."""
    snap1 = load_snapshot(date1)
    snap2 = load_snapshot(date2)
    if not snap1 or not snap2:
        sys.exit(1)

    print(f"{'=' * 60}")
    print(f"Snapshot Comparison: {date1} -> {date2}")
    print(f"{'=' * 60}")
    print()

    def delta(a, b):
        d = b - a
        return f"+{d}" if d >= 0 else str(d)

    print(f"{'Metric':<30} {'Before':>10} {'After':>10} {'Change':>10}")
    print(f"{'-' * 60}")

    # Files
    for key in ["total", "concepts", "sources", "entities", "comparisons", "meta", "other"]:
        v1 = snap1["files"].get(key, 0)
        v2 = snap2["files"].get(key, 0)
        label = f"Files ({key})"
        print(f"{label:<30} {v1:>10} {v2:>10} {delta(v1, v2):>10}")

    print()

    # Words
    for key in ["total", "concepts", "sources"]:
        v1 = snap1["words"].get(key, 0)
        v2 = snap2["words"].get(key, 0)
        label = f"Words ({key})"
        print(f"{label:<30} {v1:>10,} {v2:>10,} {delta(v1, v2):>10}")

    print()

    # Links
    v1 = snap1["links"]["total"]
    v2 = snap2["links"]["total"]
    print(f"{'Links (total)':<30} {v1:>10} {v2:>10} {delta(v1, v2):>10}")
    v1 = snap1["links"]["unique_targets"]
    v2 = snap2["links"]["unique_targets"]
    print(f"{'Links (unique targets)':<30} {v1:>10} {v2:>10} {delta(v1, v2):>10}")

    print()

    # New files
    files1 = {f["path"] for f in snap1.get("file_list", [])}
    files2 = {f["path"] for f in snap2.get("file_list", [])}
    new_files = files2 - files1
    removed_files = files1 - files2

    if new_files:
        print(f"New files ({len(new_files)}):")
        for f in sorted(new_files):
            print(f"  + {f}")
    if removed_files:
        print(f"Removed files ({len(removed_files)}):")
        for f in sorted(removed_files):
            print(f"  - {f}")

    # Tag changes
    tags1 = snap1.get("tags", {})
    tags2 = snap2.get("tags", {})
    all_tags = set(tags1.keys()) | set(tags2.keys())
    if all_tags:
        print()
        print("Tag changes:")
        for tag in sorted(all_tags):
            t1 = tags1.get(tag, 0)
            t2 = tags2.get(tag, 0)
            if t1 != t2:
                print(f"  {tag}: {t1} -> {t2} ({delta(t1, t2)})")


def list_snapshots():
    """List all available snapshots."""
    if not SNAPSHOTS_DIR.exists():
        print("No snapshots found.")
        return
    snaps = sorted(SNAPSHOTS_DIR.glob("*.json"))
    if not snaps:
        print("No snapshots found.")
        return
    print("Available snapshots:")
    for s in snaps:
        data = json.loads(s.read_text())
        print(f"  {s.stem} — {data['files']['total']} files, {data['words']['total']:,} words")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 snapshot.py save [YYYY-MM-DD]   Save a snapshot (default: today)")
        print("  python3 snapshot.py compare DATE1 DATE2  Compare two snapshots")
        print("  python3 snapshot.py list                 List available snapshots")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "save":
        date_str = sys.argv[2] if len(sys.argv) > 2 else None
        save_snapshot(date_str)
    elif cmd == "compare":
        if len(sys.argv) < 4:
            print("Usage: python3 snapshot.py compare DATE1 DATE2")
            sys.exit(1)
        compare_snapshots(sys.argv[2], sys.argv[3])
    elif cmd == "list":
        list_snapshots()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
