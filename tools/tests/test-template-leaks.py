#!/usr/bin/env python3
"""
Regression tests for the template placeholder leak checker.

Usage: python3 tools/tests/test-template-leaks.py [--json]
"""

import argparse
import importlib.util
import json
import sys
import tempfile
import textwrap
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHECKER_PATH = BASE_DIR / "tools" / "tests" / "check-template-leaks.py"


def load_checker():
    spec = importlib.util.spec_from_file_location(
        "check_template_leaks",
        CHECKER_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECKER = load_checker()

TEST_CASES = [
    {
        "name": "flags_placeholders_in_prose",
        "content": """
        Plain prose with [[title]] and {{summary}} should fail.
        """,
        "expected_tokens": ["[[title]]", "{{summary}}"],
    },
    {
        "name": "ignores_inline_code_and_fenced_blocks",
        "content": """
        Inline syntax example `[[title]]` should be allowed.
        ```
        {{summary}}
        [[wikilinks]]
        ```
        """,
        "expected_tokens": [],
    },
    {
        "name": "still_flags_prose_when_inline_code_is_present",
        "content": """
        Use [[title]] in prose but show `[[wikilinks]]` and `{{name}}` literally.
        """,
        "expected_tokens": ["[[title]]"],
    },
    # Indented-code-block cases: these use raw_content because dedent
    # would strip the 4-space indent that marks the code block.
    {
        "name": "ignores_indented_code_blocks",
        "raw_content": (
            "Some prose describing the template syntax:\n"
            "\n"
            "    [[title]]\n"
            "    {{summary}}\n"
            "\n"
            "End of example.\n"
        ),
        "expected_tokens": [],
    },
    {
        "name": "ignores_tab_indented_code_blocks",
        "raw_content": (
            "Another example with a tab indent:\n"
            "\n"
            "\t[[wikilinks]]\n"
            "\t{{name}}\n"
            "\n"
            "Back to prose.\n"
        ),
        "expected_tokens": [],
    },
    {
        "name": "still_flags_prose_after_indented_code_block",
        "raw_content": (
            "Intro text.\n"
            "\n"
            "    [[title]]\n"
            "\n"
            "Now prose with [[wikilinks]] that must still be flagged.\n"
        ),
        "expected_tokens": ["[[wikilinks]]"],
    },
    {
        "name": "flags_mustache_placeholders_with_hyphens_and_spaces",
        "content": """
        Leaked templates like {{foo-bar}} and {{3-5 bullet points}} must
        be caught even though they contain hyphens or multi-word content.
        """,
        "expected_tokens": ["{{foo-bar}}", "{{3-5 bullet points}}"],
    },
]


def scan_text(content: Optional[str] = None, raw_content: Optional[str] = None):
    with tempfile.TemporaryDirectory() as tmpdir:
        sample = Path(tmpdir) / "sample.md"
        if raw_content is not None:
            sample.write_text(raw_content, encoding="utf-8")
        else:
            sample.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")
        return CHECKER.scan_file(sample)


def run_checks():
    cases = []
    ok = True

    for case in TEST_CASES:
        leaks = scan_text(
            content=case.get("content"),
            raw_content=case.get("raw_content"),
        )
        tokens = [leak["token"] for leak in leaks]
        passed = tokens == case["expected_tokens"]
        if not passed:
            ok = False

        cases.append(
            {
                "name": case["name"],
                "passed": passed,
                "expected_tokens": case["expected_tokens"],
                "actual_tokens": tokens,
            }
        )

    return {
        "ok": ok,
        "cases": cases,
    }


def print_report(result):
    print("=" * 60)
    print("  Template Placeholder Leak Checker Tests")
    print("=" * 60)
    print()

    for case in result["cases"]:
        symbol = "\033[32m✓\033[0m" if case["passed"] else "\033[31m✗\033[0m"
        print(f"  {symbol} {case['name']}")
        if not case["passed"]:
            print(f"      expected: {case['expected_tokens']}")
            print(f"      actual:   {case['actual_tokens']}")

    print()
    if result["ok"]:
        print("\033[32mAll template leak checker tests passed.\033[0m")
    else:
        print("\033[31mTemplate leak checker regressions detected.\033[0m")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Regression tests for the template placeholder leak checker"
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
