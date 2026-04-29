"""``kb search`` — full-text search delegating to qmd / search.sh / grep."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from kb.models import EXIT_ERROR, EXIT_NOOP, EXIT_SUCCESS, SearchHit, SearchResult
from kb.commands._common import CommandContext


def run(ctx: CommandContext, query: str, top_k: int = 10) -> SearchResult:
    query = (query or "").strip()
    if not query:
        return SearchResult(
            command="search",
            query=query,
            ok=False,
            exit_code=EXIT_NOOP,
            message="Empty query",
        )

    ws = ctx.workspace
    # Prefer qmd if available
    qmd_path = ws.kb_dir / "tools" / "search-engine" / "qmd"
    if qmd_path.exists() and qmd_path.is_file():
        return _run_qmd(ctx, query, top_k, qmd_path)

    # Fallback: search.sh
    legacy = ws.kb_dir / "tools" / "search.sh"
    if legacy.exists() and legacy.is_file():
        proc = subprocess.run(
            ["bash", str(legacy), query],
            capture_output=True, text=True, check=False,
            cwd=str(ws.kb_dir),
        )
        return SearchResult(
            command="search",
            query=query,
            ok=proc.returncode == 0,
            exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
            backend="search.sh",
            message=proc.stdout + proc.stderr,
        )

    # Final fallback: grep
    return _run_grep(ctx, query, top_k)


def _run_qmd(ctx: CommandContext, query: str, top_k: int, qmd_path: Path) -> SearchResult:
    cmd = [str(qmd_path), query, "--top", str(top_k)]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, check=False, cwd=str(ctx.workspace.kb_dir)
    )
    if proc.returncode != 0:
        return SearchResult(
            command="search",
            query=query,
            ok=False,
            exit_code=EXIT_ERROR,
            backend="qmd",
            message=proc.stderr or proc.stdout,
        )

    hits = _parse_qmd(proc.stdout, top_k)
    # Put qmd's raw stdout in ``details["raw_output"]`` (debug channel)
    # rather than ``message``. The ``hits`` list is the structured output;
    # leaking unstructured stdout through ``message`` in --json mode
    # contradicts the PR's structured-JSON contract. The CLI renderer
    # prints ``hits`` when present, and falls back to ``message`` only
    # when hits are empty, so the fallback path still works.
    if hits:
        return SearchResult(
            command="search",
            query=query,
            ok=True,
            exit_code=EXIT_SUCCESS,
            backend="qmd",
            hits=hits,
            details={"raw_output": proc.stdout},
        )
    # No parseable hits — keep raw qmd output visible for fallback rendering.
    return SearchResult(
        command="search",
        query=query,
        ok=True,
        exit_code=EXIT_SUCCESS,
        backend="qmd",
        hits=[],
        message=proc.stdout if not ctx.json_output else None,
        details={"raw_output": proc.stdout} if ctx.json_output else {},
    )


def _parse_qmd(output: str, top_k: int) -> list[SearchHit]:
    """Best-effort parser for qmd's LLM-optimised text output.

    qmd prints blocks like::

        1. **Document Title** [concept] score=3.14
           snippet snippet snippet
           file: concepts/document-title.md
    """
    hits: list[SearchHit] = []
    header_re = re.compile(
        r"^\s*(?P<idx>\d+)\.\s+\*\*(?P<title>.+?)\*\*"
        r"(?:\s+\[(?P<doc_type>[^\]]+)\])?"
        r"(?:\s+score=(?P<score>[\d\.]+))?\s*$"
    )
    file_re = re.compile(r"^\s*file:\s*(?P<path>\S.+?)\s*$")
    current: SearchHit | None = None

    def _flush(hit: SearchHit | None) -> None:
        if hit is not None and hit.path:
            hits.append(hit)

    for line in output.splitlines():
        header = header_re.match(line)
        if header:
            _flush(current)
            score = header.group("score")
            current = SearchHit(
                path="",
                title=header.group("title"),
                score=float(score) if score else None,
            )
            continue

        if current is None:
            continue

        file_match = file_re.match(line)
        if file_match:
            current.path = file_match.group("path").strip()
            continue

        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("backlinks:"):
            continue
        if current.snippet is None:
            current.snippet = stripped

    _flush(current)
    return hits[:top_k]


def _run_grep(ctx: CommandContext, query: str, top_k: int) -> SearchResult:
    ws = ctx.workspace
    hits: list[SearchHit] = []
    for root in (ws.wiki_dir, ws.raw_dir):
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if query.lower() in text.lower():
                snippet = _first_match_snippet(text, query)
                hits.append(
                    SearchHit(
                        path=str(p.relative_to(ws.kb_dir)),
                        snippet=snippet,
                    )
                )
                if len(hits) >= top_k:
                    break
        if len(hits) >= top_k:
            break
    return SearchResult(
        command="search",
        query=query,
        ok=True,
        exit_code=EXIT_SUCCESS,
        backend="grep",
        hits=hits,
    )


def _first_match_snippet(text: str, query: str, window: int = 120) -> str | None:
    idx = text.lower().find(query.lower())
    if idx < 0:
        return None
    start = max(0, idx - window // 2)
    end = min(len(text), idx + window // 2)
    return text[start:end].replace("\n", " ").strip()
