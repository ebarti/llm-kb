#!/usr/bin/env python3
"""Tests for schema-driven typed compilation."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from tools.kb.commands._common import CommandContext
from tools.kb.runner import LLMResult
from tools.kb.typed_compile import compile_workspace
from tools.kb.workspace import Workspace


LONG_DETAIL = (
    "Schema driven compilation separates extraction from rendering. The source "
    "argues that a knowledge base compiler should ask for validated facts, "
    "concept updates, entity references, and comparison dimensions before it "
    "writes markdown. That separation makes retries easier, keeps frontmatter "
    "predictable, and lets unit tests exercise the compiler without making "
    "network calls or running an actual language model. The approach also "
    "makes unchanged raw sources stable because cached typed objects can be "
    "rendered repeatedly into identical wiki pages."
)


def _long_point(label: str) -> str:
    return (
        f"{label} is described as a durable finding with enough context to "
        "stand alone in the generated wiki article and survive the review gate."
    )


def _payload_for_prompt(prompt: str) -> dict:
    if "SourceSummary" in prompt:
        return {
            "title": "Structured RAG Notes",
            "key_points": [
                _long_point("Typed extraction"),
                _long_point("Deterministic rendering"),
                _long_point("Hash based cache reuse"),
            ],
            "detailed_summary": LONG_DETAIL,
            "notable_quotes": ["Validated objects make retries precise."],
            "related_concepts": [
                "retrieval augmented generation",
                "schema driven compilation",
            ],
            "entities_mentioned": ["Example Compiler"],
        }
    if "ConceptUpdateBatch" in prompt:
        return {
            "updates": [
                {
                    "concept_id": "retrieval-augmented-generation",
                    "new_key_ideas": [
                        _long_point("Retrieval augmented generation"),
                        _long_point("Source grounded synthesis"),
                    ],
                    "source_citation": (
                        "Explains how typed compiler outputs keep source "
                        "summaries tied to retrievable evidence."
                    ),
                    "related_concepts": ["schema-driven-compilation"],
                },
                {
                    "concept_id": "schema-driven-compilation",
                    "new_key_ideas": [
                        _long_point("Schema driven compilation"),
                        _long_point("Validation before rendering"),
                    ],
                    "source_citation": (
                        "Defines compile outputs as structured data before "
                        "markdown assembly."
                    ),
                    "related_concepts": ["retrieval-augmented-generation"],
                },
                {
                    "concept_id": "freeform-compilation",
                    "new_key_ideas": [
                        _long_point("Freeform compilation"),
                        _long_point("Prompt only rendering risk"),
                    ],
                    "source_citation": (
                        "Contrasts validated typed objects with a single "
                        "freeform prompt that edits files directly."
                    ),
                    "related_concepts": ["schema-driven-compilation"],
                },
            ]
        }
    if "EntityRefBatch" in prompt:
        return {
            "entities": [
                {
                    "name": "Example Compiler",
                    "entity_type": "tool",
                    "role_in_source": (
                        "Used as the named example for validating extracted "
                        "objects before wiki pages are rendered."
                    ),
                    "aliases": ["Compiler Example"],
                }
            ]
        }
    if "ComparisonBatch" in prompt:
        return {
            "comparisons": [
                {
                    "subject_a": "schema driven compilation",
                    "subject_b": "freeform compilation",
                    "dimensions": [
                        {
                            "dimension": "Validation",
                            "subject_a": "Pydantic validates every object and field.",
                            "subject_b": "A single prompt may emit malformed markdown.",
                        },
                        {
                            "dimension": "Repeatability",
                            "subject_a": "Cached typed objects render byte-identical pages.",
                            "subject_b": "Repeated freeform edits can drift between runs.",
                        },
                    ],
                    "tradeoffs": [
                        _long_point("Typed compile requires more calls"),
                        _long_point("Freeform compile can be faster initially"),
                    ],
                }
            ]
        }
    raise AssertionError(f"unexpected prompt: {prompt[:200]}")


class TypedCompileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._write_minimal_workspace()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _write_minimal_workspace(self) -> None:
        (self.root / "wiki" / "_meta").mkdir(parents=True)
        (self.root / "wiki" / "log.md").write_text("# Knowledge Base Log\n", encoding="utf-8")
        raw = self.root / "raw" / "structured-rag"
        raw.mkdir(parents=True)
        raw.joinpath("clean.md").write_text(
            "# Structured RAG Notes\n\n" + LONG_DETAIL + "\n",
            encoding="utf-8",
        )
        raw.joinpath("meta.json").write_text(
            json.dumps(
                {
                    "slug": "structured-rag",
                    "url": "https://example.test/structured-rag",
                    "sha256_clean": "test",
                }
            ),
            encoding="utf-8",
        )
        compile_dir = self.root / "tools" / "compile"
        pages_dir = compile_dir / "pages"
        pages_dir.mkdir(parents=True)
        compile_dir.joinpath("regen_meta.py").write_text(
            "from pathlib import Path\n"
            "Path('wiki/_meta/summaries.md').write_text('# summaries\\n')\n",
            encoding="utf-8",
        )
        pages_dir.joinpath("generate_all.py").write_text(
            "from pathlib import Path\n"
            "Path('wiki/Dashboard.md').write_text('# Dashboard\\n\\nGenerated summary.\\n')\n",
            encoding="utf-8",
        )

    def _ctx(self) -> CommandContext:
        return CommandContext(
            workspace=Workspace(kb_home=self.root, kb_dir=self.root),
            no_commit=True,
        )

    def test_compile_uses_typed_calls_and_renders_pages(self) -> None:
        calls: list[str] = []

        def fake_invoke(*, prompt, budget, **_kwargs):
            calls.append(prompt)
            budget.add(input_tokens=5, output_tokens=7)
            return LLMResult(text=json.dumps(_payload_for_prompt(prompt)), returncode=0)

        result = compile_workspace(
            self._ctx(),
            invoke_model=fake_invoke,
            now=datetime(2026, 4, 27, 12, tzinfo=timezone.utc),
        )

        self.assertTrue(result.ok, result.message)
        self.assertEqual(4, len(calls))
        self.assertEqual(4, result.details["llm_calls"])
        self.assertTrue((self.root / "wiki" / "sources" / "structured-rag.md").exists())
        self.assertTrue(
            (self.root / "wiki" / "concepts" / "schema-driven-compilation.md").exists()
        )
        self.assertTrue((self.root / "wiki" / "entities" / "example-compiler.md").exists())
        self.assertTrue(
            (
                self.root
                / "wiki"
                / "comparisons"
                / "schema-driven-compilation-vs-freeform-compilation.md"
            ).exists()
        )
        source_text = (self.root / "wiki" / "sources" / "structured-rag.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("type: \"source-summary\"", source_text)
        self.assertIn("[[raw/structured-rag]]", source_text)
        self.assertTrue((self.root / "wiki" / "_meta" / "typed-compile-cache.json").exists())

    def test_second_compile_uses_cache_and_preserves_source_bytes(self) -> None:
        def fake_invoke(*, prompt, budget, **_kwargs):
            budget.add(input_tokens=5, output_tokens=7)
            return LLMResult(text=json.dumps(_payload_for_prompt(prompt)), returncode=0)

        first = compile_workspace(
            self._ctx(),
            invoke_model=fake_invoke,
            now=datetime(2026, 4, 27, 12, tzinfo=timezone.utc),
        )
        self.assertTrue(first.ok, first.message)
        source_path = self.root / "wiki" / "sources" / "structured-rag.md"
        before = source_path.read_bytes()

        def fail_if_called(**_kwargs):
            raise AssertionError("LLM should not be called when typed cache is current")

        second = compile_workspace(
            self._ctx(),
            invoke_model=fail_if_called,
            now=datetime(2026, 4, 28, 12, tzinfo=timezone.utc),
        )

        self.assertTrue(second.ok, second.message)
        self.assertEqual(0, second.details["llm_calls"])
        self.assertEqual(before, source_path.read_bytes())

    def test_validation_failure_names_object_and_field(self) -> None:
        def fake_invoke(*, prompt, **_kwargs):
            self.assertIn("SourceSummary", prompt)
            return LLMResult(text=json.dumps({"title": "Incomplete"}), returncode=0)

        result = compile_workspace(
            self._ctx(),
            invoke_model=fake_invoke,
            now=datetime(2026, 4, 27, 12, tzinfo=timezone.utc),
        )

        self.assertFalse(result.ok)
        self.assertIn("SourceSummary", result.message or "")
        self.assertIn("key_points", result.message or "")
        self.assertFalse((self.root / "wiki" / "sources" / "structured-rag.md").exists())


if __name__ == "__main__":
    json_mode = "--json" in sys.argv
    if json_mode:
        sys.argv.remove("--json")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TypedCompileTests)
    stream = io.StringIO() if json_mode else sys.stderr
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0 if json_mode else 1,
    ).run(suite)
    if json_mode:
        print(
            json.dumps(
                {
                    "total": result.testsRun,
                    "passed": result.testsRun - len(result.failures) - len(result.errors),
                    "failed": len(result.failures) + len(result.errors),
                    "ok": result.wasSuccessful(),
                }
            )
        )
    raise SystemExit(0 if result.wasSuccessful() else 1)
