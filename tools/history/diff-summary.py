#!/usr/bin/env python3
"""Diff Summary Tool — human-readable summary of wiki changes between two commits."""

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


def get_head():
    return git("rev-parse", "HEAD")


def get_previous_commit():
    """Get the commit before HEAD."""
    log = git("log", "--pretty=format:%H", "-2")
    lines = log.splitlines()
    if len(lines) >= 2:
        return lines[1]
    return lines[0] if lines else None


def get_changed_files(commit_from, commit_to):
    """Get list of changed wiki files between two commits."""
    raw = git("diff", "--name-status", commit_from, commit_to, "--", "wiki/")
    files = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            op = parts[0][0]
            fpath = parts[-1]
            files.append((op, fpath))
    return files


def get_file_diff(commit_from, commit_to, filepath):
    """Get diff for a specific file."""
    return git("diff", commit_from, commit_to, "--", filepath)


def summarize_file_diff(diff_text, filepath):
    """Create human-readable summary of changes to a file."""
    if not diff_text:
        return "No changes detected"

    added_lines = []
    removed_lines = []
    sections_added = []
    sections_removed = []
    frontmatter_changes = []
    in_frontmatter = False

    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            content = line[1:].strip()
            if content == "---":
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                frontmatter_changes.append(f"  + {content}")
            elif content.startswith("## "):
                sections_added.append(content.lstrip("# ").strip())
            else:
                added_lines.append(content)
        elif line.startswith("-") and not line.startswith("---"):
            content = line[1:].strip()
            if content == "---":
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                frontmatter_changes.append(f"  - {content}")
            elif content.startswith("## "):
                sections_removed.append(content.lstrip("# ").strip())
            else:
                removed_lines.append(content)

    parts = []
    parts.append(f"  +{len(added_lines)} / -{len(removed_lines)} content lines")

    if sections_added:
        parts.append(f"  New sections: {', '.join(sections_added)}")
    if sections_removed:
        parts.append(f"  Removed sections: {', '.join(sections_removed)}")
    if frontmatter_changes:
        parts.append("  Frontmatter changes:")
        for fc in frontmatter_changes[:5]:
            parts.append(f"    {fc}")

    # Show a few representative added lines
    meaningful = [l for l in added_lines if len(l) > 20 and not l.startswith(("```", "---", "|||"))]
    if meaningful:
        parts.append("  Key additions:")
        for line in meaningful[:3]:
            preview = line[:100] + "..." if len(line) > 100 else line
            parts.append(f"    > {preview}")

    return "\n".join(parts)


def extract_summary(filepath):
    """Extract summary from frontmatter."""
    full = ROOT / filepath
    if not full.exists():
        return ""
    text = full.read_text(errors="ignore")
    match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    return match.group(1)[:120] if match else ""


def file_to_wikilink(fpath):
    rel = fpath.replace("wiki/", "", 1)
    if rel.endswith(".md"):
        rel = rel[:-3]
    return f"[[{rel}]]"


def main():
    if len(sys.argv) == 3:
        commit_from = sys.argv[1]
        commit_to = sys.argv[2]
    elif len(sys.argv) == 1:
        commit_to = get_head()
        commit_from = get_previous_commit()
        if not commit_from or commit_from == commit_to:
            print("Only one commit in history. Showing all wiki files as new.")
            commit_from = git("hash-object", "-t", "tree", "/dev/null")  # empty tree
            if not commit_from:
                commit_from = "4b825dc642cb6eb9a060e54bf899d15f71799817"  # git empty tree
    else:
        print("Usage: python3 diff-summary.py [commit_from commit_to]")
        print("  Defaults to comparing last commit with HEAD")
        sys.exit(1)

    short_from = commit_from[:10]
    short_to = commit_to[:10]

    print(f"{'=' * 60}")
    print(f"Wiki Diff Summary")
    print(f"{'=' * 60}")
    print(f"Comparing: {short_from} -> {short_to}")
    print()

    # Check for working tree changes (unstaged)
    working_changes = git("diff", "--name-status", "--", "wiki/")
    staged_changes = git("diff", "--cached", "--name-status", "--", "wiki/")

    files = get_changed_files(commit_from, commit_to)
    if not files:
        print("No wiki changes between these commits.")
        if working_changes or staged_changes:
            print("\nHowever, there are uncommitted changes:")
            if working_changes:
                print(f"  Unstaged:\n    {working_changes.replace(chr(10), chr(10) + '    ')}")
            if staged_changes:
                print(f"  Staged:\n    {staged_changes.replace(chr(10), chr(10) + '    ')}")
        return

    added = [(op, f) for op, f in files if op == "A"]
    modified = [(op, f) for op, f in files if op == "M"]
    deleted = [(op, f) for op, f in files if op == "D"]

    print(f"Summary: {len(added)} added, {len(modified)} modified, {len(deleted)} deleted")
    print()

    if added:
        print(f"--- NEW FILES ({len(added)}) ---")
        for _, fpath in sorted(added, key=lambda x: x[1]):
            link = file_to_wikilink(fpath)
            summary = extract_summary(fpath)
            desc = f" — {summary}" if summary else ""
            print(f"  + {link}{desc}")
        print()

    if modified:
        print(f"--- MODIFIED FILES ({len(modified)}) ---")
        for _, fpath in sorted(modified, key=lambda x: x[1]):
            link = file_to_wikilink(fpath)
            print(f"  ~ {link}")
            diff = get_file_diff(commit_from, commit_to, fpath)
            print(summarize_file_diff(diff, fpath))
            print()

    if deleted:
        print(f"--- DELETED FILES ({len(deleted)}) ---")
        for _, fpath in sorted(deleted, key=lambda x: x[1]):
            link = file_to_wikilink(fpath)
            print(f"  - {link}")
        print()

    # Also show uncommitted changes
    if working_changes or staged_changes:
        print(f"--- UNCOMMITTED CHANGES ---")
        if working_changes:
            for line in working_changes.splitlines():
                print(f"  (unstaged) {line}")
        if staged_changes:
            for line in staged_changes.splitlines():
                print(f"  (staged) {line}")
        print()


if __name__ == "__main__":
    main()
