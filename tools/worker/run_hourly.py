#!/usr/bin/env python3
"""Hourly discovery worker that fills the human-review queue."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.kb.workspace import Workspace  # noqa: E402
from tools.worker.queue_store import enqueue_discovered_sources  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Discover new URLs and write review candidates to .queue/"
    )
    parser.add_argument(
        "--kb-dir",
        default=os.environ.get("KB_DIR"),
        help="workspace directory; defaults to KB_DIR or the install directory",
    )
    parser.add_argument("--days", type=int, default=1, help="discovery lookback window")
    parser.add_argument("--topic", help="only discover a matching monitor topic")
    parser.add_argument(
        "--include-feeds",
        action="store_true",
        help="also check RSS feeds configured under tools/monitor/feeds.json",
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="read discovered source JSON from a file instead of calling monitor code",
    )
    parser.add_argument("--limit", type=int, help="maximum new candidates to write")
    parser.add_argument("--dry-run", action="store_true", help="discover and dedupe without writing")
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    args = parser.parse_args(argv)

    workspace = Workspace.resolve(
        kb_home=REPO_ROOT,
        kb_dir=args.kb_dir,
        dry_run=args.dry_run,
    )

    if args.input:
        discovered = load_discovered_json(args.input)
    else:
        discovered = discover_sources(
            workspace.kb_dir,
            days=args.days,
            topic_filter=args.topic,
            include_feeds=args.include_feeds,
        )

    result = enqueue_discovered_sources(
        workspace.kb_dir,
        discovered,
        limit=args.limit,
        dry_run=args.dry_run,
    )

    payload = {
        "ok": True,
        "queue_dir": str(result.queue_dir),
        "discovered": len(discovered),
        "created": len(result.created),
        "skipped": len(result.skipped),
        "created_items": result.created,
        "skipped_items": result.skipped,
        "dry_run": args.dry_run,
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(
            f"Discovery queue: discovered={payload['discovered']} "
            f"created={payload['created']} skipped={payload['skipped']}"
        )
        print(f"Queue: {result.queue_dir}")
        for item in result.created:
            print(f"  + {item['id']} {item.get('topic', 'discovery')}: {item['url']}")
        for item in result.skipped:
            url = item.get("url") or (item.get("source") or {}).get("url") or ""
            print(f"  - skipped {url} ({item.get('reason', 'unknown')})")
    return 0


def load_discovered_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in ("sources", "items", "created_items"):
            value = data.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
    raise SystemExit(f"{path} must contain a list of discovered source objects")


def discover_sources(
    kb_dir: Path,
    *,
    days: int,
    topic_filter: str | None,
    include_feeds: bool,
) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []

    monitor = importlib.import_module("tools.monitor.monitor")
    _retarget_monitor_module(monitor, kb_dir)
    topics_config = monitor.load_topics()
    for source in monitor.discover_new_sources(
        topics_config,
        days_back=days,
        topic_filter=topic_filter,
    ):
        sources.append({**source, "source_type": "web_search"})

    if include_feeds:
        rss = importlib.import_module("tools.monitor.rss")
        _retarget_rss_module(rss, kb_dir)
        feeds_config = rss.load_feeds_config()
        for feed_result in rss.check_feeds(feeds_config, since_days=days):
            feed = feed_result.get("feed", "RSS")
            for entry in feed_result.get("entries", []):
                if not entry.get("url"):
                    continue
                sources.append(
                    {
                        "topic": feed,
                        "feed": feed,
                        "url": entry.get("url"),
                        "title": entry.get("title", ""),
                        "date": entry.get("date"),
                        "summary": entry.get("summary", ""),
                        "relevant": entry.get("relevant", True),
                        "source_type": "rss",
                    }
                )

    return sources


def _retarget_monitor_module(module: Any, kb_dir: Path) -> None:
    module.KB_DIR = kb_dir
    module.MANIFEST_FILE = kb_dir / "wiki" / "_meta" / "manifest.md"
    module.STATE_FILE = kb_dir / ".queue" / ".state" / "monitor_state.json"
    module.LOG_DIR = kb_dir / ".queue" / ".logs"


def _retarget_rss_module(module: Any, kb_dir: Path) -> None:
    module.KB_DIR = kb_dir
    module.STATE_DIR = kb_dir / ".queue" / ".state"
    module.LOG_DIR = kb_dir / ".queue" / ".logs"


if __name__ == "__main__":
    raise SystemExit(main())
