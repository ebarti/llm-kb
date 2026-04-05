#!/usr/bin/env python3
"""Wiki Changelog Generator — parses git log to produce a human-readable changelog."""

import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
OUTPUT = WIKI / "Changelog.md"


def git(*args, cwd=None):
    result = subprocess.run(
        ["git"] + list(args),
        capture_output=True, text=True,
        cwd=cwd or ROOT,
    )
    return result.stdout.strip()


def get_commits():
    """Return list of (hash, date, subject) touching wiki/ files."""
    raw = git("log", "--all", "--pretty=format:%H|%ai|%s", "--name-status", "--", "wiki/")
    if not raw:
        # Fallback: look at all commits and filter wiki changes
        raw = git("log", "--all", "--pretty=format:%H|%ai|%s", "--name-status")
    commits = []
    current = None
    for line in raw.splitlines():
        if "|" in line and len(line.split("|")) >= 3 and not line.startswith(("A\t", "M\t", "D\t", "R")):
            parts = line.split("|", 2)
            current = {
                "hash": parts[0],
                "date": parts[1].strip().split(" ")[0],
                "subject": parts[2],
                "files": [],
            }
            commits.append(current)
        elif current and line.strip():
            # Parse name-status line
            parts = line.split("\t")
            if len(parts) >= 2:
                op = parts[0][0]  # A, M, D, R
                fpath = parts[-1]
                if fpath.startswith("wiki/"):
                    current["files"].append((op, fpath))
    return commits


def get_diff_sections(commit_hash, filepath):
    """For a modified file, return which sections (## headings) changed."""
    diff = git("diff", f"{commit_hash}~1..{commit_hash}", "--", filepath)
    if not diff:
        # Try first commit
        diff = git("diff", "--no-index", "/dev/null", filepath)
    sections = set()
    for line in diff.splitlines():
        if line.startswith("@@") and "##" in line:
            # Extract section from hunk header context
            match = re.search(r"##\s+(.+)", line.split("@@")[-1])
            if match:
                sections.add(match.group(1).strip())
        elif line.startswith("+") and line.startswith("+ ## ") or line.startswith("+## "):
            heading = line.lstrip("+").strip().lstrip("# ").strip()
            if heading:
                sections.add(heading)
    return sorted(sections)


def extract_summary(filepath):
    """Extract summary from frontmatter."""
    full = ROOT / filepath if not Path(filepath).is_absolute() else Path(filepath)
    if not full.exists():
        return ""
    text = full.read_text(errors="ignore")
    match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    if match:
        return match.group(1)[:120]
    return ""


def extract_source_url(filepath):
    """Extract source URL from a source article."""
    full = ROOT / filepath if not Path(filepath).is_absolute() else Path(filepath)
    if not full.exists():
        return ""
    text = full.read_text(errors="ignore")
    match = re.search(r'(https?://\S+)', text)
    if match:
        return match.group(1)
    return ""


def classify_file(fpath):
    """Classify a wiki file into a category."""
    if fpath.startswith("wiki/sources/"):
        return "source"
    elif fpath.startswith("wiki/concepts/"):
        return "concept"
    elif fpath.startswith("wiki/entities/"):
        return "entity"
    elif fpath.startswith("wiki/comparisons/"):
        return "comparison"
    elif fpath.startswith("wiki/_meta/"):
        return "meta"
    else:
        return "other"


def file_to_wikilink(fpath):
    """Convert wiki/concepts/foo.md to [[concepts/foo]]."""
    rel = fpath.replace("wiki/", "", 1)
    if rel.endswith(".md"):
        rel = rel[:-3]
    return f"[[{rel}]]"


def generate_changelog():
    commits = get_commits()
    if not commits:
        print("No wiki commits found.")
        return

    # Group by date
    by_date = defaultdict(lambda: {"added": [], "modified": [], "deleted": []})
    for commit in commits:
        date = commit["date"]
        for op, fpath in commit["files"]:
            entry = {
                "file": fpath,
                "link": file_to_wikilink(fpath),
                "category": classify_file(fpath),
                "commit": commit["hash"],
                "subject": commit["subject"],
            }
            if op == "A":
                by_date[date]["added"].append(entry)
            elif op == "M":
                sections = get_diff_sections(commit["hash"], fpath)
                entry["sections"] = sections
                by_date[date]["modified"].append(entry)
            elif op == "D":
                by_date[date]["deleted"].append(entry)

    # Build markdown
    lines = ["# Wiki Changelog", ""]
    lines.append(f"> Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M')} from git history.")
    lines.append("")

    for date in sorted(by_date.keys(), reverse=True):
        day = by_date[date]
        lines.append(f"## {date}")
        lines.append("")

        # New articles
        new_concepts = [e for e in day["added"] if e["category"] == "concept"]
        new_sources = [e for e in day["added"] if e["category"] == "source"]
        new_entities = [e for e in day["added"] if e["category"] == "entity"]
        new_comparisons = [e for e in day["added"] if e["category"] == "comparison"]
        new_other = [e for e in day["added"] if e["category"] in ("other", "meta")]

        if new_concepts:
            lines.append("### New Concept Articles")
            for e in sorted(new_concepts, key=lambda x: x["file"]):
                summary = extract_summary(e["file"])
                desc = f" — {summary}" if summary else ""
                lines.append(f"- {e['link']}{desc}")
            lines.append("")

        if new_sources:
            lines.append("### New Sources Ingested")
            for e in sorted(new_sources, key=lambda x: x["file"]):
                summary = extract_summary(e["file"])
                url = extract_source_url(e["file"])
                desc_parts = []
                if summary:
                    desc_parts.append(summary)
                if url:
                    desc_parts.append(f"from {url}")
                desc = f" — {', '.join(desc_parts)}" if desc_parts else ""
                lines.append(f"- {e['link']}{desc}")
            lines.append("")

        if new_entities:
            lines.append("### New Entity Articles")
            for e in sorted(new_entities, key=lambda x: x["file"]):
                summary = extract_summary(e["file"])
                desc = f" — {summary}" if summary else ""
                lines.append(f"- {e['link']}{desc}")
            lines.append("")

        if new_comparisons:
            lines.append("### New Comparisons")
            for e in sorted(new_comparisons, key=lambda x: x["file"]):
                summary = extract_summary(e["file"])
                desc = f" — {summary}" if summary else ""
                lines.append(f"- {e['link']}{desc}")
            lines.append("")

        if new_other:
            lines.append("### Other New Files")
            for e in sorted(new_other, key=lambda x: x["file"]):
                lines.append(f"- {e['link']}")
            lines.append("")

        # Updated articles
        if day["modified"]:
            lines.append("### Updated Articles")
            for e in sorted(day["modified"], key=lambda x: x["file"]):
                if e["sections"]:
                    sec_str = ", ".join(e["sections"][:5])
                    lines.append(f"- {e['link']} — changed sections: {sec_str}")
                else:
                    lines.append(f"- {e['link']}")
            lines.append("")

        # Deleted articles
        if day["deleted"]:
            lines.append("### Removed Articles")
            for e in sorted(day["deleted"], key=lambda x: x["file"]):
                lines.append(f"- ~~{e['link']}~~")
            lines.append("")

    # Write output
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Changelog written to {OUTPUT}")
    print(f"  {sum(len(d['added']) for d in by_date.values())} additions, "
          f"{sum(len(d['modified']) for d in by_date.values())} modifications, "
          f"{sum(len(d['deleted']) for d in by_date.values())} deletions "
          f"across {len(by_date)} day(s)")


if __name__ == "__main__":
    generate_changelog()
