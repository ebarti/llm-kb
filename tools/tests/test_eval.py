#!/usr/bin/env python3
"""
Tests for the evaluation harness.

Validates:
  - goldset.jsonl schema (required keys, types, uniqueness of ids)
  - citation normalization
  - metric math (Recall@k, DCG/IDCG/NDCG@k, MRR) on hand-verifiable cases
  - every expected_citation resolves to an existing wiki file
  - eval-retrieval and eval-generation scripts run end-to-end

Run:
  python3 tools/tests/test_eval.py
  python3 tools/tests/test_eval.py --json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EVAL_DIR = REPO_ROOT / "tools" / "eval"
GOLDSET = EVAL_DIR / "goldset.jsonl"
RETRIEVAL_SCRIPT = EVAL_DIR / "eval-retrieval.py"
GENERATION_SCRIPT = EVAL_DIR / "eval-generation.py"
WIKI_DIR = REPO_ROOT / "wiki"

# Dynamically import eval-retrieval (filename has a hyphen so dynamic load)
_spec = importlib.util.spec_from_file_location("eval_retrieval", RETRIEVAL_SCRIPT)
eval_retrieval = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(eval_retrieval)  # type: ignore[union-attr]


# ---------------------------------------------------------------------------
# Test runner (tiny homegrown harness to avoid pytest dependency)
# ---------------------------------------------------------------------------

class TestResult:
    def __init__(self, name: str, passed: bool, message: str = ""):
        self.name = name
        self.passed = passed
        self.message = message

    def to_dict(self) -> dict:
        return {"name": self.name, "passed": self.passed, "message": self.message}


RESULTS: list[TestResult] = []


def check(name: str, ok: bool, message: str = "") -> None:
    RESULTS.append(TestResult(name, ok, message))


def expect(actual, expected, label: str) -> None:
    ok = actual == expected
    msg = "" if ok else f"{label}: expected {expected!r}, got {actual!r}"
    check(label, ok, msg)


def expect_close(actual: float, expected: float, label: str, tol: float = 1e-6) -> None:
    ok = abs(actual - expected) < tol
    msg = "" if ok else (
        f"{label}: expected {expected:.6f} ± {tol}, got {actual:.6f}"
    )
    check(label, ok, msg)


# ---------------------------------------------------------------------------
# Goldset schema tests
# ---------------------------------------------------------------------------

REQUIRED_KEYS = {"q", "expected_citations"}
RECOMMENDED_KEYS = {"expected_answer_sketch", "tags", "type", "id"}


def test_goldset_schema() -> None:
    check("goldset exists", GOLDSET.exists(), f"{GOLDSET} missing")
    if not GOLDSET.exists():
        return

    entries = []
    with GOLDSET.open("r", encoding="utf-8") as f:
        for line_num, raw in enumerate(f, 1):
            line = raw.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                check(f"line {line_num} valid JSON", False, str(e))
                continue
            check(f"line {line_num} valid JSON", True)
            entries.append((line_num, entry))

    check(
        "goldset has >= 20 entries",
        len(entries) >= 20,
        f"found {len(entries)}",
    )

    ids_seen: set[str] = set()
    tag_types_seen: set[str] = set()
    for line_num, e in entries:
        missing = REQUIRED_KEYS - e.keys()
        check(f"q{line_num} has required keys", not missing, f"missing {missing}")
        if "q" in e:
            check(
                f"q{line_num} question non-empty string",
                isinstance(e["q"], str) and bool(e["q"].strip()),
            )
        if "expected_citations" in e:
            check(
                f"q{line_num} expected_citations is list",
                isinstance(e["expected_citations"], list)
                and all(isinstance(c, str) for c in e["expected_citations"]),
            )
            check(
                f"q{line_num} at least one expected citation",
                len(e["expected_citations"]) >= 1,
            )
        if "id" in e:
            check(
                f"q{line_num} id is unique",
                e["id"] not in ids_seen,
                f"duplicate id {e['id']!r}",
            )
            ids_seen.add(e["id"])
        if "type" in e:
            tag_types_seen.add(str(e["type"]))

    # Gold set should span multiple article types to be meaningful
    check(
        "gold set covers at least 3 question types",
        len(tag_types_seen) >= 3,
        f"types seen: {sorted(tag_types_seen)}",
    )


def test_expected_citations_exist() -> None:
    if not GOLDSET.exists():
        return
    missing = []
    with GOLDSET.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            for c in entry.get("expected_citations", []):
                path = c[len("wiki/"):] if c.startswith("wiki/") else c
                if (REPO_ROOT / "wiki" / path.lstrip("/")).exists():
                    continue
                # Also accept the doc-id style "concepts/foo" without .md
                doc_id = eval_retrieval.citation_to_doc_id(c)
                if (WIKI_DIR / f"{doc_id}.md").exists():
                    continue
                missing.append((entry.get("id"), c))
    check(
        "every expected_citation resolves to a wiki file",
        not missing,
        f"{len(missing)} broken — first few: {missing[:3]}",
    )


# ---------------------------------------------------------------------------
# Citation normalization tests
# ---------------------------------------------------------------------------

def test_citation_to_doc_id() -> None:
    expect(
        eval_retrieval.citation_to_doc_id("wiki/concepts/foo.md"),
        "concepts/foo",
        "normalize wiki path",
    )
    expect(
        eval_retrieval.citation_to_doc_id("concepts/foo"),
        "concepts/foo",
        "already normalized",
    )
    expect(
        eval_retrieval.citation_to_doc_id("[[concepts/foo]]"),
        "concepts/foo",
        "strip wikilink brackets",
    )
    expect(
        eval_retrieval.citation_to_doc_id("concepts/foo|display"),
        "concepts/foo",
        "strip wikilink alias",
    )
    expect(
        eval_retrieval.citation_to_doc_id("wiki/entities/bar.md"),
        "entities/bar",
        "normalize entity path",
    )


# ---------------------------------------------------------------------------
# Metric math tests
# ---------------------------------------------------------------------------

def test_recall_at_k() -> None:
    # 3 relevant docs total; top-5 contains all 3 -> recall@5 = 1.0
    ranked = ["a", "b", "c", "d", "e"]
    rel = {"a", "b", "c"}
    expect_close(
        eval_retrieval.recall_at_k(ranked, rel, 5), 1.0, "recall@5 all found"
    )
    # top-2 contains 2 of 3 -> 2/3
    expect_close(
        eval_retrieval.recall_at_k(ranked, rel, 2), 2 / 3, "recall@2 partial"
    )
    # no relevant -> 0
    expect_close(
        eval_retrieval.recall_at_k(ranked, {"z"}, 5), 0.0, "recall no hit"
    )
    # empty relevant -> 0 (no divide by zero)
    expect_close(
        eval_retrieval.recall_at_k(ranked, set(), 5), 0.0, "recall empty rel"
    )


def test_dcg_and_ndcg() -> None:
    ranked = ["a", "b", "c", "d"]
    rel = {"a", "c"}
    # DCG@3 = 1/log2(2) + 0/log2(3) + 1/log2(4) = 1.0 + 0 + 0.5 = 1.5
    expect_close(
        eval_retrieval.dcg_at_k(ranked, rel, 3), 1.5, "dcg@3 manual"
    )
    # IDCG@3 with 2 relevant = 1/log2(2) + 1/log2(3) = 1 + 0.63093...
    idcg_expected = 1.0 + (1.0 / math.log2(3))
    ndcg_expected = 1.5 / idcg_expected
    expect_close(
        eval_retrieval.ndcg_at_k(ranked, rel, 3),
        ndcg_expected,
        "ndcg@3 manual",
        tol=1e-6,
    )

    # Perfect ranking -> NDCG = 1.0
    expect_close(
        eval_retrieval.ndcg_at_k(["a", "b", "x", "y"], {"a", "b"}, 4),
        1.0,
        "ndcg perfect ranking",
    )

    # Reverse order: worst case still > 0
    ndcg_bad = eval_retrieval.ndcg_at_k(
        ["x", "y", "a", "b"], {"a", "b"}, 4
    )
    check(
        "ndcg reverse order < ndcg perfect",
        0.0 < ndcg_bad < 1.0,
        f"got ndcg={ndcg_bad}",
    )


def test_mrr() -> None:
    # First relevant at rank 2 -> 0.5
    expect_close(
        eval_retrieval.mean_reciprocal_rank(["x", "a", "b"], {"a"}, 5),
        0.5,
        "mrr rank 2",
    )
    expect_close(
        eval_retrieval.mean_reciprocal_rank(["a", "b"], {"a"}, 5),
        1.0,
        "mrr rank 1",
    )
    expect_close(
        eval_retrieval.mean_reciprocal_rank(["x", "y"], {"a"}, 5),
        0.0,
        "mrr no hit",
    )


# ---------------------------------------------------------------------------
# End-to-end script smoke tests
# ---------------------------------------------------------------------------

def test_retrieval_script_runs() -> None:
    with tempfile.TemporaryDirectory() as td:
        rc = subprocess.run(
            [
                sys.executable,
                str(RETRIEVAL_SCRIPT),
                "--output-dir",
                td,
                "--quiet",
                "--k-values",
                "5",
                "10",
                "--top-k",
                "10",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
        )
        ok = rc.returncode == 0
        check(
            "eval-retrieval.py exits 0",
            ok,
            f"stdout={rc.stdout[:200]} stderr={rc.stderr[:200]}",
        )
        latest = Path(td) / "eval-retrieval-latest.json"
        check("eval-retrieval produces latest.json", latest.exists())
        if latest.exists():
            data = json.loads(latest.read_text())
            for key in ("recall@5", "recall@10", "ndcg@5", "ndcg@10"):
                check(
                    f"retrieval report contains {key}",
                    key in data.get("aggregated_metrics", {}),
                )


def test_generation_script_runs() -> None:
    with tempfile.TemporaryDirectory() as td:
        rc = subprocess.run(
            [
                sys.executable,
                str(GENERATION_SCRIPT),
                "--output-dir",
                td,
                "--mode",
                "mock",
                "--top-k",
                "3",
                "--quiet",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
        )
        ok = rc.returncode == 0
        check(
            "eval-generation.py exits 0",
            ok,
            f"stdout={rc.stdout[:200]} stderr={rc.stderr[:200]}",
        )
        latest = Path(td) / "eval-generation-latest.json"
        check("eval-generation produces latest.json", latest.exists())
        if latest.exists():
            data = json.loads(latest.read_text())
            for key in ("correctness", "citation_accuracy", "groundedness"):
                check(
                    f"generation report contains {key}",
                    key in data.get("aggregated_scores", {}),
                )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

TESTS = [
    test_goldset_schema,
    test_expected_citations_exist,
    test_citation_to_doc_id,
    test_recall_at_k,
    test_dcg_and_ndcg,
    test_mrr,
    test_retrieval_script_runs,
    test_generation_script_runs,
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    for t in TESTS:
        try:
            t()
        except Exception as e:  # noqa: BLE001
            RESULTS.append(TestResult(t.__name__, False, f"exception: {e!r}"))

    passed = sum(1 for r in RESULTS if r.passed)
    failed = len(RESULTS) - passed

    if args.json:
        print(
            json.dumps(
                {
                    "total": len(RESULTS),
                    "passed": passed,
                    "failed": failed,
                    "ok": failed == 0,
                    "results": [r.to_dict() for r in RESULTS],
                },
                indent=2,
            )
        )
    else:
        print("=" * 60)
        print("  Eval Harness Tests")
        print("=" * 60)
        for r in RESULTS:
            icon = "\033[32m✓\033[0m" if r.passed else "\033[31m✗\033[0m"
            print(f"  {icon} {r.name}")
            if not r.passed and r.message:
                print(f"      {r.message}")
        print()
        print(f"Total: {len(RESULTS)}  Passed: {passed}  Failed: {failed}")
        if failed == 0:
            print("\033[32mALL EVAL HARNESS TESTS PASSED\033[0m")
        else:
            print(f"\033[31m{failed} TEST(S) FAILED\033[0m")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
