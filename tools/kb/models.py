"""
Pydantic result schemas for the kb Python CLI.

Every subcommand returns one of these models so --json callers receive a
stable, typed shape. Freeform prose never flows back out of --json mode.
"""

from __future__ import annotations

from typing import Any, Optional

try:
    from pydantic import BaseModel, Field
except ImportError:  # pragma: no cover - pydantic is a declared dependency
    raise SystemExit(
        "pydantic is required. Install with: pip install -r requirements.txt"
    )


# --------------------------------------------------------------------------- #
#  Common result envelope
# --------------------------------------------------------------------------- #


class TokenUsage(BaseModel):
    """Aggregated Anthropic token usage for one command invocation."""

    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0

    @property
    def total(self) -> int:
        return (
            self.input_tokens
            + self.output_tokens
            + self.cache_creation_input_tokens
            + self.cache_read_input_tokens
        )


class CommandResult(BaseModel):
    """Base envelope for every subcommand result.

    Exit codes:
      0  success
      1  general error
      2  budget exceeded
      3  user abort
      4  no-op (nothing to do)
    """

    command: str
    ok: bool = True
    exit_code: int = 0
    dry_run: bool = False
    budget_limit: Optional[int] = None
    usage: TokenUsage = Field(default_factory=TokenUsage)
    message: Optional[str] = None
    details: dict[str, Any] = Field(default_factory=dict)


# --------------------------------------------------------------------------- #
#  Per-command results
# --------------------------------------------------------------------------- #


class LLMInvocationResult(CommandResult):
    """Shared shape for LLM-invoking commands (research, compile, ingest,
    ask, lint, slides, report, compare, entity, discover, freeform)."""

    prompt: Optional[str] = None
    topic: Optional[str] = None
    model: Optional[str] = None
    committed: bool = False
    commit_label: Optional[str] = None


class StatsSection(BaseModel):
    name: str
    files: int
    words: int
    last_modified: Optional[str] = None


class StatsResult(CommandResult):
    sections: list[StatsSection] = Field(default_factory=list)
    total_wiki_files: int = 0
    total_wiki_words: int = 0
    total_raw_words: int = 0
    git_commits: Optional[int] = None
    top_tags: list[dict[str, Any]] = Field(default_factory=list)


class LogResult(CommandResult):
    entries: list[str] = Field(default_factory=list)
    log_path: Optional[str] = None


class SearchHit(BaseModel):
    path: str
    title: Optional[str] = None
    score: Optional[float] = None
    snippet: Optional[str] = None


class SearchResult(CommandResult):
    query: str = ""
    hits: list[SearchHit] = Field(default_factory=list)
    backend: str = "qmd"  # qmd | grep | search.sh


class WorkspaceEntry(BaseModel):
    name: str
    path: str
    articles: int
    is_default: bool = False


class WorkspacesResult(CommandResult):
    workspaces: list[WorkspaceEntry] = Field(default_factory=list)


class InitResult(CommandResult):
    target: str
    created_files: list[str] = Field(default_factory=list)


class TestSuiteResult(BaseModel):
    name: str
    passed: bool
    returncode: int
    output: Optional[str] = None


class TestResult(CommandResult):
    suites: list[TestSuiteResult] = Field(default_factory=list)
    total: int = 0
    passed: int = 0
    failed: int = 0


class VizResult(CommandResult):
    viz_type: str
    generated: list[str] = Field(default_factory=list)


class ExportResult(CommandResult):
    format: str
    output_path: Optional[str] = None


class ServeResult(CommandResult):
    port: int
    url: str


# --------------------------------------------------------------------------- #
#  Exit codes (as integers, intentionally verbose names)
# --------------------------------------------------------------------------- #


EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_BUDGET = 2
EXIT_ABORT = 3
EXIT_NOOP = 4
