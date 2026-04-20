"""``kb workspaces`` — enumerate known KB workspaces."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from ..models import EXIT_SUCCESS, WorkspaceEntry, WorkspacesResult
from ._common import CommandContext


def _count_articles(wiki_dir: Path) -> int:
    if not wiki_dir.exists():
        return 0
    return sum(1 for _ in wiki_dir.rglob("*.md") if _.is_file())


def run(ctx: CommandContext, base: Optional[Path] = None) -> WorkspacesResult:
    ws = ctx.workspace
    # argparse hands in strings; coerce before using Path methods.
    if base is None:
        base_dir = Path.home() / "kb-workspaces"
    else:
        base_dir = Path(base).expanduser() if not isinstance(base, Path) else base

    entries: list[WorkspaceEntry] = []

    # The install/default workspace
    entries.append(
        WorkspaceEntry(
            name="(default)",
            path=str(ws.kb_home),
            articles=_count_articles(ws.kb_home / "wiki"),
            is_default=True,
        )
    )

    # Named workspaces under ~/kb-workspaces/
    if base_dir.exists():
        for p in sorted(base_dir.iterdir()):
            if p.is_dir() and (p / "wiki").exists():
                entries.append(
                    WorkspaceEntry(
                        name=p.name,
                        path=str(p),
                        articles=_count_articles(p / "wiki"),
                        is_default=False,
                    )
                )

    return WorkspacesResult(
        command="workspaces",
        ok=True,
        exit_code=EXIT_SUCCESS,
        workspaces=entries,
    )
