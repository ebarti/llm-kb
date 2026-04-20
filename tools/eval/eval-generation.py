#!/usr/bin/env python3
"""
Generation Evaluation Harness.

For each Q in the gold set:
  1. Retrieve the top-k articles using the BM25 search engine.
  2. Compose an answer grounded in the retrieved articles.
  3. Score the answer on {correctness, citation_accuracy, groundedness}
     using an LLM judge.

Two modes:

  --mode mock     (default) deterministic no-network scoring. Citation accuracy
                  is computed by set overlap with expected_citations;
                  correctness is a token-overlap proxy between the composed
                  answer and expected_answer_sketch; groundedness is measured
                  as the fraction of composed-answer tokens backed by the
                  retrieved corpus. This mode is used in CI and for smoke
                  tests, so no API key is required.

  --mode api      uses the Anthropic SDK if ANTHROPIC_API_KEY is set. Both
                  the answer composition step and the judge use Claude. Opt-in
                  because it costs real money.

Output:
  output/eval-generation-<timestamp>.json
  output/eval-generation-latest.json

Usage:
  python3 tools/eval/eval-generation.py
  python3 tools/eval/eval-generation.py --mode api
  python3 tools/eval/eval-generation.py --top-k 5 --goldset path.jsonl
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SEARCH_DIR = REPO_ROOT / "tools" / "search-engine"
WIKI_DIR = REPO_ROOT / "wiki"
sys.path.insert(0, str(SEARCH_DIR))

import search  # noqa: E402

# Reuse gold-set loader + citation normalizer from eval-retrieval
sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib.util

_retrieval_path = Path(__file__).resolve().parent / "eval-retrieval.py"
_spec = importlib.util.spec_from_file_location("eval_retrieval", _retrieval_path)
eval_retrieval = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(eval_retrieval)  # type: ignore[union-attr]

citation_to_doc_id = eval_retrieval.citation_to_doc_id
load_goldset = eval_retrieval.load_goldset


# ---------------------------------------------------------------------------
# Tokenization helpers for mock-mode scoring
# ---------------------------------------------------------------------------

_STOP = frozenset(search.STOP_WORDS)


def tokens(text: str) -> set[str]:
    return {t for t in search.tokenize(text) if t not in _STOP and len(t) > 2}


# ---------------------------------------------------------------------------
# Article loading
# ---------------------------------------------------------------------------

def load_article(doc_id: str) -> tuple[str, str]:
    """Return (title, body_text) for a doc_id like 'concepts/foo'."""
    path = WIKI_DIR / f"{doc_id}.md"
    if not path.exists():
        return doc_id, ""
    raw = path.read_text(encoding="utf-8")
    meta, body = search.parse_frontmatter(raw)
    title = meta.get("title", doc_id)
    return title, body


# ---------------------------------------------------------------------------
# Retrieval step
# ---------------------------------------------------------------------------

def retrieve(query: str, index: dict, k: int) -> list[dict]:
    return search.search(query, index, top_n=k)


# ---------------------------------------------------------------------------
# Answer composition
# ---------------------------------------------------------------------------

def compose_answer_mock(query: str, retrieved: list[dict]) -> dict:
    """Deterministic answer composition: concatenate summaries of retrieved
    articles and cite them as wikilinks. Used for CI and offline testing."""
    cited_ids = [r["id"] for r in retrieved[:3]]
    lines = []
    if retrieved:
        lines.append(f"Based on the wiki, relevant material for \"{query}\":")
        for r in retrieved[:3]:
            s = r.get("summary") or ""
            lines.append(f"- [[{r['id']}]] — {s}")
    answer = "\n".join(lines) if lines else "No relevant articles found."
    return {"answer": answer, "citations": cited_ids, "backend": "mock"}


def compose_answer_anthropic(
    query: str,
    retrieved: list[dict],
    model: str = "claude-haiku-4-5",
    max_tokens: int = 800,
) -> dict:
    import anthropic  # type: ignore

    client = anthropic.Anthropic()
    # Assemble a compact context from retrieved articles
    context_chunks = []
    for r in retrieved[:5]:
        title, body = load_article(r["id"])
        # Truncate body to ~2k chars to keep prompt small
        snippet = body.strip()[:2000]
        context_chunks.append(
            f"### [[{r['id']}]] — {title}\n{r.get('summary', '')}\n\n{snippet}\n"
        )
    context = "\n\n---\n\n".join(context_chunks)

    prompt = (
        "You are answering a question using ONLY the provided wiki articles. "
        "Cite articles inline using [[doc-id]] wikilink syntax. Keep the "
        "answer concise (3-6 sentences). If the articles do not contain "
        "enough information, say so explicitly.\n\n"
        f"# Wiki articles\n\n{context}\n\n# Question\n\n{query}\n\n# Answer"
    )
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = "".join(
        block.text for block in message.content if getattr(block, "type", "") == "text"
    )
    citations = list(dict.fromkeys(re.findall(r"\[\[([^\]]+)\]\]", answer)))
    return {"answer": answer, "citations": citations, "backend": model}


# ---------------------------------------------------------------------------
# Judging
# ---------------------------------------------------------------------------

def judge_mock(q: dict, composed: dict, retrieved: list[dict]) -> dict:
    """Heuristic judge used in CI/offline mode.

    - correctness      : token-overlap F1 between composed answer and the
                         expected_answer_sketch (proxy for semantic match).
    - citation_accuracy: Jaccard similarity between normalized composed
                         citations and expected_citations.
    - groundedness     : fraction of content-word tokens in the answer
                         that appear in at least one retrieved article.
    All scores are in [0, 1]; Likert-style 1-5 mapping is also returned.
    """
    sketch = q.get("expected_answer_sketch") or ""
    ans = composed.get("answer") or ""

    ans_tokens = tokens(ans)
    sketch_tokens = tokens(sketch)

    if not ans_tokens or not sketch_tokens:
        correctness = 0.0
    else:
        overlap = ans_tokens & sketch_tokens
        precision = len(overlap) / len(ans_tokens)
        recall = len(overlap) / len(sketch_tokens)
        correctness = (
            (2 * precision * recall) / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )

    expected_ids = {citation_to_doc_id(c) for c in q.get("expected_citations", [])}
    composed_ids = {citation_to_doc_id(c) for c in composed.get("citations", [])}
    if not expected_ids and not composed_ids:
        citation_accuracy = 1.0
    elif not expected_ids or not composed_ids:
        citation_accuracy = 0.0
    else:
        inter = expected_ids & composed_ids
        union = expected_ids | composed_ids
        citation_accuracy = len(inter) / len(union)

    # Groundedness: does the answer use vocabulary from the retrieved corpus?
    corpus_tokens: set[str] = set()
    for r in retrieved:
        _, body = load_article(r["id"])
        corpus_tokens |= tokens(body)
        corpus_tokens |= tokens(r.get("summary", ""))
    if ans_tokens and corpus_tokens:
        grounded_words = ans_tokens & corpus_tokens
        groundedness = len(grounded_words) / len(ans_tokens)
    else:
        groundedness = 0.0

    # Likert 1-5 bands
    def to_likert(x: float) -> int:
        return max(1, min(5, int(round(1 + 4 * x))))

    return {
        "correctness": round(correctness, 4),
        "citation_accuracy": round(citation_accuracy, 4),
        "groundedness": round(groundedness, 4),
        "correctness_likert": to_likert(correctness),
        "citation_likert": to_likert(citation_accuracy),
        "groundedness_likert": to_likert(groundedness),
        "judge_backend": "mock",
    }


JUDGE_PROMPT_TEMPLATE = """You are an impartial evaluator of an AI's answer to a
factual question. Score the answer on three 1-5 dimensions:

 - correctness        — how factually accurate is the answer relative to the
                        expected answer sketch? 5 = fully correct, 1 = wrong.
 - citation_accuracy  — how well do the citations match the expected ones? 5 =
                        all expected citations present, no fabrications.
 - groundedness       — are the claims in the answer supported by the retrieved
                        articles? 5 = fully grounded, 1 = unsupported.

Respond with ONLY a JSON object of the form:
{{"correctness": int, "citation_accuracy": int, "groundedness": int,
  "notes": "one sentence"}}

# Question
{q}

# Expected answer sketch
{sketch}

# Expected citations
{expected_citations}

# Retrieved article IDs (ground truth corpus used by the system)
{retrieved_ids}

# Model answer
{answer}

# Model-provided citations
{citations}
"""


def judge_anthropic(
    q: dict,
    composed: dict,
    retrieved: list[dict],
    model: str = "claude-haiku-4-5",
) -> dict:
    import anthropic  # type: ignore

    client = anthropic.Anthropic()
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        q=q["q"],
        sketch=q.get("expected_answer_sketch", ""),
        expected_citations=", ".join(q.get("expected_citations", [])),
        retrieved_ids=", ".join(r["id"] for r in retrieved),
        answer=composed.get("answer", ""),
        citations=", ".join(composed.get("citations", [])),
    )
    message = client.messages.create(
        model=model,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(
        b.text for b in message.content if getattr(b, "type", "") == "text"
    )
    # Try to parse a JSON blob from the response
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"Judge returned non-JSON response: {text[:200]}")
    data = json.loads(match.group(0))
    return {
        "correctness_likert": int(data.get("correctness", 0)),
        "citation_likert": int(data.get("citation_accuracy", 0)),
        "groundedness_likert": int(data.get("groundedness", 0)),
        "correctness": round((data.get("correctness", 0) - 1) / 4, 4),
        "citation_accuracy": round((data.get("citation_accuracy", 0) - 1) / 4, 4),
        "groundedness": round((data.get("groundedness", 0) - 1) / 4, 4),
        "notes": data.get("notes", ""),
        "judge_backend": model,
    }


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_generation(
    goldset: list[dict],
    top_k: int,
    mode: str,
    compose_model: str,
    judge_model: str,
) -> dict:
    index = search.get_index()
    per_q = []
    agg: dict[str, list[float]] = {}
    latencies_retrieve: list[float] = []
    latencies_compose: list[float] = []
    latencies_judge: list[float] = []

    for q in goldset:
        t0 = time.perf_counter()
        retrieved = retrieve(q["q"], index, top_k)
        t1 = time.perf_counter()
        if mode == "api":
            composed = compose_answer_anthropic(q["q"], retrieved, model=compose_model)
        else:
            composed = compose_answer_mock(q["q"], retrieved)
        t2 = time.perf_counter()
        if mode == "api":
            scored = judge_anthropic(q, composed, retrieved, model=judge_model)
        else:
            scored = judge_mock(q, composed, retrieved)
        t3 = time.perf_counter()

        latencies_retrieve.append((t1 - t0) * 1000.0)
        latencies_compose.append((t2 - t1) * 1000.0)
        latencies_judge.append((t3 - t2) * 1000.0)

        for k in ("correctness", "citation_accuracy", "groundedness"):
            agg.setdefault(k, []).append(scored.get(k, 0.0))

        per_q.append({
            "id": q.get("id"),
            "q": q["q"],
            "type": q.get("type"),
            "retrieved": [r["id"] for r in retrieved],
            "composed": composed,
            "scored": scored,
            "latency_ms": {
                "retrieve": round((t1 - t0) * 1000.0, 2),
                "compose": round((t2 - t1) * 1000.0, 2),
                "judge": round((t3 - t2) * 1000.0, 2),
            },
        })

    aggregated = {k: round(sum(v) / len(v), 4) for k, v in agg.items()}

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "compose_model": compose_model if mode == "api" else "mock",
        "judge_model": judge_model if mode == "api" else "mock",
        "goldset_size": len(goldset),
        "top_k": top_k,
        "index_size": index["num_docs"],
        "aggregated_scores": aggregated,
        "latency_ms": {
            "retrieve_avg": round(
                sum(latencies_retrieve) / len(latencies_retrieve), 2
            ) if latencies_retrieve else 0.0,
            "compose_avg": round(
                sum(latencies_compose) / len(latencies_compose), 2
            ) if latencies_compose else 0.0,
            "judge_avg": round(
                sum(latencies_judge) / len(latencies_judge), 2
            ) if latencies_judge else 0.0,
        },
        "per_question": per_q,
    }


def render_summary(report: dict) -> str:
    agg = report["aggregated_scores"]
    lines = [
        f"Generation eval — mode={report['mode']} — "
        f"{report['goldset_size']} questions over {report['index_size']} articles",
        f"  correctness         {agg.get('correctness', 0):.4f}",
        f"  citation_accuracy   {agg.get('citation_accuracy', 0):.4f}",
        f"  groundedness        {agg.get('groundedness', 0):.4f}",
    ]
    lat = report["latency_ms"]
    lines.append(
        f"  latency retrieve {lat['retrieve_avg']:.2f}ms | "
        f"compose {lat['compose_avg']:.2f}ms | "
        f"judge {lat['judge_avg']:.2f}ms"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--goldset",
        default=str(Path(__file__).resolve().parent / "goldset.jsonl"),
    )
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument(
        "--mode",
        choices=["mock", "api"],
        default="mock",
        help="mock = deterministic offline; api = Anthropic SDK (needs key)",
    )
    parser.add_argument("--compose-model", default="claude-haiku-4-5")
    parser.add_argument("--judge-model", default="claude-haiku-4-5")
    parser.add_argument("--output-dir", default=str(REPO_ROOT / "output"))
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.mode == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "--mode api requires ANTHROPIC_API_KEY env var. "
            "Re-run with --mode mock for offline scoring.",
            file=sys.stderr,
        )
        return 2

    goldset = load_goldset(Path(args.goldset))
    if not goldset:
        print("ERROR: gold set is empty.", file=sys.stderr)
        return 2

    report = evaluate_generation(
        goldset,
        top_k=args.top_k,
        mode=args.mode,
        compose_model=args.compose_model,
        judge_model=args.judge_model,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (output_dir / f"eval-generation-{ts}.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    (output_dir / "eval-generation-latest.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    if args.json:
        print(json.dumps(report, indent=2))
    elif not args.quiet:
        print(render_summary(report))
        print(f"\nReport written to: output/eval-generation-{ts}.json")

    return 0


if __name__ == "__main__":
    sys.exit(main())
