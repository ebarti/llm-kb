from __future__ import annotations

import json
import subprocess
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

from tools.kb.budget import BudgetTracker
from tools.kb.commands.search import _parse_qmd
from tools.kb.runner import invoke_llm
from tools.kb.workspace import Workspace


REPO_ROOT = Path(__file__).resolve().parents[3]
KB_SCRIPT = REPO_ROOT / "kb"


class QmdParseTests(unittest.TestCase):
    def test_parse_qmd_current_llm_format(self) -> None:
        output = """# Search: "attention" — 2 results

1. **Softmax Attention vs Linear Attention** [comparison] score=13.0283
   Softmax attention (O(N^2*d), exact, sharp retrieval) vs linear attention.
   file: comparisons/softmax-vs-linear-attention.md
   backlinks: concepts/linear-attention
2. **Attention Mechanisms** [concept] score=13.0038
   The family of mechanisms enabling neural networks to focus on relevant input.
   file: concepts/attention-mechanisms.md
"""
        hits = _parse_qmd(output, top_k=10)

        self.assertEqual(2, len(hits))
        self.assertEqual(
            "comparisons/softmax-vs-linear-attention.md",
            hits[0].path,
        )
        self.assertEqual(
            "Softmax Attention vs Linear Attention",
            hits[0].title,
        )
        self.assertAlmostEqual(13.0283, hits[0].score)
        self.assertIn("Softmax attention", hits[0].snippet or "")


class RunnerBudgetTests(unittest.TestCase):
    @mock.patch("tools.kb.runner.subprocess.run")
    def test_cli_backend_rejects_hard_budgets(self, run_mock: mock.Mock) -> None:
        result = invoke_llm(
            "prompt",
            model="sonnet",
            budget=BudgetTracker(limit=1000),
            force_backend="cli",
        )

        self.assertEqual("cli", result.backend)
        self.assertTrue(result.budget_exceeded)
        self.assertEqual(1, result.returncode)
        self.assertIn("hard token budgets require the Anthropic SDK backend", result.text)
        run_mock.assert_not_called()

    def test_sdk_backend_caps_max_tokens_to_budget_remaining(self) -> None:
        create = mock.Mock(
            return_value=types.SimpleNamespace(content=[], usage={})
        )
        fake_client = types.SimpleNamespace(
            messages=types.SimpleNamespace(create=create)
        )
        fake_anthropic = types.SimpleNamespace(Anthropic=lambda: fake_client)
        budget = BudgetTracker(limit=100)
        budget.add(output_tokens=60)

        with mock.patch.dict("sys.modules", {"anthropic": fake_anthropic}):
            result = invoke_llm(
                "prompt",
                model="sonnet",
                budget=budget,
                force_backend="sdk",
            )

        self.assertEqual("sdk", result.backend)
        self.assertEqual(0, result.returncode)
        create.assert_called_once()
        self.assertEqual(40, create.call_args.kwargs["max_tokens"])

    def test_sdk_backend_fails_fast_when_budget_is_exhausted(self) -> None:
        create = mock.Mock()
        fake_client = types.SimpleNamespace(
            messages=types.SimpleNamespace(create=create)
        )
        fake_anthropic = types.SimpleNamespace(Anthropic=lambda: fake_client)
        budget = BudgetTracker(limit=25)
        budget.add(output_tokens=25)

        with mock.patch.dict("sys.modules", {"anthropic": fake_anthropic}):
            result = invoke_llm(
                "prompt",
                model="sonnet",
                budget=budget,
                force_backend="sdk",
            )

        self.assertEqual("sdk", result.backend)
        self.assertTrue(result.budget_exceeded)
        self.assertEqual(1, result.returncode)
        self.assertIn("token budget exhausted before SDK call", result.text)
        create.assert_not_called()


class WorkspaceDryRunTests(unittest.TestCase):
    def test_dry_run_does_not_initialize_new_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "fresh-ws"
            # Pre-existing parent but target directory does not exist.
            self.assertFalse(target.exists())
            Workspace.resolve(dir_flag=str(target), dry_run=True)
            # Dry-run must not create the workspace tree, copy tools, init git, etc.
            self.assertFalse((target / "wiki").exists())
            self.assertFalse((target / ".git").exists())
            self.assertFalse((target / "tools").exists())

    def test_non_dry_run_initializes_new_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "live-ws"
            Workspace.resolve(dir_flag=str(target), dry_run=False)
            self.assertTrue((target / "wiki").exists())


class WorkspaceInitTests(unittest.TestCase):
    def test_initialize_copies_templates_into_empty_destination(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            kb_home = root / "kb-home"
            src_templates = kb_home / "templates"
            src_templates.mkdir(parents=True)
            (src_templates / "source.md").write_text(
                "# source template\n", encoding="utf-8"
            )

            target = root / "workspace"
            (target / ".git").mkdir(parents=True)

            ws = Workspace(kb_home=kb_home, kb_dir=target)
            ws.initialize(copy_tools=True)

            self.assertEqual(
                "# source template\n",
                (target / "templates" / "source.md").read_text(encoding="utf-8"),
            )


class WorkspacesCommandTests(unittest.TestCase):
    def test_workspaces_accepts_string_base(self) -> None:
        # Regression: passing a string base used to raise AttributeError
        # because Path methods were called on a str.
        with tempfile.TemporaryDirectory() as td:
            proc = subprocess.run(
                [str(KB_SCRIPT), "workspaces", td, "--json"],
                cwd=str(REPO_ROOT),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, proc.returncode, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual("workspaces", payload["command"])


class WrapperIntegrationTests(unittest.TestCase):
    def test_kb_wrapper_executes_python_cli(self) -> None:
        proc = subprocess.run(
            [str(KB_SCRIPT), "stats", "--json"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(0, proc.returncode, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual("stats", payload["command"])
        self.assertIn("total_wiki_files", payload)


if __name__ == "__main__":
    unittest.main()
