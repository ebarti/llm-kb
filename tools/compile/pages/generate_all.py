#!/usr/bin/env python3
"""Run every decoration-page generator in `tools/compile/pages/`.

Called by `uv run kb compile` so every `wiki/<Page>.md` that is auto-generatable
(Dashboard, Graph, Tags, Glossary, Changelog) ends up with a fresh
`last_compiled` timestamp on every compile.

Usage:
    python3 tools/compile/pages/generate_all.py
"""

from __future__ import annotations

import sys
import traceback
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

# Import generators directly so they can share the _common module.
import gen_dashboard
import gen_graph
import gen_tags
import gen_glossary
import gen_changelog


GENERATORS = [
    ("dashboard", gen_dashboard.generate),
    ("graph", gen_graph.generate),
    ("tags", gen_tags.generate),
    ("glossary", gen_glossary.generate),
    ("changelog", gen_changelog.generate),
]


def main() -> int:
    failures = 0
    for name, fn in GENERATORS:
        try:
            out = fn()
            print(f"  [compile.pages] {name}: wrote {out.name}")
        except Exception as exc:  # noqa: BLE001 — report and continue
            failures += 1
            print(f"  [compile.pages] {name}: FAILED — {exc}")
            traceback.print_exc()
    if failures:
        print(f"  [compile.pages] {failures} generator(s) failed.")
        return 1
    print("  [compile.pages] All decoration pages generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
