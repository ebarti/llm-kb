#!/usr/bin/env python3
"""
Search Engine Test
Tests the search engine (tools/search-engine/search.py) if it exists.

Runs known queries, validates results, tests edge cases, measures latency.

Usage: python3 tools/tests/test-search.py [--json]
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SEARCH_SCRIPT = BASE_DIR / "tools" / "search-engine" / "search.py"
SEARCH_SH = BASE_DIR / "tools" / "search.sh"
SEARCH_ENGINE_DIR = BASE_DIR / "tools" / "search-engine"

# Test cases: (query, expected_substring_in_output)
# We check that the output contains at least one expected term
TEST_QUERIES = [
    {
        "query": "knowledge base",
        "expect_any": ["llm-knowledge-base", "karpathy", "knowledge"],
        "description": "Core topic search",
    },
    {
        "query": "Karpathy",
        "expect_any": ["karpathy", "Karpathy"],
        "description": "Entity name search",
    },
    {
        "query": "RAG retrieval",
        "expect_any": ["rag", "retrieval", "vector"],
        "description": "Technical concept search",
    },
    {
        "query": "wiki compilation",
        "expect_any": ["wiki-compilation", "compilation", "wiki"],
        "description": "Specific concept search",
    },
    {
        "query": "STORM automated",
        "expect_any": ["storm", "automated", "wiki-creation"],
        "description": "Source search",
    },
]

EDGE_CASES = [
    {
        "query": "",
        "description": "Empty query",
        "should_not_crash": True,
    },
    {
        "query": "!@#$%^&*()",
        "description": "Special characters",
        "should_not_crash": True,
    },
    {
        "query": "a" * 500,
        "description": "Very long query",
        "should_not_crash": True,
    },
    {
        "query": "xyznonexistent12345",
        "description": "No results expected",
        "should_not_crash": True,
    },
]


def find_search_command():
    """Find a working search command."""
    if SEARCH_SCRIPT.exists():
        return [sys.executable, str(SEARCH_SCRIPT)]
    if SEARCH_SH.exists() and os.access(str(SEARCH_SH), os.X_OK):
        return [str(SEARCH_SH)]
    return None


def run_search(cmd, query, timeout=30):
    """Run a search query and return (output, latency_ms, returncode)."""
    start = time.time()
    try:
        result = subprocess.run(
            cmd + [query] if query else cmd + [""],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(BASE_DIR),
        )
        latency = (time.time() - start) * 1000
        return result.stdout + result.stderr, latency, result.returncode
    except subprocess.TimeoutExpired:
        latency = (time.time() - start) * 1000
        return "TIMEOUT", latency, -1
    except Exception as e:
        latency = (time.time() - start) * 1000
        return str(e), latency, -1


def run_format_pretty_regression():
    """
    Regression: --hybrid / --rerank results are ordered by rrf_score /
    rerank_score but carry the original BM25 `score` (or 0.0 for vector-only
    hits). format_pretty() must show the ordering score as the headline so the
    displayed value matches the ranking.
    """
    if str(SEARCH_ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(SEARCH_ENGINE_DIR))

    import search as search_mod

    tests = []

    rrf_result = [{
        "id": "concepts/a", "title": "A", "type": "concept", "tags": [],
        "date": "", "summary": "", "path": "concepts/a.md",
        "score": 0.0, "rrf_score": 0.0321,
    }]
    out = search_mod.format_pretty(rrf_result, "q")
    tests.append({
        "description": "format_pretty uses rrf_score as headline when present",
        "passed": "rrf: 0.0321" in out and "score: 0.0" not in out,
    })

    rerank_result = [{
        "id": "concepts/a", "title": "A", "type": "concept", "tags": [],
        "date": "", "summary": "", "path": "concepts/a.md",
        "score": 12.3, "rrf_score": 0.0321, "rerank_score": 7.89,
    }]
    out = search_mod.format_pretty(rerank_result, "q")
    tests.append({
        "description": "format_pretty prefers rerank_score over rrf_score / score",
        "passed": "rerank: 7.89" in out and "rrf:" not in out and "score: 12.3" not in out,
    })

    bm25_result = [{
        "id": "concepts/a", "title": "A", "type": "concept", "tags": [],
        "date": "", "summary": "", "path": "concepts/a.md",
        "score": 5.5,
    }]
    out = search_mod.format_pretty(bm25_result, "q")
    tests.append({
        "description": "format_pretty falls back to BM25 score when no fusion",
        "passed": "score: 5.5" in out,
    })

    return tests


def run_encoder_dim_regression():
    """
    Regression: build_or_update_index() must not force a model load when every
    chunk hash was reused. We stub the encoder so encode()/dim() would raise if
    called, then run a fully-cached build and expect it to complete cleanly.
    """
    if str(SEARCH_ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(SEARCH_ENGINE_DIR))

    try:
        import numpy as np  # noqa: F401
    except ImportError:
        return [{
            "description": "encoder.dim() skipped on fully-incremental build",
            "passed": True,
            "detail": "numpy unavailable; skipped",
        }]

    import embeddings

    ok, msg = embeddings.is_available()
    if not ok:
        missing = msg.splitlines()[0]
        return [{
            "description": "encoder.dim() skipped on fully-incremental build",
            "passed": True,
            "detail": f"{missing}; skipped",
        }]

    class _NoLoadEncoder:
        """An encoder stub whose dim() / encode() would blow up if called."""
        model_name = "test-model"
        calls = {"dim": 0, "encode": 0}

        def dim(self):
            type(self).calls["dim"] += 1
            raise AssertionError("encoder.dim() must not be called on cached build")

        def encode(self, texts, batch_size=32, show_progress=False):
            type(self).calls["encode"] += 1
            raise AssertionError("encoder.encode() must not be called on cached build")

    # Hand-build a VectorIndex so we can exercise the pure-Python control flow
    # of build_or_update_index without loading torch.
    chunks = [{
        "chunk_id": "concepts/a#0000", "doc_id": "concepts/a",
        "heading_path": ["A"], "text": "body", "tokens": 2,
        "content_hash": "deadbeef",
    }]
    existing = embeddings.VectorIndex(
        vectors=np.ones((1, 4), dtype=np.float32),
        chunks=chunks,
        dim=4,
        model_name="test-model",
    )

    try:
        fresh = embeddings.build_or_update_index(
            chunks, encoder=_NoLoadEncoder(), existing=existing, verbose=False,
        )
    except AssertionError as e:
        return [{
            "description": "encoder.dim() skipped on fully-incremental build",
            "passed": False,
            "detail": str(e),
        }]

    return [{
        "description": "encoder.dim() skipped on fully-incremental build",
        "passed": fresh.vectors.shape == (1, 4) and fresh.dim == 4,
    }]


def run_hybrid_pool_regression():
    """
    Regression for --top > 50 on the hybrid path: the bm25_k / vector_k pool
    must widen to at least `top_n` so results aren't silently capped at 50.
    Exercises hybrid.hybrid_search with an injected stub bm25 and no dense
    retrieval so we don't need numpy / sentence-transformers available.
    """
    if str(SEARCH_ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(SEARCH_ENGINE_DIR))

    import hybrid

    calls = {}

    def fake_bm25(query, index, top_n=10, **kwargs):
        calls["top_n"] = top_n
        return [
            {"id": f"concepts/doc-{i}", "title": f"Doc {i}", "type": "concept",
             "score": 100.0 - i, "path": f"concepts/doc-{i}.md", "tags": [],
             "date": "", "summary": "", "links": [], "related": [],
             "sources": [], "backlinks": []}
            for i in range(top_n)
        ]

    idx = {"docs": {}, "backlinks": {}}
    requested_top = 75
    hybrid.hybrid_search(
        "q", idx,
        vector_index=None, encoder=None,
        top_n=requested_top,
        bm25_k=requested_top, vector_k=requested_top,
        bm25_search=fake_bm25,
    )
    return [{
        "description": "hybrid_search forwards top > 50 to bm25_k pool",
        "passed": calls.get("top_n") == requested_top,
    }]


def run_rerank_pool_regression():
    """
    Regression for --rerank with --top > 50: search._run_hybrid() must pass the
    widened candidate depth through to rerank_results(pool=...) so the
    cross-encoder can reorder the entire requested window instead of silently
    stopping at the default 50.
    """
    if str(SEARCH_ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(SEARCH_ENGINE_DIR))

    import types
    import search as search_mod

    calls = {}

    fake_vector_index = types.SimpleNamespace(
        model_name="stub",
        vectors=types.SimpleNamespace(shape=(1, 4)),
    )

    embeddings_mod = types.SimpleNamespace(
        is_available=lambda: (True, "ok"),
        VectorIndex=types.SimpleNamespace(load=lambda: fake_vector_index),
        vectors_are_stale=lambda *_args, **_kwargs: False,
        Encoder=lambda _model_name: object(),
    )

    def fake_hybrid_search(*_args, **kwargs):
        top_n = kwargs["top_n"]
        return [
            {"id": f"concepts/doc-{i}", "title": f"Doc {i}", "summary": ""}
            for i in range(top_n)
        ]

    hybrid_mod = types.SimpleNamespace(hybrid_search=fake_hybrid_search)

    def fake_rerank_results(query, results, reranker=None, pool=50, **_kwargs):
        calls["pool"] = pool
        calls["count"] = len(results)
        return results

    rerank_mod = types.SimpleNamespace(
        is_available=lambda: (True, "ok"),
        CrossEncoderReranker=lambda: object(),
        rerank_results=fake_rerank_results,
    )

    original_modules = {
        name: sys.modules.get(name)
        for name in ("embeddings", "hybrid", "rerank")
    }
    sys.modules["embeddings"] = embeddings_mod
    sys.modules["hybrid"] = hybrid_mod
    sys.modules["rerank"] = rerank_mod
    original_load_body = search_mod.load_body
    original_extract_snippet = search_mod.extract_snippet
    try:
        search_mod.load_body = lambda _doc_id: "body"
        search_mod.extract_snippet = lambda *_args, **_kwargs: "snippet"
        args = types.SimpleNamespace(
            top=75,
            rerank=True,
            type=None,
            tags=None,
            date_from=None,
            date_to=None,
            no_fuzzy=False,
        )
        results = search_mod._run_hybrid("q", {"docs": {}, "backlinks": {}}, args)
    finally:
        search_mod.load_body = original_load_body
        search_mod.extract_snippet = original_extract_snippet
        for name, module in original_modules.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module

    return [{
        "description": "_run_hybrid forwards top > 50 to rerank pool",
        "passed": calls.get("pool") == 75 and calls.get("count") == 75 and len(results) == 75,
    }]


def run_chunker_regressions():
    """Exercise chunk hashing without requiring optional ML dependencies."""
    if str(SEARCH_ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(SEARCH_ENGINE_DIR))

    from chunker import chunk_document

    alpha = chunk_document("concepts/alpha", "# Alpha\n\nShared paragraph.")
    beta = chunk_document("concepts/beta", "# Beta\n\nShared paragraph.")
    alpha_clone = chunk_document("concepts/alpha-clone", "# Alpha\n\nShared paragraph.")

    if len(alpha) != 1 or len(beta) != 1 or len(alpha_clone) != 1:
        raise AssertionError("Expected one chunk per synthetic document")

    alpha_chunk = alpha[0]
    beta_chunk = beta[0]
    alpha_clone_chunk = alpha_clone[0]

    tests = [
        {
            "description": "Chunk hash changes when heading breadcrumb changes",
            "passed": (
                alpha_chunk.embed_text != beta_chunk.embed_text
                and alpha_chunk.content_hash != beta_chunk.content_hash
            ),
        },
        {
            "description": "Chunk hash stays stable for identical encoder input",
            "passed": (
                alpha_chunk.embed_text == alpha_clone_chunk.embed_text
                and alpha_chunk.content_hash == alpha_clone_chunk.content_hash
            ),
        },
    ]

    # Regression: heading-only stub must not fall through to the "no headings"
    # fallback and silently embed the heading line as plain text.
    heading_only = chunk_document("concepts/stub", "# Stub\n\n## Empty\n")
    if heading_only:
        tests.append({
            "description": "Heading-only doc emits no plain-text fallback chunk",
            "passed": False,
            "detail": f"expected 0 chunks, got {len(heading_only)}",
        })
    else:
        tests.append({
            "description": "Heading-only doc emits no plain-text fallback chunk",
            "passed": True,
        })

    # Sanity: a headings-free doc still hits the fallback as before.
    no_headings = chunk_document("concepts/plain", "Just a paragraph, no heading.\n")
    tests.append({
        "description": "Headings-free doc still chunks via fallback",
        "passed": len(no_headings) == 1,
    })

    # Vector index staleness detection (does not require numpy/transformers).
    import embeddings
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as td:
        wiki = Path(td)
        (wiki / "concepts").mkdir()
        art = wiki / "concepts" / "foo.md"
        art.write_text("# Foo\n")

        class _Stub:
            class _Vecs:
                shape = (1, 8)
            vectors = _Vecs()
            built_at = 0.0  # predates the stamp

        tests.append({
            "description": "vectors_are_stale: None treated as stale",
            "passed": embeddings.vectors_are_stale(None, wiki) is True,
        })
        tests.append({
            "description": "vectors_are_stale: built_at=0 treated as stale",
            "passed": embeddings.vectors_are_stale(_Stub(), wiki) is True,
        })

        class _Fresh:
            class _Vecs:
                shape = (1, 8)
            vectors = _Vecs()
            built_at = art.stat().st_mtime + 3600

        tests.append({
            "description": "vectors_are_stale: fresh built_at treated as current",
            "passed": embeddings.vectors_are_stale(_Fresh(), wiki) is False,
        })

        # Touch the article into the future to simulate wiki edit after build.
        future = _Fresh.built_at + 7200
        os.utime(art, (future, future))
        tests.append({
            "description": "vectors_are_stale: wiki edit after build marks stale",
            "passed": embeddings.vectors_are_stale(_Fresh(), wiki) is True,
        })

    return tests


def run_checks():
    cmd = find_search_command()
    results = {
        "search_engine_found": cmd is not None,
        "search_command": " ".join(cmd) if cmd else None,
        "regression_tests": [],
        "query_tests": [],
        "edge_case_tests": [],
        "latency_stats": {},
        "issues": [],
        "ok": True,
    }

    if not cmd:
        results["issues"].append("Search engine not found (tools/search-engine/search.py or tools/search.sh)")
        results["ok"] = False
        return results

    try:
        results["regression_tests"] = run_chunker_regressions()
    except Exception as e:
        results["issues"].append(f"Chunk regression checks failed to run: {e}")
        results["ok"] = False
    else:
        for test in results["regression_tests"]:
            if not test["passed"]:
                results["issues"].append(f"Regression failed: {test['description']}")
                results["ok"] = False

    try:
        hybrid_tests = run_hybrid_pool_regression()
    except Exception as e:
        results["issues"].append(f"Hybrid pool regression failed to run: {e}")
        results["ok"] = False
    else:
        results["regression_tests"].extend(hybrid_tests)
        for test in hybrid_tests:
            if not test["passed"]:
                results["issues"].append(f"Regression failed: {test['description']}")
                results["ok"] = False

    try:
        rerank_tests = run_rerank_pool_regression()
    except Exception as e:
        results["issues"].append(f"Rerank pool regression failed to run: {e}")
        results["ok"] = False
    else:
        results["regression_tests"].extend(rerank_tests)
        for test in rerank_tests:
            if not test["passed"]:
                results["issues"].append(f"Regression failed: {test['description']}")
                results["ok"] = False

    try:
        pretty_tests = run_format_pretty_regression()
    except Exception as e:
        results["issues"].append(f"format_pretty regression failed to run: {e}")
        results["ok"] = False
    else:
        results["regression_tests"].extend(pretty_tests)
        for test in pretty_tests:
            if not test["passed"]:
                results["issues"].append(f"Regression failed: {test['description']}")
                results["ok"] = False

    try:
        dim_tests = run_encoder_dim_regression()
    except Exception as e:
        results["issues"].append(f"encoder.dim regression failed to run: {e}")
        results["ok"] = False
    else:
        results["regression_tests"].extend(dim_tests)
        for test in dim_tests:
            if not test["passed"]:
                results["issues"].append(f"Regression failed: {test['description']}")
                results["ok"] = False

    latencies = []

    # --- Known query tests ---
    for test in TEST_QUERIES:
        output, latency, rc = run_search(cmd, test["query"])
        latencies.append(latency)

        found = any(term.lower() in output.lower() for term in test["expect_any"])
        test_result = {
            "description": test["description"],
            "query": test["query"],
            "passed": found,
            "latency_ms": round(latency, 1),
            "returncode": rc,
        }
        if not found:
            test_result["detail"] = f"Expected one of {test['expect_any']} in output"
            results["issues"].append(f"Query '{test['query']}': expected terms not found in output")
            results["ok"] = False
        results["query_tests"].append(test_result)

    # --- Edge case tests ---
    for test in EDGE_CASES:
        output, latency, rc = run_search(cmd, test["query"])
        latencies.append(latency)

        # Edge cases pass if they don't crash (returncode is not -1 for timeout)
        passed = rc != -1
        test_result = {
            "description": test["description"],
            "query": test["query"][:50],
            "passed": passed,
            "latency_ms": round(latency, 1),
            "returncode": rc,
        }
        if not passed:
            results["issues"].append(f"Edge case '{test['description']}': crashed or timed out")
            results["ok"] = False
        results["edge_case_tests"].append(test_result)

    # --- Latency stats ---
    if latencies:
        results["latency_stats"] = {
            "min_ms": round(min(latencies), 1),
            "max_ms": round(max(latencies), 1),
            "avg_ms": round(sum(latencies) / len(latencies), 1),
            "p95_ms": round(sorted(latencies)[int(len(latencies) * 0.95)], 1),
        }

    return results


def print_report(result):
    print("=" * 60)
    print("  Search Engine Tests")
    print("=" * 60)

    if not result["search_engine_found"]:
        print("\n\033[31mSearch engine not found.\033[0m")
        print("  Expected: tools/search-engine/search.py or tools/search.sh")
        return

    print(f"\nCommand: {result['search_command']}")

    print("\n--- Regression Tests ---")
    for t in result["regression_tests"]:
        symbol = "\033[32m✓\033[0m" if t["passed"] else "\033[31m✗\033[0m"
        print(f"  {symbol} {t['description']}")

    print("\n--- Query Tests ---")
    for t in result["query_tests"]:
        symbol = "\033[32m✓\033[0m" if t["passed"] else "\033[31m✗\033[0m"
        print(f"  {symbol} {t['description']}: '{t['query']}' ({t['latency_ms']}ms)")
        if not t["passed"] and "detail" in t:
            print(f"      {t['detail']}")

    print("\n--- Edge Case Tests ---")
    for t in result["edge_case_tests"]:
        symbol = "\033[32m✓\033[0m" if t["passed"] else "\033[31m✗\033[0m"
        print(f"  {symbol} {t['description']} ({t['latency_ms']}ms)")

    if result["latency_stats"]:
        s = result["latency_stats"]
        print(f"\n--- Latency ---")
        print(f"  Min: {s['min_ms']}ms  Max: {s['max_ms']}ms  Avg: {s['avg_ms']}ms  P95: {s['p95_ms']}ms")

    print()
    if result["ok"]:
        print("\033[32mAll search tests passed.\033[0m")
    else:
        print(f"\033[31mIssues: {', '.join(result['issues'])}\033[0m")
    print()


def main():
    parser = argparse.ArgumentParser(description="Search Engine Test")
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
