#!/usr/bin/env python3
"""Generate wiki/Changelog.md from git history.

Parses `git log --name-status` for paths under `wiki/` and `raw/`, grouping
additions, modifications, and deletions by commit date. Includes a fresh
`last_compiled` frontmatter timestamp.

Usage:
    python3 tools/compile/pages/gen_changelog.py
"""

from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from _common import (
    ROOT,
    WIKI,
    today,
    write_page,
)

MAX_COMMITS = 500
MAX_DAYS_SHOWN = 60


def _git(*args: str) -> str | None:
    """Run a git command, return stdout or None on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout


def _parse_git_log():
    """Return list of commits: [{'hash','date','subject','files': [(op, path)...]}]"""
    log_output = _git(
        "log",
        f"--max-count={MAX_COMMITS}",
        "--pretty=format:COMMIT|%H|%ai|%s",
        "--name-status",
        "--",
        "wiki/",
        "raw/",
    )
    if log_output is None:
        return None
    commits = []
    current = None
    for line in log_output.splitlines():
        line = line.rstrip()
        if not line:
            current = None
            continue
        if line.startswith("COMMIT|"):
            parts = line.split("|", 3)
            if len(parts) != 4:
                current = None
                continue
            _, h, date_full, subject = parts
            current = {
                "hash": h[:8],
                "date": date_full.split(" ")[0],
                "subject": subject,
                "files": [],
            }
            commits.append(current)
            continue
        if current is None:
            continue
        # Name-status line, e.g. "A\twiki/concepts/foo.md" or "R100\told\tnew".
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        op = parts[0][:1]
        fpath = parts[-1]
        if not fpath.endswith(".md"):
            continue
        if not (fpath.startswith("wiki/") or fpath.startswith("raw/")):
            continue
        current["files"].append((op, fpath))
    return commits


def _classify(fpath: str) -> str:
    if fpath.startswith("wiki/sources/"):
        return "source"
    if fpath.startswith("wiki/concepts/"):
        return "concept"
    if fpath.startswith("wiki/entities/"):
        return "entity"
    if fpath.startswith("wiki/comparisons/"):
        return "comparison"
    if fpath.startswith("wiki/_meta/"):
        return "meta"
    if fpath.startswith("raw/"):
        return "raw"
    return "other"


def _file_to_wikilink(fpath: str, existing_wiki_paths: set[str] | None = None) -> str:
    """Render a wiki-relative path as a wikilink *only* when the target
    still exists in the current wiki. Historical entries for deleted or
    renamed files fall back to inline code so the changelog never emits
    a broken ``[[...]]`` link.
    """
    if fpath.startswith("wiki/"):
        rel = fpath[len("wiki/"):]
        if rel.endswith(".md"):
            rel = rel[:-3]
        if existing_wiki_paths is None or rel in existing_wiki_paths:
            return f"[[{rel}]]"
        return f"`{fpath}`"
    return f"`{fpath}`"


def _collect_existing_wiki_paths() -> set[str]:
    """Return the set of current wiki article ids (path relative to
    ``wiki/``, without the ``.md`` suffix). Used to guard wikilink
    emission for historical changelog entries.
    """
    paths: set[str] = set()
    if not WIKI.is_dir():
        return paths
    for fp in WIKI.rglob("*.md"):
        rel = fp.relative_to(WIKI)
        if rel.parts and rel.parts[0] == "_meta":
            # Meta files are not article targets.
            continue
        paths.add(str(rel)[:-3])
    return paths


def _latest_hash_by_path(items: list[tuple[str, str]]) -> dict[str, str]:
    """Deduplicate same-day file entries by path, keeping the newest hash.

    `git log` yields newest commits first, so the first hash seen for a path is
    the most recent one for that day.
    """
    latest: dict[str, str] = {}
    for path, h in items:
        latest.setdefault(path, h)
    return latest


def generate() -> Path:
    commits = _parse_git_log()
    existing = _collect_existing_wiki_paths()

    lines: list[str] = []
    lines.append("# Wiki Changelog")
    lines.append("")
    lines.append(
        f"_Auto-generated on {today()} from git history by "
        "`tools/compile/pages/gen_changelog.py`._"
    )
    lines.append("")

    if commits is None:
        lines.append(
            "> Git history is unavailable in this checkout — unable to generate a changelog."
        )
        body = "\n".join(lines)
    else:
        # Group by date
        by_date: dict[str, dict[str, list[tuple[str, str]]]] = defaultdict(
            lambda: {"A": [], "M": [], "D": []}
        )
        for c in commits:
            for op, path in c["files"]:
                bucket = "A" if op == "A" else "D" if op == "D" else "M"
                # Key: (category, path, commit-hash) so the reader can trace back
                by_date[c["date"]][bucket].append((path, c["hash"]))

        if not by_date:
            lines.append("_No wiki or raw-source changes recorded in git yet._")
            body = "\n".join(lines)
        else:
            dates_shown = sorted(by_date.keys(), reverse=True)[:MAX_DAYS_SHOWN]
            total_A = sum(len(_latest_hash_by_path(by_date[date]["A"])) for date in dates_shown)
            total_M = sum(len(_latest_hash_by_path(by_date[date]["M"])) for date in dates_shown)
            total_D = sum(len(_latest_hash_by_path(by_date[date]["D"])) for date in dates_shown)
            lines.append(
                f"Additions: **{total_A}** · Modifications: **{total_M}** · "
                f"Deletions: **{total_D}** across **{len(dates_shown)}** day(s)."
            )
            lines.append("")

            for date in dates_shown:
                day = by_date[date]
                lines.append(f"## {date}")
                lines.append("")

                # Additions grouped by category
                if day["A"]:
                    grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)
                    for path, h in day["A"]:
                        grouped[_classify(path)].append((path, h))
                    section_titles = [
                        ("concept", "New Concept Articles"),
                        ("source", "New Sources Ingested"),
                        ("entity", "New Entity Articles"),
                        ("comparison", "New Comparisons"),
                        ("raw", "New Raw Sources"),
                        ("meta", "New Meta Files"),
                        ("other", "Other New Files"),
                    ]
                    for cat, title in section_titles:
                        items = grouped.get(cat, [])
                        if not items:
                            continue
                        lines.append(f"### {title}")
                        latest_additions = _latest_hash_by_path(items)
                        for path in sorted(latest_additions):
                            h = latest_additions[path]
                            lines.append(f"- {_file_to_wikilink(path, existing)}  `({h})`")
                        lines.append("")

                if day["M"]:
                    lines.append("### Updated")
                    latest_updates = _latest_hash_by_path(day["M"])
                    for path in sorted(latest_updates):
                        h = latest_updates[path]
                        lines.append(f"- {_file_to_wikilink(path, existing)}  `({h})`")
                    lines.append("")

                if day["D"]:
                    lines.append("### Removed")
                    latest_deletions = _latest_hash_by_path(day["D"])
                    for path in sorted(latest_deletions):
                        h = latest_deletions[path]
                        lines.append(f"- ~~`{path}`~~  `({h})`")
                    lines.append("")

            if len(by_date) > MAX_DAYS_SHOWN:
                skipped = len(by_date) - MAX_DAYS_SHOWN
                lines.append(f"_...and {skipped} earlier day(s) elided._")
                lines.append("")

            body = "\n".join(lines)

    frontmatter = {
        "title": "Changelog",
        "type": "meta",
        "summary": "Auto-generated changelog of wiki additions, modifications, and deletions from git history.",
    }

    out_path = WIKI / "Changelog.md"
    write_page(out_path, frontmatter, body)
    return out_path


def main() -> int:
    out = generate()
    print(f"  [changelog] Written to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
