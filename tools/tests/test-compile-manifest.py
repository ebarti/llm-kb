#!/usr/bin/env python3
"""Tests for content-hash incremental compile manifests."""

from __future__ import annotations

import json
import sys
import types
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.compile import manifest as compile_manifest
from tools.kb.commands import llm_commands
from tools.kb.commands._common import CommandContext
from tools.kb.models import LLMInvocationResult
from tools.kb.workspace import Workspace


def _write_raw_v2(root: Path, slug: str, clean: str, raw: bytes | None = None) -> None:
    source_dir = root / "raw" / slug
    source_dir.mkdir(parents=True, exist_ok=True)
    (source_dir / "clean.md").write_text(clean, encoding="utf-8")
    if raw is not None:
        (source_dir / "raw.txt").write_bytes(raw)
    (source_dir / "meta.json").write_text(
        json.dumps({"slug": slug, "sha256_clean": "test"}) + "\n",
        encoding="utf-8",
    )


def _ctx(root: Path) -> CommandContext:
    return CommandContext(
        workspace=Workspace(kb_home=REPO_ROOT, kb_dir=root),
        no_commit=True,
    )


def _successful_decoration_run() -> types.SimpleNamespace:
    return types.SimpleNamespace(returncode=0, stdout="", stderr="")


class CompileManifestTests(unittest.TestCase):
    def test_second_compile_is_noop_without_llm_call(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_llm,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))
                second = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertTrue(second.details["llm_skipped"])
            manifest = compile_manifest.load_manifest(root)
            self.assertIn("raw/alpha/", manifest)
            self.assertEqual(
                compile_manifest.COMPILER_VERSION,
                manifest["raw/alpha/"]["compiler_version"],
            )
            self.assertIn("wiki/sources/alpha.md", manifest["raw/alpha/"]["outputs"])

    def test_changed_raw_source_scopes_compile_prompt(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            _write_raw_v2(root, "beta", "# Beta\n", b"beta raw")

            def write_both_outputs() -> None:
                out_dir = root / "wiki" / "sources"
                out_dir.mkdir(parents=True, exist_ok=True)
                (out_dir / "alpha.md").write_text("# Alpha source\n", encoding="utf-8")
                (out_dir / "beta.md").write_text("# Beta source\n", encoding="utf-8")

            def fake_first(_ctx, *, command, topic, prompt_builder, commit_label):
                prompt_builder()
                write_both_outputs()
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_first,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            _write_raw_v2(root, "beta", "# Beta changed\n", b"beta raw")
            prompts: list[str] = []

            def fake_second(_ctx, *, command, topic, prompt_builder, commit_label):
                prompts.append(prompt_builder())
                beta_out = root / "wiki" / "sources" / "beta.md"
                beta_out.write_text("# Beta changed source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_second,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                result = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(result.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertIn("raw/beta/", prompts[0])
            self.assertNotIn("raw/alpha/", prompts[0])
            self.assertEqual(
                ["sha256-changed"],
                result.details["reasons"]["raw/beta/"],
            )

    def test_missing_output_recompiles_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_llm,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            (root / "wiki" / "sources" / "alpha.md").unlink()

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_llm,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                result = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(result.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertIn(
                "missing-output:wiki/sources/alpha.md",
                result.details["reasons"]["raw/alpha/"],
            )

    def test_compiler_version_bump_invalidates_manifest_entry(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_llm,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            with mock.patch("tools.compile.manifest.COMPILER_VERSION", "999.0"):
                with mock.patch(
                    "tools.kb.commands.llm_commands.run_llm_command",
                    side_effect=fake_llm,
                ) as run_mock, mock.patch(
                    "tools.kb.commands.llm_commands.subprocess.run",
                    return_value=_successful_decoration_run(),
                ):
                    result = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(result.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertIn(
                "compiler-version-changed",
                result.details["reasons"]["raw/alpha/"],
            )


if __name__ == "__main__":
    unittest.main()
