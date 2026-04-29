"""``kb queue`` — review and promote discovered source candidates."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Sequence

from kb.models import (
    EXIT_ERROR,
    EXIT_SUCCESS,
    QueueItemSummary,
    QueueResult,
)
from kb.commands import llm_commands
from kb.commands._common import CommandContext


def run(ctx: CommandContext, args: Sequence[str]) -> QueueResult:
    parser = argparse.ArgumentParser(prog="kb queue")
    sub = parser.add_subparsers(dest="action", required=True)

    sub.add_parser("list", help="list pending discovery candidates")

    approve = sub.add_parser("approve", help="promote a candidate through kb ingest")
    approve.add_argument("id", help="queue item id or unique prefix")

    reject = sub.add_parser("reject", help="archive a candidate so it will not resurface")
    reject.add_argument("id", help="queue item id or unique prefix")
    reject.add_argument("reason", nargs="*", help="optional rejection reason")
    reject.add_argument("--reason", dest="reason_flag", help="optional rejection reason")

    ns = parser.parse_args(list(args))
    if ns.action == "list":
        return _list(ctx)
    if ns.action == "approve":
        return _approve(ctx, ns.id)
    if ns.action == "reject":
        reason = _rejection_reason(ns)
        return _reject(ctx, ns.id, reason=reason)
    return QueueResult(
        command="queue",
        action=str(ns.action),
        ok=False,
        exit_code=EXIT_ERROR,
        message=f"unknown queue action: {ns.action}",
        queue_dir=_queue_dir(ctx),
    )


def _list(ctx: CommandContext) -> QueueResult:
    store = _store()
    items = [_summary(item) for item in store.list_pending_items(ctx.workspace.kb_dir)]
    return QueueResult(
        command="queue",
        action="list",
        ok=True,
        exit_code=EXIT_SUCCESS,
        queue_dir=_queue_dir(ctx),
        items=items,
        message=f"{len(items)} queued candidate(s)",
    )


def _approve(ctx: CommandContext, item_id: str) -> QueueResult:
    store = _store()
    try:
        item = store.read_pending_item(ctx.workspace.kb_dir, item_id)
    except store.QueueError as exc:
        return _queue_error("approve", exc, ctx)

    summary = _summary(item)
    if not summary.url:
        return QueueResult(
            command="queue",
            action="approve",
            ok=False,
            exit_code=EXIT_ERROR,
            queue_dir=_queue_dir(ctx),
            item=summary,
            message=f"queue item has no URL: {summary.id}",
        )

    try:
        store.validate_fetch_url(summary.url)
    except store.UnsafeFetchURL as exc:
        return QueueResult(
            command="queue",
            action="approve",
            ok=False,
            exit_code=EXIT_ERROR,
            queue_dir=_queue_dir(ctx),
            item=summary,
            message=f"queue item has unsafe URL: {exc}",
        )

    if ctx.dry_run:
        return QueueResult(
            command="queue",
            action="approve",
            ok=True,
            exit_code=EXIT_SUCCESS,
            dry_run=True,
            queue_dir=_queue_dir(ctx),
            item=summary,
            message=f"[dry-run] would ingest {summary.url}",
        )

    ingest_result = llm_commands.ingest(ctx, [summary.url])
    if not ingest_result.ok:
        return QueueResult(
            command="queue",
            action="approve",
            ok=False,
            exit_code=ingest_result.exit_code,
            queue_dir=_queue_dir(ctx),
            item=summary,
            message=f"ingest failed for {summary.id}: {ingest_result.message or ''}".strip(),
            details={"ingest_result": _model_dump(ingest_result)},
        )

    archived = store.archive_item(
        ctx.workspace.kb_dir,
        summary.id,
        "approved",
        metadata={"ingest_result": _model_dump(ingest_result)},
    )
    archived_summary = _summary(archived)
    return QueueResult(
        command="queue",
        action="approve",
        ok=True,
        exit_code=EXIT_SUCCESS,
        queue_dir=_queue_dir(ctx),
        item=archived_summary,
        message=f"approved {archived_summary.id}; ingested {archived_summary.url}",
        details={"ingest_result": _model_dump(ingest_result)},
    )


def _reject(ctx: CommandContext, item_id: str, *, reason: str) -> QueueResult:
    store = _store()
    try:
        item = store.read_pending_item(ctx.workspace.kb_dir, item_id)
    except store.QueueError as exc:
        return _queue_error("reject", exc, ctx)

    summary = _summary(item)
    if ctx.dry_run:
        return QueueResult(
            command="queue",
            action="reject",
            ok=True,
            exit_code=EXIT_SUCCESS,
            dry_run=True,
            queue_dir=_queue_dir(ctx),
            item=summary,
            message=f"[dry-run] would reject {summary.id}: {reason}",
        )

    archived = store.archive_item(
        ctx.workspace.kb_dir,
        summary.id,
        "rejected",
        metadata={"rejection_reason": reason},
    )
    archived_summary = _summary(archived)
    return QueueResult(
        command="queue",
        action="reject",
        ok=True,
        exit_code=EXIT_SUCCESS,
        queue_dir=_queue_dir(ctx),
        item=archived_summary,
        message=f"rejected {archived_summary.id}: {reason}",
    )


def _rejection_reason(ns: argparse.Namespace) -> str:
    parts: list[str] = []
    if ns.reason_flag:
        parts.append(str(ns.reason_flag))
    parts.extend(str(part) for part in ns.reason)
    return " ".join(part.strip() for part in parts if part.strip()) or "rejected by user"


def _queue_error(action: str, exc: Exception, ctx: CommandContext) -> QueueResult:
    return QueueResult(
        command="queue",
        action=action,
        ok=False,
        exit_code=EXIT_ERROR,
        queue_dir=_queue_dir(ctx),
        message=str(exc),
    )


def _summary(item: dict[str, Any]) -> QueueItemSummary:
    source = item.get("source") if isinstance(item.get("source"), dict) else {}
    preview = (
        item.get("fetch_preview") if isinstance(item.get("fetch_preview"), dict) else {}
    )
    return QueueItemSummary(
        id=str(item.get("id", "")),
        status=str(item.get("status", "pending")),
        topic=_optional_str(item.get("topic") or source.get("topic") or source.get("feed")),
        title=_optional_str(item.get("title") or source.get("title") or preview.get("title")),
        url=_optional_str(item.get("url") or source.get("url")),
        content_hash=_optional_str(item.get("content_hash")),
        created_at=_optional_str(item.get("created_at")),
        preview=_optional_str(preview.get("text")),
    )


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value)
    return text if text else None


def _model_dump(value: Any) -> dict[str, Any]:
    if hasattr(value, "model_dump"):
        return value.model_dump()
    if hasattr(value, "dict"):
        return value.dict()
    return dict(value)


def _queue_dir(ctx: CommandContext) -> str:
    return str(Path(ctx.workspace.kb_dir) / ".queue")


def _store() -> Any:
    from kb import queue_store

    return queue_store
