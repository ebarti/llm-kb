"""``kb test`` — delegates to the bash test runner, returning typed results."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from kb.models import EXIT_ERROR, EXIT_SUCCESS, TestResult, TestSuiteResult
from kb.commands._common import CommandContext


def run(ctx: CommandContext) -> TestResult:
    runner = ctx.workspace.kb_dir / "tools" / "tests" / "run-all.sh"
    if not runner.exists():
        return _fallback(ctx)

    proc = subprocess.run(
        ["bash", str(runner), "--json"],
        capture_output=True, text=True, check=False,
        cwd=str(ctx.workspace.kb_dir),
    )

    suites: list[TestSuiteResult] = []
    total = passed = failed = 0

    try:
        data = json.loads(proc.stdout)
    except (ValueError, json.JSONDecodeError):
        data = None

    parse_error = not isinstance(data, dict)

    if isinstance(data, dict):
        total = int(data.get("total_suites", 0))
        passed = int(data.get("passed", 0))
        failed = int(data.get("failed", 0))
        for s in data.get("suites", []) or []:
            suites.append(
                TestSuiteResult(
                    name=s.get("name", ""),
                    passed=bool(s.get("passed")),
                    returncode=int(s.get("returncode", 0)),
                )
            )

    message_parts: list[str] = []
    if parse_error:
        message_parts.append("test runner did not return valid JSON")
        if proc.stdout:
            message_parts.append(f"stdout:\n{proc.stdout}")
        if proc.stderr:
            message_parts.append(f"stderr:\n{proc.stderr}")

    return TestResult(
        command="test",
        ok=(not parse_error and failed == 0 and proc.returncode == 0),
        exit_code=(
            EXIT_SUCCESS
            if (not parse_error and failed == 0 and proc.returncode == 0)
            else EXIT_ERROR
        ),
        suites=suites,
        total=total,
        passed=passed,
        failed=failed,
        message="\n\n".join(message_parts) if parse_error else None,
    )


def _fallback(ctx: CommandContext) -> TestResult:
    """Run the basic structural checks from bash kb when run-all.sh is missing."""
    ws = ctx.workspace
    errors: list[str] = []
    for d in [
        "raw",
        "wiki",
        "wiki/_meta",
        "wiki/concepts",
        "wiki/sources",
        "wiki/entities",
        "wiki/comparisons",
        "output",
    ]:
        if not (ws.kb_dir / d).exists():
            errors.append(f"missing dir: {d}/")
    for f in ["wiki/_index.md", "wiki/log.md", "wiki/_meta/summaries.md", "CLAUDE.md"]:
        if not (ws.kb_dir / f).exists():
            errors.append(f"missing file: {f}")

    return TestResult(
        command="test",
        ok=not errors,
        exit_code=EXIT_SUCCESS if not errors else EXIT_ERROR,
        suites=[],
        total=1,
        passed=0 if errors else 1,
        failed=1 if errors else 0,
        message="; ".join(errors) if errors else "basic checks passed",
    )
