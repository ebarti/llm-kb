#!/usr/bin/env python3
"""Offline tests for the discovery review queue.

Usage: python3 tools/tests/test-queue.py [--json]
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
UV_BIN = os.environ.get("UV", "uv")
sys.path.insert(0, str(REPO_ROOT))

from tools.kb.commands import queue as queue_cmd  # noqa: E402
from tools.kb.commands._common import CommandContext  # noqa: E402
from tools.kb.models import LLMInvocationResult  # noqa: E402
from tools.kb.workspace import Workspace  # noqa: E402
from tools.worker import queue_store, run_hourly  # noqa: E402


def kb_command(*args: str) -> list[str]:
    return [UV_BIN, "run", "--locked", "--project", str(REPO_ROOT), "kb", *args]


def fetch_result_for(body: bytes) -> queue_store.FetchResult:
    return queue_store.FetchResult(
        content_hash=f"sha256:{hashlib.sha256(body).hexdigest()}",
        hash_source="content",
        fetch_preview={
            "ok": True,
            "status": 200,
            "content_type": "text/html",
            "bytes_read": len(body),
            "truncated": False,
            "title": "Fetched title",
            "text": body.decode("utf-8"),
            "fetched_at": "2026-04-26T00:00:00+00:00",
        },
    )


class QueueStoreTests(unittest.TestCase):
    def test_fetch_url_preview_rejects_unsafe_urls_before_opening(self) -> None:
        unsafe_urls = [
            "file:///etc/passwd",
            "ftp://example.com/feed.xml",
            "http://localhost:8000/metadata",
            "http://127.0.0.1:8000/metadata",
            "http://169.254.169.254/latest/meta-data",
        ]

        for url in unsafe_urls:
            with self.subTest(url=url):
                with mock.patch.object(queue_store._URL_OPENER, "open") as open_mock:
                    result = queue_store.fetch_url_preview(url)

                self.assertEqual("url-fallback", result.hash_source)
                self.assertFalse(result.fetch_preview["ok"])
                self.assertIn("UnsafeFetchURL", result.fetch_preview["error"])
                open_mock.assert_not_called()

    def test_fetch_url_preview_rejects_private_peer_before_reading(self) -> None:
        class FakeSocket:
            def getpeername(self) -> tuple[str, int]:
                return ("127.0.0.1", 80)

        class FakeRaw:
            _sock = FakeSocket()

        class FakeFP:
            raw = FakeRaw()

        class FakeResponse:
            fp = FakeFP()
            status = 200
            headers = {"content-type": "text/plain"}

            def __init__(self) -> None:
                self.read_called = False

            def __enter__(self) -> "FakeResponse":
                return self

            def __exit__(self, *_exc: object) -> None:
                return None

            def getcode(self) -> int:
                return 200

            def geturl(self) -> str:
                return "http://8.8.8.8/article"

            def read(self, _size: int) -> bytes:
                self.read_called = True
                return b"private response"

        response = FakeResponse()
        with mock.patch.object(queue_store._URL_OPENER, "open", return_value=response):
            result = queue_store.fetch_url_preview("http://8.8.8.8/article")

        self.assertEqual("url-fallback", result.hash_source)
        self.assertFalse(result.fetch_preview["ok"])
        self.assertIn("UnsafeFetchURL", result.fetch_preview["error"])
        self.assertFalse(response.read_called)

    def test_enqueue_writes_candidate_and_dedupes_by_content_hash(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)

            def fetcher(_url: str) -> queue_store.FetchResult:
                return fetch_result_for(b"same article body")

            result = queue_store.enqueue_discovered_sources(
                root,
                [
                    {
                        "topic": "RAG Systems",
                        "url": "https://example.com/article",
                        "title": "Primary",
                    },
                    {
                        "topic": "RAG Systems",
                        "url": "https://mirror.example/article",
                        "title": "Mirror",
                    },
                ],
                fetcher=fetcher,
                now="2026-04-26T00:00:00+00:00",
            )

            self.assertEqual(1, len(result.created))
            self.assertEqual(1, len(result.skipped))
            self.assertEqual("known_content_hash", result.skipped[0]["reason"])
            queue_files = list((root / ".queue").glob("*.json"))
            self.assertEqual(1, len(queue_files))
            payload = json.loads(queue_files[0].read_text(encoding="utf-8"))
            self.assertEqual("RAG Systems", payload["topic"])
            self.assertEqual("https://example.com/article", payload["url"])
            self.assertEqual("Primary", payload["source"]["title"])
            self.assertEqual("same article body", payload["fetch_preview"]["text"])
            self.assertTrue(payload["content_hash"].startswith("sha256:"))

    def test_rejected_items_are_archived_and_do_not_resurface(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)

            def fetcher(_url: str) -> queue_store.FetchResult:
                return fetch_result_for(b"reject me")

            first = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "Agents", "url": "https://example.com/reject"}],
                fetcher=fetcher,
            )
            item_id = first.created[0]["id"]

            archived = queue_store.archive_item(
                root,
                item_id,
                "rejected",
                metadata={"rejection_reason": "not useful"},
                now="2026-04-26T01:00:00+00:00",
            )

            self.assertEqual("rejected", archived["status"])
            self.assertEqual("not useful", archived["rejection_reason"])
            self.assertFalse((root / ".queue" / f"{item_id}.json").exists())
            self.assertTrue((root / ".queue" / ".rejected" / f"{item_id}.json").exists())

            second = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "Agents", "url": "https://other.example/same-content"}],
                fetcher=fetcher,
            )

            self.assertEqual([], second.created)
            self.assertEqual("known_content_hash", second.skipped[0]["reason"])


class QueueCommandTests(unittest.TestCase):
    def test_list_and_approve_use_existing_ingest_path_without_real_llm(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ws = Workspace(kb_home=REPO_ROOT, kb_dir=root)
            ctx = CommandContext(workspace=ws)
            enqueued = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "PKM", "url": "https://example.com/pkm", "title": "PKM"}],
                fetcher=lambda _url: fetch_result_for(b"pkm article"),
            )
            item_id = enqueued.created[0]["id"]

            list_result = queue_cmd.run(ctx, ["list"])
            self.assertTrue(list_result.ok)
            self.assertEqual(1, len(list_result.items))
            self.assertEqual(item_id, list_result.items[0].id)

            with (
                mock.patch("tools.worker.queue_store.validate_fetch_url") as validate_mock,
                mock.patch("tools.kb.commands.queue.llm_commands.ingest") as ingest_mock,
            ):
                ingest_mock.return_value = LLMInvocationResult(
                    command="ingest",
                    ok=True,
                    exit_code=0,
                    message="ingested",
                )
                approve_result = queue_cmd.run(ctx, ["approve", item_id[:8]])

            self.assertTrue(approve_result.ok)
            validate_mock.assert_called_once_with("https://example.com/pkm")
            ingest_mock.assert_called_once()
            called_ctx, called_urls = ingest_mock.call_args.args
            self.assertIs(called_ctx, ctx)
            self.assertEqual(["https://example.com/pkm"], called_urls)
            self.assertFalse((root / ".queue" / f"{item_id}.json").exists())
            approved = root / ".queue" / ".approved" / f"{item_id}.json"
            self.assertTrue(approved.exists())
            archived = json.loads(approved.read_text(encoding="utf-8"))
            self.assertEqual("approved", archived["status"])
            self.assertEqual("ingested", archived["ingest_result"]["message"])

    def test_approve_rejects_unsafe_url_before_ingest(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ws = Workspace(kb_home=REPO_ROOT, kb_dir=root)
            ctx = CommandContext(workspace=ws)
            enqueued = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "PKM", "url": "file:///etc/passwd", "title": "Local"}],
            )
            item_id = enqueued.created[0]["id"]

            with mock.patch("tools.kb.commands.queue.llm_commands.ingest") as ingest_mock:
                approve_result = queue_cmd.run(ctx, ["approve", item_id])

            self.assertFalse(approve_result.ok)
            self.assertIn("unsafe URL", approve_result.message or "")
            ingest_mock.assert_not_called()
            self.assertTrue((root / ".queue" / f"{item_id}.json").exists())

    def test_reject_command_records_reason(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ctx = CommandContext(workspace=Workspace(kb_home=REPO_ROOT, kb_dir=root))
            enqueued = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "RAG", "url": "https://example.com/nope"}],
                fetcher=lambda _url: fetch_result_for(b"nope"),
            )
            item_id = enqueued.created[0]["id"]

            result = queue_cmd.run(ctx, ["reject", item_id, "--reason", "duplicate"])

            self.assertTrue(result.ok)
            archived = root / ".queue" / ".rejected" / f"{item_id}.json"
            payload = json.loads(archived.read_text(encoding="utf-8"))
            self.assertEqual("duplicate", payload["rejection_reason"])
            self.assertEqual("rejected", payload["status"])

    def test_reject_command_combines_reason_flag_with_trailing_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ctx = CommandContext(workspace=Workspace(kb_home=REPO_ROOT, kb_dir=root))
            enqueued = queue_store.enqueue_discovered_sources(
                root,
                [{"topic": "RAG", "url": "https://example.com/nope"}],
                fetcher=lambda _url: fetch_result_for(b"nope"),
            )
            item_id = enqueued.created[0]["id"]

            result = queue_cmd.run(
                ctx,
                ["reject", item_id, "--reason", "duplicate", "low", "signal"],
            )

            self.assertTrue(result.ok)
            archived = root / ".queue" / ".rejected" / f"{item_id}.json"
            payload = json.loads(archived.read_text(encoding="utf-8"))
            self.assertEqual("duplicate low signal", payload["rejection_reason"])

    def test_named_dir_queue_list_uses_kb_workspaces(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td) / "custom-workspaces"
            workspace = base / "named"
            queue_store.enqueue_discovered_sources(
                workspace,
                [{"topic": "Queue", "url": "https://example.com/named"}],
                fetcher=lambda _url: fetch_result_for(b"named workspace article"),
            )

            env = os.environ.copy()
            env["KB_WORKSPACES"] = str(base)
            proc = subprocess.run(
                kb_command("--dir", "named", "queue", "list", "--json"),
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(0, proc.returncode, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(str(workspace.resolve() / ".queue"), payload["queue_dir"])
            self.assertEqual(1, len(payload["items"]))
            self.assertEqual("https://example.com/named", payload["items"][0]["url"])

    def test_named_dir_queue_reject_uses_kb_workspaces(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td) / "custom-workspaces"
            workspace = base / "named"
            enqueued = queue_store.enqueue_discovered_sources(
                workspace,
                [{"topic": "Queue", "url": "https://example.com/reject-named"}],
                fetcher=lambda _url: fetch_result_for(b"reject named workspace"),
            )
            item_id = enqueued.created[0]["id"]

            env = os.environ.copy()
            env["KB_WORKSPACES"] = str(base)
            proc = subprocess.run(
                kb_command(
                    "--dir",
                    "named",
                    "queue",
                    "reject",
                    item_id[:8],
                    "--reason",
                    "outside scope",
                    "--json",
                ),
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(0, proc.returncode, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(str(workspace.resolve() / ".queue"), payload["queue_dir"])
            self.assertFalse((workspace / ".queue" / f"{item_id}.json").exists())
            rejected = workspace / ".queue" / ".rejected" / f"{item_id}.json"
            self.assertTrue(rejected.exists())
            archived = json.loads(rejected.read_text(encoding="utf-8"))
            self.assertEqual("outside scope", archived["rejection_reason"])


class WorkerScriptTests(unittest.TestCase):
    def test_dry_run_discovery_does_not_write_queue_state(self) -> None:
        topics_config = {
            "max_results_per_query": 1,
            "topics": [{"name": "Dry Run", "queries": ["llm knowledge base"]}],
        }
        feeds_config = {
            "feeds": [{"name": "Dry Feed", "url": "https://feeds.example/rss"}],
            "keywords": [],
        }
        feed_xml = """<?xml version="1.0"?>
<rss><channel><item><title>Feed Item</title><link>https://example.com/feed</link><guid>feed-1</guid></item></channel></rss>
"""

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with (
                mock.patch("tools.monitor.monitor.load_topics", return_value=topics_config),
                mock.patch(
                    "tools.monitor.monitor.search_web",
                    return_value=[{"url": "https://example.com/search", "title": "Search"}],
                ),
                mock.patch("tools.monitor.rss.load_feeds_config", return_value=feeds_config),
                mock.patch("tools.monitor.rss.fetch_feed", return_value=feed_xml),
            ):
                sources = run_hourly.discover_sources(
                    root,
                    days=1,
                    topic_filter=None,
                    include_feeds=True,
                    dry_run=True,
                )
                result = queue_store.enqueue_discovered_sources(
                    root,
                    sources,
                    fetcher=lambda _url: fetch_result_for(b"dry run"),
                    dry_run=True,
                )

            self.assertEqual(2, len(sources))
            self.assertEqual(1, len(result.created))
            self.assertFalse((root / ".queue").exists())

    def test_setup_schedule_escapes_plist_template_values(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            kb_dir = root / "kb&root|with>chars"
            worker_dir = kb_dir / "tools" / "worker"
            worker_dir.mkdir(parents=True)
            (worker_dir / "run_hourly.py").write_text("#!/usr/bin/env python3\n", encoding="utf-8")

            home = root / "home"
            bin_dir = root / "bin"
            bin_dir.mkdir()
            home.mkdir()
            uname = bin_dir / "uname"
            uname.write_text("#!/usr/bin/env bash\nprintf 'Darwin\\n'\n", encoding="utf-8")
            launchctl = bin_dir / "launchctl"
            launchctl.write_text("#!/usr/bin/env bash\nexit 0\n", encoding="utf-8")
            uname.chmod(0o755)
            launchctl.chmod(0o755)

            python_bin = str(root / "python&bin|py>3")
            env = os.environ.copy()
            env["HOME"] = str(home)
            env["KB_DIR"] = str(kb_dir)
            env["PYTHON_BIN"] = python_bin
            env["PATH"] = f"{bin_dir}{os.pathsep}{env['PATH']}"

            proc = subprocess.run(
                [str(REPO_ROOT / "tools" / "worker" / "setup-schedule.sh")],
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(0, proc.returncode, proc.stderr)
            plist = home / "Library" / "LaunchAgents" / "com.llm-kb.discovery-worker.plist"
            text = plist.read_text(encoding="utf-8")
            self.assertNotIn("__KB_DIR__", text)
            self.assertIn(python_bin.replace("&", "&amp;").replace(">", "&gt;"), text)
            self.assertIn(str(kb_dir).replace("&", "&amp;").replace(">", "&gt;"), text)
            self.assertIn(
                str(worker_dir / "run_hourly.py").replace("&", "&amp;").replace(">", "&gt;"),
                text,
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    output = stream.getvalue()

    if args.json:
        print(
            json.dumps(
                {
                    "ok": result.wasSuccessful(),
                    "tests": result.testsRun,
                    "failures": len(result.failures),
                    "errors": len(result.errors),
                    "output": output,
                },
                indent=2,
            )
        )
    else:
        print(output, end="")

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
