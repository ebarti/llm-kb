"""Timestamped CLI events and per-run output logs."""

from __future__ import annotations

import datetime as _dt
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO


_CURRENT: "RunLogger | None" = None


def _timestamp() -> str:
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def _filename_timestamp() -> str:
    return _dt.datetime.now(tz=_dt.UTC).strftime("%Y%m%dT%H%M%S%fZ")


def _slug(text: str, *, fallback: str = "run", max_len: int = 60) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())
    value = "-".join(words).strip("-")
    if not value:
        return fallback
    return value[:max_len].strip("-") or fallback


class _TeeStream:
    def __init__(self, stream: TextIO, log_file: TextIO) -> None:
        self._stream = stream
        self._log_file = log_file

    def write(self, data: str) -> int:
        written = self._stream.write(data)
        self._log_file.write(data)
        return written

    def flush(self) -> None:
        self._stream.flush()
        self._log_file.flush()

    def isatty(self) -> bool:
        isatty = getattr(self._stream, "isatty", None)
        return bool(isatty and isatty())

    @property
    def encoding(self) -> str | None:
        return getattr(self._stream, "encoding", None)


@dataclass
class RunLogger:
    path: Path
    command: str
    workspace: Path
    json_output: bool
    _log_file: TextIO
    _stdout: TextIO
    _stderr: TextIO

    def emit(self, component: str, message: str = "", *, visible: bool = True) -> None:
        line = _format_event(component, message)
        if visible and not self.json_output:
            print(line, file=sys.stderr)
        else:
            self._log_file.write(line + "\n")
            self._log_file.flush()

    def close(self) -> None:
        sys.stdout = self._stdout
        sys.stderr = self._stderr
        self._log_file.flush()
        self._log_file.close()


def start_run_log(
    workspace: Path,
    *,
    command: str,
    topic: str | None = None,
    json_output: bool = False,
    dry_run: bool = False,
) -> Path | None:
    """Start tee logging for one CLI invocation.

    Dry-runs remain side-effect-free, so they do not create log files.
    """
    global _CURRENT
    if dry_run or os.environ.get("KB_RUN_LOG", "").strip().lower() in {
        "0",
        "false",
        "no",
        "off",
    }:
        return None

    stop_run_log()

    log_root = os.environ.get("KB_LOG_DIR")
    log_dir = Path(log_root).expanduser() if log_root else workspace / "output" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    topic_slug = _slug(topic or command)
    path = log_dir / f"{_filename_timestamp()}-{_slug(command)}-{topic_slug}.log"
    log_file = path.open("a", encoding="utf-8")
    log_file.write(
        f"# kb run log\n"
        f"started={_timestamp()}\n"
        f"command={command}\n"
        f"topic={topic or ''}\n"
        f"workspace={workspace}\n\n"
    )
    log_file.flush()

    logger = RunLogger(
        path=path,
        command=command,
        workspace=workspace,
        json_output=json_output,
        _log_file=log_file,
        _stdout=sys.stdout,
        _stderr=sys.stderr,
    )
    sys.stdout = _TeeStream(sys.stdout, log_file)  # type: ignore[assignment]
    sys.stderr = _TeeStream(sys.stderr, log_file)  # type: ignore[assignment]
    _CURRENT = logger
    return path


def stop_run_log() -> None:
    global _CURRENT
    if _CURRENT is None:
        return
    logger = _CURRENT
    _CURRENT = None
    logger.close()


def current_log_path() -> Path | None:
    return _CURRENT.path if _CURRENT is not None else None


def event(component: str, message: str = "", *, visible: bool = True) -> None:
    logger = _CURRENT
    if logger is not None:
        logger.emit(component, message, visible=visible)
        return
    if visible:
        print(_format_event(component, message), file=sys.stderr)


def _format_event(component: str, message: str) -> str:
    suffix = f" | {message}" if message else ""
    return f"[{_timestamp()}] [kb] {component}{suffix}"
