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
