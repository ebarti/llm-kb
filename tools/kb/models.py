"""
Pydantic result schemas for the kb Python CLI.

Every subcommand returns one of these models so --json callers receive a
stable, typed shape. The envelope stays structured in --json mode, but some
fields such as `message` may contain raw subprocess output or LLM text.
"""

from __future__ import annotations

from typing import Any, Optional

try:
    from pydantic import BaseModel, Field
except Exception:  # pragma: no cover - pydantic is an optional dependency
    # Fallback: minimal stub so `./kb --help`, ``kb stats``, ``kb search``
    # etc. keep working without a functioning pydantic installed. We catch
    # ``Exception`` (not just ``ImportError``) because broken pydantic/
    # pydantic-core version mismatches raise ``SystemError`` at module
    # load — that must not take the whole CLI down. ``model_dump_json``
    # keeps the --json output path functional. Install pydantic
    # (``pip install pydantic``) for full validation.

    import json as _json

    class _FieldInfo:
        __slots__ = ("default", "default_factory")

        def __init__(self, default=None, default_factory=None):
            self.default = default
            self.default_factory = default_factory

    def Field(default=None, *, default_factory=None, **_kwargs):  # type: ignore[misc]
        return _FieldInfo(default=default, default_factory=default_factory)

    class _StubBase:
        """Minimal BaseModel stand-in.

        Collects annotated class attributes (walking the MRO so inherited
        fields are preserved) and provides a kwargs-only ``__init__`` plus
        ``model_dump``/``model_dump_json`` for JSON serialization.
        """

        def __init__(self, **kwargs):
            fields = self._stub_fields()
            for name, default_getter in fields.items():
                if name in kwargs:
                    setattr(self, name, kwargs.pop(name))
                else:
                    setattr(self, name, default_getter())
            if kwargs:
                raise TypeError(
                    f"Unexpected fields for {type(self).__name__}: {list(kwargs)}"
                )

        @classmethod
        def _stub_fields(cls) -> dict:
            # Walk MRO from base -> derived so subclass overrides win.
            fields: dict = {}
            _MISSING = object()
            for klass in reversed(cls.__mro__):
                ann = getattr(klass, "__annotations__", {}) or {}
                for name in ann:
                    raw = klass.__dict__.get(name, _MISSING)
                    if isinstance(raw, _FieldInfo):
                        if raw.default_factory is not None:
                            factory = raw.default_factory
                            fields[name] = (lambda f=factory: f())
                        else:
                            dflt = raw.default
                            fields[name] = (lambda v=dflt: v)
                    elif raw is _MISSING:
                        # No default: caller must supply. Raise if missing.
                        def _required(n=name, c=klass.__name__):
                            raise TypeError(
                                f"{c}: missing required field '{n}'"
                            )
                        fields[name] = _required
                    else:
                        dflt = raw
                        fields[name] = (lambda v=dflt: v)
            return fields

        def model_dump(self) -> dict:
            out: dict = {}
            for name in self._stub_fields():
                out[name] = _dump_value(getattr(self, name, None))
            return out

        def model_dump_json(self, indent: int | None = None) -> str:
            return _json.dumps(self.model_dump(), indent=indent, default=str)

        # pydantic v1 compatibility aliases
        def dict(self) -> dict:
            return self.model_dump()

        def json(self, indent: int | None = None) -> str:
            return self.model_dump_json(indent=indent)

    def _dump_value(val):
        if isinstance(val, _StubBase):
            return val.model_dump()
        if isinstance(val, list):
            return [_dump_value(v) for v in val]
        if isinstance(val, dict):
            return {k: _dump_value(v) for k, v in val.items()}
        return val

    BaseModel = _StubBase  # type: ignore[assignment,misc]


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


class QueueItemSummary(BaseModel):
    id: str
    status: str = "pending"
    topic: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    content_hash: Optional[str] = None
    created_at: Optional[str] = None
    preview: Optional[str] = None


class QueueResult(CommandResult):
    action: str
    queue_dir: str
    items: list[QueueItemSummary] = Field(default_factory=list)
    item: Optional[QueueItemSummary] = None


# --------------------------------------------------------------------------- #
#  Exit codes (as integers, intentionally verbose names)
# --------------------------------------------------------------------------- #


EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_BUDGET = 2
EXIT_ABORT = 3
EXIT_NOOP = 4
