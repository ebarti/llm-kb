#!/usr/bin/env python3
"""
Regenerator tests.

Ensures ``tools/compile/regen_meta.py``:

  1. Produces all five meta files.
  2. Is deterministic -- a second run is a byte-for-byte no-op.
  3. Covers every file in ``raw/`` in the manifest.
  4. Lists every wiki article in summaries.md.
  5. Contains no phantom entries in links.md (every target resolves).
  6. stats.json reflects the actual file count.

Usage: ``python3 tools/tests/test-regen-meta.py [--json]``
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR = BASE_DIR / "raw"
META_DIR = WIKI_DIR / "_meta"
REGEN_PATH = BASE_DIR / "tools" / "compile" / "regen_meta.py"


def _import_regen():
    spec = importlib.util.spec_from_file_location("regen_meta", REGEN_PATH)
    assert spec is not None and spec.loader is not None, "cannot load regen_meta"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _snapshot_meta() -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("stats.json", "manifest.md", "summaries.md", "links.md", "freshness-report.md"):
        p = META_DIR / name
        out[name] = p.read_text(encoding="utf-8") if p.exists() else ""
    return out


def test_produces_all_files(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    missing = [
        n
        for n in ("stats.json", "manifest.md", "summaries.md", "links.md", "freshness-report.md")
        if not (META_DIR / n).exists()
    ]
    return (not missing), ("missing: " + ", ".join(missing) if missing else "all 5 present")


def test_idempotent(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    snap1 = _snapshot_meta()
    regen.regenerate(quiet=True)
    snap2 = _snapshot_meta()
    diff = [n for n in snap1 if snap1[n] != snap2[n]]
    return (not diff), ("changed: " + ", ".join(diff) if diff else "byte-identical on rerun")


def test_check_mode_clean(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    rc = regen.regenerate(check=True, quiet=True)
    return (rc == 0), f"--check rc={rc} (expected 0 after regen)"


def test_manifest_covers_all_raw(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    text = (META_DIR / "manifest.md").read_text(encoding="utf-8")
    tracked = set(re.findall(r"`raw/([^`]+)\.md`", text))
    actual = {p.stem for p in RAW_DIR.glob("*.md")}
    missing = sorted(actual - tracked)
    return (not missing), (
        f"{len(tracked)}/{len(actual)} covered"
        + (f"; missing: {missing[:5]}" if missing else "")
    )


def test_summaries_covers_all_articles(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    text = (META_DIR / "summaries.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text))

    # Only compare against the four real article subdirectories --
    # structural pages (_index, Dashboard, ...) are intentionally
    # excluded from summaries.md.
    expected = set()
    for sub in ("concepts", "sources", "entities", "comparisons"):
        d = WIKI_DIR / sub
        if d.is_dir():
            for f in d.glob("*.md"):
                expected.add(f"{sub}/{f.stem}")
    missing = sorted(expected - listed)
    return (not missing), (
        f"{len(expected & listed)}/{len(expected)} listed"
        + (f"; missing: {missing[:5]}" if missing else "")
    )


def test_links_no_phantoms(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    text = (META_DIR / "links.md").read_text(encoding="utf-8")
    targets: set[str] = set()
    for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text):
        target = link.split("#", 1)[0].strip()
        if target:
            targets.add(target)

    known: set[str] = set()
    for f in WIKI_DIR.rglob("*.md"):
        rel = str(f.relative_to(WIKI_DIR))[:-3]
        known.add(rel)

    phantoms = sorted(t for t in targets if t not in known)
    return (not phantoms), (
        f"all {len(targets)} link targets resolve"
        if not phantoms
        else f"{len(phantoms)} phantoms, e.g. {phantoms[:3]}"
    )


def test_stats_reflects_reality(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    data = json.loads((META_DIR / "stats.json").read_text(encoding="utf-8"))
    reported = data["current"]["total_files"]
    actual = sum(
        1
        for f in WIKI_DIR.rglob("*.md")
        if "_meta" not in f.relative_to(WIKI_DIR).parts[:1]
    )
    return (reported == actual), f"stats.total_files={reported} actual={actual}"


TESTS = [
    ("produces_all_five_files", test_produces_all_files),
    ("idempotent_second_run_is_noop", test_idempotent),
    ("check_mode_clean_after_regen", test_check_mode_clean),
    ("manifest_covers_all_raw_files", test_manifest_covers_all_raw),
    ("summaries_covers_all_articles", test_summaries_covers_all_articles),
    ("links_no_phantom_entries", test_links_no_phantoms),
    ("stats_matches_actual_file_count", test_stats_reflects_reality),
]


def run() -> dict:
    regen = _import_regen()
    results = []
    for name, fn in TESTS:
        try:
            ok, detail = fn(regen)
        except Exception as exc:  # pragma: no cover - defensive
            ok, detail = False, f"exception: {exc!r}"
        results.append({"name": name, "passed": bool(ok), "detail": detail})
    return {
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "failed": sum(1 for r in results if not r["passed"]),
        "tests": results,
        "ok": all(r["passed"] for r in results),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Regenerator tests")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    result = run()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("  Regenerator Tests (tools/compile/regen_meta.py)")
        print("=" * 60)
        for t in result["tests"]:
            sym = "\033[32m\u2713\033[0m" if t["passed"] else "\033[31m\u2717\033[0m"
            print(f"  {sym} {t['name']}: {t['detail']}")
        print()
        print(f"Total: {result['total']}  Passed: {result['passed']}  Failed: {result['failed']}")
        if result["ok"]:
            print("\033[32mAll regenerator tests passed.\033[0m")
        else:
            print("\033[31mRegenerator tests failed.\033[0m")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
