"""
Workspace resolution and filesystem scaffolding.

The bash `kb` supported:
  - ``KB_DIR`` env var
  - ``--dir`` / ``-d`` pointing at either a bare workspace name (resolved to
    ``$KB_WORKSPACES/<name>`` or ``$HOME/kb-workspaces/<name>``) or an
    absolute/relative path
  - Auto-initialization of freshly-created workspaces

This module centralises that logic so every subcommand can reuse it.
"""

from __future__ import annotations

import datetime as _dt
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# Files created by ``cmd_init`` in the bash kb. Kept in sync here so the
# Python implementation produces an identical layout.
_GITIGNORE_CONTENT = """# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
.venv/

# Node
node_modules/

# Build artifacts
*.pdf
*.epub

# Obsidian
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# Secrets
.env

# Discovery review queue (local operational state)
.queue/
"""


_OBSIDIAN_APP = """{
  "strictLineBreaks": false,
  "showFrontmatter": true,
  "livePreview": true,
  "readableLineLength": true
}
"""


_OBSIDIAN_THEME = """{
  "accentColor": "#7c5cbf",
  "theme": "obsidian"
}
"""


_CLAUDE_MD_STUB = """# LLM Knowledge Base

You are operating an LLM-powered personal knowledge base. This is an Obsidian
vault where YOU (the LLM) author and maintain all wiki content.

**You are a research agent first, a wiki compiler second, and a Q&A system third.**

## Directory Structure

```
raw/            -> Raw ingested content (source of truth)
wiki/           -> LLM-compiled wiki (YOU maintain this)
  _index.md     -> Master index
  log.md        -> Chronological operation log
  _meta/        -> Metadata (summaries, links, manifest)
  concepts/     -> Concept articles
  entities/     -> Entity pages
  comparisons/  -> Comparison articles
  sources/      -> Per-source summaries
output/         -> Generated outputs (reports, slides, images)
tools/          -> Helper scripts
```

See the full CLAUDE.md in the kb install directory for detailed operation instructions.
"""


_INDEX_STUB = """---
title: "Knowledge Base Index"
type: index
last_updated: ""
---

# Knowledge Base Index

## Concepts

_No concept articles yet. Run `./kb research "<topic>"` to get started._

## Entities

## Sources

## Comparisons
"""


def _is_path_like(dir_flag: str) -> bool:
    dir_path = Path(dir_flag)
    return (
        dir_path.is_absolute()
        or dir_flag.startswith("~")
        or dir_flag.startswith(".")
        or any(
            sep and sep in dir_flag for sep in (os.sep, os.altsep, "/", "\\")
        )
    )


def _workspaces_root() -> Path:
    """Return the base directory for named workspaces."""
    return Path(
        os.environ.get("KB_WORKSPACES") or (Path.home() / "kb-workspaces")
    ).expanduser()


@dataclass
class Workspace:
    """A resolved workspace pairing an install location with an active KB."""

    kb_home: Path  # Where the `kb` script / tools / CLAUDE.md live
    kb_dir: Path   # Active workspace (wiki/raw/output live here)

    # ------------------------------------------------------------------ #
    #  Resolution
    # ------------------------------------------------------------------ #

    @classmethod
    def resolve(
        cls,
        kb_home: Optional[Path] = None,
        kb_dir: Optional[str] = None,
        dir_flag: Optional[str] = None,
        dry_run: bool = False,
    ) -> "Workspace":
        """Resolve the install location and the active workspace path.

        Mirrors the bash logic:
          - ``kb_home`` defaults to the directory containing this package's
            parent (the repo root)
          - ``KB_DIR`` env var overrides ``kb_home`` as the active dir
          - ``--dir <x>`` further overrides; a bare name is resolved under
            ``$KB_WORKSPACES/<name>`` (default ``$HOME/kb-workspaces/<name>``);
            a path is used as-is

        Under ``dry_run=True`` no directories are created and auto-init is
        skipped — callers that actually need to write to the workspace must
        run without ``--dry-run``.
        """
        if kb_home is None:
            kb_home = Path(__file__).resolve().parents[2]
        kb_home = Path(kb_home).resolve()

        # Step 1: start from env var or install location
        base_dir = Path(
            kb_dir or os.environ.get("KB_DIR") or str(kb_home)
        ).expanduser()

        # Step 2: --dir/-d flag overrides
        if dir_flag:
            if _is_path_like(dir_flag):
                base_dir = Path(dir_flag).expanduser()
            else:
                base_dir = _workspaces_root() / dir_flag

        if not dry_run:
            base_dir.mkdir(parents=True, exist_ok=True)
        # Resolve may still work if parents exist; otherwise expand without
        # touching disk so --dry-run stays purely read-only.
        try:
            base_dir = base_dir.resolve()
        except OSError:
            base_dir = base_dir.expanduser()

        ws = cls(kb_home=kb_home, kb_dir=base_dir)

        # Auto-init freshly created workspaces (only when --dir was used and
        # we aren't in dry-run). Under --dry-run we deliberately skip init
        # so the command preview stays side-effect-free.
        if dir_flag and not dry_run and not (base_dir / "wiki").exists():
            ws.initialize()

        return ws

    # ------------------------------------------------------------------ #
    #  Paths
    # ------------------------------------------------------------------ #

    @property
    def raw_dir(self) -> Path:
        return self.kb_dir / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.kb_dir / "wiki"

    @property
    def output_dir(self) -> Path:
        return self.kb_dir / "output"

    @property
    def log_path(self) -> Path:
        return self.wiki_dir / "log.md"

    # ------------------------------------------------------------------ #
    #  Scaffolding
    # ------------------------------------------------------------------ #

    def ensure_dirs(self) -> None:
        """Create the standard directory tree if missing."""
        subdirs = [
            self.raw_dir,
            self.wiki_dir / "_meta",
            self.wiki_dir / "concepts",
            self.wiki_dir / "sources",
            self.wiki_dir / "entities",
            self.wiki_dir / "comparisons",
            self.output_dir / "reports",
            self.output_dir / "slides",
            self.output_dir / "images",
        ]
        for d in subdirs:
            d.mkdir(parents=True, exist_ok=True)

    def initialize(self, copy_tools: bool = True) -> list[str]:
        """Create the full directory layout + seed files; return created paths.

        Matches the semantics of bash ``cmd_init`` including copying tools
        and templates from the install location when initializing a new
        workspace that is not the install directory itself.
        """
        created: list[str] = []
        self.ensure_dirs()
        # Extra dirs used by init
        for d in (self.kb_dir / "tools", self.kb_dir / "templates", self.kb_dir / "Clippings"):
            d.mkdir(parents=True, exist_ok=True)

        gitignore = self.kb_dir / ".gitignore"
        if not gitignore.exists():
            gitignore.write_text(_GITIGNORE_CONTENT, encoding="utf-8")
            created.append(str(gitignore))

        obs_dir = self.kb_dir / ".obsidian"
        if not obs_dir.exists():
            obs_dir.mkdir(parents=True, exist_ok=True)
            (obs_dir / "app.json").write_text(_OBSIDIAN_APP, encoding="utf-8")
            (obs_dir / "appearance.json").write_text(_OBSIDIAN_THEME, encoding="utf-8")
            created.append(str(obs_dir / "app.json"))
            created.append(str(obs_dir / "appearance.json"))

        claude_md = self.kb_dir / "CLAUDE.md"
        if not claude_md.exists():
            src = self.kb_home / "CLAUDE.md"
            if src.exists() and src.resolve() != claude_md.resolve():
                claude_md.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                claude_md.write_text(_CLAUDE_MD_STUB, encoding="utf-8")
            created.append(str(claude_md))

        if copy_tools:
            src_tools = self.kb_home / "tools"
            dst_tools = self.kb_dir / "tools"
            if (
                src_tools.exists()
                and src_tools.resolve() != dst_tools.resolve()
                and not (dst_tools / "search-engine").exists()
            ):
                _copy_tree(src_tools, dst_tools)
                created.append(str(dst_tools))

            src_tpl = self.kb_home / "templates"
            dst_tpl = self.kb_dir / "templates"
            if (
                src_tpl.exists()
                and src_tpl.resolve() != dst_tpl.resolve()
                and (not dst_tpl.exists() or not any(dst_tpl.iterdir()))
            ):
                _copy_tree(src_tpl, dst_tpl)
                created.append(str(dst_tpl))

        index_md = self.wiki_dir / "_index.md"
        if not index_md.exists():
            index_md.write_text(_INDEX_STUB, encoding="utf-8")
            created.append(str(index_md))

        log_md = self.log_path
        if not log_md.exists():
            today = _dt.date.today().isoformat()
            log_md.write_text(
                f"# Knowledge Base Log\n\n## [{today}] init | Knowledge base initialized\n"
                f"- Created directory structure\n- Ready for research\n",
                encoding="utf-8",
            )
            created.append(str(log_md))

        for meta in ("summaries.md", "links.md", "manifest.md"):
            target = self.wiki_dir / "_meta" / meta
            if not target.exists():
                target.write_text(f"# {target.stem}\n", encoding="utf-8")
                created.append(str(target))

        # Git init if missing
        if not (self.kb_dir / ".git").exists():
            try:
                subprocess.run(
                    ["git", "-C", str(self.kb_dir), "init", "-q"],
                    check=True,
                )
                subprocess.run(
                    ["git", "-C", str(self.kb_dir), "add", "-A"],
                    check=False,
                )
                subprocess.run(
                    [
                        "git",
                        "-C",
                        str(self.kb_dir),
                        "commit",
                        "-q",
                        "-m",
                        "kb: initialize knowledge base",
                    ],
                    check=False,
                )
            except (FileNotFoundError, subprocess.CalledProcessError):
                pass  # git not installed or init failed — not fatal

        return created


# --------------------------------------------------------------------------- #
#  Helpers
# --------------------------------------------------------------------------- #


def _copy_tree(src: Path, dst: Path) -> None:
    """Copy ``src`` recursively into ``dst``; tolerate ``dst`` existing."""
    import shutil

    if dst.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copytree(src, dst)
