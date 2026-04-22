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
import os
import subprocess
import shutil
import sys
import sqlite3
import tempfile
import traceback
import unittest
from unittest import mock
from pathlib import Path

# Make `graph` importable when run directly.
TOOLS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = TOOLS_DIR.parent
GQ = TOOLS_DIR / "graph" / "gq"

sys.path.insert(0, str(TOOLS_DIR))

from graph.store import GraphStore, PREDICATES, DEFAULT_PREDICATE  # noqa: E402
from graph.extract import (  # noqa: E402
    detect_predicate,
    extract_nodes_and_edges,
    fingerprint,
    PREDICATE_PATTERNS,
    WINDOW_CHARS,
)
import graph.extract as graph_extract  # noqa: E402


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

    def test_upsert_edge_requires_non_empty_endpoints(self):
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
        with self.assertRaises(ValueError):
            list(self.store.query("PRAGMA user_version = 7"))
        # Read-only query should work.
        rows = list(self.store.query("SELECT COUNT(*) FROM edges"))
        self.assertEqual(rows[0][0], 1)

    def test_query_rejects_newline_bypass(self):
        """Mutating keywords smuggled behind a leading SELECT/WITH via
        newlines, commas, or SQL comments must still be rejected."""
        self.store.upsert_edge("a", "b", "cites")
        # Newline-separated statement inside a WITH — the old guard
        # required literal spaces around keywords and missed this.
        with self.assertRaises(ValueError):
            list(self.store.query(
                "WITH x AS (SELECT 1)\nDELETE FROM edges"
            ))
        with self.assertRaises(ValueError):
            list(self.store.query(
                "WITH x AS (SELECT 1)\nINSERT INTO nodes (id) VALUES ('z')"
            ))
        # Block comment hiding a mutating verb.
        with self.assertRaises(ValueError):
            list(self.store.query(
                "SELECT 1; /* trailing */ DROP TABLE edges"
            ))
        # Line comment before a verb.
        with self.assertRaises(ValueError):
            list(self.store.query(
                "SELECT 1\n-- comment\nUPDATE edges SET predicate='x'"
            ))
        # After all those, the underlying data must still be intact.
        rows = list(self.store.query("SELECT COUNT(*) FROM edges"))
        self.assertEqual(rows[0][0], 1)

    def test_query_allows_string_literals_and_scalar_functions(self):
        rows = list(self.store.query(
            "SELECT 'delete' AS word, replace('table', 't', 'T') AS renamed"
        ))
        self.assertEqual(rows[0]["word"], "delete")
        self.assertEqual(rows[0]["renamed"], "Table")

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
        # Regression: the `per\s+` branch used to end in \s+ and so the
        # outer \b[^.?!]*$ could never anchor, silently dropping `per`
        # triggers. `per(?=\s)` with a lookahead fixes that.
        self.assertEqual(detect_predicate("per ")[0], "cites")
        self.assertEqual(detect_predicate("as per ")[0], "cites")
        # Must not fire when `per` is part of a longer word.
        self.assertEqual(detect_predicate("experiment performed with ")[0], "mentions")

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


def _run_gq(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(GQ), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )


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
        self.assertEqual(
            self.provenance[("sources/awesome-rag-paper", "concepts/rag", "cites")],
            "frontmatter:sources",
        )

    def test_frontmatter_source_scalar_maps_to_cites(self):
        # The source: field points at raw/awesome-rag-paper.
        self.assertIn(
            "cites",
            self.edge_map.get(
                ("sources/awesome-rag-paper", "raw/awesome-rag-paper"), set()
            ),
        )
        self.assertEqual(
            self.provenance[
                ("sources/awesome-rag-paper", "raw/awesome-rag-paper", "cites")
            ],
            "frontmatter:source",
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

    def test_edges_override_validation_uses_original_frontmatter_key(self):
        fm_block = """
edges:
  - {to: "concepts/rag", predicate: "still_nope"}
"""
        with self.assertRaisesRegex(ValueError, r"source=frontmatter:edges"):
            graph_extract._extract_edges_override(fm_block)

    def test_fingerprint_stable(self):
        nodes, edges = extract_nodes_and_edges(self.wiki, raw_dir=self.raw)
        f1 = fingerprint(nodes, edges)
        f2 = fingerprint(self.nodes, self.edges)
        self.assertEqual(f1, f2)

    def test_extraction_passes_only_window_sized_left_context(self):
        tmp = Path(tempfile.mkdtemp(prefix="graph-window-"))
        try:
            wiki = tmp / "wiki"
            raw = tmp / "raw"
            (wiki / "concepts").mkdir(parents=True)
            raw.mkdir()

            (wiki / "concepts" / "target.md").write_text(
                """---
title: "Target"
type: concept
summary: "target"
last_compiled: 2026-04-21
---
""",
                encoding="utf-8",
            )
            (wiki / "concepts" / "window.md").write_text(
                f"""---
title: "Window"
type: concept
summary: "window"
last_compiled: 2026-04-21
---

{"x" * (WINDOW_CHARS + 25)}[[concepts/target]]
""",
                encoding="utf-8",
            )

            seen: list[str] = []

            def _fake_detect_predicate(left_context: str):
                seen.append(left_context)
                return ("mentions", "default")

            with mock.patch(
                "graph.extract.detect_predicate",
                side_effect=_fake_detect_predicate,
            ):
                graph_extract.extract_nodes_and_edges(wiki, raw_dir=raw)

            self.assertEqual(len(seen), 1)
            self.assertEqual(len(seen[0]), WINDOW_CHARS)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


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


class CliBuildTests(unittest.TestCase):
    def test_build_preserves_last_good_db_on_failure(self):
        tmp = Path(tempfile.mkdtemp(prefix="graph-cli-"))
        try:
            wiki = tmp / "wiki"
            raw = tmp / "raw"
            (wiki / "concepts").mkdir(parents=True)
            raw.mkdir()

            good_article = wiki / "concepts" / "a.md"
            peer_article = wiki / "concepts" / "b.md"
            good_article.write_text(
                """---
title: "A"
type: concept
summary: "a"
last_compiled: 2026-04-20
---

[[concepts/b]]
""",
                encoding="utf-8",
            )
            peer_article.write_text(
                """---
title: "B"
type: concept
summary: "b"
last_compiled: 2026-04-20
---
""",
                encoding="utf-8",
            )

            db = tmp / ".graph.db"
            first_build = _run_gq(
                "--db", str(db), "build", "--wiki", str(wiki), "--raw", str(raw)
            )
            self.assertEqual(first_build.returncode, 0, first_build.stderr)

            conn = sqlite3.connect(db)
            seed_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
            seed_edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
            conn.close()
            self.assertEqual(seed_nodes, 2)
            self.assertEqual(seed_edges, 1)

            good_article.write_text(
                """---
title: "A"
type: concept
summary: "a"
last_compiled: 2026-04-20
edges:
  - {to: "concepts/b", predicate: "still_nope"}
---

[[concepts/b]]
""",
                encoding="utf-8",
            )

            failed_build = _run_gq(
                "--db", str(db), "build", "--wiki", str(wiki), "--raw", str(raw)
            )
            self.assertNotEqual(failed_build.returncode, 0)
            self.assertIn("invalid predicate", failed_build.stderr)

            conn = sqlite3.connect(db)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0],
                seed_nodes,
            )
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0],
                seed_edges,
            )
            conn.close()
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class VizFreshnessTests(unittest.TestCase):
    """viz/graph.py must not render a stale DB when the wiki has moved."""

    def _load_viz(self):
        import importlib.util
        viz_path = TOOLS_DIR / "viz" / "graph.py"
        spec = importlib.util.spec_from_file_location("viz_graph", viz_path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore[union-attr]
        return module

    def test_build_graph_data_preserves_dangling_edges(self):
        """Edges with an endpoint missing from the nodes map should surface
        in the viz via placeholder nodes rather than being silently dropped
        — otherwise the reader can't spot broken wikilinks in the graph."""
        viz = self._load_viz()
        nodes = {
            "concepts/a": {"title": "A", "type": "concept", "summary": ""},
        }
        edges = [
            ("concepts/a", "concepts/b", "mentions"),   # tgt missing
            ("concepts/a", "raw/paper", "cites"),        # raw/ tgt missing
        ]
        data = viz.build_graph_data(nodes, edges)
        ids = {n["id"] for n in data["nodes"]}
        self.assertIn("concepts/b", ids)
        self.assertIn("raw/paper", ids)
        # Both edges must still be rendered.
        self.assertEqual(len(data["links"]), 2)
        # Raw placeholder keeps its type so colouring stays consistent.
        by_id = {n["id"]: n for n in data["nodes"]}
        self.assertEqual(by_id["raw/paper"]["type"], "raw")
        self.assertEqual(by_id["concepts/b"]["type"], "meta")

    def test_load_from_wiki_rejects_invalid_frontmatter_predicate(self):
        viz = self._load_viz()
        tmp = Path(tempfile.mkdtemp(prefix="viz-invalid-predicate-"))
        try:
            wiki = tmp / "wiki"
            (wiki / "concepts").mkdir(parents=True)
            (wiki / "concepts" / "a.md").write_text(
                """---
title: "A"
type: concept
summary: "a"
last_compiled: 2026-04-21
edges:
  - {to: "concepts/b", predicate: "still_nope"}
---

[[concepts/b]]
""",
                encoding="utf-8",
            )
            (wiki / "concepts" / "b.md").write_text(
                """---
title: "B"
type: concept
summary: "b"
last_compiled: 2026-04-21
---
""",
                encoding="utf-8",
            )
            original_wiki = viz.WIKI
            try:
                viz.WIKI = str(wiki)
                with self.assertRaisesRegex(ValueError, "invalid predicate"):
                    viz.load_from_wiki()
            finally:
                viz.WIKI = original_wiki
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_wiki_is_newer_than_db(self):
        viz = self._load_viz()
        tmp = Path(tempfile.mkdtemp(prefix="viz-freshness-"))
        try:
            wiki = tmp / "wiki"
            wiki.mkdir()
            article = wiki / "a.md"
            article.write_text("hi", encoding="utf-8")

            db = tmp / ".graph.db"
            db.write_bytes(b"")
            import os as _os
            import time as _time
            # Make the wiki article newer than the DB.
            past = _os.path.getmtime(db) - 60
            _os.utime(article, (past + 120, past + 120))
            _os.utime(db, (past, past))
            self.assertTrue(viz._wiki_is_newer_than_db(str(db), str(wiki)))

            # Now make the DB newer.
            _os.utime(db, (past + 240, past + 240))
            self.assertFalse(viz._wiki_is_newer_than_db(str(db), str(wiki)))

            # Missing DB -> treat as stale (force fresh extraction).
            _os.unlink(db)
            self.assertTrue(viz._wiki_is_newer_than_db(str(db), str(wiki)))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_wiki_is_newer_than_db_ignores_skipped_files(self):
        viz = self._load_viz()
        tmp = Path(tempfile.mkdtemp(prefix="viz-freshness-skipped-"))
        try:
            wiki = tmp / "wiki"
            (wiki / "concepts").mkdir(parents=True)
            (wiki / "_meta").mkdir()

            relevant = wiki / "concepts" / "a.md"
            relevant.write_text("concept", encoding="utf-8")
            skipped_meta = wiki / "_meta" / "summaries.md"
            skipped_meta.write_text("meta", encoding="utf-8")
            skipped_index = wiki / "_index.md"
            skipped_index.write_text("index", encoding="utf-8")
            skipped_log = wiki / "log.md"
            skipped_log.write_text("log", encoding="utf-8")
            skipped_private = wiki / "concepts" / "_draft.md"
            skipped_private.write_text("draft", encoding="utf-8")

            db = tmp / ".graph.db"
            db.write_bytes(b"")

            import os as _os

            base = _os.path.getmtime(db)
            _os.utime(relevant, (base - 120, base - 120))
            _os.utime(skipped_meta, (base + 120, base + 120))
            _os.utime(skipped_index, (base + 120, base + 120))
            _os.utime(skipped_log, (base + 120, base + 120))
            _os.utime(skipped_private, (base + 120, base + 120))
            _os.utime(db, (base, base))

            self.assertFalse(viz._wiki_is_newer_than_db(str(db), str(wiki)))

            _os.utime(relevant, (base + 240, base + 240))
            self.assertTrue(viz._wiki_is_newer_than_db(str(db), str(wiki)))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_load_from_graph_db_returns_none_when_connect_fails(self):
        viz = self._load_viz()
        with mock.patch.object(
            viz.sqlite3,
            "connect",
            side_effect=sqlite3.OperationalError("unable to open database file"),
        ):
            self.assertIsNone(viz.load_from_graph_db(__file__))

    def test_load_from_wiki_does_not_duplicate_tools_path(self):
        viz = self._load_viz()
        tmp = Path(tempfile.mkdtemp(prefix="viz-sys-path-"))
        try:
            wiki = tmp / "wiki"
            (wiki / "concepts").mkdir(parents=True)
            (wiki / "concepts" / "a.md").write_text(
                """---
title: "A"
type: concept
summary: "a"
last_compiled: 2026-04-22
---

[[concepts/b]]
""",
                encoding="utf-8",
            )
            (wiki / "concepts" / "b.md").write_text(
                """---
title: "B"
type: concept
summary: "b"
last_compiled: 2026-04-22
---
""",
                encoding="utf-8",
            )

            original_wiki = viz.WIKI
            tools_path = os.path.join(viz.BASE, "tools")
            original_sys_path = list(sys.path)
            try:
                sys.path[:] = [p for p in sys.path if p != tools_path]
                viz.WIKI = str(wiki)
                viz.load_from_wiki()
                viz.load_from_wiki()
                self.assertEqual(sum(p == tools_path for p in sys.path), 1)
            finally:
                viz.WIKI = original_wiki
                sys.path[:] = original_sys_path
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_generate_html_uses_text_nodes_and_safe_script_json(self):
        viz = self._load_viz()
        graph_data = {
            "nodes": [{
                "id": "concepts/x",
                "title": '</script><img src=x onerror="alert(1)">',
                "type": "concept",
                "summary": "<b>unsafe</b>",
                "connections": 1,
            }],
            "links": [],
        }

        html_doc = viz.generate_html(graph_data)

        self.assertNotIn("tt.innerHTML =", html_doc)
        self.assertIn("tt.replaceChildren(", html_doc)
        self.assertNotIn('</script><img src=x onerror="alert(1)">', html_doc)
        self.assertIn(
            '\\u003c/script\\u003e\\u003cimg src=x onerror=\\"alert(1)\\"\\u003e',
            html_doc,
        )
        self.assertIn('\\u003cb\\u003eunsafe\\u003c/b\\u003e', html_doc)

    def test_generate_svg_escapes_titles(self):
        viz = self._load_viz()
        svg = viz.generate_svg({
            "nodes": [{
                "id": "concepts/x",
                "title": 'A & <B> "C"',
                "type": "concept",
                "summary": "",
                "connections": 0,
            }],
            "links": [],
        })

        self.assertIn("A &amp; &lt;B&gt; &quot;C&quot;", svg)
        self.assertNotIn('A & <B> "C"', svg)


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
        loader.loadTestsFromTestCase(CliBuildTests),
        loader.loadTestsFromTestCase(VizFreshnessTests),
    ])

    if args.json:
        with open(os.devnull, "w") as devnull:
            runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
            try:
                result = runner.run(suite)
            except Exception:
                traceback.print_exc()
                return 2
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
