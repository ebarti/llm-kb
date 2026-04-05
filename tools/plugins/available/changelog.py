#!/usr/bin/env python3
"""
Changelog plugin — generates a changelog from git history.

Hook: post_compile
Reads git log for wiki/ changes and generates wiki/Changelog.md
showing what articles were added/modified per commit.
"""

import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime


def register():
    return {"post_compile": run_post_compile}


def run_git(args, cwd):
    """Run a git command and return stdout, or None on error."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def run_post_compile(root, *args):
    """Generate changelog from git history."""
    wiki_dir = os.path.join(root, "wiki")

    # Check if we're in a git repo
    if run_git(["rev-parse", "--git-dir"], root) is None:
        print("  [changelog] Not a git repository, generating from file timestamps.")
        generate_from_timestamps(root, wiki_dir)
        return

    # Get git log for wiki/ and raw/ directories
    log_output = run_git([
        "log", "--pretty=format:%H|%ai|%s",
        "--name-status", "--diff-filter=ACDMR",
        "-50",  # Last 50 commits
        "--", "wiki/", "raw/"
    ], root)

    if not log_output:
        print("  [changelog] No git history found, generating from file timestamps.")
        generate_from_timestamps(root, wiki_dir)
        return

    # Parse git log
    entries = []
    current_commit = None

    for line in log_output.split("\n"):
        if not line.strip():
            continue

        # Commit header line
        if "|" in line and not line.startswith(("A\t", "M\t", "D\t", "R\t", "C\t")):
            parts = line.split("|", 2)
            if len(parts) == 3:
                current_commit = {
                    "hash": parts[0][:8],
                    "date": parts[1].strip()[:10],
                    "message": parts[2].strip(),
                    "added": [],
                    "modified": [],
                    "deleted": [],
                }
                entries.append(current_commit)
        elif current_commit and "\t" in line:
            status, filepath = line.split("\t", 1)
            filepath = filepath.strip()
            if not filepath.endswith(".md"):
                continue
            name = os.path.basename(filepath).replace(".md", "")
            display = filepath

            if status.startswith("A"):
                current_commit["added"].append(display)
            elif status.startswith("M"):
                current_commit["modified"].append(display)
            elif status.startswith("D"):
                current_commit["deleted"].append(display)

    generate_changelog(wiki_dir, entries)


def generate_from_timestamps(root, wiki_dir):
    """Fallback: generate changelog from file modification times."""
    entries = []
    files_by_date = defaultdict(list)

    for dirpath, _, filenames in os.walk(wiki_dir):
        rel_dir = os.path.relpath(dirpath, wiki_dir)
        if rel_dir.startswith("_meta"):
            continue
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            if fname in ("Changelog.md", "Glossary.md", "Reading-List.md"):
                continue
            fpath = os.path.join(dirpath, fname)
            mtime = os.path.getmtime(fpath)
            date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            relpath = os.path.relpath(fpath, wiki_dir)
            files_by_date[date_str].append(relpath)

    # Also check raw/
    raw_dir = os.path.join(root, "raw")
    if os.path.isdir(raw_dir):
        for fname in os.listdir(raw_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(raw_dir, fname)
            mtime = os.path.getmtime(fpath)
            date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            files_by_date[date_str].append(f"raw/{fname}")

    for date_str in sorted(files_by_date.keys(), reverse=True):
        files = files_by_date[date_str]
        entries.append({
            "hash": "",
            "date": date_str,
            "message": f"Files modified on {date_str}",
            "added": files,
            "modified": [],
            "deleted": [],
        })

    generate_changelog(wiki_dir, entries)


def generate_changelog(wiki_dir, entries):
    """Write the changelog file from parsed entries."""
    now = datetime.now().strftime("%Y-%m-%d")
    lines = [
        "---",
        'title: "Changelog"',
        "type: meta",
        f"last_updated: {now}",
        "---",
        "",
        "# Changelog",
        "",
        "Recent changes to the knowledge base.",
        "",
    ]

    if not entries:
        lines.append("_No changes recorded yet._")
    else:
        current_date = None
        for entry in entries:
            date = entry["date"]
            if date != current_date:
                lines.append(f"## {date}")
                lines.append("")
                current_date = date

            msg = entry["message"]
            hash_str = f" `{entry['hash']}`" if entry["hash"] else ""
            lines.append(f"### {msg}{hash_str}")
            lines.append("")

            if entry["added"]:
                for f in entry["added"]:
                    name = os.path.basename(f).replace(".md", "")
                    lines.append(f"- **Added**: {f}")
            if entry["modified"]:
                for f in entry["modified"]:
                    lines.append(f"- **Modified**: {f}")
            if entry["deleted"]:
                for f in entry["deleted"]:
                    lines.append(f"- **Deleted**: {f}")

            if not entry["added"] and not entry["modified"] and not entry["deleted"]:
                lines.append("- _(no wiki file changes)_")

            lines.append("")

    changelog_path = os.path.join(wiki_dir, "Changelog.md")
    with open(changelog_path, "w") as f:
        f.write("\n".join(lines))

    total_changes = sum(
        len(e["added"]) + len(e["modified"]) + len(e["deleted"])
        for e in entries
    )
    print(f"  [changelog] Generated changelog with {len(entries)} entries, "
          f"{total_changes} file changes")
    print(f"  [changelog] Written to wiki/Changelog.md")
