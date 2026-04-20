#!/usr/bin/env python3
"""
Template Placeholder Leak Checker

Scans wiki/ for literal template placeholders that leaked through compilation,
such as:

  - [[concept-name]], [[source-name]], [[entity-name]], [[tool-name]],
    [[comparison-name]]              -- placeholder names from templates/*.md
  - [[wikilinks]], [[wikilink]]      -- the word "wikilink(s)" used as if it
                                       were a real target article
  - [[x]], [[y]], [[foo]], [[bar]]   -- toy placeholders
  - [[title]], [[name]], [[filename]], [[date]]  -- Jinja-style names left
                                       as bare wikilinks
  - {{title}}, {{name}}, {{date}},
    {{summary}}, {{filename}}, ...   -- literal Mustache-style placeholders

Anything matched here indicates content was not properly substituted during
compilation and must be replaced with real links (or removed).

Excludes: templates/ and raw/ (placeholders there are intentional).

Usage: python3 tools/tests/check-template-leaks.py [--json]
"""

import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"

# Placeholder wikilink targets that should never appear in the wiki.
# These are lowercase tokens with no category prefix -- genuine wiki links
# always have a category like concepts/, sources/, entities/, etc., or map
# to a top-level page such as log, _index, Dashboard.
PLACEHOLDER_WIKILINKS = {
    "concept-name",
    "source-name",
    "entity-name",
    "tool-name",
    "comparison-name",
    "wikilinks",
    "wikilink",
    "x",
    "y",
    "foo",
    "bar",
    "title",
    "name",
    "filename",
    "date",
    "summary",
}

# Matches any [[target]] (ignoring the | alias part).
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")

# Matches common Mustache / Jinja-style placeholders like {{title}}, {{date}},
# {{summary}}, {{filename}}, {{Source A}}, {{Author}} etc. that appear in
# templates/*.md. Inside wiki/, these always indicate a leak.
MUSTACHE_PLACEHOLDER_RE = re.compile(r"\{\{[A-Za-z0-9_ ]+\}\}")


def scan_file(filepath: Path):
    """Return a list of (line_number, line_text, kind, token) leak records."""
    leaks = []
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return leaks

    for i, line in enumerate(text.splitlines(), start=1):
        # --- Placeholder wikilinks ---
        for m in WIKILINK_RE.finditer(line):
            target = m.group(1).strip()
            if target.endswith(".md"):
                target = target[:-3]
            if target in PLACEHOLDER_WIKILINKS:
                leaks.append({
                    "line": i,
                    "text": line.strip(),
                    "kind": "placeholder_wikilink",
                    "token": f"[[{target}]]",
                })

        # --- Mustache-style placeholders ---
        for m in MUSTACHE_PLACEHOLDER_RE.finditer(line):
            leaks.append({
                "line": i,
                "text": line.strip(),
                "kind": "mustache_placeholder",
                "token": m.group(0),
            })

    return leaks


def run_checks():
    """Scan all wiki/ .md files for template placeholder leaks."""
    leaks_by_file = {}
    total_files = 0

    if not WIKI_DIR.is_dir():
        return {
            "total_files": 0,
            "files_with_leaks": 0,
            "total_leaks": 0,
            "leaks_by_file": {},
            "ok": True,
        }

    for filepath in sorted(WIKI_DIR.rglob("*.md")):
        total_files += 1
        leaks = scan_file(filepath)
        if leaks:
            rel = str(filepath.relative_to(BASE_DIR))
            leaks_by_file[rel] = leaks

    total_leaks = sum(len(v) for v in leaks_by_file.values())

    return {
        "total_files": total_files,
        "files_with_leaks": len(leaks_by_file),
        "total_leaks": total_leaks,
        "leaks_by_file": leaks_by_file,
        "ok": total_leaks == 0,
    }


def print_report(result):
    print("=" * 60)
    print("  Template Placeholder Leak Check")
    print("=" * 60)
    print(f"\nFiles scanned: {result['total_files']}")
    print(f"Files with leaks: {result['files_with_leaks']}")
    print(f"Total leaks: {result['total_leaks']}")
    print()

    if result["ok"]:
        print("\033[32mNo template placeholder leaks found.\033[0m")
        print()
        return

    print("\033[31mPlaceholder leaks detected:\033[0m")
    for path, leaks in sorted(result["leaks_by_file"].items()):
        print(f"\n  {path}:")
        for leak in leaks:
            kind = leak["kind"]
            token = leak["token"]
            print(f"    line {leak['line']} [{kind}] {token}")
            if leak["text"]:
                snippet = leak["text"]
                if len(snippet) > 100:
                    snippet = snippet[:97] + "..."
                print(f"      > {snippet}")
    print()
    print(
        "Fix: replace each placeholder with a real wikilink, delete the "
        "line, or rephrase the sentence so it does not need a link."
    )
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Template Placeholder Leak Checker"
    )
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
