"""Thin wrapper around the `git` CLI for kb's auto-commit behaviour."""

from __future__ import annotations

import subprocess
from pathlib import Path


def auto_commit(kb_dir: Path, label: str, *, dry_run: bool = False) -> bool:
    """Stage and commit any dirty state in ``kb_dir`` with message ``kb: <label>``.

    Returns True if a commit was created, False otherwise (no changes, not a
    git repo, git missing, etc.). Never raises.
    """
    if dry_run:
        return False
    try:
        status = subprocess.run(
            ["git", "-C", str(kb_dir), "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return False
    if status.returncode != 0:
        return False
    if not status.stdout.strip():
        return False

    subprocess.run(
        ["git", "-C", str(kb_dir), "add", "-A"],
        capture_output=True, text=True, check=False,
    )
    commit = subprocess.run(
        ["git", "-C", str(kb_dir), "commit", "-q", "-m", f"kb: {label}"],
        capture_output=True, text=True, check=False,
    )
    return commit.returncode == 0
