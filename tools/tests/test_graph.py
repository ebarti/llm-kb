#!/usr/bin/env python3
"""Tests for the typed graph store (tools/graph).

Covers:
    - GraphStore schema + upserts (nodes & edges)
    - Predicate vocabulary enforcement
    - Read-only query guard
    - Heuristic predicate detection from surrounding text
    - End-to-end extraction against a synthesized wiki fixture
    - Frontmatter override takes precedence over heuristics

Run: python3 tools/tests/test_graph.py [--json]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import sqlite3
import tempfile
import traceback
import unittest
from pathlib import Path

# Make `graph` importable when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from graph.store import GraphStore, PREDICATES, DEFAULT_PREDICATE  # noqa: E402
from graph.extract import (  # noqa: E402
    detect_predicate,
    extract_nodes_and_edges,
    fingerprint,
    PREDICATE_PATTERNS,
)


# ---------------------------------------------------------------------- #
#  Store tests
# ---------------------------------------------------------------------- #
class StoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.mkdtemp(prefix="graph-test-")
        self.db = str(Path(self.tmp) / ".graph.db")
        self.store = GraphStore(self.db)
        self.store.init_schema()

    def tearDown(self) -> None:
        self.store.close()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_schema_is_idempotent(self):
        # Calling init_schema twice must not raise.
        self.store.init_schema()
        self.store.init_schema()

    def test_upsert_node_and_fetch(self):
        self.store.upsert_node(
            "concepts/rag",
            type="concept",
            title="RAG",
            path="/fake/path",
            summary="Retrieval-augmented generation",
        )
        row = self.store.get_node("concepts/rag")
        self.assertIsNotNone(row)
        self.assertEqual(row["type"], "concept")
        self.assertEqual(row["title"], "RAG")
        self.assertEqual(row["summary"], "Retrieval-augmented generation")

    def test_upsert_node_overwrites(self):
        self.store.upsert_node("a", type="concept", title="A", path="", summary="")
        self.store.upsert_node("a", type="entity", title="A2", path="", summary="")
        row = self.store.get_node("a")
        self.assertEqual(row["type"], "entity")
        self.assertEqual(row["title"], "A2")

    def test_upsert_edge_valid(self):
        self.store.upsert_node("a", type="concept")
        self.store.upsert_node("b", type="concept")
        self.store.upsert_edge("a", "b", "cites", provenance="frontmatter:sources")
        rows = self.store.outgoing("a")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["predicate"], "cites")
        self.assertEqual(rows[0]["provenance"], "frontmatter:sources")

    def test_upsert_edge_rejects_unknown_predicate(self):
        self.store.upsert_node("a", type="concept")
        self.store.upsert_node("b", type="concept")
        with self.assertRaises(ValueError):
            self.store.upsert_edge("a", "b", "notapredicate")

    def test_upsert_edge_requires_nodes(self):
        with self.assertRaises(ValueError):
            self.store.upsert_edge("", "b", "cites")
        with self.assertRaises(ValueError):
            self.store.upsert_edge("a", "", "cites")

    def test_edge_pk_dedup_but_provenance_wins(self):
        self.store.upsert_edge("a", "b", "cites", provenance="heuristic:cites")
        self.store.upsert_edge("a", "b", "cites", provenance="frontmatter:sources")
        # Still a single row, but with the updated provenance.
        rows = list(self.store.conn.execute("SELECT * FROM edges"))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["provenance"], "frontmatter:sources")

    def test_multiple_predicates_between_same_nodes(self):
        self.store.upsert_edge("a", "b", "cites")
        self.store.upsert_edge("a", "b", "extends")
        self.assertEqual(self.store.count("edges"), 2)

    def test_predicate_counts(self):
        self.store.upsert_edge("a", "b", "cites")
        self.store.upsert_edge("a", "c", "cites")
        self.store.upsert_edge("a", "d", "mentions")
        counts = dict(self.store.predicate_counts())
        self.assertEqual(counts["cites"], 2)
        self.assertEqual(counts["mentions"], 1)

    def test_cites_of_and_mentioned_by(self):
        self.store.upsert_edge("a", "b", "cites")
        self.store.upsert_edge("a", "c", "mentions")
        self.store.upsert_edge("d", "b", "mentions")
        self.assertEqual([r["dst"] for r in self.store.cites_of("a")], ["b"])
        mentioned = [r["src"] for r in self.store.mentioned_by("b")]
        self.assertIn("d", mentioned)
        self.assertNotIn("a", mentioned)

    def test_contradictions(self):
        self.store.upsert_edge("a", "b", "contradicts")
        self.store.upsert_edge("a", "c", "refutes")
        self.store.upsert_edge("a", "d", "mentions")
        rows = self.store.contradictions()
        preds = {r["predicate"] for r in rows}
        self.assertEqual(preds, {"contradicts", "refutes"})
        self.assertEqual(len(rows), 2)

    def test_query_rejects_writes(self):
        self.store.upsert_edge("a", "b", "cites")
        with self.assertRaises(ValueError):
            list(self.store.query("DELETE FROM edges"))
        with self.assertRaises(ValueError):
            list(self.store.query("UPDATE edges SET predicate='x'"))
        with self.assertRaises(ValueError):
            list(self.store.query("DROP TABLE edges"))
        # Read-only query should work.
        rows = list(self.store.query("SELECT COUNT(*) FROM edges"))
        self.assertEqual(rows[0][0], 1)

    def test_predicates_exposed(self):
        # Sanity: the constant list has every predicate in the issue spec.
        expected = {
            "cites", "mentions", "compares", "implements", "extends",
            "contradicts", "refutes", "part_of", "instance_of",
        }
        self.assertEqual(set(PREDICATES), expected)
        self.assertEqual(DEFAULT_PREDICATE, "mentions")


# ---------------------------------------------------------------------- #
#  Heuristic tests
# ---------------------------------------------------------------------- #
class HeuristicTests(unittest.TestCase):
    def test_cites(self):
        self.assertEqual(detect_predicate("as shown in ")[0], "cites")
        self.assertEqual(detect_predicate("according to ")[0], "cites")
        self.assertEqual(detect_predicate("The paper cites ")[0], "cites")
        self.assertEqual(detect_predicate("see also ")[0], "cites")

    def test_contradicts_and_refutes(self):
        self.assertEqual(detect_predicate("this contradicts ")[0], "contradicts")
        self.assertEqual(detect_predicate("which disagrees with ")[0], "contradicts")
        self.assertEqual(detect_predicate("the work refutes ")[0], "refutes")
        self.assertEqual(detect_predicate("that debunks ")[0], "refutes")

    def test_extends_and_implements(self):
        self.assertEqual(detect_predicate("Our method extends ")[0], "extends")
        self.assertEqual(detect_predicate("This approach builds on ")[0], "extends")
        self.assertEqual(detect_predicate("We implement ")[0], "implements")
        self.assertEqual(detect_predicate("which realizes ")[0], "implements")

    def test_compares(self):
        self.assertEqual(detect_predicate("When compared with ")[0], "compares")
        self.assertEqual(detect_predicate("X versus ")[0], "compares")

    def test_part_of_and_instance_of(self):
        self.assertEqual(detect_predicate("which is part of ")[0], "part_of")
        self.assertEqual(detect_predicate("is a component of ")[0], "part_of")
        self.assertEqual(detect_predicate("which is an example of ")[0], "instance_of")

    def test_default_is_mentions(self):
        pred, provenance = detect_predicate("Hello world, consider ")
        self.assertEqual(pred, "mentions")
        self.assertEqual(provenance, "default")

    def test_window_limit(self):
        # Word far outside the 50-char window should not fire the heuristic.
        padding = " " * 200
        pred, _ = detect_predicate("contradicts" + padding)
        self.assertEqual(pred, "mentions")

    def test_patterns_compile(self):
        # Every pattern must be a compiled regex and reference a valid predicate.
        for pred, pat in PREDICATE_PATTERNS:
            self.assertIn(pred, PREDICATES)
            self.assertTrue(hasattr(pat, "search"))


# ---------------------------------------------------------------------- #
#  End-to-end extraction tests (against a synthesized wiki)
# ---------------------------------------------------------------------- #
FIXTURE = {
    "wiki/concepts/rag.md": """---
title: "RAG"
type: concept
summary: "Retrieval-augmented generation"
last_compiled: 2026-04-01
related: ["[[concepts/retrieval]]"]
---

## Overview

RAG builds on [[concepts/retrieval]] and extends [[concepts/language-models]].
It contradicts [[concepts/parametric-only-models]].
See also [[concepts/vector-search]] for the underlying retrieval step.

RAG is a component of [[concepts/agentic-systems]] — you will see that
pipelines refer to [[entities/langchain]] quite often.
""",
    "wiki/concepts/retrieval.md": """---
title: "Retrieval"
type: concept
summary: "Fetching relevant docs"
last_compiled: 2026-04-01
---

## Overview

Retrieval is an instance of [[concepts/information-access]].
""",
    "wiki/concepts/language-models.md": """---
title: "Language Models"
type: concept
summary: "LMs"
last_compiled: 2026-04-01
---

## Overview
LMs.
""",
    "wiki/concepts/parametric-only-models.md": """---
title: "Parametric-only Models"
type: concept
summary: "stuff"
last_compiled: 2026-04-01
---

## Overview
Stuff.
""",
    "wiki/concepts/vector-search.md": """---
title: "Vector Search"
type: concept
summary: "Embeddings"
last_compiled: 2026-04-01
---

## Overview
Vecs.
""",
    "wiki/concepts/agentic-systems.md": """---
title: "Agentic Systems"
type: concept
summary: "Agents"
last_compiled: 2026-04-01
---

## Overview
Agents.
""",
    "wiki/concepts/information-access.md": """---
title: "Information Access"
type: concept
summary: "Umbrella"
last_compiled: 2026-04-01
---

## Overview
Umbrella.
""",
    "wiki/entities/langchain.md": """---
title: "LangChain"
type: entity
entity_type: tool
summary: "Framework"
last_compiled: 2026-04-01
---

## Overview
Tool.
""",
    "wiki/sources/awesome-rag-paper.md": """---
title: "Source: Awesome RAG Paper"
type: source-summary
source: "[[raw/awesome-rag-paper]]"
sources: ["[[concepts/rag]]", "[[concepts/retrieval]]"]
last_compiled: 2026-04-01
summary: "A paper"
---

## Key Points

- This paper cites [[concepts/retrieval]] and extends [[concepts/rag]].
""",
    "wiki/comparisons/rag-vs-long-context.md": """---
title: "RAG vs Long Context"
type: comparison
subjects: ["[[concepts/rag]]", "[[concepts/language-models]]"]
last_compiled: 2026-04-01
summary: "Comparison"
---

## Overview
Compare them.
""",
    "wiki/concepts/override-source.md": """---
title: "Override Source"
type: concept
summary: "has explicit edges"
last_compiled: 2026-04-01
edges:
  - {to: "concepts/rag", predicate: "extends"}
  - {to: "concepts/retrieval", predicate: "implements"}
---

## Overview
We also talk about [[concepts/rag]] in the body, but the frontmatter override wins.
""",
    "raw/awesome-rag-paper.md": """---
title: "Awesome RAG Paper"
source: "https://example.com/rag"
summary: "raw paper"
---

Body of the raw paper.
""",
}


def _write_fixture(root: Path) -> None:
    for rel, content in FIXTURE.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


class ExtractionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="graph-fixture-"))
        _write_fixture(self.tmp)
        self.wiki = self.tmp / "wiki"
        self.raw = self.tmp / "raw"
        self.nodes, self.edges = extract_nodes_and_edges(self.wiki, raw_dir=self.raw)
        self.edge_map: dict[tuple[str, str], set[str]] = {}
        for e in self.edges:
            self.edge_map.setdefault((e.src, e.dst), set()).add(e.predicate)
        self.provenance: dict[tuple[str, str, str], str] = {
            (e.src, e.dst, e.predicate): e.provenance for e in self.edges
        }

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_nodes_present(self):
        ids = {n.id for n in self.nodes}
        self.assertIn("concepts/rag", ids)
        self.assertIn("entities/langchain", ids)
        self.assertIn("sources/awesome-rag-paper", ids)
        self.assertIn("comparisons/rag-vs-long-context", ids)
        self.assertIn("raw/awesome-rag-paper", ids)

    def test_heuristic_extends(self):
        # "RAG builds on [[concepts/retrieval]] and extends [[concepts/language-models]]"
        self.assertIn(
            "extends",
            self.edge_map.get(("concepts/rag", "concepts/retrieval"), set()),
        )
        self.assertIn(
            "extends",
            self.edge_map.get(("concepts/rag", "concepts/language-models"), set()),
        )

    def test_heuristic_contradicts(self):
        self.assertIn(
            "contradicts",
            self.edge_map.get(
                ("concepts/rag", "concepts/parametric-only-models"), set()
            ),
        )

    def test_heuristic_cites_see_also(self):
        self.assertIn(
            "cites",
            self.edge_map.get(("concepts/rag", "concepts/vector-search"), set()),
        )

    def test_heuristic_part_of(self):
        self.assertIn(
            "part_of",
            self.edge_map.get(("concepts/rag", "concepts/agentic-systems"), set()),
        )

    def test_default_mentions(self):
        # "pipelines refer to [[entities/langchain]] quite often." — no pattern fires.
        self.assertIn(
            "mentions",
            self.edge_map.get(("concepts/rag", "entities/langchain"), set()),
        )

    def test_instance_of(self):
        # "Retrieval is an instance of [[concepts/information-access]]"
        self.assertIn(
            "instance_of",
            self.edge_map.get(
                ("concepts/retrieval", "concepts/information-access"), set()
            ),
        )

    def test_frontmatter_sources_maps_to_cites(self):
        # Source article lists sources: [[concepts/rag]], [[concepts/retrieval]]
        self.assertIn(
            "cites",
            self.edge_map.get(("sources/awesome-rag-paper", "concepts/rag"), set()),
        )
        self.assertIn(
            "cites",
            self.edge_map.get(
                ("sources/awesome-rag-paper", "concepts/retrieval"), set()
            ),
        )

    def test_frontmatter_source_scalar_maps_to_cites(self):
        # The source: field points at raw/awesome-rag-paper.
        self.assertIn(
            "cites",
            self.edge_map.get(
                ("sources/awesome-rag-paper", "raw/awesome-rag-paper"), set()
            ),
        )

    def test_frontmatter_subjects_maps_to_compares(self):
        self.assertIn(
            "compares",
            self.edge_map.get(
                ("comparisons/rag-vs-long-context", "concepts/rag"), set()
            ),
        )
        self.assertIn(
            "compares",
            self.edge_map.get(
                ("comparisons/rag-vs-long-context", "concepts/language-models"), set()
            ),
        )

    def test_manual_override_wins(self):
        # override-source declares an explicit 'extends' override for concepts/rag.
        preds = self.edge_map.get(
            ("concepts/override-source", "concepts/rag"), set()
        )
        self.assertIn("extends", preds)
        # The heuristic-default `mentions` path must not also be emitted
        # once the override covers that (target, predicate) pair.
        # (Behavior documented in extract.py: override suppresses both
        # structural and heuristic entries for the same (to, predicate).)
        key = ("concepts/override-source", "concepts/rag", "extends")
        self.assertEqual(self.provenance[key], "frontmatter:manual")

    def test_fingerprint_stable(self):
        nodes, edges = extract_nodes_and_edges(self.wiki, raw_dir=self.raw)
        f1 = fingerprint(nodes, edges)
        f2 = fingerprint(self.nodes, self.edges)
        self.assertEqual(f1, f2)


# ---------------------------------------------------------------------- #
#  Store + extract integration
# ---------------------------------------------------------------------- #
class IntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="graph-int-"))
        _write_fixture(self.tmp)
        self.db = str(self.tmp / ".graph.db")
        nodes, edges = extract_nodes_and_edges(
            self.tmp / "wiki", raw_dir=self.tmp / "raw"
        )
        self.store = GraphStore(self.db)
        self.store.init_schema()
        for n in nodes:
            self.store.upsert_node(
                n.id, type=n.type, title=n.title, path=n.path, summary=n.summary
            )
        for e in edges:
            self.store.upsert_edge(e.src, e.dst, e.predicate, provenance=e.provenance)
        self.store.commit()

    def tearDown(self) -> None:
        self.store.close()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_cites_count_nonzero(self):
        # Matches the acceptance criterion in the issue.
        row = self.store.conn.execute(
            "SELECT COUNT(*) AS n FROM edges WHERE predicate='cites'"
        ).fetchone()
        self.assertGreater(row["n"], 0)

    def test_cli_helpers_work_via_store(self):
        rows = self.store.cites_of("sources/awesome-rag-paper")
        dsts = {r["dst"] for r in rows}
        # Should include the source: scalar target and sources: list targets.
        self.assertIn("raw/awesome-rag-paper", dsts)
        self.assertIn("concepts/rag", dsts)
        self.assertIn("concepts/retrieval", dsts)


# ---------------------------------------------------------------------- #
#  Runner
# ---------------------------------------------------------------------- #
def _collect_results(result: unittest.TestResult) -> dict:
    return {
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "ok": result.wasSuccessful(),
        "failure_details": [f"{t}: {msg}" for t, msg in result.failures],
        "error_details": [f"{t}: {msg}" for t, msg in result.errors],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Typed graph store test suite")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    loader = unittest.TestLoader()
    suite = unittest.TestSuite([
        loader.loadTestsFromTestCase(StoreTests),
        loader.loadTestsFromTestCase(HeuristicTests),
        loader.loadTestsFromTestCase(ExtractionTests),
        loader.loadTestsFromTestCase(IntegrationTests),
    ])

    if args.json:
        runner = unittest.TextTestRunner(stream=open("/dev/null", "w"), verbosity=0)
    else:
        runner = unittest.TextTestRunner(verbosity=2)

    try:
        result = runner.run(suite)
    except Exception:
        traceback.print_exc()
        return 2

    summary = _collect_results(result)
    if args.json:
        print(json.dumps(summary, indent=2))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
