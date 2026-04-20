"""``kb export`` — produces publishable artifacts (site, pdf, epub, bundle)."""

from __future__ import annotations

import datetime as _dt
import shutil
import subprocess
import tarfile
from pathlib import Path

from ..models import EXIT_ERROR, EXIT_SUCCESS, ExportResult
from ._common import CommandContext


def run(ctx: CommandContext, fmt: str = "site") -> ExportResult:
    ws = ctx.workspace
    export_dir = ws.kb_dir / "tools" / "export"

    if fmt == "site":
        script = export_dir / "build-site.py"
        if not script.exists():
            return ExportResult(
                command="export", format=fmt, ok=False, exit_code=EXIT_ERROR,
                message="build-site.py not found",
            )
        proc = subprocess.run(
            ["python3", str(script)], capture_output=True, text=True, check=False,
            cwd=str(ws.kb_dir),
        )
        return ExportResult(
            command="export", format=fmt,
            ok=proc.returncode == 0,
            exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
            output_path=str(ws.output_dir / "site"),
            message=proc.stdout + proc.stderr,
        )

    if fmt in ("pdf", "epub"):
        if shutil.which("pandoc") is None:
            return ExportResult(
                command="export", format=fmt, ok=False, exit_code=EXIT_ERROR,
                message=f"pandoc is required for {fmt} export",
            )
        outfile = ws.output_dir / f"kb-export.{fmt}"
        md_files = sorted(
            p for p in (ws.wiki_dir).rglob("*.md")
            if "_meta" not in p.parts and p.is_file()
        )
        if not md_files:
            return ExportResult(
                command="export", format=fmt, ok=False, exit_code=EXIT_ERROR,
                message="no wiki files to export",
            )
        cmd = ["pandoc", "-o", str(outfile), "--metadata", "title=Knowledge Base Export"]
        cmd.extend(str(p) for p in md_files)
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return ExportResult(
            command="export", format=fmt,
            ok=proc.returncode == 0,
            exit_code=EXIT_SUCCESS if proc.returncode == 0 else EXIT_ERROR,
            output_path=str(outfile),
            message=proc.stdout + proc.stderr,
        )

    if fmt == "bundle":
        outfile = ws.output_dir / f"kb-bundle-{_dt.date.today().strftime('%Y%m%d')}.tar.gz"
        outfile.parent.mkdir(parents=True, exist_ok=True)
        with tarfile.open(outfile, "w:gz") as tar:
            for name in ("wiki", "raw", "output", "CLAUDE.md"):
                p = ws.kb_dir / name
                if p.exists():
                    tar.add(p, arcname=name)
        return ExportResult(
            command="export", format=fmt,
            ok=True, exit_code=EXIT_SUCCESS,
            output_path=str(outfile),
            message=f"Bundle created: {outfile}",
        )

    return ExportResult(
        command="export", format=fmt, ok=False, exit_code=EXIT_ERROR,
        message=f"Unknown format: {fmt} (try: site, pdf, epub, bundle)",
    )
