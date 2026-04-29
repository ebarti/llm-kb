"""``kb viz`` — delegates to scripts in tools/viz/."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from kb.models import EXIT_ERROR, EXIT_SUCCESS, VizResult
from kb.commands._common import CommandContext


VIZ_SCRIPTS = {
    "graph": "graph.py",
    "timeline": "timeline.py",
    "stats": "stats.py",
    "concept-map": "concept-map.py",
    "canvas": "canvas.py",
}


def run(ctx: CommandContext, viz_type: str = "stats") -> VizResult:
    ws = ctx.workspace
    viz_dir = ws.kb_dir / "tools" / "viz"

    if viz_type == "all":
        runner = viz_dir / "generate-all.sh"
        if runner.exists():
            proc = subprocess.run(
                ["bash", str(runner)], capture_output=True, text=True, check=False,
                cwd=str(ws.kb_dir),
            )
            return VizResult(
                command="viz",
                viz_type="all",
                ok=proc.returncode == 0,
                exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
                generated=list(VIZ_SCRIPTS.keys()) if proc.returncode == 0 else [],
                message=proc.stdout + proc.stderr,
            )
        generated: list[str] = []
        failed: list[str] = []
        for vt in VIZ_SCRIPTS:
            sub = run(ctx, vt)
            if sub.ok:
                generated.extend(sub.generated)
            else:
                failed.append(vt)
        return VizResult(
            command="viz",
            viz_type="all",
            ok=not failed,
            exit_code=EXIT_SUCCESS if not failed else EXIT_ERROR,
            generated=generated,
            message=(
                f"Failed to generate: {', '.join(failed)}"
                if failed
                else f"Generated: {', '.join(generated)}"
            ),
        )

    script = VIZ_SCRIPTS.get(viz_type)
    if not script:
        return VizResult(
            command="viz",
            viz_type=viz_type,
            ok=False,
            exit_code=EXIT_ERROR,
            message=f"Unknown viz type: {viz_type!r} (try: {', '.join(VIZ_SCRIPTS)} or 'all')",
        )

    script_path = viz_dir / script
    if not script_path.exists():
        return VizResult(
            command="viz",
            viz_type=viz_type,
            ok=False,
            exit_code=EXIT_ERROR,
            message=f"{script} not found in {viz_dir}",
        )

    python = sys.executable or "python3"
    proc = subprocess.run(
        [python, str(script_path)], capture_output=True, text=True, check=False,
        cwd=str(ws.kb_dir),
    )
    return VizResult(
        command="viz",
        viz_type=viz_type,
        ok=proc.returncode == 0,
        exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
        generated=[viz_type] if proc.returncode == 0 else [],
        message=proc.stdout + proc.stderr,
    )
