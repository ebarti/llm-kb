#!/usr/bin/env python3
"""
Word count plugin — tracks word count statistics over time.

Hook: post_compile
Updates wiki/_meta/stats.json with current word counts and historical data.
"""

import json
import os
import re
from datetime import datetime


def register():
    return {"post_compile": run_post_compile}


def count_words(text):
    """Count words in text, stripping markdown syntax."""
    # Remove frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Remove markdown links but keep text
    text = re.sub(r"\[\[([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r"`[^`]*`", "", text)
    # Remove headers markers
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    # Count words
    words = text.split()
    return len(words)


def run_post_compile(root, *args):
    """Update word count statistics."""
    wiki_dir = os.path.join(root, "wiki")
    meta_dir = os.path.join(wiki_dir, "_meta")
    stats_path = os.path.join(meta_dir, "stats.json")

    os.makedirs(meta_dir, exist_ok=True)

    # Load existing stats
    stats = {}
    if os.path.exists(stats_path):
        try:
            with open(stats_path, "r") as f:
                stats = json.load(f)
        except (json.JSONDecodeError, OSError):
            stats = {}

    # Count words per directory and per file
    total_words = 0
    file_counts = {}
    dir_counts = {}

    for dirpath, _, filenames in os.walk(wiki_dir):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(fpath, wiki_dir)
            try:
                with open(fpath, "r", errors="replace") as f:
                    text = f.read()
            except OSError:
                continue

            wc = count_words(text)
            file_counts[relpath] = wc
            total_words += wc

            # Aggregate by top-level directory
            top_dir = relpath.split(os.sep)[0] if os.sep in relpath else "(root)"
            dir_counts[top_dir] = dir_counts.get(top_dir, 0) + wc

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Update current snapshot
    stats["current"] = {
        "total_words": total_words,
        "total_files": len(file_counts),
        "by_directory": dict(sorted(dir_counts.items())),
        "timestamp": now,
    }

    # Append to history (keep last 100 entries)
    history = stats.get("history", [])
    history.append({
        "timestamp": now,
        "total_words": total_words,
        "total_files": len(file_counts),
    })
    stats["history"] = history[-100:]

    # Top files by word count
    top_files = sorted(file_counts.items(), key=lambda x: -x[1])[:20]
    stats["current"]["top_files"] = [
        {"file": f, "words": w} for f, w in top_files
    ]

    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
        f.write("\n")

    print(f"  [word_count] Total: {total_words:,} words across {len(file_counts)} files")
    print(f"  [word_count] Stats saved to wiki/_meta/stats.json")

    # Show per-directory breakdown
    for d, wc in sorted(dir_counts.items(), key=lambda x: -x[1]):
        print(f"    {d}: {wc:,} words")
