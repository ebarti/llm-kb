"""``kb init`` and ``kb new`` — workspace scaffolding."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from ..models import EXIT_SUCCESS, InitResult
from ..workspace import Workspace
from ._common import CommandContext


def run_init(
    ctx: CommandContext,
    target: Optional[Path | str] = None,
    dry_run: bool = False,
) -> InitResult:
    if target:
        target_path = Path(target).expanduser()
        if not target_path.is_absolute():
            target_path = ctx.workspace.kb_dir / target_path
    else:
        target_path = ctx.workspace.kb_dir
    target_path = target_path.resolve()

    if dry_run or ctx.dry_run:
        return InitResult(
            command="init",
            dry_run=True,
            target=str(target_path),
            message=f"[dry-run] would initialize workspace at {target_path}",
        )

    new_ws = Workspace(kb_home=ctx.workspace.kb_home, kb_dir=target_path)
    created = new_ws.initialize()
    return InitResult(
        command="init",
        ok=True,
        exit_code=EXIT_SUCCESS,
        target=str(target_path),
        created_files=created,
        message=f"Knowledge base initialized at {target_path}",
    )


def run_new(ctx: CommandContext, name: str, base: Optional[Path] = None, dry_run: bool = False) -> InitResult:
    base_dir = Path(base) if base else (Path.home() / "kb-workspaces")
    base_dir = base_dir.expanduser().resolve()
    target = base_dir / name
    return run_init(ctx, target=target, dry_run=dry_run)
