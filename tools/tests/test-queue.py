#!/usr/bin/env python3
"""Offline tests for the discovery review queue.

Usage: python3 tools/tests/test-queue.py [--json]
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.kb.commands import queue as queue_cmd  # noqa: E402
from tools.kb.commands._common import CommandContext  # noqa: E402
from tools.kb.models import LLMInvocationResult  # noqa: E402
from tools.kb.workspace import Workspace  # noqa: E402
from tools.worker import queue_store  # noqa: E402


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

            with mock.patch("tools.kb.commands.queue.llm_commands.ingest") as ingest_mock:
                ingest_mock.return_value = LLMInvocationResult(
                    command="ingest",
                    ok=True,
                    exit_code=0,
                    message="ingested",
                )
                approve_result = queue_cmd.run(ctx, ["approve", item_id[:8]])

            self.assertTrue(approve_result.ok)
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
