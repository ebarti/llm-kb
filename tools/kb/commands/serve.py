"""``kb serve`` / ``kb mcp`` — long-running server commands.

``kb serve`` execs into the search server so the CLI process is replaced
and Ctrl+C lands directly on the server. ``kb mcp`` intentionally stays a
child subprocess so the caller gets a typed ``ServeResult`` with the
server's eventual exit status. For JSON mode we return a descriptor
without starting either server.
"""

from __future__ import annotations

import os
import subprocess
import sys
from typing import Optional

from ..models import EXIT_ERROR, EXIT_SUCCESS, ServeResult
from ._common import CommandContext


def run_serve(ctx: CommandContext, port: int = 8765) -> ServeResult:
    ws = ctx.workspace
    server = ws.kb_dir / "tools" / "search-engine" / "server.py"
    if not server.exists():
        return ServeResult(
            command="serve", ok=False, exit_code=EXIT_ERROR,
            port=port, url=f"http://localhost:{port}",
            message=f"search server not found at {server}",
        )

    if ctx.json_output or ctx.dry_run:
        return ServeResult(
            command="serve", ok=True, exit_code=EXIT_SUCCESS,
            port=port, url=f"http://localhost:{port}",
            message="server descriptor (not started in --json/--dry-run mode)",
        )

    # Replace this process with the server so Ctrl+C behaves naturally.
    try:
        os.execvp("python3", ["python3", str(server), str(port)])
    except OSError as exc:
        return ServeResult(
            command="serve",
            ok=False,
            exit_code=EXIT_ERROR,
            port=port,
            url=f"http://localhost:{port}",
            message=f"failed to launch search server ({exc}); is python3 on PATH?",
        )
    # Unreachable on success — execvp replaces this process.
    return ServeResult(command="serve", port=port, url=f"http://localhost:{port}")


def run_mcp(ctx: CommandContext, args: Optional[list[str]] = None) -> ServeResult:
    ws = ctx.workspace
    server = ws.kb_dir / "tools" / "mcp-server" / "server.py"
    if not server.exists():
        return ServeResult(
            command="mcp", ok=False, exit_code=EXIT_ERROR,
            port=0, url="stdio",
            message=f"MCP server not found at {server}",
        )

    if ctx.json_output or ctx.dry_run:
        return ServeResult(
            command="mcp", ok=True, exit_code=EXIT_SUCCESS,
            port=0, url="stdio",
            message="MCP server descriptor (not started in --json/--dry-run mode)",
        )

    cmd = ["python3", str(server)] + (args or [])
    # mcp-server/server.py defaults WIKI_ROOT to os.getcwd(); without this
    # an invocation via `kb --dir <tmp> mcp` would serve the caller's
    # checkout, not the selected workspace.
    env = os.environ.copy()
    env["WIKI_ROOT"] = str(ws.kb_dir)
    proc = subprocess.run(cmd, check=False, cwd=str(ws.kb_dir), env=env)
    return ServeResult(
        command="mcp",
        ok=proc.returncode == 0,
        exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
        port=0, url="stdio",
    )
