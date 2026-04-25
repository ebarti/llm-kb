"""``kb stats`` — summary statistics for a workspace."""

from __future__ import annotations

import datetime as _dt
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Optional

from ..models import EXIT_SUCCESS, StatsResult, StatsSection
from ._common import CommandContext


def _count_md(path: Path, recursive: bool = False) -> int:
    if not path.exists():
        return 0
    if recursive:
        return sum(1 for _ in path.rglob("*.md") if _.is_file())
    return sum(1 for p in path.iterdir() if p.is_file() and p.suffix == ".md")


def _word_count(path: Path) -> int:
    if not path.exists():
        return 0
    total = 0
    for p in path.rglob("*.md"):
        if not p.is_file():
            continue
        try:
            total += len(p.read_text(encoding="utf-8", errors="ignore").split())
        except OSError:
            continue
    return total


def _last_modified(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    latest: Optional[float] = None
    for p in path.rglob("*.md"):
        if p.is_file():
            m = p.stat().st_mtime
            if latest is None or m > latest:
                latest = m
    if latest is None:
        return None
    return _dt.datetime.fromtimestamp(latest).strftime("%Y-%m-%d %H:%M")


def _git_commits(kb_dir: Path) -> Optional[int]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(kb_dir), "rev-list", "--count", "HEAD"],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    try:
        return int(proc.stdout.strip())
    except ValueError:
        return None


def _top_tags(concepts_dir: Path, top_n: int = 5) -> list[dict]:
    if not concepts_dir.exists():
        return []
    counter: Counter[str] = Counter()
    tag_line_re = re.compile(r"^tags:\s*(.+)$", re.IGNORECASE)
    for p in concepts_dir.glob("*.md"):
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line in content.splitlines():
            m = tag_line_re.match(line.strip())
            if not m:
                continue
            raw = m.group(1).strip().strip("[]")
            for piece in re.split(r"[,\s]+", raw):
                piece = piece.strip().strip("\"'")
                if piece:
                    counter[piece] += 1
    return [{"tag": t, "count": c} for t, c in counter.most_common(top_n)]


def run(ctx: CommandContext) -> StatsResult:
    ws = ctx.workspace
    sections_map = [
        ("raw/", ws.raw_dir),
        ("wiki/concepts/", ws.wiki_dir / "concepts"),
        ("wiki/sources/", ws.wiki_dir / "sources"),
        ("wiki/entities/", ws.wiki_dir / "entities"),
        ("wiki/comparisons/", ws.wiki_dir / "comparisons"),
        ("output/", ws.output_dir),
    ]
    sections = [
        StatsSection(
            name=name,
            files=_count_md(path, recursive=(name == "output/")),
            words=_word_count(path),
            last_modified=_last_modified(path),
        )
        for name, path in sections_map
    ]
    return StatsResult(
        command="stats",
        ok=True,
        exit_code=EXIT_SUCCESS,
        sections=sections,
        total_wiki_files=_count_md(ws.wiki_dir, recursive=True),
        total_wiki_words=_word_count(ws.wiki_dir),
        total_raw_words=_word_count(ws.raw_dir),
        git_commits=_git_commits(ws.kb_dir),
        top_tags=_top_tags(ws.wiki_dir / "concepts"),
    )
