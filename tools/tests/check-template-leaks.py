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
# {{summary}}, {{filename}}, {{Source A}}, {{Author}}, {{foo-bar}},
# {{3-5 bullet points}}, etc. that appear in templates/*.md. Inside wiki/,
# these always indicate a leak. Any non-brace content between {{ and }}
# counts -- code-fence and indented-code stripping already prevents false
# positives from literal syntax examples.
MUSTACHE_PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


def get_fence_delimiter(line: str):
    """Return (char, length) when the line opens/closes a fenced code block."""
    match = FENCE_RE.match(line.lstrip())
    if not match:
        return None

    marker = match.group(1)
    return marker[0], len(marker)


def strip_inline_code(line: str):
    """Remove inline code spans so literal syntax examples don't trigger leaks."""
    cleaned = []
    index = 0

    while index < len(line):
        if line[index] != "`":
            cleaned.append(line[index])
            index += 1
            continue

        tick_start = index
        while index < len(line) and line[index] == "`":
            index += 1
        tick_count = index - tick_start
        closing = line.find("`" * tick_count, index)

        if closing == -1:
            # No matching closing backticks -- treat the remainder as
            # literal text and stop scanning to avoid an infinite loop.
            cleaned.append(line[tick_start:])
            break

        index = closing + tick_count

    return "".join(cleaned)


def _is_indented_code_line(line: str) -> bool:
    """A non-empty line that begins with 4 spaces or a tab (CommonMark).

    Lines that are entirely whitespace are not code lines on their own;
    they extend an already-open indented block but do not start one.
    """
    if not line.strip():
        return False
    if line.startswith("\t"):
        return True
    if line.startswith("    "):
        return True
    return False


def scan_file(filepath: Path):
    """Return a list of leak record dicts with line_number, line_text, kind, and token keys."""
    leaks = []
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return leaks

    in_fence = False
    fence_char = None
    fence_length = 0
    # CommonMark indented code block state. A block opens when a line
    # indented by 4+ spaces (or a tab) follows a blank line (or is the
    # first non-empty line in the file), and closes on the next
    # non-blank line that is not itself indented.
    in_indented_code = False
    prev_blank = True  # start-of-file counts as "after a blank line"

    for i, line in enumerate(text.splitlines(), start=1):
        fence = get_fence_delimiter(line)
        if in_fence:
            if fence and fence[0] == fence_char and fence[1] >= fence_length:
                in_fence = False
                fence_char = None
                fence_length = 0
            prev_blank = False
            continue

        if fence:
            in_fence = True
            fence_char, fence_length = fence
            in_indented_code = False
            prev_blank = False
            continue

        is_blank = not line.strip()

        if in_indented_code:
            # Indented blocks continue across blank lines, but a
            # non-blank, non-indented line closes them.
            if is_blank:
                prev_blank = True
                continue
            if _is_indented_code_line(line):
                prev_blank = False
                continue
            in_indented_code = False

        if prev_blank and _is_indented_code_line(line):
            in_indented_code = True
            prev_blank = False
            continue

        prev_blank = is_blank
        if is_blank:
            continue

        scan_line = strip_inline_code(line)

        # --- Placeholder wikilinks ---
        for m in WIKILINK_RE.finditer(scan_line):
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
        for m in MUSTACHE_PLACEHOLDER_RE.finditer(scan_line):
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
