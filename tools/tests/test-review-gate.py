#!/usr/bin/env python3
"""Regression tests for the compile review gate."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from tools.compile import review  # noqa: E402
from kb.commands import llm_commands  # noqa: E402
from kb.commands._common import CommandContext, run_llm_command  # noqa: E402
from kb.runner import LLMResult  # noqa: E402
from kb.workspace import Workspace  # noqa: E402

CHECKER_PATH = BASE_DIR / "tools" / "tests" / "check-template-leaks.py"


def load_template_checker():
    spec = importlib.util.spec_from_file_location("check_template_leaks", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {CHECKER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TEMPLATE_CHECKER = load_template_checker()


def long_body(words: int = 95) -> str:
    prose = " ".join(f"word{i}" for i in range(words))
    return f"""## Overview

{prose}

## Sources

- [[sources/source-one]] documents the source material.
"""


def valid_concept(title: str = "Good Concept") -> str:
    return f"""---
title: "{title}"
type: concept
sources: ["[[sources/source-one]]"]
related: []
last_compiled: 2026-04-26
summary: "A useful concept summary."
---

{long_body()}
"""


def source_summary(title: str = "Short Source", *, words: int = 95, summary: str = "Source summary.") -> str:
    prose = " ".join(f"sourceword{i}" for i in range(words))
    return f"""---
title: "{title}"
type: source-summary
source: "[[sources/source-one]]"
last_compiled: 2026-04-26
summary: "{summary}"
---

## Key Points

{prose}
"""


class ReviewGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for subdir in ("wiki/concepts", "wiki/sources", "wiki/_meta", "raw"):
            (self.root / subdir).mkdir(parents=True, exist_ok=True)
        (self.root / "wiki" / "sources" / "source-one.md").write_text(
            "# Source One\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_valid_changed_article_passes_and_logs_zero_reviewer_cost(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        article = self.root / "wiki" / "concepts" / "good.md"
        article.write_text(valid_concept(), encoding="utf-8")

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertTrue(outcome.ok, outcome.rejection_summary())
        self.assertEqual(1, outcome.candidates)
        self.assertEqual(1, len(outcome.accepted))
        self.assertEqual(0, outcome.llm_cost["total_tokens"])
        log_path = self.root / "wiki" / "_meta" / "compile-review.jsonl"
        self.assertTrue(log_path.exists())
        event = json.loads(log_path.read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(1, event["accepted"])
        self.assertEqual(0, event["llm"]["cost"]["total_tokens"])

    def test_placeholder_rejection_quarantines_new_article(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        article = self.root / "wiki" / "concepts" / "bad.md"
        article.write_text(
            valid_concept("Bad Concept").replace(
                "A useful concept summary.",
                "{{summary}}",
            ),
            encoding="utf-8",
        )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertFalse(outcome.ok)
        self.assertFalse(article.exists())
        self.assertEqual(1, len(outcome.rejected))
        self.assertTrue((self.root / "wiki" / ".pending").is_dir())
        pending_files = list((self.root / "wiki" / ".pending").rglob("bad.md"))
        note_files = list((self.root / "wiki" / ".pending").rglob("bad.review.md"))
        self.assertEqual(1, len(pending_files))
        self.assertEqual(1, len(note_files))
        self.assertIn("template_placeholder", note_files[0].read_text(encoding="utf-8"))

    def test_min_length_is_warning_not_rejection(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        article = self.root / "wiki" / "sources" / "short.md"
        article.write_text(source_summary(words=12), encoding="utf-8")

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertTrue(outcome.ok, outcome.rejection_summary())
        self.assertTrue(article.exists())
        self.assertEqual(1, len(outcome.accepted))
        self.assertEqual("min_length", outcome.accepted[0].warnings[0].code)
        event = json.loads(
            (self.root / "wiki" / "_meta" / "compile-review.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()[-1]
        )
        self.assertEqual("min_length", event["articles"][0]["warnings"][0]["code"])

    def test_short_source_warning_does_not_cascade_to_linking_articles(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        source = self.root / "wiki" / "sources" / "short.md"
        source.write_text(source_summary(words=12), encoding="utf-8")
        concept = self.root / "wiki" / "concepts" / "linked.md"
        concept.write_text(
            valid_concept("Linked Concept").replace(
                "[[sources/source-one]]",
                "[[sources/short]]",
            ),
            encoding="utf-8",
        )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertTrue(outcome.ok, outcome.rejection_summary())
        self.assertEqual(2, len(outcome.accepted))
        self.assertTrue(source.exists())
        self.assertTrue(concept.exists())
        self.assertFalse((self.root / "wiki" / ".pending").exists())

    def test_rejection_summary_separates_root_causes_from_dependents(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        bad_source = self.root / "wiki" / "sources" / "bad.md"
        bad_source.write_text(
            source_summary(words=95, summary="{{summary}}"),
            encoding="utf-8",
        )
        concept = self.root / "wiki" / "concepts" / "linked-bad.md"
        concept.write_text(
            valid_concept("Linked Bad").replace(
                "[[sources/source-one]]",
                "[[sources/bad]]",
            ),
            encoding="utf-8",
        )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertFalse(outcome.ok)
        summary = outcome.rejection_summary()
        self.assertIn("1 root rejection(s)", summary)
        self.assertIn("1 dependent rejection(s)", summary)
        self.assertIn("Root rejections:", summary)
        self.assertIn("Dependent rejection targets:", summary)
        self.assertIn("[[sources/bad]]: 1 article(s)", summary)

    def test_structural_wiki_markdown_template_leaks_are_rejected(self) -> None:
        cases = [
            "_index.md",
            "log.md",
            "_meta/summaries.md",
        ]
        for rel_path in cases:
            with self.subTest(rel_path=rel_path):
                root = Path(tempfile.mkdtemp(dir=self.root))
                (root / "wiki" / "_meta").mkdir(parents=True, exist_ok=True)
                before = review.snapshot_articles(root / "wiki")
                target = root / "wiki" / rel_path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    f"Structural page leaked {{{{summary}}}} in {rel_path}\n",
                    encoding="utf-8",
                )

                outcome = review.review_wiki_writes(
                    root,
                    before_snapshot=before,
                    config=review.ReviewerConfig(enable_llm=False),
                )

                self.assertFalse(outcome.ok)
                self.assertEqual(1, outcome.candidates)
                self.assertEqual(
                    "template_placeholder",
                    outcome.rejected[0].issues[0].code,
                )
                self.assertFalse(target.exists())
                self.assertEqual(
                    1,
                    len(list((root / "wiki" / ".pending").rglob(Path(rel_path).name))),
                )

    def test_structural_wiki_markdown_does_not_require_article_frontmatter(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        log_path = self.root / "wiki" / "log.md"
        log_path.write_text(
            "## [2026-04-26] compile | updated metadata\n- Plain structural log entry.\n",
            encoding="utf-8",
        )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertTrue(outcome.ok, outcome.rejection_summary())
        self.assertEqual(1, outcome.candidates)
        self.assertEqual("wiki-page", outcome.accepted[0].article_type)

    def test_existing_article_is_restored_when_rejected(self) -> None:
        article = self.root / "wiki" / "concepts" / "stable.md"
        original = valid_concept("Stable Concept")
        article.write_text(original, encoding="utf-8")
        before = review.snapshot_articles(self.root / "wiki")

        article.write_text(
            """---
title: "Stable Concept"
type: concept
sources: ["[[sources/source-one]]"]
last_compiled: 2026-04-26
summary: ""
---

Too short.
""",
            encoding="utf-8",
        )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=False),
        )

        self.assertFalse(outcome.ok)
        self.assertEqual(original, article.read_text(encoding="utf-8"))
        self.assertEqual(1, len(list((self.root / "wiki" / ".pending").rglob("stable.md"))))

    def test_optional_llm_reviewer_can_reject_without_live_call(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        article = self.root / "wiki" / "concepts" / "llm-reject.md"
        article.write_text(valid_concept("LLM Reject"), encoding="utf-8")
        calls = []

        def fake_reviewer(candidate, _context, _config):
            calls.append(candidate.rel_path)
            return review.LLMReviewDecision(
                ok=False,
                notes=["internal contradiction"],
                usage={"input_tokens": 7, "output_tokens": 3, "total_tokens": 10},
            )

        outcome = review.review_wiki_writes(
            self.root,
            before_snapshot=before,
            config=review.ReviewerConfig(enable_llm=True, llm_model="haiku"),
            llm_reviewer=fake_reviewer,
        )

        self.assertEqual(["concepts/llm-reject.md"], calls)
        self.assertFalse(outcome.ok)
        self.assertEqual(10, outcome.llm_cost["total_tokens"])
        self.assertIn("internal contradiction", outcome.rejection_summary())
        self.assertFalse(article.exists())

    def test_optional_llm_review_context_is_loaded_once_per_review(self) -> None:
        before = review.snapshot_articles(self.root / "wiki")
        (self.root / "wiki" / "concepts" / "first.md").write_text(
            valid_concept("First Concept"),
            encoding="utf-8",
        )
        (self.root / "wiki" / "concepts" / "second.md").write_text(
            valid_concept("Second Concept"),
            encoding="utf-8",
        )
        context_calls = []
        reviewer_contexts = []

        def fake_context(_wiki_dir, _config):
            context_calls.append("loaded")
            return "shared context"

        def fake_reviewer(_candidate, context, _config):
            reviewer_contexts.append(context)
            return review.LLMReviewDecision(
                ok=True,
                usage={"input_tokens": 2, "output_tokens": 3},
            )

        with mock.patch.object(review, "_load_review_context", side_effect=fake_context):
            outcome = review.review_wiki_writes(
                self.root,
                before_snapshot=before,
                config=review.ReviewerConfig(enable_llm=True, llm_model="haiku"),
                llm_reviewer=fake_reviewer,
            )

        self.assertTrue(outcome.ok, outcome.rejection_summary())
        self.assertEqual(["loaded"], context_calls)
        self.assertEqual(["shared context", "shared context"], reviewer_contexts)
        self.assertEqual(10, outcome.llm_cost["total_tokens"])

    def test_pending_quarantine_is_ignored_by_template_leak_checker(self) -> None:
        pending = self.root / "wiki" / ".pending" / "batch" / "concepts"
        pending.mkdir(parents=True)
        (pending / "bad.md").write_text("Leaked {{summary}}\n", encoding="utf-8")

        old_base = TEMPLATE_CHECKER.BASE_DIR
        old_wiki = TEMPLATE_CHECKER.WIKI_DIR
        TEMPLATE_CHECKER.BASE_DIR = self.root
        TEMPLATE_CHECKER.WIKI_DIR = self.root / "wiki"
        try:
            result = TEMPLATE_CHECKER.run_checks()
        finally:
            TEMPLATE_CHECKER.BASE_DIR = old_base
            TEMPLATE_CHECKER.WIKI_DIR = old_wiki

        self.assertTrue(result["ok"])
        self.assertEqual(0, result["total_leaks"])

    @mock.patch("kb.commands._common.invoke_llm")
    def test_shared_llm_helper_runs_review_before_accepting_writes(self, invoke_mock) -> None:
        def fake_invoke(*_args, **_kwargs):
            article = self.root / "wiki" / "concepts" / "from-agent.md"
            article.write_text(
                textwrap.dedent(
                    """\
                    ---
                    title: "From Agent"
                    type: concept
                    sources: ["[[sources/source-one]]"]
                    last_compiled: 2026-04-26
                    summary: "{{summary}}"
                    ---

                    """
                )
                + long_body(),
                encoding="utf-8",
            )
            return LLMResult(text="compile finished", returncode=0)

        invoke_mock.side_effect = fake_invoke
        ctx = CommandContext(
            workspace=Workspace(kb_home=self.root, kb_dir=self.root),
            no_commit=False,
        )

        result = run_llm_command(
            ctx,
            command="compile",
            topic=None,
            prompt_builder=lambda: "compile",
            commit_label="compile wiki",
        )

        self.assertFalse(result.ok)
        self.assertIn("compile review rejected", result.message or "")
        self.assertIn("compile_review", result.details)
        self.assertFalse((self.root / "wiki" / "concepts" / "from-agent.md").exists())

    @mock.patch("kb.commands._common.invoke_llm")
    def test_shared_llm_helper_rejects_index_only_template_write(self, invoke_mock) -> None:
        def fake_invoke(*_args, **_kwargs):
            (self.root / "wiki" / "_index.md").write_text(
                "# Index\n\nLeaked {{summary}}\n",
                encoding="utf-8",
            )
            return LLMResult(text="compile finished", returncode=0)

        invoke_mock.side_effect = fake_invoke
        ctx = CommandContext(
            workspace=Workspace(kb_home=self.root, kb_dir=self.root),
            no_commit=False,
        )

        result = run_llm_command(
            ctx,
            command="compile",
            topic=None,
            prompt_builder=lambda: "compile",
            commit_label="compile wiki",
        )

        self.assertFalse(result.ok)
        self.assertIn("compile review rejected", result.message or "")
        self.assertIn("compile_review", result.details)
        self.assertEqual(1, result.details["compile_review"]["candidates"])
        self.assertFalse((self.root / "wiki" / "_index.md").exists())

    @mock.patch("kb.commands._common.invoke_llm")
    def test_shared_llm_helper_verbose_reports_review_counts(self, invoke_mock) -> None:
        def fake_invoke(*_args, **_kwargs):
            (self.root / "wiki" / "_index.md").write_text(
                "# Index\n\nLeaked {{summary}}\n",
                encoding="utf-8",
            )
            return LLMResult(text="compile finished", returncode=0)

        invoke_mock.side_effect = fake_invoke
        ctx = CommandContext(
            workspace=Workspace(kb_home=self.root, kb_dir=self.root),
            no_commit=False,
            verbose=True,
        )
        stderr = io.StringIO()

        with contextlib.redirect_stderr(stderr):
            result = run_llm_command(
                ctx,
                command="compile",
                topic=None,
                prompt_builder=lambda: "compile",
                commit_label="compile wiki",
            )

        self.assertFalse(result.ok)
        output = stderr.getvalue()
        self.assertIn("[kb] llm | command=compile", output)
        self.assertIn("[kb] review | scanning changed wiki writes", output)
        self.assertIn("candidates=1 accepted=0 rejected=1", output)

    def _write_fake_generate_all(self, body: str) -> None:
        regen = self.root / "tools" / "compile" / "regen_meta.py"
        regen.parent.mkdir(parents=True, exist_ok=True)
        regen.write_text(
            "from pathlib import Path\n"
            "Path('wiki/_meta').mkdir(parents=True, exist_ok=True)\n"
            "Path('wiki/_meta/summaries.md').write_text('# summaries\\n')\n",
            encoding="utf-8",
        )
        script = self.root / "tools" / "compile" / "pages" / "generate_all.py"
        script.parent.mkdir(parents=True, exist_ok=True)
        script.write_text(body, encoding="utf-8")

    @mock.patch("kb.commands.llm_commands.auto_commit")
    def test_compile_wiki_rejects_invalid_post_decoration_write(
        self,
        auto_commit_mock,
    ) -> None:
        self._write_fake_generate_all(
            textwrap.dedent(
                """\
                from pathlib import Path

                Path("wiki").mkdir(exist_ok=True)
                Path("wiki/_index.md").write_text("# Index\\n\\nLeaked {{summary}}\\n")
                """
            )
        )
        ctx = CommandContext(workspace=Workspace(kb_home=self.root, kb_dir=self.root))

        result = llm_commands.compile_wiki(ctx)

        self.assertFalse(result.ok)
        self.assertIn("post-decoration compile review rejected", result.message or "")
        self.assertIn("post_decoration_review", result.details)
        self.assertGreaterEqual(
            result.details["post_decoration_review"]["candidates"],
            1,
        )
        self.assertNotIn(
            "{{summary}}",
            (self.root / "wiki" / "_index.md").read_text(encoding="utf-8"),
        )
        self.assertEqual(
            1,
            len(list((self.root / "wiki" / ".pending").rglob("_index.md"))),
        )
        auto_commit_mock.assert_not_called()

    @mock.patch("kb.commands.llm_commands.auto_commit")
    def test_compile_wiki_reviews_partial_decoration_writes_on_generator_failure(
        self,
        auto_commit_mock,
    ) -> None:
        self._write_fake_generate_all(
            textwrap.dedent(
                """\
                from pathlib import Path
                import sys

                Path("wiki").mkdir(exist_ok=True)
                Path("wiki/_index.md").write_text("# Index\\n\\nLeaked {{summary}}\\n")
                sys.exit(1)
                """
            )
        )
        ctx = CommandContext(workspace=Workspace(kb_home=self.root, kb_dir=self.root))

        result = llm_commands.compile_wiki(ctx)

        self.assertFalse(result.ok)
        self.assertIn("generate_all.py failed", result.message or "")
        self.assertIn("post-decoration compile review rejected", result.message or "")
        self.assertIn("post_decoration_review", result.details)
        self.assertGreaterEqual(
            result.details["post_decoration_review"]["candidates"],
            1,
        )
        self.assertNotIn(
            "{{summary}}",
            (self.root / "wiki" / "_index.md").read_text(encoding="utf-8"),
        )
        self.assertEqual(
            1,
            len(list((self.root / "wiki" / ".pending").rglob("_index.md"))),
        )
        auto_commit_mock.assert_not_called()

    @mock.patch("kb.commands.llm_commands.auto_commit")
    def test_compile_wiki_accepts_valid_post_decoration_write_before_commit(
        self,
        auto_commit_mock,
    ) -> None:
        self._write_fake_generate_all(
            textwrap.dedent(
                """\
                from pathlib import Path

                Path("wiki").mkdir(exist_ok=True)
                Path("wiki/Dashboard.md").write_text("# Dashboard\\n\\nGenerated summary.\\n")
                """
            )
        )
        auto_commit_mock.return_value = True
        ctx = CommandContext(workspace=Workspace(kb_home=self.root, kb_dir=self.root))

        result = llm_commands.compile_wiki(ctx)

        self.assertTrue(result.ok, result.message)
        self.assertIn("post_decoration_review", result.details)
        self.assertGreaterEqual(
            result.details["post_decoration_review"]["candidates"],
            1,
        )
        self.assertTrue((self.root / "wiki" / "Dashboard.md").exists())
        auto_commit_mock.assert_called_once_with(
            self.root,
            "compile wiki",
            dry_run=False,
        )


if __name__ == "__main__":
    json_mode = "--json" in sys.argv
    if json_mode:
        sys.argv.remove("--json")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReviewGateTests)
    stream = io.StringIO() if json_mode else sys.stderr
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0 if json_mode else 1,
    ).run(suite)
    if json_mode:
        print(
            json.dumps(
                {
                    "ok": result.wasSuccessful(),
                    "tests": result.testsRun,
                    "failures": len(result.failures),
                    "errors": len(result.errors),
                },
                indent=2,
            )
        )
    sys.exit(0 if result.wasSuccessful() else 1)
