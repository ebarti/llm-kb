from __future__ import annotations

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

from tools.kb import cli as cli_mod
from tools.kb.budget import BudgetTracker
from tools.kb.commands import export as export_cmd, serve as serve_cmd
from tools.kb.commands import test_cmd as test_cmd_module, viz as viz_cmd
from tools.kb.commands._common import CommandContext
from tools.kb.commands.search import _parse_qmd
from tools.kb.models import EXIT_ERROR
from tools.kb.runner import DEFAULT_MAX_OUTPUT_TOKENS, invoke_llm
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

    def test_sdk_backend_caps_large_budget_to_safe_output_limit(self) -> None:
        create = mock.Mock(
            return_value=types.SimpleNamespace(content=[], usage={})
        )
        fake_client = types.SimpleNamespace(
            messages=types.SimpleNamespace(create=create)
        )
        fake_anthropic = types.SimpleNamespace(Anthropic=lambda: fake_client)
        budget = BudgetTracker(limit=50_000)

        with mock.patch.dict("sys.modules", {"anthropic": fake_anthropic}):
            result = invoke_llm(
                "prompt",
                model="sonnet",
                budget=budget,
                force_backend="sdk",
            )

        self.assertEqual("sdk", result.backend)
        self.assertEqual(0, result.returncode)
        self.assertEqual(
            DEFAULT_MAX_OUTPUT_TOKENS,
            create.call_args.kwargs["max_tokens"],
        )

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

    @mock.patch("tools.kb.runner.shutil.which", return_value=None)
    def test_cli_backend_reports_sdk_available_when_cli_is_forced(
        self,
        _which_mock: mock.Mock,
    ) -> None:
        budget = BudgetTracker(limit=None)
        fake_anthropic = types.SimpleNamespace()

        with mock.patch.dict(
            "os.environ",
            {"ANTHROPIC_API_KEY": "test-key"},
            clear=False,
        ):
            with mock.patch.dict("sys.modules", {"anthropic": fake_anthropic}):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=budget,
                    force_backend="cli",
                )

        self.assertEqual("cli", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("SDK backend is available", result.text)

    @mock.patch("tools.kb.runner._invoke_cli")
    @mock.patch(
        "tools.kb.runner._sdk_import_error",
        return_value=ImportError("missing anthropic"),
    )
    def test_forced_sdk_backend_does_not_fallback_to_cli_when_unavailable(
        self,
        _sdk_import_error_mock: mock.Mock,
        invoke_cli_mock: mock.Mock,
    ) -> None:
        result = invoke_llm(
            "prompt",
            model="sonnet",
            budget=BudgetTracker(limit=None),
            force_backend="sdk",
        )

        self.assertEqual("sdk", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("forced SDK backend is unavailable", result.text)
        invoke_cli_mock.assert_not_called()

    @mock.patch("tools.kb.runner._invoke_cli")
    def test_invalid_force_backend_env_fails_fast(self, invoke_cli_mock: mock.Mock) -> None:
        with mock.patch.dict("os.environ", {"KB_FORCE_BACKEND": "bogus"}, clear=False):
            result = invoke_llm(
                "prompt",
                model="sonnet",
                budget=BudgetTracker(limit=None),
            )

        self.assertEqual("cli", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("invalid KB_FORCE_BACKEND value 'bogus'", result.text)
        invoke_cli_mock.assert_not_called()

    @mock.patch("tools.kb.runner.shutil.which", return_value="/usr/bin/claude")
    @mock.patch(
        "tools.kb.runner._sdk_import_error",
        return_value=RuntimeError("broken anthropic"),
    )
    @mock.patch("tools.kb.runner.subprocess.run")
    def test_auto_backend_falls_back_to_cli_on_broken_sdk_import(
        self,
        run_mock: mock.Mock,
        _sdk_import_error_mock: mock.Mock,
        _which_mock: mock.Mock,
    ) -> None:
        run_mock.return_value = types.SimpleNamespace(
            stdout="ok",
            stderr="",
            returncode=0,
        )

        with mock.patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False):
            result = invoke_llm(
                "prompt",
                model="sonnet",
                budget=BudgetTracker(limit=None),
            )

        self.assertEqual("cli", result.backend)
        self.assertEqual(0, result.returncode)
        run_mock.assert_called_once()


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

    def test_relative_parent_dir_is_treated_as_path_not_workspace_name(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            nested = root / "base" / "child"
            nested.mkdir(parents=True)
            home = root / "home"
            home.mkdir()
            previous_cwd = Path.cwd()
            try:
                os.chdir(nested)
                with mock.patch("pathlib.Path.home", return_value=home):
                    ws = Workspace.resolve(dir_flag="..", dry_run=True)
            finally:
                os.chdir(previous_cwd)

        self.assertEqual((root / "base").resolve(), ws.kb_dir)
        self.assertFalse(str(ws.kb_dir).startswith(str(home / "kb-workspaces")))


class GlobalOptionTests(unittest.TestCase):
    def test_budget_must_be_positive(self) -> None:
        with self.assertRaisesRegex(SystemExit, "positive integer"):
            cli_mod._parse_global_options(["--budget", "0", "stats"])
        with self.assertRaisesRegex(SystemExit, "positive integer"):
            cli_mod._parse_global_options(["--budget=-5", "stats"])

    def test_build_context_uses_kb_token_budget_only(self) -> None:
        opts = cli_mod.GlobalOptions()
        with mock.patch.dict("os.environ", {"KB_BUDGET": "7", "KB_TOKEN_BUDGET": "11"}, clear=False):
            ctx = cli_mod._build_context(opts)
        self.assertEqual(11, ctx.budget_limit)


class WorkspaceInitTests(unittest.TestCase):
    def test_run_init_resolves_relative_target_against_workspace_dir(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td) / "ws"
            workspace.mkdir()
            ctx = cli_mod._build_context(cli_mod.GlobalOptions(dir_flag=str(workspace)))

            result = cli_mod.init_cmd.run_init(ctx, target="child", dry_run=True)

            self.assertEqual(str((workspace / "child").resolve()), result.target)

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


class ServeCommandTests(unittest.TestCase):
    @mock.patch("tools.kb.commands.serve.os.execvp")
    def test_run_serve_uses_sys_executable(self, execvp_mock: mock.Mock) -> None:
        ctx = CommandContext(workspace=Workspace.resolve(dry_run=True))
        execvp_mock.side_effect = OSError("boom")

        result = serve_cmd.run_serve(ctx, port=9999)

        self.assertFalse(result.ok)
        execvp_mock.assert_called_once()
        exe, argv = execvp_mock.call_args.args
        self.assertEqual(sys.executable or "python3", exe)
        self.assertEqual(sys.executable or "python3", argv[0])


class ExportCommandTests(unittest.TestCase):
    @mock.patch("tools.kb.commands.export.subprocess.run")
    def test_site_export_uses_active_python_interpreter(self, run_mock: mock.Mock) -> None:
        run_mock.return_value = types.SimpleNamespace(returncode=0, stdout="", stderr="")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            script = root / "tools" / "export" / "build-site.py"
            script.parent.mkdir(parents=True)
            script.write_text("print('ok')\n", encoding="utf-8")
            ctx = CommandContext(workspace=Workspace(kb_home=root, kb_dir=root))

            result = export_cmd.run(ctx, "site")

            self.assertTrue(result.ok)
            args = run_mock.call_args.args[0]
            self.assertEqual(sys.executable or "python3", args[0])

    @mock.patch("tools.kb.commands.export.subprocess.run")
    @mock.patch("tools.kb.commands.export.shutil.which", return_value="/usr/bin/pandoc")
    def test_pdf_export_creates_output_dir(self, _which_mock: mock.Mock, run_mock: mock.Mock) -> None:
        run_mock.return_value = types.SimpleNamespace(returncode=0, stdout="", stderr="")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "wiki").mkdir()
            (root / "wiki" / "note.md").write_text("# Note\n", encoding="utf-8")
            ws = Workspace(kb_home=root, kb_dir=root)
            ctx = CommandContext(workspace=ws)

            result = export_cmd.run(ctx, "pdf")

            self.assertTrue((root / "output").exists())
            self.assertTrue(result.ok)
            self.assertEqual(str(root / "output" / "kb-export.pdf"), result.output_path)


class VizCommandTests(unittest.TestCase):
    @mock.patch("tools.kb.commands.viz.subprocess.run")
    def test_viz_uses_active_python_interpreter(self, run_mock: mock.Mock) -> None:
        run_mock.return_value = types.SimpleNamespace(returncode=0, stdout="", stderr="")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            script = root / "tools" / "viz" / "graph.py"
            script.parent.mkdir(parents=True)
            script.write_text("print('ok')\n", encoding="utf-8")
            ctx = CommandContext(workspace=Workspace(kb_home=root, kb_dir=root))

            result = viz_cmd.run(ctx, "graph")

            self.assertTrue(result.ok)
            args = run_mock.call_args.args[0]
            self.assertEqual(sys.executable or "python3", args[0])


class TestCommandTests(unittest.TestCase):
    @mock.patch("tools.kb.commands.test_cmd.subprocess.run")
    def test_invalid_json_output_is_treated_as_failure(self, run_mock: mock.Mock) -> None:
        run_mock.return_value = types.SimpleNamespace(
            returncode=0,
            stdout="not-json",
            stderr="warning",
        )
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            runner = root / "tools" / "tests" / "run-all.sh"
            runner.parent.mkdir(parents=True)
            runner.write_text("#!/bin/bash\n", encoding="utf-8")
            ctx = CommandContext(workspace=Workspace(kb_home=root, kb_dir=root))

            result = test_cmd_module.run(ctx)

            self.assertFalse(result.ok)
            self.assertEqual(EXIT_ERROR, result.exit_code)
            self.assertIn("did not return valid JSON", result.message or "")
            self.assertIn("stdout:\nnot-json", result.message or "")
            self.assertIn("stderr:\nwarning", result.message or "")


class MainExitHandlingTests(unittest.TestCase):
    def test_main_prints_non_integer_system_exit_messages(self) -> None:
        stderr = io.StringIO()
        with mock.patch.dict(
            cli_mod._COMMANDS,
            {"boom": lambda _ctx, _args: (_ for _ in ()).throw(SystemExit("boom"))},
            clear=False,
        ):
            with contextlib.redirect_stderr(stderr):
                exit_code = cli_mod.main(["boom"])

        self.assertEqual(EXIT_ERROR, exit_code)
        self.assertIn("boom", stderr.getvalue())


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

    def test_kb_wrapper_preserves_caller_cwd_for_relative_kb_dir(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "wiki" / "concepts").mkdir(parents=True)
            (root / "wiki" / "concepts" / "only.md").write_text(
                "# only\n",
                encoding="utf-8",
            )

            env = os.environ.copy()
            env["KB_DIR"] = "."
            proc = subprocess.run(
                [str(KB_SCRIPT), "stats", "--json"],
                cwd=str(root),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(0, proc.returncode, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(1, payload["total_wiki_files"])


if __name__ == "__main__":
    unittest.main()
