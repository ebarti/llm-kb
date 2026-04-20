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
