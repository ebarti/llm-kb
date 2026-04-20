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
from tempfile import TemporaryDirectory


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


def _parse_links_md(text: str) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    declared_outgoing: dict[str, set[str]] = {}
    declared_incoming: dict[str, set[str]] = {}
    current_article = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("## ") and line not in {"## Orphan Pages", "## Summary"}:
            current_article = line[3:].strip()
            declared_outgoing.setdefault(current_article, set())
            declared_incoming.setdefault(current_article, set())
        elif current_article and line.startswith("→"):
            declared_outgoing[current_article].update(
                link.strip()
                for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)
            )
        elif current_article and line.startswith("←"):
            declared_incoming[current_article].update(
                link.strip()
                for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)
            )

    return declared_outgoing, declared_incoming


def _actual_self_links() -> set[str]:
    self_links: set[str] = set()
    for sub in ("concepts", "sources", "entities", "comparisons"):
        directory = WIKI_DIR / sub
        if not directory.is_dir():
            continue
        for article in sorted(directory.glob("*.md")):
            article_id = f"{sub}/{article.stem}"
            text = article.read_text(encoding="utf-8", errors="replace")
            for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text):
                target = link.split("#", 1)[0].strip()
                if target.endswith(".md"):
                    target = target[:-3]
                if target == article_id:
                    self_links.add(article_id)
                    break
    return self_links


def test_committed_artifacts_are_up_to_date(regen) -> tuple[bool, str]:
    """Preflight: the committed wiki/_meta files must match what the
    regenerator would emit right now. This runs before any other test
    mutates META_DIR, so a stale checked-in artifact surfaces as a real
    failure instead of being silently repaired.

    ``freshness-report.md`` is excluded because its ``last_updated`` /
    ``age_days`` values are anchored to wall-clock ``date.today()`` by
    design, so a day-over-day drift is expected and handled by its own
    regeneration on compile.
    """
    targets = ("stats.json", "manifest.md", "summaries.md", "links.md")
    scan = regen.WikiScan()
    scan.scan()
    renderers = {
        "stats.json": regen.render_stats,
        "manifest.md": regen.render_manifest,
        "summaries.md": regen.render_summaries,
        "links.md": regen.render_links,
    }
    stale: list[str] = []
    for name in targets:
        existing = (META_DIR / name).read_text(encoding="utf-8") if (META_DIR / name).exists() else ""
        expected = renderers[name](scan)
        if existing != expected:
            stale.append(name)
    return (not stale), (
        "all committed meta files up to date"
        if not stale
        else f"stale committed artifacts: {stale} (run ./kb compile or python3 tools/compile/regen_meta.py)"
    )


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


def test_stats_preserves_existing_history(regen) -> tuple[bool, str]:
    scan = regen.WikiScan()
    scan.scan()
    current_timestamp = scan.generated_date.isoformat()

    with TemporaryDirectory() as tmpdir:
        tmp_meta_dir = Path(tmpdir)
        seed_history = [
            {"timestamp": "2026-03-01 12:00", "total_words": 111, "total_files": 11},
            {"timestamp": current_timestamp, "total_words": 1, "total_files": 1},
            {"timestamp": "2026-03-15 12:00", "total_words": 222, "total_files": 22},
        ]
        (tmp_meta_dir / "stats.json").write_text(
            json.dumps({"current": {}, "history": seed_history}, indent=2) + "\n",
            encoding="utf-8",
        )

        original_meta_dir = regen.META_DIR
        try:
            regen.META_DIR = tmp_meta_dir
            regen.regenerate(quiet=True)
        finally:
            regen.META_DIR = original_meta_dir

        data = json.loads((tmp_meta_dir / "stats.json").read_text(encoding="utf-8"))
        history = data["history"]
        timestamps = [entry["timestamp"] for entry in history]

        preserved = {"2026-03-01 12:00", "2026-03-15 12:00"}.issubset(timestamps)
        current_entries = [entry for entry in history if entry["timestamp"] == current_timestamp]
        replaced_snapshot = (
            len(current_entries) == 1
            and current_entries[0]["total_words"] == data["current"]["total_words"]
            and current_entries[0]["total_files"] == data["current"]["total_files"]
        )

        ok = preserved and replaced_snapshot
        detail = (
            f"history_len={len(history)} preserved_prior={preserved} "
            f"current_entries={len(current_entries)}"
        )
        return ok, detail


def test_links_include_self_links(regen) -> tuple[bool, str]:
    regen.regenerate(quiet=True)
    expected_self_links = _actual_self_links()
    text = (META_DIR / "links.md").read_text(encoding="utf-8")
    declared_outgoing, _declared_incoming = _parse_links_md(text)

    missing = sorted(
        article_id
        for article_id in expected_self_links
        if article_id not in declared_outgoing.get(article_id, set())
    )
    return (not missing), (
        f"{len(expected_self_links)}/{len(expected_self_links)} self-links preserved"
        if not missing
        else f"missing self-links for: {missing[:5]}"
    )


TESTS = [
    # Preflight must run first -- subsequent tests call regenerate() and
    # would silently repair any stale committed artifacts.
    ("committed_artifacts_are_up_to_date", test_committed_artifacts_are_up_to_date),
    ("produces_all_five_files", test_produces_all_files),
    ("idempotent_second_run_is_noop", test_idempotent),
    ("check_mode_clean_after_regen", test_check_mode_clean),
    ("manifest_covers_all_raw_files", test_manifest_covers_all_raw),
    ("summaries_covers_all_articles", test_summaries_covers_all_articles),
    ("links_no_phantom_entries", test_links_no_phantoms),
    ("stats_matches_actual_file_count", test_stats_reflects_reality),
    ("stats_preserves_existing_history", test_stats_preserves_existing_history),
    ("links_include_self_links", test_links_include_self_links),
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
