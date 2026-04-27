#!/usr/bin/env python3
"""Tests for content-hash incremental compile manifests."""

from __future__ import annotations

import json
import io
import os
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


def _ctx(root: Path, *, with_generate_all: bool = True) -> CommandContext:
    if with_generate_all:
        generate_all = root / "tools" / "compile" / "pages" / "generate_all.py"
        generate_all.parent.mkdir(parents=True, exist_ok=True)
        generate_all.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
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

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
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

    def test_changed_wiki_outputs_are_tracked_for_missing_output_detection(
        self,
    ) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                source_out = root / "wiki" / "sources" / "alpha.md"
                concept_out = root / "wiki" / "concepts" / "alpha.md"
                source_out.parent.mkdir(parents=True, exist_ok=True)
                concept_out.parent.mkdir(parents=True, exist_ok=True)
                source_out.write_text("# Alpha source\n", encoding="utf-8")
                concept_out.write_text("# Alpha concept\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_llm,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            manifest = compile_manifest.load_manifest(root)
            outputs = manifest["raw/alpha/"]["outputs"]
            self.assertIn("wiki/sources/alpha.md", outputs)
            self.assertIn("wiki/concepts/alpha.md", outputs)

            (root / "wiki" / "concepts" / "alpha.md").unlink()
            replanned = compile_manifest.plan_compile(root)

            self.assertEqual(["raw/alpha/"], [s.key for s in replanned.changed_sources])
            self.assertIn(
                "missing-output:wiki/concepts/alpha.md",
                replanned.reasons["raw/alpha/"],
            )

    def test_snapshot_wiki_outputs_tracks_expected_markdown_outputs_only(
        self,
    ) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            paths = [
                "wiki/_index.md",
                "wiki/log.md",
                "wiki/_meta/summaries.md",
                "wiki/sources/alpha.md",
                "wiki/concepts/alpha.md",
                "wiki/entities/example-tool.md",
                "wiki/comparisons/alpha-vs-beta.md",
                "wiki/assets/ignored.md",
                "wiki/sources/ignored.json",
                compile_manifest.MANIFEST_REL_PATH,
            ]
            for rel in paths:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(rel, encoding="utf-8")

            before = compile_manifest.snapshot_wiki_outputs(root)
            source_output = root / "wiki" / "sources" / "alpha.md"
            touched_ns = source_output.stat().st_mtime_ns + 1_000_000_000
            os.utime(source_output, ns=(touched_ns, touched_ns))
            after = compile_manifest.snapshot_wiki_outputs(root)

            self.assertEqual(
                {
                    "wiki/_index.md",
                    "wiki/log.md",
                    "wiki/_meta/summaries.md",
                    "wiki/sources/alpha.md",
                    "wiki/concepts/alpha.md",
                    "wiki/entities/example-tool.md",
                    "wiki/comparisons/alpha-vs-beta.md",
                },
                set(before),
            )
            self.assertEqual(
                ["wiki/sources/alpha.md"],
                compile_manifest.changed_outputs(before, after),
            )

    def test_compile_reports_missing_generate_all_before_llm_call(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command"
            ) as run_mock:
                result = llm_commands.compile_wiki(
                    _ctx(root, with_generate_all=False)
                )

            self.assertFalse(result.ok)
            self.assertIn("Missing generate_all script:", result.message)
            run_mock.assert_not_called()

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

            def fake_first(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
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

            def fake_second(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
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
                ["sha256-changed", "content-sha256-changed"],
                result.details["reasons"]["raw/beta/"],
            )

    def test_missing_output_recompiles_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
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

            def fake_llm(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
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

    def test_byte_identical_compiler_version_recompile_advances_manifest(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_initial(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_initial,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            def fake_no_change(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch("tools.compile.manifest.COMPILER_VERSION", "999.0"):
                with mock.patch(
                    "tools.kb.commands.llm_commands.run_llm_command",
                    side_effect=fake_no_change,
                ) as run_mock, mock.patch(
                    "tools.kb.commands.llm_commands.subprocess.run",
                    return_value=_successful_decoration_run(),
                ):
                    first = llm_commands.compile_wiki(_ctx(root))
                    second = llm_commands.compile_wiki(_ctx(root))

            manifest = compile_manifest.load_manifest(root)
            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertEqual("999.0", manifest["raw/alpha/"]["compiler_version"])

    def test_byte_identical_raw_blob_recompile_advances_manifest_hash(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw v1")

            def fake_initial(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_initial,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            old_manifest = compile_manifest.load_manifest(root)
            (root / "raw" / "alpha" / "raw.txt").write_bytes(b"alpha raw v2")
            expected_sha = compile_manifest.discover_raw_sources(root)[0].sha256

            def fake_no_change(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_no_change,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))
                second = llm_commands.compile_wiki(_ctx(root))

            new_manifest = compile_manifest.load_manifest(root)
            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertNotEqual(old_manifest["raw/alpha/"]["sha256"], expected_sha)
            self.assertEqual(expected_sha, new_manifest["raw/alpha/"]["sha256"])

    def test_changed_clean_without_touched_summary_stays_stale(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_initial(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_initial,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            old_manifest = compile_manifest.load_manifest(root)
            (root / "raw" / "alpha" / "clean.md").write_text(
                "# Alpha changed\n",
                encoding="utf-8",
            )
            expected_sha = compile_manifest.discover_raw_sources(root)[0].sha256

            def fake_no_change(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_no_change,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))
                second = llm_commands.compile_wiki(_ctx(root))

            new_manifest = compile_manifest.load_manifest(root)
            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(2, run_mock.call_count)
            self.assertNotEqual(old_manifest["raw/alpha/"]["sha256"], expected_sha)
            self.assertNotEqual(expected_sha, new_manifest["raw/alpha/"]["sha256"])

    def test_changed_clean_with_touched_byte_identical_summary_advances(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_initial(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_initial,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                self.assertTrue(llm_commands.compile_wiki(_ctx(root)).ok)

            (root / "raw" / "alpha" / "clean.md").write_text(
                "# Alpha changed\n",
                encoding="utf-8",
            )
            expected_sha = compile_manifest.discover_raw_sources(root)[0].sha256

            def fake_touch_same_bytes(
                _ctx,
                *,
                command,
                topic,
                prompt_builder,
                commit_label,
                **_kwargs,
            ):
                prompt_builder()
                out = root / "wiki" / "sources" / "alpha.md"
                old_text = out.read_text(encoding="utf-8")
                out.write_text(old_text, encoding="utf-8")
                touched_ns = out.stat().st_mtime_ns + 1_000_000_000
                os.utime(out, ns=(touched_ns, touched_ns))
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_touch_same_bytes,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))
                second = llm_commands.compile_wiki(_ctx(root))

            new_manifest = compile_manifest.load_manifest(root)
            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertEqual(expected_sha, new_manifest["raw/alpha/"]["sha256"])

    def test_partial_batch_outputs_do_not_advance_unwritten_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            _write_raw_v2(root, "beta", "# Beta\n", b"beta raw")

            prompts: list[str] = []

            def fake_first(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompts.append(prompt_builder())
                out = root / "wiki" / "sources" / "alpha.md"
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text("# Alpha source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_first,
            ), mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))

            manifest = compile_manifest.load_manifest(root)
            self.assertTrue(first.ok)
            self.assertIn("raw/alpha/", manifest)
            self.assertNotIn("raw/beta/", manifest)

            def fake_second(_ctx, *, command, topic, prompt_builder, commit_label, **_kwargs):
                prompts.append(prompt_builder())
                beta_out = root / "wiki" / "sources" / "beta.md"
                beta_out.write_text("# Beta source\n", encoding="utf-8")
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_second,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                second = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(second.ok)
            self.assertEqual(1, run_mock.call_count)
            self.assertIn("raw/beta/", prompts[-1])
            self.assertNotIn("raw/alpha/", prompts[-1])

    def test_empty_outputs_manifest_entry_recompiles_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            plan = compile_manifest.plan_compile(root)
            compile_manifest.save_manifest_if_changed(
                root,
                {
                    "raw/alpha/": {
                        "sha256": plan.sources[0].sha256,
                        "last_compiled": "2026-04-26T00:00:00Z",
                        "compiler_version": compile_manifest.COMPILER_VERSION,
                        "outputs": [],
                    }
                },
            )

            replanned = compile_manifest.plan_compile(root)

            self.assertEqual(["raw/alpha/"], [s.key for s in replanned.changed_sources])
            self.assertIn("missing-outputs", replanned.reasons["raw/alpha/"])

    def test_successful_compile_with_no_outputs_does_not_advance_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            def fake_empty_compile(
                _ctx,
                *,
                command,
                topic,
                prompt_builder,
                commit_label,
                **_kwargs,
            ):
                prompt_builder()
                return LLMInvocationResult(command=command, topic=topic, ok=True)

            with mock.patch(
                "tools.kb.commands.llm_commands.run_llm_command",
                side_effect=fake_empty_compile,
            ) as run_mock, mock.patch(
                "tools.kb.commands.llm_commands.subprocess.run",
                return_value=_successful_decoration_run(),
            ):
                first = llm_commands.compile_wiki(_ctx(root))
                second = llm_commands.compile_wiki(_ctx(root))

            self.assertTrue(first.ok)
            self.assertTrue(second.ok)
            self.assertEqual(2, run_mock.call_count)
            self.assertNotIn("raw/alpha/", compile_manifest.load_manifest(root))


if __name__ == "__main__":
    json_mode = "--json" in sys.argv
    if json_mode:
        sys.argv.remove("--json")

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CompileManifestTests)
    stream = io.StringIO() if json_mode else sys.stderr
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0 if json_mode else 1,
    ).run(suite)

    if json_mode:
        failed = len(result.failures) + len(result.errors)
        print(
            json.dumps(
                {
                    "total": result.testsRun,
                    "passed": result.testsRun - failed,
                    "failed": failed,
                    "ok": result.wasSuccessful(),
                }
            )
        )

    raise SystemExit(0 if result.wasSuccessful() else 1)
