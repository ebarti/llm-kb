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


def _load_eval_retrieval():
    """Dynamically import eval-retrieval.py (hyphen in filename).

    This is deferred so that a missing/broken script surfaces as a test
    failure via `check()` rather than crashing the entire test runner at
    import time.
    """
    spec = importlib.util.spec_from_file_location(
        "eval_retrieval", RETRIEVAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise ImportError(
            f"could not load module spec for {RETRIEVAL_SCRIPT}"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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

REQUIRED_KEYS = {"question", "expected_citations", "expected_answer_sketch"}
RECOMMENDED_KEYS = {"tags", "type", "id"}


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
        # Legacy `q` is accepted by load_goldset(), but new gold sets should
        # use `question`. Enforce the new name in tests to catch regressions.
        missing = REQUIRED_KEYS - e.keys()
        check(f"q{line_num} has required keys", not missing, f"missing {missing}")
        if "question" in e:
            check(
                f"q{line_num} question non-empty string",
                isinstance(e["question"], str) and bool(e["question"].strip()),
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
        if "expected_answer_sketch" in e:
            check(
                f"q{line_num} expected_answer_sketch non-empty string",
                isinstance(e["expected_answer_sketch"], str)
                and bool(e["expected_answer_sketch"].strip()),
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
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
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


def test_load_goldset_requires_expected_answer_sketch() -> None:
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return

    with tempfile.TemporaryDirectory() as td:
        fixture = Path(td) / "goldset.jsonl"
        fixture.write_text(
            json.dumps({
                "id": "qfx-missing-sketch",
                "question": "What is RAG?",
                "expected_citations": [
                    "wiki/concepts/retrieval-augmented-generation.md",
                ],
            })
            + "\n",
            encoding="utf-8",
        )

        try:
            eval_retrieval.load_goldset(fixture)
        except ValueError as e:
            check(
                "load_goldset rejects entries missing expected_answer_sketch",
                "expected_answer_sketch" in str(e),
                str(e),
            )
        else:
            check(
                "load_goldset rejects entries missing expected_answer_sketch",
                False,
                "load_goldset accepted an entry without expected_answer_sketch",
            )


# ---------------------------------------------------------------------------
# Citation normalization tests
# ---------------------------------------------------------------------------

def test_citation_to_doc_id() -> None:
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
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
        eval_retrieval.citation_to_doc_id("[[wiki/concepts/foo.md]]"),
        "concepts/foo",
        "normalize wiki-prefixed wikilink",
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
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
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
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
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
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
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


def test_render_markdown_uses_report_k_values() -> None:
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
    report = {
        "timestamp": "2026-01-01T00:00:00+00:00",
        "goldset_size": 1,
        "top_k": 3,
        "k_values": [3],
        "index_size": 10,
        "aggregated_metrics": {"recall@3": 1.0, "ndcg@3": 1.0, "mrr@3": 1.0},
        "latency_ms": {"avg": 1.0, "p95": 1.0, "max": 1.0},
        "per_question": [
            {
                "id": "qmd1",
                "type": "concept",
                "top_results": ["a"],
                "expected": ["a"],
                "metrics": {"recall@3": 1.0, "ndcg@3": 1.0, "mrr@3": 1.0},
            }
        ],
    }
    md = eval_retrieval.render_markdown(report)
    # Header must reflect the requested k=3, not hardcoded 5/10.
    check(
        "markdown header includes Recall@3",
        "Recall@3" in md,
        md,
    )
    check(
        "markdown header includes NDCG@3",
        "NDCG@3" in md,
        md,
    )
    # And must NOT silently render columns for unscored ks.
    check(
        "markdown header omits unscored Recall@10",
        "Recall@10" not in md,
        md,
    )
    check(
        "markdown header omits unscored NDCG@5",
        "NDCG@5" not in md,
        md,
    )


def test_render_ci_summary_uses_report_k_values() -> None:
    try:
        eval_retrieval = _load_eval_retrieval()
    except Exception as e:  # noqa: BLE001
        check(
            "eval-retrieval module importable",
            False,
            f"import failed: {e!r}",
        )
        return
    report = {
        "goldset_size": 2,
        "index_size": 42,
        "k_values": [5],
        "aggregated_metrics": {"recall@5": 0.5, "ndcg@5": 0.5},
        "latency_ms": {"avg": 12.3, "p95": 18.4},
        "per_question": [
            {
                "id": "q-hit",
                "question": "question with a relevant result",
                "metrics": {"recall@5": 1.0},
            },
            {
                "id": "q-miss",
                "question": "question with no relevant result",
                "metrics": {"recall@5": 0.0},
            },
        ],
    }

    summary = eval_retrieval.render_ci_summary(report)

    check(
        "ci summary labels misses with requested recall metric",
        "miss(0 recall@5): 1 question(s)" in summary,
        summary,
    )
    check(
        "ci summary lists only actual misses for requested recall metric",
        "q-miss" in summary and "q-hit" not in summary,
        summary,
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


def test_retrieval_fail_under_uses_custom_k_values() -> None:
    """Regression guard for --fail-under with a custom --k-values.

    The CLI used to hardcode recall@10 for its --fail-under threshold, which
    meant passing --k-values 5 silently compared against a metric the user
    didn't request. The threshold and the summary miss label must both use
    the highest requested k (recall@5 here, not recall@10).
    """
    # Build a tiny fixture goldset so the test does not depend on the
    # production gold set or on the search-engine index shape.
    with tempfile.TemporaryDirectory() as td:
        fixture = Path(td) / "goldset.jsonl"
        fixture.write_text(
            json.dumps({
                "id": "qfx1",
                "question": "what is retrieval augmented generation",
                "expected_citations": [
                    "wiki/concepts/retrieval-augmented-generation.md",
                ],
                "expected_answer_sketch": (
                    "RAG retrieves relevant documents at query time."
                ),
                "type": "concept",
            })
            + "\n",
            encoding="utf-8",
        )

        # Threshold chosen above 1.0 so the run is guaranteed to fail with
        # exit code 1 regardless of real retrieval performance.
        rc = subprocess.run(
            [
                sys.executable,
                str(RETRIEVAL_SCRIPT),
                "--goldset",
                str(fixture),
                "--k-values",
                "5",
                "--top-k",
                "5",
                "--output-dir",
                td,
                "--fail-under",
                "1.5",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
        )

        check(
            "--fail-under above ceiling exits 1",
            rc.returncode == 1,
            f"exit={rc.returncode} stdout={rc.stdout[:200]} stderr={rc.stderr[:200]}",
        )
        # The failure message must name the metric derived from --k-values,
        # not the legacy recall@10.
        check(
            "--fail-under error names recall@5 (not recall@10)",
            "recall@5" in rc.stderr and "recall@10" not in rc.stderr,
            f"stderr={rc.stderr[:300]}",
        )
        # The non-quiet stdout summary must not reference recall@10 when the
        # user requested --k-values 5 (miss line, if present, uses recall@5).
        check(
            "ci summary does not mention recall@10 under --k-values 5",
            "recall@10" not in rc.stdout,
            f"stdout={rc.stdout[:300]}",
        )
        # And it must include the recall@5 metric line.
        check(
            "ci summary includes recall@5 metric",
            "recall@5" in rc.stdout,
            f"stdout={rc.stdout[:300]}",
        )


def test_retrieval_rejects_top_k_below_k_values() -> None:
    with tempfile.TemporaryDirectory() as td:
        fixture = Path(td) / "goldset.jsonl"
        fixture.write_text(
            json.dumps({
                "id": "qfx-topk",
                "question": "what is retrieval augmented generation",
                "expected_citations": [
                    "wiki/concepts/retrieval-augmented-generation.md",
                ],
                "expected_answer_sketch": "RAG retrieves documents at query time.",
            })
            + "\n",
            encoding="utf-8",
        )

        rc = subprocess.run(
            [
                sys.executable,
                str(RETRIEVAL_SCRIPT),
                "--goldset",
                str(fixture),
                "--k-values",
                "10",
                "--top-k",
                "5",
                "--output-dir",
                td,
                "--quiet",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
        )

        check(
            "--top-k below requested --k-values exits 2",
            rc.returncode == 2,
            f"exit={rc.returncode} stdout={rc.stdout[:200]} stderr={rc.stderr[:200]}",
        )
        check(
            "--top-k validation mentions requested k-values",
            "--top-k" in rc.stderr and "--k-values" in rc.stderr,
            f"stderr={rc.stderr[:300]}",
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


def test_generation_import_guard_for_missing_retrieval_loader() -> None:
    script = r"""
import importlib.machinery
import importlib.util
import sys
from pathlib import Path
from unittest import mock

path = Path("tools/eval/eval-generation.py")
spec = importlib.util.spec_from_file_location("eval_generation_under_test", path)
if spec is None or spec.loader is None:
    print("could not load eval-generation.py", file=sys.stderr)
    sys.exit(90)
module = importlib.util.module_from_spec(spec)

missing_loader = importlib.machinery.ModuleSpec("eval_retrieval", None)
with mock.patch("importlib.util.spec_from_file_location", return_value=missing_loader):
    try:
        spec.loader.exec_module(module)
    except ImportError as e:
        if "eval-retrieval" in str(e):
            sys.exit(0)
        print(str(e), file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(4)
    else:
        print("missing ImportError", file=sys.stderr)
        sys.exit(5)
"""
    rc = subprocess.run(
        [sys.executable, "-c", script],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )
    check(
        "eval-generation import guard raises ImportError for missing loader",
        rc.returncode == 0,
        f"exit={rc.returncode} stdout={rc.stdout[:200]} stderr={rc.stderr[:200]}",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

TESTS = [
    test_goldset_schema,
    test_expected_citations_exist,
    test_load_goldset_requires_expected_answer_sketch,
    test_citation_to_doc_id,
    test_recall_at_k,
    test_dcg_and_ndcg,
    test_mrr,
    test_render_markdown_uses_report_k_values,
    test_render_ci_summary_uses_report_k_values,
    test_retrieval_script_runs,
    test_retrieval_fail_under_uses_custom_k_values,
    test_retrieval_rejects_top_k_below_k_values,
    test_generation_script_runs,
    test_generation_import_guard_for_missing_retrieval_loader,
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
