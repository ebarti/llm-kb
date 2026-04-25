#!/usr/bin/env python3
"""
Index Validator
Verifies that all index/meta files are complete and consistent.

Checks:
  - wiki/_index.md lists ALL articles
  - wiki/_meta/summaries.md has entries for ALL articles
  - wiki/_meta/manifest.md lists ALL raw files
  - Finds articles missing from index
  - Finds index entries pointing to nonexistent files

Usage: python3 tools/tests/check-index.py [--json]
"""

import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR = BASE_DIR / "raw"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")


def normalize_raw_reference(ref):
    """Normalise raw references to a slug stem."""
    ref = ref.strip()
    if not ref.startswith("raw/"):
        return None

    path = ref[4:]
    if path.endswith("/clean.md"):
        path = path[:-9]
    elif path.endswith("/clean"):
        path = path[:-6]
    elif path.endswith(".md"):
        path = path[:-3]

    parts = [part for part in path.split("/") if part]
    if len(parts) == 1:
        return parts[0]
    return None


def collect_wiki_articles():
    """Collect all article paths (relative to wiki/, no .md)."""
    articles = set()
    for subdir in ["concepts", "sources", "comparisons", "entities"]:
        dirpath = WIKI_DIR / subdir
        if dirpath.is_dir():
            for f in sorted(dirpath.iterdir()):
                if f.suffix == ".md":
                    articles.add(str(f.relative_to(WIKI_DIR)).replace(".md", ""))
    return articles


def collect_raw_files():
    """Collect all raw source slugs from legacy files and v2 directories."""
    if not RAW_DIR.is_dir():
        return set()
    raw_sources = set()
    for entry in RAW_DIR.iterdir():
        if entry.is_file() and entry.suffix == ".md":
            raw_sources.add(entry.stem)
        elif entry.is_dir() and (entry / "clean.md").exists():
            raw_sources.add(entry.name)
    return raw_sources


def extract_wikilinks(filepath):
    """Extract all wikilinks from a file."""
    if not filepath.exists():
        return set()
    text = filepath.read_text(encoding="utf-8", errors="replace")
    links = WIKILINK_RE.findall(text)
    result = set()
    for link in links:
        link = link.strip()
        if link.endswith(".md"):
            link = link[:-3]
        result.add(link)
    return result


def extract_manifest_raw_files(filepath):
    """Extract raw source slugs from manifest.md."""
    if not filepath.exists():
        return set()
    text = filepath.read_text(encoding="utf-8", errors="replace")
    raw_sources = set()
    for ref in re.findall(r"`(raw/[^`]+)`", text):
        slug = normalize_raw_reference(ref)
        if slug:
            raw_sources.add(slug)
    return raw_sources


def run_checks():
    articles = collect_wiki_articles()
    raw_files = collect_raw_files()
    results = {}
    issues = []

    # --- Check _index.md ---
    index_file = WIKI_DIR / "_index.md"
    index_links = extract_wikilinks(index_file)

    missing_from_index = sorted(articles - index_links)
    phantom_in_index = sorted(index_links - articles)
    # Filter phantom to only article-like paths
    phantom_in_index = [p for p in phantom_in_index if "/" in p and not p.startswith("raw/")]

    results["index"] = {
        "file": str(index_file),
        "articles_in_index": len(index_links & articles),
        "total_articles": len(articles),
        "missing_from_index": missing_from_index,
        "phantom_entries": phantom_in_index,
    }
    if missing_from_index:
        issues.append(f"{len(missing_from_index)} article(s) missing from _index.md")
    if phantom_in_index:
        issues.append(f"{len(phantom_in_index)} phantom entry/entries in _index.md (point to nonexistent files)")

    # --- Check summaries.md ---
    summaries_file = WIKI_DIR / "_meta" / "summaries.md"
    summary_links = extract_wikilinks(summaries_file)

    missing_from_summaries = sorted(articles - summary_links)
    phantom_in_summaries = sorted(summary_links - articles)
    phantom_in_summaries = [p for p in phantom_in_summaries if "/" in p and not p.startswith("raw/")]

    results["summaries"] = {
        "file": str(summaries_file),
        "articles_in_summaries": len(summary_links & articles),
        "total_articles": len(articles),
        "missing_from_summaries": missing_from_summaries,
        "phantom_entries": phantom_in_summaries,
    }
    if missing_from_summaries:
        issues.append(f"{len(missing_from_summaries)} article(s) missing from summaries.md")
    if phantom_in_summaries:
        issues.append(f"{len(phantom_in_summaries)} phantom entry/entries in summaries.md")

    # --- Check manifest.md ---
    manifest_file = WIKI_DIR / "_meta" / "manifest.md"
    manifest_raws = extract_manifest_raw_files(manifest_file)

    missing_from_manifest = sorted(raw_files - manifest_raws)
    phantom_in_manifest = sorted(manifest_raws - raw_files)

    results["manifest"] = {
        "file": str(manifest_file),
        "raws_in_manifest": len(manifest_raws & raw_files),
        "total_raw_files": len(raw_files),
        "missing_from_manifest": missing_from_manifest,
        "phantom_entries": phantom_in_manifest,
    }
    if missing_from_manifest:
        issues.append(f"{len(missing_from_manifest)} raw file(s) missing from manifest.md")
    if phantom_in_manifest:
        issues.append(f"{len(phantom_in_manifest)} phantom entry/entries in manifest.md")

    results["issues"] = issues
    results["ok"] = len(issues) == 0

    return results


def print_report(result):
    print("=" * 60)
    print("  Index Validator")
    print("=" * 60)

    for section in ["index", "summaries", "manifest"]:
        data = result[section]
        print(f"\n--- {section.upper()} ---")
        if section == "manifest":
            print(f"  Raw files tracked: {data['raws_in_manifest']}/{data['total_raw_files']}")
        else:
            print(f"  Articles listed: {data.get('articles_in_index', data.get('articles_in_summaries', 0))}/{data['total_articles']}")

        missing_key = [k for k in data if k.startswith("missing_")][0]
        missing = data[missing_key]
        if missing:
            print(f"  \033[31mMissing ({len(missing)}):\033[0m")
            for m in missing:
                print(f"    - {m}")

        phantom = data.get("phantom_entries", [])
        if phantom:
            print(f"  \033[33mPhantom entries ({len(phantom)}):\033[0m")
            for p in phantom:
                print(f"    - {p}")

        if not missing and not phantom:
            print("  \033[32mAll good.\033[0m")

    print()
    if result["ok"]:
        print("\033[32mAll checks passed.\033[0m")
    else:
        print(f"\033[31mIssues found: {', '.join(result['issues'])}\033[0m")
    print()


def main():
    parser = argparse.ArgumentParser(description="Index Validator")
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
