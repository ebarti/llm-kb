from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path
from unittest import mock

from tools.kb.budget import BudgetTracker
from tools.kb.commands.search import _parse_qmd
from tools.kb.runner import invoke_llm


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
