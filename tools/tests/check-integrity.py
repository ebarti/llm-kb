#!/usr/bin/env python3
"""
Wiki Integrity Checker
Validates all wiki markdown files for structural correctness.

Checks:
  - Valid YAML frontmatter on every file
  - Required fields present (title, type, summary, last_compiled)
  - All [[wikilinks]] resolve to existing files
  - No duplicate titles
  - No empty articles (minimum content length)
  - Frontmatter dates are valid ISO 8601
  - File names match conventions (lowercase, hyphens, no spaces)
  - Type field matches directory (concepts/ -> concept, sources/ -> source-summary, etc.)

Usage: python3 tools/tests/check-integrity.py [--json]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"

# Minimum body length (characters, excluding frontmatter)
MIN_CONTENT_LENGTH = 100

# Expected type per directory
DIR_TYPE_MAP = {
    "concepts": "concept",
    "sources": "source-summary",
    "comparisons": "comparison",
    "entities": "entity",
}

# Required frontmatter fields per type
REQUIRED_FIELDS = {
    "default": ["title", "type", "summary", "last_compiled"],
    "source-summary": ["title", "type", "summary", "last_compiled", "source"],
    "entity": ["title", "type", "summary", "last_compiled", "entity_type"],
}

# ISO 8601 date pattern (YYYY-MM-DD)
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Wikilink pattern
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")

# Valid filename pattern: lowercase, hyphens, digits, dots for extension
VALID_FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9\-]*\.md$")


def parse_frontmatter(text):
    """Parse YAML-ish frontmatter. Returns (dict, body_text) or (None, text)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm_block = text[4:end]
    body = text[end + 4:]
    meta = {}
    for line in fm_block.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        colon = line.find(":")
        if colon == -1:
            continue
        key = line[:colon].strip()
        val = line[colon + 1:].strip().strip('"').strip("'")
        meta[key] = val
    return meta, body


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


def get_relative_wiki_path(filepath):
    """Get path relative to wiki/ without extension, e.g. 'concepts/llm-knowledge-base'."""
    return str(filepath.relative_to(WIKI_DIR)).replace(".md", "")


def run_checks():
    files = collect_wiki_files()
    issues = []
    passed = 0
    failed = 0
    checks = {
        "frontmatter_valid": {"pass": 0, "fail": 0, "issues": []},
        "required_fields": {"pass": 0, "fail": 0, "issues": []},
        "wikilinks_resolve": {"pass": 0, "fail": 0, "issues": []},
        "no_duplicate_titles": {"pass": 0, "fail": 0, "issues": []},
        "min_content_length": {"pass": 0, "fail": 0, "issues": []},
        "valid_dates": {"pass": 0, "fail": 0, "issues": []},
        "filename_conventions": {"pass": 0, "fail": 0, "issues": []},
        "type_matches_dir": {"pass": 0, "fail": 0, "issues": []},
    }

    # Build set of all known article paths (relative to wiki/, no .md)
    known_paths = set()
    for f in files:
        known_paths.add(get_relative_wiki_path(f))

    # Also include meta/index files for wikilink resolution
    for f in WIKI_DIR.rglob("*.md"):
        rel = str(f.relative_to(WIKI_DIR)).replace(".md", "")
        known_paths.add(rel)

    # Also allow raw/ references (both legacy flat files and v2 directories)
    raw_dir = BASE_DIR / "raw"
    if raw_dir.is_dir():
        for f in raw_dir.iterdir():
            if f.is_file() and f.suffix == ".md":
                # Legacy: raw/<slug>.md
                known_paths.add("raw/" + f.stem)
            elif f.is_dir() and (f / "clean.md").exists():
                # v2: raw/<slug>/clean.md — accept both raw/<slug> and raw/<slug>/clean
                known_paths.add("raw/" + f.name)
                known_paths.add("raw/" + f.name + "/clean")

    titles_seen = {}
    all_wikilinks = []

    for filepath in files:
        rel_path = get_relative_wiki_path(filepath)
        filename = filepath.name
        text = filepath.read_text(encoding="utf-8", errors="replace")

        # --- Filename conventions ---
        if VALID_FILENAME_RE.match(filename):
            checks["filename_conventions"]["pass"] += 1
        else:
            msg = f"{rel_path}: filename '{filename}' violates conventions (must be lowercase, hyphens, no spaces)"
            checks["filename_conventions"]["fail"] += 1
            checks["filename_conventions"]["issues"].append(msg)

        # --- Frontmatter ---
        meta, body = parse_frontmatter(text)
        if meta is None:
            checks["frontmatter_valid"]["fail"] += 1
            checks["frontmatter_valid"]["issues"].append(f"{rel_path}: missing or invalid frontmatter")
            # Skip further meta-dependent checks
            checks["required_fields"]["fail"] += 1
            checks["required_fields"]["issues"].append(f"{rel_path}: no frontmatter to check")
            checks["valid_dates"]["fail"] += 1
            checks["type_matches_dir"]["fail"] += 1
        else:
            checks["frontmatter_valid"]["pass"] += 1

            # --- Required fields ---
            article_type = meta.get("type", "")
            req = REQUIRED_FIELDS.get(article_type, REQUIRED_FIELDS["default"])
            missing = [f for f in req if f not in meta or not meta[f]]
            if missing:
                checks["required_fields"]["fail"] += 1
                checks["required_fields"]["issues"].append(
                    f"{rel_path}: missing required fields: {', '.join(missing)}"
                )
            else:
                checks["required_fields"]["pass"] += 1

            # --- Valid dates ---
            date_val = meta.get("last_compiled", "")
            if date_val and ISO_DATE_RE.match(date_val):
                checks["valid_dates"]["pass"] += 1
            elif date_val:
                checks["valid_dates"]["fail"] += 1
                checks["valid_dates"]["issues"].append(
                    f"{rel_path}: last_compiled '{date_val}' is not valid ISO 8601"
                )
            else:
                checks["valid_dates"]["fail"] += 1
                checks["valid_dates"]["issues"].append(
                    f"{rel_path}: last_compiled is empty or missing"
                )

            # --- Type matches directory ---
            parts = rel_path.split("/")
            if len(parts) >= 2:
                dir_name = parts[0]
                expected_type = DIR_TYPE_MAP.get(dir_name)
                if expected_type and article_type == expected_type:
                    checks["type_matches_dir"]["pass"] += 1
                elif expected_type:
                    checks["type_matches_dir"]["fail"] += 1
                    checks["type_matches_dir"]["issues"].append(
                        f"{rel_path}: type '{article_type}' should be '{expected_type}' for {dir_name}/"
                    )
                else:
                    checks["type_matches_dir"]["pass"] += 1

            # --- Duplicate titles ---
            title = meta.get("title", "")
            if title:
                if title in titles_seen:
                    checks["no_duplicate_titles"]["fail"] += 1
                    checks["no_duplicate_titles"]["issues"].append(
                        f"{rel_path}: duplicate title '{title}' (also in {titles_seen[title]})"
                    )
                else:
                    titles_seen[title] = rel_path
                    checks["no_duplicate_titles"]["pass"] += 1
            else:
                checks["no_duplicate_titles"]["pass"] += 1

        # --- Content length ---
        if len(body.strip()) >= MIN_CONTENT_LENGTH:
            checks["min_content_length"]["pass"] += 1
        else:
            checks["min_content_length"]["fail"] += 1
            checks["min_content_length"]["issues"].append(
                f"{rel_path}: body is only {len(body.strip())} chars (min {MIN_CONTENT_LENGTH})"
            )

        # --- Wikilinks resolve ---
        links = WIKILINK_RE.findall(text)
        bad_links = []
        for link in links:
            link_clean = link.strip()
            # Normalize: strip .md if present
            if link_clean.endswith(".md"):
                link_clean = link_clean[:-3]
            if link_clean not in known_paths:
                bad_links.append(link_clean)
        if bad_links:
            checks["wikilinks_resolve"]["fail"] += 1
            checks["wikilinks_resolve"]["issues"].append(
                f"{rel_path}: broken wikilinks: {', '.join(bad_links)}"
            )
        else:
            checks["wikilinks_resolve"]["pass"] += 1

    # Tally
    total_pass = sum(c["pass"] for c in checks.values())
    total_fail = sum(c["fail"] for c in checks.values())
    total = total_pass + total_fail
    score = (total_pass / total * 100) if total > 0 else 0

    return {
        "total_files": len(files),
        "checks": checks,
        "total_pass": total_pass,
        "total_fail": total_fail,
        "total_checks": total,
        "score": round(score, 1),
        "ok": total_fail == 0,
    }


def print_report(result):
    print("=" * 60)
    print("  Wiki Integrity Check")
    print("=" * 60)
    print(f"\nFiles scanned: {result['total_files']}")
    print()

    for name, data in result["checks"].items():
        status = "PASS" if data["fail"] == 0 else "FAIL"
        symbol = "\033[32m✓\033[0m" if data["fail"] == 0 else "\033[31m✗\033[0m"
        print(f"  {symbol} {name}: {data['pass']} passed, {data['fail']} failed")
        for issue in data["issues"]:
            print(f"      - {issue}")

    print()
    print(f"Score: {result['score']}% ({result['total_pass']}/{result['total_checks']} checks passed)")
    print(f"Result: {'ALL PASSED' if result['ok'] else 'ISSUES FOUND'}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Wiki Integrity Checker")
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
