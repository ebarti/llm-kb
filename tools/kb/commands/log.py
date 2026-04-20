"""``kb log`` — return the last N entries from ``wiki/log.md``."""

from __future__ import annotations

from ..models import EXIT_ERROR, EXIT_SUCCESS, LogResult
from ._common import CommandContext


def run(ctx: CommandContext, n: int | None = 10, all_entries: bool = False) -> LogResult:
    log_path = ctx.workspace.log_path
    if not log_path.exists():
        return LogResult(
            command="log",
            ok=False,
            exit_code=EXIT_ERROR,
            message=f"No log file found at {log_path}",
            log_path=str(log_path),
        )

    text = log_path.read_text(encoding="utf-8")
    # Split on entry headers: each entry starts with "## ["
    lines = text.splitlines()
    entries: list[list[str]] = []
    current: list[str] | None = None
    for line in lines:
        if line.startswith("## ["):
            if current is not None:
                entries.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        entries.append(current)

    if all_entries:
        selected = entries
    else:
        count = max(1, n or 10)
        selected = entries[-count:] if entries else []

    rendered = ["\n".join(entry).strip() for entry in selected]
    return LogResult(
        command="log",
        ok=True,
        exit_code=EXIT_SUCCESS,
        entries=rendered,
        log_path=str(log_path),
    )
