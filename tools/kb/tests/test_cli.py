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
from typing import Optional
from unittest import mock

from tools.kb import cli as cli_mod
from tools.kb.budget import BudgetTracker
from tools.kb.commands import export as export_cmd, serve as serve_cmd
from tools.kb.commands import test_cmd as test_cmd_module, viz as viz_cmd
from tools.kb.commands._common import CommandContext
from tools.kb.commands.search import _parse_qmd
from tools.kb.models import EXIT_ERROR
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


def _make_fake_agent_sdk():
    """Build a fake ``claude_agent_sdk`` module.

    Returns (module, sequence, captured, FakeAssistantMessage, FakeResultMessage).
    Tests mutate ``sequence`` to control what ``query()`` yields and inspect
    ``captured`` to assert on the options/prompt that the runner passed in.
    """

    class FakeAssistantMessage:
        def __init__(self, text: str) -> None:
            self.content = [types.SimpleNamespace(text=text)]

    class FakeResultMessage:
        def __init__(
            self,
            *,
            result: str = "",
            usage: Optional[dict] = None,
            is_error: bool = False,
            subtype: Optional[str] = None,
        ) -> None:
            self.result = result
            self.usage = usage or {}
            self.is_error = is_error
            self.subtype = subtype

    captured: dict = {}

    class FakeOptions:
        def __init__(self, **kwargs) -> None:
            captured["options"] = kwargs

    sequence: list = []

    async def query(prompt, options):  # noqa: ARG001 — options must be accepted
        captured["prompt"] = prompt
        for msg in sequence:
            yield msg

    module = types.SimpleNamespace(
        query=query,
        ClaudeAgentOptions=FakeOptions,
        AssistantMessage=FakeAssistantMessage,
        ResultMessage=FakeResultMessage,
    )
    return module, sequence, captured, FakeAssistantMessage, FakeResultMessage


class RunnerAgentBackendTests(unittest.TestCase):
    def test_agent_backend_returns_final_text_and_usage(self) -> None:
        module, seq, captured, Am, Rm = _make_fake_agent_sdk()
        seq.append(Am("streamed chunk "))
        seq.append(
            Rm(
                result="final answer",
                usage={"input_tokens": 10, "output_tokens": 7},
            )
        )

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=BudgetTracker(limit=None),
                )

        self.assertEqual("agent", result.backend)
        self.assertEqual(0, result.returncode)
        self.assertEqual("final answer", result.text)
        self.assertEqual(10, result.usage.input_tokens)
        self.assertEqual(7, result.usage.output_tokens)
        self.assertEqual("prompt", captured["prompt"])
        self.assertEqual("claude-sonnet-4-6", captured["options"]["model"])
        self.assertEqual("bypassPermissions", captured["options"]["permission_mode"])

    def test_agent_backend_falls_back_to_assistant_text_when_result_empty(self) -> None:
        module, seq, _captured, Am, Rm = _make_fake_agent_sdk()
        seq.append(Am("partial "))
        seq.append(Am("output"))
        seq.append(Rm(result="", usage={"output_tokens": 3}))

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=BudgetTracker(limit=None),
                )

        self.assertEqual(0, result.returncode)
        self.assertEqual("partial output", result.text)

    def test_agent_backend_flags_budget_exceeded_when_response_crosses_cap(self) -> None:
        module, seq, _captured, Am, Rm = _make_fake_agent_sdk()
        seq.append(Am("some text"))
        seq.append(Rm(result="some text", usage={"output_tokens": 120}))
        budget = BudgetTracker(limit=100)

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=budget,
                )

        self.assertEqual("agent", result.backend)
        self.assertTrue(result.budget_exceeded)
        self.assertEqual(1, result.returncode)
        self.assertEqual("some text", result.text)
        self.assertEqual(120, result.usage.output_tokens)

    def test_agent_backend_fails_fast_when_budget_already_exhausted(self) -> None:
        module, _seq, captured, _Am, _Rm = _make_fake_agent_sdk()
        budget = BudgetTracker(limit=25)
        budget.add(output_tokens=25)

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=budget,
                )

        self.assertEqual("agent", result.backend)
        self.assertTrue(result.budget_exceeded)
        self.assertEqual(1, result.returncode)
        self.assertIn("token budget exhausted before agent call", result.text)
        self.assertNotIn("prompt", captured)  # query() was never called

    def test_agent_backend_errors_without_api_key(self) -> None:
        module, _seq, _captured, _Am, _Rm = _make_fake_agent_sdk()

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict("os.environ", {}, clear=True):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=BudgetTracker(limit=None),
                )

        self.assertEqual("agent", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("ANTHROPIC_API_KEY", result.text)

    def test_agent_backend_errors_when_sdk_not_installed(self) -> None:
        # Force-import failure by stubbing claude_agent_sdk with a non-module.
        with mock.patch("tools.kb.runner._missing_sdk_error", return_value=ImportError("nope")):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=BudgetTracker(limit=None),
                )

        self.assertEqual("agent", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("claude-agent-sdk", result.text)

    def test_agent_backend_surfaces_agent_reported_error(self) -> None:
        module, seq, _captured, _Am, Rm = _make_fake_agent_sdk()
        seq.append(
            Rm(
                result="",
                usage={"input_tokens": 5, "output_tokens": 0},
                is_error=True,
                subtype="error_during_execution",
            )
        )

        with mock.patch.dict("sys.modules", {"claude_agent_sdk": module}):
            with mock.patch.dict(
                "os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=False
            ):
                result = invoke_llm(
                    "prompt",
                    model="sonnet",
                    budget=BudgetTracker(limit=None),
                )

        self.assertEqual("agent", result.backend)
        self.assertEqual(1, result.returncode)
        self.assertIn("error_during_execution", result.text)

    def test_dry_run_short_circuits_agent_call(self) -> None:
        result = invoke_llm(
            "prompt",
            model="sonnet",
            budget=BudgetTracker(limit=None),
            dry_run=True,
        )
        self.assertEqual("dry-run", result.backend)
        self.assertIn("DRY RUN", result.text)


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

    def test_named_dir_uses_kb_workspaces_env(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            custom_base = root / "custom-workspaces"
            home = root / "home"
            home.mkdir()

            with mock.patch("pathlib.Path.home", return_value=home):
                with mock.patch.dict(
                    "os.environ",
                    {"KB_WORKSPACES": str(custom_base)},
                    clear=False,
                ):
                    ws = Workspace.resolve(dir_flag="named", dry_run=True)

            self.assertEqual((custom_base / "named").resolve(), ws.kb_dir)
            self.assertFalse((home / "kb-workspaces" / "named").exists())


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
