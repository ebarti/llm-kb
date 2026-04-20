#!/usr/bin/env python3
"""
test-raw-writer.py — Unit tests for _raw_writer.py and migrate_raw_to_v2.py.

Covers:
  - write_raw() produces expected files
  - sha256_raw + sha256_clean are correct
  - Idempotency: re-running with same raw bytes is a no-op
  - Migration preserves bytes exactly (reversibility)
  - Migration handles files with and without frontmatter

Usage:
    python3 tools/tests/test-raw-writer.py
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def _load(name: str, relpath: str):
    spec = importlib.util.spec_from_file_location(name, BASE_DIR / relpath)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


raw_writer = _load("_raw_writer", "tools/ingest/_raw_writer.py")
migrate = _load("migrate_raw_to_v2", "tools/ingest/migrate_raw_to_v2.py")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class TestRawWriter(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        (self.base / "raw").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def test_write_raw_basic(self):
        raw_bytes = b"<html>hello</html>"
        result = raw_writer.write_raw(
            base_dir=self.base,
            slug="example",
            url="https://example.com",
            fetcher="web",
            clean_content="# hello\n\nThis is clean content.",
            raw_bytes=raw_bytes,
            raw_ext="html",
            content_type="html",
        )
        self.assertEqual(result["status"], "wrote")

        d = self.base / "raw" / "example"
        self.assertTrue((d / "raw.html").exists())
        self.assertTrue((d / "clean.md").exists())
        self.assertTrue((d / "meta.json").exists())

        meta = json.loads((d / "meta.json").read_text())
        self.assertEqual(meta["sha256_raw"], _sha(raw_bytes))
        self.assertEqual(
            meta["sha256_clean"],
            _sha(b"# hello\n\nThis is clean content."),
        )
        self.assertTrue(meta["raw_bytes_available"])
        self.assertFalse(meta["migrated_legacy"])
        self.assertEqual(meta["fetcher"], "web")
        self.assertEqual(meta["slug"], "example")
        self.assertEqual(meta["url"], "https://example.com")

    def test_idempotent_on_hash_match(self):
        raw_bytes = b"same bytes"
        clean = "# same clean"

        result1 = raw_writer.write_raw(
            base_dir=self.base,
            slug="idem",
            url="https://example.com",
            fetcher="web",
            clean_content=clean,
            raw_bytes=raw_bytes,
            raw_ext="txt",
        )
        self.assertEqual(result1["status"], "wrote")
        first_fetched_at = result1["meta"]["fetched_at"]

        # Re-run with same raw bytes -> no-op
        result2 = raw_writer.write_raw(
            base_dir=self.base,
            slug="idem",
            url="https://example.com",
            fetcher="web",
            clean_content=clean,
            raw_bytes=raw_bytes,
            raw_ext="txt",
        )
        self.assertEqual(result2["status"], "skipped_hash_match")
        # meta unchanged
        on_disk = json.loads((self.base / "raw" / "idem" / "meta.json").read_text())
        self.assertEqual(on_disk["fetched_at"], first_fetched_at)

    def test_rewrite_on_hash_change(self):
        raw_writer.write_raw(
            base_dir=self.base,
            slug="change",
            url="https://example.com",
            fetcher="web",
            clean_content="v1",
            raw_bytes=b"v1-raw",
            raw_ext="txt",
        )
        result = raw_writer.write_raw(
            base_dir=self.base,
            slug="change",
            url="https://example.com",
            fetcher="web",
            clean_content="v2",
            raw_bytes=b"v2-raw",
            raw_ext="txt",
        )
        self.assertEqual(result["status"], "wrote")
        clean = (self.base / "raw" / "change" / "clean.md").read_text()
        self.assertEqual(clean, "v2")

    def test_no_raw_bytes(self):
        result = raw_writer.write_raw(
            base_dir=self.base,
            slug="noraw",
            url="https://example.com",
            fetcher="web",
            clean_content="hi",
        )
        self.assertEqual(result["status"], "wrote")
        d = self.base / "raw" / "noraw"
        self.assertFalse(list(d.glob("raw.*")))
        meta = json.loads((d / "meta.json").read_text())
        self.assertIsNone(meta["sha256_raw"])
        self.assertFalse(meta["raw_bytes_available"])

    def test_idempotent_without_raw_bytes_on_clean_hash(self):
        result1 = raw_writer.write_raw(
            base_dir=self.base,
            slug="noraw-idem",
            url="https://example.com",
            fetcher="web",
            clean_content="same clean",
        )
        self.assertEqual(result1["status"], "wrote")
        first_fetched_at = result1["meta"]["fetched_at"]

        result2 = raw_writer.write_raw(
            base_dir=self.base,
            slug="noraw-idem",
            url="https://example.com",
            fetcher="web",
            clean_content="same clean",
        )
        self.assertEqual(result2["status"], "skipped_hash_match")

        on_disk = json.loads((self.base / "raw" / "noraw-idem" / "meta.json").read_text())
        self.assertEqual(on_disk["fetched_at"], first_fetched_at)

    def test_rewrite_without_raw_bytes_preserves_prior_raw(self):
        """Raw-less rewrite must preserve the prior raw.* file and its
        metadata (sha256_raw, size_bytes_raw, raw_extension,
        raw_bytes_available=true) so a retry that only carries updated clean
        content never silently drops raw bytes we captured earlier."""
        raw_bytes = b"<html>old</html>"
        first = raw_writer.write_raw(
            base_dir=self.base,
            slug="preserve",
            url="https://example.com",
            fetcher="web",
            clean_content="v1",
            raw_bytes=raw_bytes,
            raw_ext="html",
        )
        self.assertEqual(first["status"], "wrote")
        d = self.base / "raw" / "preserve"
        self.assertTrue((d / "raw.html").exists())
        prior_sha = first["meta"]["sha256_raw"]
        prior_size = first["meta"]["size_bytes_raw"]

        # Rewrite with no raw bytes and different clean content.
        second = raw_writer.write_raw(
            base_dir=self.base,
            slug="preserve",
            url="https://example.com",
            fetcher="web",
            clean_content="v2 different",
        )
        self.assertEqual(second["status"], "wrote")

        # The raw.html must survive the raw-less rewrite.
        self.assertTrue((d / "raw.html").exists(), "prior raw.html should be preserved")
        self.assertEqual((d / "raw.html").read_bytes(), raw_bytes)

        meta = json.loads((d / "meta.json").read_text())
        self.assertTrue(meta["raw_bytes_available"])
        self.assertEqual(meta["sha256_raw"], prior_sha)
        self.assertEqual(meta["size_bytes_raw"], prior_size)
        self.assertEqual(meta["raw_extension"], "html")
        # Clean content did change.
        self.assertEqual((d / "clean.md").read_bytes(), b"v2 different")
        self.assertEqual(meta["sha256_clean"], _sha(b"v2 different"))

    def test_rewrite_without_raw_bytes_no_prior_raw_stays_false(self):
        """If there is no prior raw blob, a raw-less rewrite leaves the
        bundle with raw_bytes_available=false and no raw.* files (state must
        match what meta.json claims)."""
        raw_writer.write_raw(
            base_dir=self.base,
            slug="noprior",
            url="https://example.com",
            fetcher="web",
            clean_content="v1",
        )
        d = self.base / "raw" / "noprior"
        self.assertFalse(list(d.glob("raw.*")))

        raw_writer.write_raw(
            base_dir=self.base,
            slug="noprior",
            url="https://example.com",
            fetcher="web",
            clean_content="v2 different",
        )
        self.assertFalse(list(d.glob("raw.*")))
        meta = json.loads((d / "meta.json").read_text())
        self.assertFalse(meta["raw_bytes_available"])
        self.assertIsNone(meta["sha256_raw"])

    def test_rewrite_replaces_raw_with_new_extension(self):
        """A subsequent raw write with a different extension must purge the
        prior raw.* so only one canonical raw blob lives in the bundle."""
        raw_writer.write_raw(
            base_dir=self.base,
            slug="ext",
            url="https://example.com",
            fetcher="web",
            clean_content="v1",
            raw_bytes=b"<html/>",
            raw_ext="html",
        )
        raw_writer.write_raw(
            base_dir=self.base,
            slug="ext",
            url="https://example.com",
            fetcher="pdf",
            clean_content="v2",
            raw_bytes=b"%PDF-1.4",
            raw_ext="pdf",
        )
        d = self.base / "raw" / "ext"
        remaining = sorted(p.name for p in d.glob("raw.*"))
        self.assertEqual(remaining, ["raw.pdf"])

    def test_sha256_matches_file_contents(self):
        raw_bytes = b"\x00\x01\x02binary\xffbytes"
        raw_writer.write_raw(
            base_dir=self.base,
            slug="binary",
            url="x",
            fetcher="pdf",
            clean_content="clean",
            raw_bytes=raw_bytes,
            raw_ext="pdf",
        )
        d = self.base / "raw" / "binary"
        meta = json.loads((d / "meta.json").read_text())
        # Reading raw.pdf back yields the same sha256
        actual = hashlib.sha256((d / "raw.pdf").read_bytes()).hexdigest()
        self.assertEqual(meta["sha256_raw"], actual)
        self.assertEqual(meta["sha256_raw"], _sha(raw_bytes))


class TestMigration(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        (self.base / "raw").mkdir()
        # Monkey-patch migrate module's RAW_DIR/BASE_DIR for isolation
        self._saved_raw_dir = migrate.RAW_DIR
        self._saved_base_dir = migrate.BASE_DIR
        migrate.BASE_DIR = self.base
        migrate.RAW_DIR = self.base / "raw"

    def tearDown(self):
        migrate.RAW_DIR = self._saved_raw_dir
        migrate.BASE_DIR = self._saved_base_dir
        self._tmp.cleanup()

    def _write_flat(self, name: str, content: str) -> Path:
        p = self.base / "raw" / f"{name}.md"
        p.write_text(content, encoding="utf-8")
        return p

    def test_migrate_simple(self):
        flat = self._write_flat(
            "sample",
            "---\ntitle: Sample\nsource: https://x/y\ntype: article\ndate_ingested: 2026-01-05\n---\n\nBody text.\n",
        )
        result = migrate.migrate_one(flat, dry_run=False)
        self.assertEqual(result["status"], "migrated")

        d = self.base / "raw" / "sample"
        self.assertTrue((d / "clean.md").exists())
        self.assertTrue((d / "meta.json").exists())
        self.assertFalse((d / "raw.md").exists())

        # clean.md is byte-identical to flat source (reversibility)
        self.assertEqual(
            (d / "clean.md").read_bytes(),
            flat.read_bytes(),
        )

        meta = json.loads((d / "meta.json").read_text())
        self.assertTrue(meta["migrated_legacy"])
        self.assertFalse(meta["raw_bytes_available"])
        self.assertIsNone(meta["sha256_raw"])
        self.assertEqual(meta["url"], "https://x/y")
        self.assertEqual(meta["fetcher"], "web")
        # sha256_clean matches
        self.assertEqual(meta["sha256_clean"], _sha(flat.read_bytes()))
        self.assertEqual(meta["fetched_at"], "2026-01-05T00:00:00Z")

    def test_migrate_infers_fetcher_from_prefix(self):
        pairs = [
            ("yt-foo", "youtube"),
            ("arxiv-bar", "arxiv"),
            ("gh-baz", "github"),
            ("pdf-qux", "pdf"),
            ("tweet-abc", "tweet"),
            ("clip-def", "clippings"),
            ("random-slug", "web"),
        ]
        for stem, expected in pairs:
            flat = self._write_flat(stem, "---\ntitle: t\n---\n\nbody")
            result = migrate.migrate_one(flat, dry_run=False)
            self.assertEqual(result["status"], "migrated", stem)
            meta = json.loads((self.base / "raw" / stem / "meta.json").read_text())
            self.assertEqual(meta["fetcher"], expected, f"{stem} → {meta['fetcher']}")

    def test_migrate_idempotent(self):
        flat = self._write_flat("twice", "---\ntitle: t\n---\n\nbody")
        migrate.migrate_one(flat, dry_run=False)
        result = migrate.migrate_one(flat, dry_run=False)
        self.assertEqual(result["status"], "already_migrated")

    def test_migrate_handles_no_frontmatter(self):
        flat = self._write_flat("plain", "just a body, no frontmatter\n")
        result = migrate.migrate_one(flat, dry_run=False)
        self.assertEqual(result["status"], "migrated")
        meta = json.loads((self.base / "raw" / "plain" / "meta.json").read_text())
        self.assertEqual(meta["url"], "")
        self.assertEqual(meta["fetcher"], "web")

    def test_sha256_reversibility(self):
        """Migration is reversible: clean.md bytes == original flat file bytes."""
        content = "---\ntitle: x\n---\n\n" + "line\n" * 500
        flat = self._write_flat("rev", content)
        original_sha = _sha(flat.read_bytes())
        migrate.migrate_one(flat, dry_run=False)
        new_sha = _sha((self.base / "raw" / "rev" / "clean.md").read_bytes())
        self.assertEqual(original_sha, new_sha)

    def test_conflict_skips_live_v2_bundle(self):
        """If raw/<slug>/ already holds a v2 bundle (fresh ingest) and the
        legacy flat raw/<slug>.md is still around, the migrator must NOT
        overwrite the live v2 content. It must return a 'conflict' status
        and leave both files untouched."""
        # Simulate a fresh v2 ingest at raw/live/.
        live_dir = self.base / "raw" / "live"
        live_dir.mkdir()
        (live_dir / "clean.md").write_text("fresh v2 clean", encoding="utf-8")
        (live_dir / "raw.html").write_bytes(b"<html>fresh</html>")
        live_meta = {
            "slug": "live",
            "url": "https://fresh/v2",
            "fetched_at": "2026-04-19T00:00:00Z",
            "fetcher": "web",
            "fetcher_version": "v2.0.0",
            "content_type": "html",
            "sha256_raw": _sha(b"<html>fresh</html>"),
            "sha256_clean": _sha(b"fresh v2 clean"),
            "size_bytes_raw": len(b"<html>fresh</html>"),
            "size_bytes_clean": len(b"fresh v2 clean"),
            "raw_bytes_available": True,
            "raw_extension": "html",
            "migrated_legacy": False,
        }
        (live_dir / "meta.json").write_text(
            json.dumps(live_meta, indent=2) + "\n", encoding="utf-8"
        )

        # A stale flat file with DIFFERENT content lingers.
        flat = self._write_flat("live", "---\ntitle: old\n---\n\nstale legacy body\n")

        result = migrate.migrate_one(flat, dry_run=False)
        self.assertEqual(result["status"], "conflict")
        self.assertIn("refusing to overwrite", result["error"])

        # Live v2 content is untouched.
        self.assertEqual(
            (live_dir / "clean.md").read_text(encoding="utf-8"), "fresh v2 clean"
        )
        on_disk_meta = json.loads((live_dir / "meta.json").read_text())
        self.assertEqual(on_disk_meta["url"], "https://fresh/v2")
        self.assertFalse(on_disk_meta["migrated_legacy"])
        # Legacy flat file is still present for operator review.
        self.assertTrue(flat.exists())


def _main() -> int:
    # run-all.sh invokes child tests with --json; unittest.main() doesn't know
    # that flag, so strip it here and emit a tiny JSON summary after the run.
    json_mode = False
    argv = [sys.argv[0]]
    for a in sys.argv[1:]:
        if a == "--json":
            json_mode = True
        else:
            argv.append(a)

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=0 if json_mode else 2, stream=sys.stderr)
    result = runner.run(suite)

    if json_mode:
        print(json.dumps({
            "ok": result.wasSuccessful(),
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
        }, indent=2))

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(_main())
