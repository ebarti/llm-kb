#!/usr/bin/env python3
"""
Retrieval Evaluation Harness.

For each Q in tools/eval/goldset.jsonl, call the BM25 search and score the
top-k results against the hand-labeled expected_citations. Reports Recall@5,
Recall@10, NDCG@5, and MRR, both per-question and aggregated.

Output is written to:
  output/eval-retrieval-<timestamp>.json  (machine-readable full report)
  output/eval-retrieval-latest.json       (symlink-like copy for CI)

Usage:
  python3 tools/eval/eval-retrieval.py
  python3 tools/eval/eval-retrieval.py --top-k 10 --goldset path/to/set.jsonl
  python3 tools/eval/eval-retrieval.py --ci     (non-interactive, exit code 0)
  python3 tools/eval/eval-retrieval.py --markdown output/report.md

Metric definitions:
  Recall@k = (# relevant in top-k) / (# relevant total)
  NDCG@k   = DCG@k / IDCG@k, with DCG = sum_i rel_i / log2(i + 2), i=0..k-1
             Ideal DCG assumes all relevant docs are ranked first.
  MRR      = 1 / rank of first relevant result (0 if none in top-k).
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SEARCH_DIR = REPO_ROOT / "tools" / "search-engine"
sys.path.insert(0, str(SEARCH_DIR))

import search  # noqa: E402  (must be imported after sys.path edit)


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def citation_to_doc_id(citation: str) -> str:
    """Normalize a gold-set citation string to the search engine's doc id.

    Gold-set stores citations like "wiki/concepts/retrieval-augmented-generation.md".
    Search indexes documents by "<subdir>/<stem>" (no "wiki/" prefix, no ".md").
    """
    c = citation.strip().strip('"').strip("'")
    # Strip leading wiki/
    if c.startswith("wiki/"):
        c = c[len("wiki/"):]
    # Strip [[wikilink]] brackets if present
    if c.startswith("[[") and c.endswith("]]"):
        c = c[2:-2]
    # Handle aliases like "concepts/foo|display"
    if "|" in c:
        c = c.split("|", 1)[0]
    # Strip trailing .md
    if c.endswith(".md"):
        c = c[:-3]
    return c


# ---------------------------------------------------------------------------
# Metric math
# ---------------------------------------------------------------------------

def recall_at_k(ranked_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if not relevant_ids:
        return 0.0
    top = ranked_ids[:k]
    hits = sum(1 for d in top if d in relevant_ids)
    return hits / len(relevant_ids)


def dcg_at_k(ranked_ids: list[str], relevant_ids: set[str], k: int) -> float:
    dcg = 0.0
    for i, doc_id in enumerate(ranked_ids[:k]):
        rel = 1.0 if doc_id in relevant_ids else 0.0
        if rel:
            dcg += rel / math.log2(i + 2)  # i is 0-indexed; position = i+1
    return dcg


def ndcg_at_k(ranked_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if not relevant_ids:
        return 0.0
    dcg = dcg_at_k(ranked_ids, relevant_ids, k)
    # Ideal DCG: best case all relevant docs are at the top (up to k slots).
    ideal_hits = min(len(relevant_ids), k)
    idcg = sum(1.0 / math.log2(i + 2) for i in range(ideal_hits))
    return dcg / idcg if idcg > 0 else 0.0


def mean_reciprocal_rank(ranked_ids: list[str], relevant_ids: set[str], k: int) -> float:
    for i, doc_id in enumerate(ranked_ids[:k]):
        if doc_id in relevant_ids:
            return 1.0 / (i + 1)
    return 0.0


def _percentile(samples: list[float], q: float) -> float:
    """Nearest-rank percentile for a non-empty list of samples.

    For q=0.95 and n=20 this returns the 19th-ranked sample (index 18), not
    the maximum, which `int(n * 0.95)` (== 19 == max index) would produce.
    """
    if not samples:
        return 0.0
    s = sorted(samples)
    n = len(s)
    # Nearest-rank: ceil(q * n), clamped to [1, n], then to 0-based index.
    rank = max(1, min(n, math.ceil(q * n)))
    return s[rank - 1]


# ---------------------------------------------------------------------------
# Gold-set loading
# ---------------------------------------------------------------------------

def load_goldset(path: Path) -> list[dict]:
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line_num, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{line_num}: invalid JSON — {e}")
            # Accept either `question` (preferred) or `q` (legacy) for backward
            # compatibility with older gold sets. Normalize to `question` in
            # memory so downstream readers only need one shape.
            if "question" not in item and "q" in item:
                item["question"] = item["q"]
            if "question" not in item or "expected_citations" not in item:
                raise ValueError(
                    f"{path}:{line_num}: entry missing 'question' or "
                    "'expected_citations'"
                )
            item.setdefault("id", f"q{line_num:03d}")
            items.append(item)
    return items


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate(goldset: list[dict], top_k: int, k_values: list[int]) -> dict:
    index = search.get_index()
    doc_universe = set(index["docs"].keys())

    per_q: list[dict] = []
    agg: dict[str, list[float]] = {}
    latencies: list[float] = []

    max_k = max([top_k] + k_values)

    for q in goldset:
        expected = [citation_to_doc_id(c) for c in q["expected_citations"]]
        # Warn (in output) if an expected citation is not even in the index.
        # Score against the FULL expected set so that missing-from-index gold
        # entries are reflected as recall misses rather than silently dropped
        # (which would inflate Recall@k). The missing list is preserved in the
        # report so the CI comment / reviewer can see them.
        missing_from_index = [c for c in expected if c not in doc_universe]
        relevant = set(expected)

        question_text = q.get("question") or q.get("q") or ""
        start = time.perf_counter()
        results = search.search(question_text, index, top_n=max_k)
        latency_ms = (time.perf_counter() - start) * 1000.0
        latencies.append(latency_ms)

        ranked_ids = [r["id"] for r in results]

        q_metrics: dict[str, float] = {}
        for k in k_values:
            rk = recall_at_k(ranked_ids, relevant, k)
            nk = ndcg_at_k(ranked_ids, relevant, k)
            q_metrics[f"recall@{k}"] = round(rk, 4)
            q_metrics[f"ndcg@{k}"] = round(nk, 4)
            agg.setdefault(f"recall@{k}", []).append(rk)
            agg.setdefault(f"ndcg@{k}", []).append(nk)

        mrr_val = mean_reciprocal_rank(ranked_ids, relevant, max_k)
        q_metrics[f"mrr@{max_k}"] = round(mrr_val, 4)
        agg.setdefault(f"mrr@{max_k}", []).append(mrr_val)

        per_q.append({
            "id": q.get("id"),
            "question": question_text,
            "type": q.get("type"),
            "tags": q.get("tags", []),
            "expected": expected,
            "missing_from_index": missing_from_index,
            "top_results": ranked_ids[:max_k],
            "latency_ms": round(latency_ms, 2),
            "metrics": q_metrics,
        })

    aggregated = {
        name: round(sum(values) / len(values), 4) if values else 0.0
        for name, values in agg.items()
    }

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "goldset_size": len(goldset),
        "top_k": top_k,
        "k_values": k_values,
        "index_size": index["num_docs"],
        "aggregated_metrics": aggregated,
        "latency_ms": {
            "avg": round(sum(latencies) / len(latencies), 2) if latencies else 0.0,
            "p95": round(_percentile(latencies, 0.95), 2) if latencies else 0.0,
            "max": round(max(latencies), 2) if latencies else 0.0,
        },
        "per_question": per_q,
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def render_markdown(report: dict) -> str:
    lines = []
    lines.append(f"# Retrieval Eval Report — {report['timestamp']}")
    lines.append("")
    lines.append(
        f"Gold set: **{report['goldset_size']}** questions | "
        f"Index: **{report['index_size']}** articles | "
        f"Top-k scored: **{report['top_k']}**"
    )
    lines.append("")
    lines.append("## Aggregated Metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for name, val in report["aggregated_metrics"].items():
        lines.append(f"| {name} | {val:.4f} |")
    lines.append("")
    lat = report["latency_ms"]
    lines.append(
        f"Latency — avg: {lat['avg']}ms, p95: {lat['p95']}ms, max: {lat['max']}ms"
    )
    lines.append("")

    lines.append("## Per-Question Results")
    lines.append("")

    # Build per-question table columns from the report's requested k-values
    # rather than hardcoding Recall@5 / Recall@10 / NDCG@5. This keeps the
    # markdown report faithful when callers pass custom --k-values; hardcoded
    # columns would silently print 0.00 for metrics that were never scored.
    k_values = sorted(set(report.get("k_values") or [5, 10]))
    recall_headers = [f"Recall@{k}" for k in k_values]
    ndcg_headers = [f"NDCG@{k}" for k in k_values]
    header_cells = ["ID", "Type", *recall_headers, *ndcg_headers, "First Hit Rank"]
    lines.append("| " + " | ".join(header_cells) + " |")
    lines.append("|" + "|".join(["---"] * len(header_cells)) + "|")

    for q in report["per_question"]:
        m = q["metrics"]
        ranked = q["top_results"]
        expected = set(q["expected"])
        first_rank = next(
            (str(i + 1) for i, d in enumerate(ranked) if d in expected), "—"
        )
        recall_cells = [f"{m.get(f'recall@{k}', 0):.2f}" for k in k_values]
        ndcg_cells = [f"{m.get(f'ndcg@{k}', 0):.2f}" for k in k_values]
        row_cells = [
            str(q["id"]),
            str(q.get("type", "?")),
            *recall_cells,
            *ndcg_cells,
            first_rank,
        ]
        lines.append("| " + " | ".join(row_cells) + " |")
    lines.append("")
    return "\n".join(lines)


def ci_miss_metric_name(report: dict) -> str:
    k_values = report.get("k_values") or []
    if k_values:
        return f"recall@{max(k_values)}"

    recall_metrics = [
        name for name in report.get("aggregated_metrics", {})
        if name.startswith("recall@")
    ]
    if recall_metrics:
        return max(recall_metrics, key=lambda name: int(name.split("@", 1)[1]))

    return "recall@10"


def render_ci_summary(report: dict) -> str:
    """Terse stdout summary for CI logs."""
    m = report["aggregated_metrics"]
    lines = [
        f"Retrieval eval — {report['goldset_size']} questions over "
        f"{report['index_size']} articles",
    ]
    for name, val in m.items():
        lines.append(f"  {name:12s} {val:.4f}")
    lat = report["latency_ms"]
    lines.append(
        f"  latency avg  {lat['avg']:.2f}ms | p95 {lat['p95']:.2f}ms"
    )
    # Surface any per-question misses for CI visibility
    miss_metric = ci_miss_metric_name(report)
    misses = [
        q for q in report["per_question"]
        if q["metrics"].get(miss_metric, 0) == 0
    ]
    if misses:
        lines.append(f"  miss(0 {miss_metric}): {len(misses)} question(s)")
        for q in misses:
            # Prefer `question`, fall back to legacy `q` for older reports.
            qtext = q.get("question") or q.get("q") or ""
            lines.append(f"    {q['id']}  — {qtext[:70]}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--goldset",
        default=str(Path(__file__).resolve().parent / "goldset.jsonl"),
        help="Path to goldset JSONL (default: tools/eval/goldset.jsonl)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Max top-k to retrieve (default: 10)",
    )
    parser.add_argument(
        "--k-values",
        type=int,
        nargs="+",
        default=[5, 10],
        help="k values to score Recall@k and NDCG@k for (default: 5 10)",
    )
    parser.add_argument(
        "--output-dir",
        default=str(REPO_ROOT / "output"),
        help="Directory to write report JSON to (default: output/)",
    )
    parser.add_argument(
        "--markdown",
        default=None,
        help="Also write a Markdown report to this path",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: write output/eval-retrieval-latest.json and a terse summary",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress stdout summary (only write files)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full JSON report to stdout",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help=(
            "Exit non-zero if the aggregated recall at the highest requested "
            "--k-values falls below this threshold. Disabled by default so CI "
            "reports drift without blocking."
        ),
    )
    args = parser.parse_args()

    goldset_path = Path(args.goldset)
    if not goldset_path.exists():
        print(f"ERROR: gold-set file not found: {goldset_path}", file=sys.stderr)
        return 2

    goldset = load_goldset(goldset_path)
    if len(goldset) == 0:
        print("ERROR: gold set is empty.", file=sys.stderr)
        return 2

    report = evaluate(goldset, top_k=args.top_k, k_values=args.k_values)

    # Write report files
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    report_path = output_dir / f"eval-retrieval-{ts}.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    latest_path = output_dir / "eval-retrieval-latest.json"
    latest_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md_path = None
    if args.markdown:
        md_path = Path(args.markdown)
    elif args.ci:
        md_path = output_dir / "eval-retrieval-latest.md"
    if md_path is not None:
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(render_markdown(report), encoding="utf-8")

    # Stdout
    if args.json:
        print(json.dumps(report, indent=2))
    elif not args.quiet:
        print(render_ci_summary(report))
        print(f"\nReport written to: {report_path}")
        if md_path is not None:
            print(f"Markdown report:   {md_path}")

    # --fail-under gate
    if args.fail_under is not None:
        metric_name = ci_miss_metric_name(report)
        recall_val = report["aggregated_metrics"].get(metric_name, 0.0)
        if recall_val < args.fail_under:
            print(
                f"FAIL: {metric_name}={recall_val:.4f} below threshold "
                f"{args.fail_under:.4f}",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
