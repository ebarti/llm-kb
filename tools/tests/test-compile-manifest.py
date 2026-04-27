#!/usr/bin/env python3
"""Tests for content-hash incremental compile manifest helpers."""

from __future__ import annotations

import io
import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.compile import manifest as compile_manifest


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


def _write_wiki_output(root: Path, rel_path: str, text: str = "# Output\n") -> None:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class CompileManifestTests(unittest.TestCase):
    def test_new_raw_source_is_planned_for_compile(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")

            plan = compile_manifest.plan_compile(root)

            self.assertEqual(["raw/alpha/"], [source.key for source in plan.sources])
            self.assertEqual(
                ["raw/alpha/"],
                [source.key for source in plan.changed_sources],
            )
            self.assertEqual(
                ["missing-manifest-entry"],
                plan.reasons["raw/alpha/"],
            )

    def test_current_manifest_makes_unchanged_source_noop(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            _write_wiki_output(root, "wiki/sources/alpha.md")
            plan = compile_manifest.plan_compile(root)

            manifest = compile_manifest.build_updated_manifest(
                plan,
                compiled_sources=plan.changed_sources,
                changed_output_paths=["wiki/sources/alpha.md"],
                available_output_paths=["wiki/sources/alpha.md"],
                compiled_at="2026-04-27T00:00:00Z",
            )
            self.assertTrue(compile_manifest.save_manifest_if_changed(root, manifest))

            replanned = compile_manifest.plan_compile(root)

            self.assertTrue(replanned.is_noop)
            self.assertEqual({}, replanned.reasons)
            self.assertEqual(manifest, compile_manifest.load_manifest(root))

    def test_missing_tracked_output_recompiles_source(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            _write_wiki_output(root, "wiki/sources/alpha.md")
            _write_wiki_output(root, "wiki/concepts/alpha.md")
            plan = compile_manifest.plan_compile(root)
            manifest = compile_manifest.build_updated_manifest(
                plan,
                compiled_sources=plan.changed_sources,
                changed_output_paths=[
                    "wiki/sources/alpha.md",
                    "wiki/concepts/alpha.md",
                ],
                available_output_paths=[
                    "wiki/sources/alpha.md",
                    "wiki/concepts/alpha.md",
                ],
                compiled_at="2026-04-27T00:00:00Z",
            )
            compile_manifest.save_manifest_if_changed(root, manifest)

            (root / "wiki" / "concepts" / "alpha.md").unlink()
            replanned = compile_manifest.plan_compile(root)

            self.assertEqual(
                ["raw/alpha/"],
                [source.key for source in replanned.changed_sources],
            )
            self.assertIn(
                "missing-output:wiki/concepts/alpha.md",
                replanned.reasons["raw/alpha/"],
            )

    def test_raw_blob_change_updates_sha256_without_content_sha_change(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw v1")
            source = compile_manifest.discover_raw_sources(root)[0]

            (root / "raw" / "alpha" / "raw.txt").write_bytes(b"alpha raw v2")
            changed = compile_manifest.discover_raw_sources(root)[0]

            self.assertNotEqual(source.sha256, changed.sha256)
            self.assertEqual(source.content_sha256, changed.content_sha256)

    def test_clean_content_change_updates_both_hashes(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            source = compile_manifest.discover_raw_sources(root)[0]

            (root / "raw" / "alpha" / "clean.md").write_text(
                "# Alpha changed\n",
                encoding="utf-8",
            )
            changed = compile_manifest.discover_raw_sources(root)[0]

            self.assertNotEqual(source.sha256, changed.sha256)
            self.assertNotEqual(source.content_sha256, changed.content_sha256)

    def test_snapshot_wiki_outputs_tracks_expected_markdown_outputs_only(self) -> None:
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
                _write_wiki_output(root, rel, rel)

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

    def test_manifest_does_not_advance_without_source_summary_output(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_raw_v2(root, "alpha", "# Alpha\n", b"alpha raw")
            plan = compile_manifest.plan_compile(root)
            manifest = compile_manifest.build_updated_manifest(
                plan,
                compiled_sources=plan.changed_sources,
                changed_output_paths=[],
                available_output_paths=[],
                compiled_at="2026-04-27T00:00:00Z",
            )

            self.assertNotIn("raw/alpha/", manifest)


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
