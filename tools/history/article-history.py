#!/usr/bin/env python3
"""Article History Viewer — shows the full edit history of a specific wiki article."""

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def git(*args, cwd=None):
    result = subprocess.run(
        ["git"] + list(args),
        capture_output=True, text=True,
        cwd=cwd or ROOT,
    )
    return result.stdout.strip()


def get_file_log(filepath):
    """Get all commits that touched this file."""
    raw = git("log", "--follow", "--pretty=format:%H|%ai|%an|%s", "--", filepath)
    if not raw:
        return []
    commits = []
    for line in raw.splitlines():
        parts = line.split("|", 3)
        if len(parts) == 4:
            commits.append({
                "hash": parts[0],
                "date": parts[1].strip(),
                "author": parts[2].strip(),
                "subject": parts[3].strip(),
            })
    return commits


def get_diff_for_commit(commit_hash, filepath):
    """Get the diff for a file at a specific commit."""
    diff = git("diff", f"{commit_hash}~1..{commit_hash}", "--", filepath)
    if not diff:
        # Might be the initial commit — show full addition
        diff = git("show", f"{commit_hash}", "--", filepath)
    return diff


def summarize_diff(diff_text):
    """Produce a human-readable summary of a diff."""
    if not diff_text:
        return "  (no diff available)"

    added = 0
    removed = 0
    sections_changed = set()
    lines_sample = []

    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            added += 1
            clean = line[1:].strip()
            if clean.startswith("## "):
                sections_changed.add(clean.lstrip("# ").strip())
            elif clean and len(lines_sample) < 5:
                if len(clean) > 100:
                    clean = clean[:100] + "..."
                lines_sample.append(f"    + {clean}")
        elif line.startswith("-") and not line.startswith("---"):
            removed += 1
            clean = line[1:].strip()
            if clean.startswith("## "):
                sections_changed.add(clean.lstrip("# ").strip())

    parts = []
    parts.append(f"  Lines: +{added} / -{removed}")
    if sections_changed:
        parts.append(f"  Sections touched: {', '.join(sorted(sections_changed))}")
    if lines_sample:
        parts.append("  Sample changes:")
        parts.extend(lines_sample)
    return "\n".join(parts)


def get_file_stats(filepath):
    """Get current file stats."""
    full = ROOT / filepath if not Path(filepath).is_absolute() else Path(filepath)
    if not full.exists():
        return None
    text = full.read_text(errors="ignore")
    words = len(text.split())
    lines = text.count("\n")
    links = len(re.findall(r'\[\[.+?\]\]', text))
    return {"words": words, "lines": lines, "links": links}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 article-history.py <path-to-wiki-article>")
        print("Example: python3 article-history.py wiki/concepts/llm-knowledge-base.md")
        sys.exit(1)

    filepath = sys.argv[1]
    # Make path relative to repo root if absolute
    if os.path.isabs(filepath):
        try:
            filepath = str(Path(filepath).relative_to(ROOT))
        except ValueError:
            pass

    full_path = ROOT / filepath
    exists = full_path.exists()

    print(f"{'=' * 60}")
    print(f"Article History: {filepath}")
    print(f"{'=' * 60}")
    print()

    if exists:
        stats = get_file_stats(filepath)
        if stats:
            print(f"Current state: {stats['words']} words, {stats['lines']} lines, {stats['links']} wikilinks")
            print()

    commits = get_file_log(filepath)
    if not commits:
        print("No git history found for this file.")
        if not exists:
            print(f"(File does not exist at {full_path})")
        sys.exit(1)

    print(f"Total edits: {len(commits)}")
    print(f"Created: {commits[-1]['date']}")
    if len(commits) > 1:
        print(f"Last modified: {commits[0]['date']}")
    print()

    for i, commit in enumerate(commits):
        if i == len(commits) - 1:
            label = "CREATED"
        else:
            label = "MODIFIED"

        print(f"--- [{label}] {commit['date']} ---")
        print(f"  Commit: {commit['hash'][:10]}")
        print(f"  Author: {commit['author']}")
        print(f"  Message: {commit['subject']}")

        diff = get_diff_for_commit(commit["hash"], filepath)
        print(summarize_diff(diff))
        print()


if __name__ == "__main__":
    main()
