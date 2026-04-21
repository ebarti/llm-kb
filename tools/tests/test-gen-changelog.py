#!/usr/bin/env python3
"""Regression tests for tools/compile/pages/gen_changelog.py.

Focused on _file_to_wikilink()'s fallback behavior: historical entries
pointing at files that no longer exist in the wiki must not emit broken
[[wikilinks]] -- they fall back to inline code so the generated
Changelog never contains phantom links.

Usage: python3 tools/tests/test-gen-changelog.py [--json]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
GEN_PATH = BASE_DIR / "tools" / "compile" / "pages" / "gen_changelog.py"


def _load():
    # gen_changelog imports _common via a sys.path insertion on its own dir.
    spec = importlib.util.spec_from_file_location("gen_changelog", GEN_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def run_checks():
    gen = _load()
    existing = {"concepts/rag", "Dashboard"}

    cases = []

    def add(name: str, expected: str, actual: str) -> None:
        cases.append({"name": name, "passed": actual == expected, "expected": expected, "actual": actual})

    add(
        "existing_target_renders_as_wikilink",
        "[[concepts/rag]]",
        gen._file_to_wikilink("wiki/concepts/rag.md", existing),
    )
    add(
        "deleted_top_level_renders_as_code",
        "`wiki/Reading-List.md`",
        gen._file_to_wikilink("wiki/Reading-List.md", existing),
    )
    add(
        "deleted_category_renders_as_code",
        "`wiki/concepts/defunct.md`",
        gen._file_to_wikilink("wiki/concepts/defunct.md", existing),
    )
    add(
        "raw_path_always_renders_as_code",
        "`raw/anything.md`",
        gen._file_to_wikilink("raw/anything.md", existing),
    )

    original_parse_git_log = gen._parse_git_log
    original_collect_existing = gen._collect_existing_wiki_paths
    original_max_days = gen.MAX_DAYS_SHOWN
    original_wiki = gen.WIKI

    try:
        synthetic_commits = [
            {
                "hash": "aaa11111",
                "date": "2024-01-03",
                "subject": "third",
                "files": [("A", "wiki/concepts/c.md"), ("M", "wiki/concepts/a.md")],
            },
            {
                "hash": "bbb22222",
                "date": "2024-01-02",
                "subject": "second",
                "files": [("A", "wiki/concepts/b.md"), ("D", "raw/old.md")],
            },
            {
                "hash": "ccc33333",
                "date": "2024-01-01",
                "subject": "first",
                "files": [("A", "wiki/concepts/a.md"), ("M", "wiki/concepts/b.md")],
            },
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            gen.WIKI = Path(tmpdir) / "wiki"
            gen.WIKI.mkdir(parents=True, exist_ok=True)
            gen.MAX_DAYS_SHOWN = 2
            gen._parse_git_log = lambda: synthetic_commits
            gen._collect_existing_wiki_paths = lambda: set()

            out_path = gen.generate()
            text = out_path.read_text(encoding="utf-8")
            summary_line = next(
                line for line in text.splitlines() if line.startswith("Additions:")
            )
            dates_rendered = [
                line[3:] for line in text.splitlines() if line.startswith("## ")
            ]

        add(
            "summary_totals_follow_dates_shown_limit",
            "Additions: **2** · Modifications: **1** · Deletions: **1** across **2** day(s).",
            summary_line,
        )
        add(
            "only_dates_shown_are_rendered",
            json.dumps(["2024-01-03", "2024-01-02"]),
            json.dumps(dates_rendered),
        )
    finally:
        gen._parse_git_log = original_parse_git_log
        gen._collect_existing_wiki_paths = original_collect_existing
        gen.MAX_DAYS_SHOWN = original_max_days
        gen.WIKI = original_wiki

    ok = all(c["passed"] for c in cases)
    return {"ok": ok, "cases": cases}


def print_report(result) -> None:
    print("=" * 60)
    print("  gen_changelog Regression Tests")
    print("=" * 60)
    print()
    for c in result["cases"]:
        sym = "\033[32mPASS\033[0m" if c["passed"] else "\033[31mFAIL\033[0m"
        print(f"  {sym} {c['name']}")
        if not c["passed"]:
            print(f"      expected: {c['expected']!r}")
            print(f"      actual:   {c['actual']!r}")
    print()
    if result["ok"]:
        print("\033[32mAll gen_changelog tests passed.\033[0m")
    else:
        print("\033[31mgen_changelog regressions detected.\033[0m")
    print()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__ or "")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    result = run_checks()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
