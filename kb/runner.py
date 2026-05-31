"""
LLM runner for kb.

The default backend is the **Claude Agent SDK** (``claude-agent-sdk`` on PyPI).
Set ``KB_LLM_PROVIDER=codex`` to run the same KB prompts through the Codex SDK
instead.
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import os
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from kb import observability
from kb.budget import BudgetExceeded, BudgetTracker
from kb.models import TokenUsage


@dataclass
class LLMResult:
    text: str = ""
    backend: str = "agent"  # 'agent' | 'codex' | 'dry-run'
    usage: TokenUsage = field(default_factory=TokenUsage)
    returncode: int = 0
    budget_exceeded: bool = False


# --------------------------------------------------------------------------- #
#  Public entry point
# --------------------------------------------------------------------------- #


def invoke_llm(
    prompt: str,
    *,
    model: str = "opus",
    budget: BudgetTracker,
    dry_run: bool = False,
    permission_mode: str = "bypassPermissions",
    verbose: bool = False,
    show_progress: bool | None = None,
    cwd: Optional[str] = None,
) -> LLMResult:
    """Run ``prompt`` through the configured LLM provider.

    Parameters
    ----------
    prompt
        The user prompt.
    model
        Model alias (``opus``/``sonnet``/``haiku``) or a full model id.
        Claude aliases are expanded below. Codex mode uses the Codex SDK
        default model unless ``KB_CODEX_MODEL`` or a non-Claude model is set.
    budget
        A :class:`~kb.budget.BudgetTracker`. The ``ResultMessage``
        usage is fed into it; if the response crosses the cap, the
        returned :class:`LLMResult` has ``budget_exceeded=True``.
    dry_run
        When true, return an :class:`LLMResult` describing what would be
        run without touching the SDK.
    permission_mode
        Forwarded to ``ClaudeAgentOptions.permission_mode`` for Claude. Codex
        mode is configured with ``KB_CODEX_SANDBOX_MODE`` and
        ``KB_CODEX_APPROVAL_POLICY``.
    cwd
        Working directory for the agent. Defaults to the process cwd.
    """
    if dry_run:
        return LLMResult(
            text=f"[DRY RUN] model={model} budget={budget.limit} prompt={prompt[:120]}...",
            backend="dry-run",
        )

    return _invoke_agent(
        prompt=prompt,
        model=model,
        budget=budget,
        permission_mode=permission_mode,
        verbose=verbose,
        show_progress=verbose if show_progress is None else show_progress,
        cwd=cwd,
    )


# --------------------------------------------------------------------------- #
#  Agent SDK backend
# --------------------------------------------------------------------------- #


_MODEL_ALIASES = {
    "opus": "claude-opus-4-7",
    "sonnet": "claude-sonnet-4-6",
    "haiku": "claude-haiku-4-5-20251001",
}

_REPO_ROOT = Path(__file__).resolve().parents[1]
_CODEX_BRIDGE = _REPO_ROOT / "tools" / "codex" / "run.mjs"
_CODEX_HOME_DIRNAME = ".codex"
_LLM_KB_CODEX_HOME_DIRNAME = ".codex_llm_kb"
_FALSEY_ENV = {"", "0", "false", "no", "off"}
_THIRD_PARTY_PROVIDER_FLAGS = {
    "vertex": "CLAUDE_CODE_USE_VERTEX",
    "bedrock": "CLAUDE_CODE_USE_BEDROCK",
    "foundry": "CLAUDE_CODE_USE_FOUNDRY",
}
_PROVIDER_ALIASES = {
    "google-vertex": "vertex",
    "openai": "codex",
    "openai-codex": "codex",
}
_SUPPORTED_PROVIDERS = {"anthropic", "codex", *_THIRD_PARTY_PROVIDER_FLAGS}


def _resolve_model(name: str) -> str:
    return _MODEL_ALIASES.get(name, name)


def _resolve_provider_model(name: str, provider: str) -> Optional[str]:
    if provider != "codex":
        return _resolve_model(name)

    env_model = os.environ.get("KB_CODEX_MODEL", "").strip()
    if env_model:
        return env_model
    if not name or name in _MODEL_ALIASES:
        return None
    return name


def _missing_sdk_error() -> Optional[Exception]:
    try:
        import claude_agent_sdk  # noqa: F401
    except Exception as exc:  # noqa: BLE001
        return exc
    return None


def _env_flag_enabled(name: str) -> bool:
    value = os.environ.get(name)
    if value is None:
        return False
    return value.strip().lower() not in _FALSEY_ENV


def _env_flag_default(name: str, default: bool) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() not in _FALSEY_ENV


def _configure_agent_provider() -> tuple[str, Optional[str]]:
    """Return the active Agent SDK provider and apply kb provider aliases."""
    requested = os.environ.get("KB_LLM_PROVIDER", "").strip().lower()
    if requested:
        requested = _PROVIDER_ALIASES.get(requested, requested)
        if requested not in _SUPPORTED_PROVIDERS:
            supported = ", ".join(sorted(_SUPPORTED_PROVIDERS))
            return (
                requested,
                f"ERROR: unsupported KB_LLM_PROVIDER={requested!r}. "
                f"Use one of: {supported}.",
            )
        if requested in _THIRD_PARTY_PROVIDER_FLAGS:
            os.environ[_THIRD_PARTY_PROVIDER_FLAGS[requested]] = "1"
        return requested, None

    for provider, flag in _THIRD_PARTY_PROVIDER_FLAGS.items():
        if _env_flag_enabled(flag):
            return provider, None
    return "anthropic", None


def _auth_preflight_error(provider: str) -> Optional[str]:
    if provider == "codex":
        return None
    if provider == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        return (
            "ERROR: ANTHROPIC_API_KEY is not set. Export it before running "
            "LLM-backed commands with the Anthropic API, for example: "
            "`export ANTHROPIC_API_KEY=<key>`. For Vertex AI, set "
            "`KB_LLM_PROVIDER=vertex` or `CLAUDE_CODE_USE_VERTEX=1` and "
            "configure Google Cloud credentials. For Codex, set "
            "`KB_LLM_PROVIDER=codex` and authenticate Codex."
        )
    return None


def _provider_failure_hint(provider: str) -> str:
    if provider == "codex":
        return (
            " Codex mode is active; verify Node.js 18+, `npm install`, "
            "`@openai/codex-sdk`, and Codex authentication via the Codex CLI "
            "or `OPENAI_API_KEY`/`CODEX_API_KEY`."
        )
    if provider == "vertex":
        return (
            " Vertex AI mode is active; verify `CLAUDE_CODE_USE_VERTEX=1`, "
            "`ANTHROPIC_VERTEX_PROJECT_ID`, `CLOUD_ML_REGION`, and Google "
            "credentials in the environment, such as `GOOGLE_APPLICATION_CREDENTIALS`."
        )
    return ""


def _invoke_agent(
    *,
    prompt: str,
    model: str,
    budget: BudgetTracker,
    permission_mode: str,
    verbose: bool,
    show_progress: bool,
    cwd: Optional[str],
) -> LLMResult:
    provider, provider_error = _configure_agent_provider()
    if provider_error is not None:
        return LLMResult(text=provider_error, backend="agent", returncode=1)

    resolved_model = _resolve_provider_model(model, provider)
    if show_progress:
        observability.event(
            "agent backend",
            f"provider={provider} model={resolved_model or 'codex-default'} "
            f"permission_mode={permission_mode} budget={budget.limit} "
            f"cwd={cwd or os.getcwd()}",
            visible=True,
        )

    if provider == "codex":
        return _invoke_codex(
            prompt=prompt,
            model=resolved_model,
            budget=budget,
            verbose=verbose,
            show_progress=show_progress,
            cwd=cwd,
        )

    sdk_error = _missing_sdk_error()
    if sdk_error is not None:
        return LLMResult(
            text=(
                "ERROR: kb LLM commands require claude-agent-sdk. Install it "
                "from the repo root with `uv sync`. The `claude` CLI is "
                f"only used for `uv run kb -i`. Import failed: {sdk_error}."
            ),
            backend="agent",
            returncode=1,
        )

    auth_error = _auth_preflight_error(provider)
    if auth_error is not None:
        return LLMResult(text=auth_error, backend="agent", returncode=1)

    remaining = budget.remaining()
    if remaining is not None and remaining <= 0:
        return LLMResult(
            text="ERROR: token budget exhausted before agent call",
            backend="agent",
            returncode=1,
            budget_exceeded=True,
        )

    try:
        text, budget_exceeded, had_error, error_subtype = asyncio.run(
            _stream_agent(
                prompt=prompt,
                model=resolved_model,
                budget=budget,
                permission_mode=permission_mode,
                cwd=cwd,
                provider=provider,
                verbose=verbose,
                show_progress=show_progress,
            )
        )
    except Exception as exc:  # noqa: BLE001
        return LLMResult(
            text=(
                f"ERROR: claude-agent-sdk call failed: {exc}."
                f"{_provider_failure_hint(provider)}"
            ),
            backend="agent",
            returncode=1,
        )

    if had_error and not text:
        text = f"ERROR: agent reported {error_subtype or 'error'} before producing output"

    returncode = 0
    if budget_exceeded or had_error:
        returncode = 1

    return LLMResult(
        text=text,
        backend="agent",
        # Rebuild explicitly to avoid leaking pydantic v2 private attrs from
        # ``**usage.__dict__`` (see review feedback on PR #23).
        usage=TokenUsage(
            input_tokens=budget.usage.input_tokens,
            output_tokens=budget.usage.output_tokens,
            cache_creation_input_tokens=budget.usage.cache_creation_input_tokens,
            cache_read_input_tokens=budget.usage.cache_read_input_tokens,
        ),
        returncode=returncode,
        budget_exceeded=budget_exceeded,
    )


async def _stream_agent(
    *,
    prompt: str,
    model: str,
    budget: BudgetTracker,
    permission_mode: str,
    cwd: Optional[str],
    provider: str,
    verbose: bool,
    show_progress: bool,
) -> tuple[str, bool, bool, Optional[str]]:
    """Drive ``claude_agent_sdk.query`` and return (text, budget_exceeded,
    had_error, error_subtype)."""
    from claude_agent_sdk import (  # type: ignore
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        query,
    )

    options_kwargs: dict = {"permission_mode": permission_mode, "model": model}
    if cwd is not None:
        options_kwargs["cwd"] = cwd
    options = ClaudeAgentOptions(**options_kwargs)

    assistant_text_parts: list[str] = []
    final_result_text: Optional[str] = None
    budget_exceeded = False
    had_error = False
    error_subtype: Optional[str] = None

    stop_heartbeat = asyncio.Event()
    heartbeat_task: asyncio.Task[None] | None = None
    if show_progress:
        heartbeat_task = asyncio.create_task(
            _agent_heartbeat(stop_heartbeat, provider=provider, model=model, cwd=cwd)
        )

    try:
        async for msg in query(prompt=prompt, options=options):
            if isinstance(msg, AssistantMessage):
                block_count = len(getattr(msg, "content", None) or [])
                observability.event(
                    "agent event",
                    f"assistant message blocks={block_count}",
                    visible=show_progress,
                )
                for block in getattr(msg, "content", None) or []:
                    block_text = getattr(block, "text", None)
                    if block_text:
                        assistant_text_parts.append(block_text)
                        observability.event(
                            "agent stream",
                            _preview_text(block_text),
                            visible=verbose,
                        )
                        continue
                    tool_name = getattr(block, "name", None)
                    if tool_name:
                        observability.event(
                            "agent tool",
                            f"name={tool_name}",
                            visible=show_progress,
                        )
            elif isinstance(msg, ResultMessage):
                final_result_text = getattr(msg, "result", None)
                if getattr(msg, "is_error", False):
                    had_error = True
                    error_subtype = getattr(msg, "subtype", None)
                try:
                    budget.add_from_response(msg)
                except BudgetExceeded:
                    budget_exceeded = True
                if show_progress:
                    observability.event(
                        "agent event",
                        "result "
                        f"error={getattr(msg, 'is_error', False)} "
                        f"subtype={getattr(msg, 'subtype', None)} "
                        f"tokens={budget.usage.total}",
                        visible=True,
                    )
    finally:
        if heartbeat_task is not None:
            stop_heartbeat.set()
            heartbeat_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await heartbeat_task

    text = final_result_text if final_result_text else "".join(assistant_text_parts)
    return text, budget_exceeded, had_error, error_subtype


# --------------------------------------------------------------------------- #
#  Codex SDK backend
# --------------------------------------------------------------------------- #


def _missing_codex_runtime_error() -> Optional[str]:
    if shutil.which("node") is None:
        return (
            "ERROR: Codex provider requires Node.js 18+ and @openai/codex-sdk. "
            "Install Node.js, then run `npm install` from the repo root."
        )
    if not _CODEX_BRIDGE.exists():
        return f"ERROR: Codex bridge not found at {_CODEX_BRIDGE}."
    return None


def _prepare_isolated_codex_home() -> Path:
    """Return llm-kb's isolated Codex home, refreshing auth from user Codex."""

    raw_target_home = os.environ.get("KB_CODEX_HOME")
    if raw_target_home:
        codex_home = Path(raw_target_home).expanduser()
    else:
        codex_home = Path.home() / _LLM_KB_CODEX_HOME_DIRNAME
    codex_home = codex_home.resolve()

    raw_source_home = os.environ.get("CODEX_HOME")
    source_home = (
        Path(raw_source_home).expanduser()
        if raw_source_home
        else Path.home() / _CODEX_HOME_DIRNAME
    ).resolve()

    codex_home.mkdir(mode=0o700, parents=True, exist_ok=True)
    codex_home.chmod(0o700)
    if source_home != codex_home:
        _copy_newer_file(source_home / "auth.json", codex_home / "auth.json", mode=0o600)
    return codex_home


def _copy_newer_file(source: Path, target: Path, *, mode: int | None = None) -> bool:
    """Copy ``source`` to ``target`` when source is newer or target is missing."""

    if not source.exists():
        if target.exists() and mode is not None:
            target.chmod(mode)
        return False
    target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    target.parent.chmod(0o700)
    if target.exists() and target.stat().st_mtime >= source.stat().st_mtime:
        if mode is not None:
            target.chmod(mode)
        return False

    shutil.copy2(source, target)
    if mode is not None:
        target.chmod(mode)
    return True


def _invoke_codex(
    *,
    prompt: str,
    model: Optional[str],
    budget: BudgetTracker,
    verbose: bool,
    show_progress: bool,
    cwd: Optional[str],
) -> LLMResult:
    runtime_error = _missing_codex_runtime_error()
    if runtime_error is not None:
        return LLMResult(text=runtime_error, backend="codex", returncode=1)
    codex_home = _prepare_isolated_codex_home()

    remaining = budget.remaining()
    if remaining is not None and remaining <= 0:
        return LLMResult(
            text="ERROR: token budget exhausted before Codex call",
            backend="codex",
            returncode=1,
            budget_exceeded=True,
        )

    try:
        payload = asyncio.run(
            _run_codex_bridge(
                prompt=prompt,
                model=model,
                cwd=cwd,
                codex_home=codex_home,
                verbose=verbose,
                show_progress=show_progress,
            )
        )
    except Exception as exc:  # noqa: BLE001
        return LLMResult(
            text=(
                f"ERROR: Codex SDK call failed: {exc}."
                f"{_provider_failure_hint('codex')}"
            ),
            backend="codex",
            returncode=1,
        )

    usage = payload.get("usage") or {}
    budget_exceeded = False
    try:
        budget.add(
            input_tokens=int(usage.get("input_tokens", 0) or 0),
            output_tokens=int(usage.get("output_tokens", 0) or 0)
            + int(usage.get("reasoning_output_tokens", 0) or 0),
            cache_read_input_tokens=int(usage.get("cached_input_tokens", 0) or 0),
        )
    except BudgetExceeded:
        budget_exceeded = True

    text = str(payload.get("finalResponse") or "")
    if not text:
        text = "ERROR: Codex completed without producing output"

    return LLMResult(
        text=text,
        backend="codex",
        usage=TokenUsage(
            input_tokens=budget.usage.input_tokens,
            output_tokens=budget.usage.output_tokens,
            cache_creation_input_tokens=budget.usage.cache_creation_input_tokens,
            cache_read_input_tokens=budget.usage.cache_read_input_tokens,
        ),
        returncode=1 if budget_exceeded or text.startswith("ERROR:") else 0,
        budget_exceeded=budget_exceeded,
    )


async def _run_codex_bridge(
    *,
    prompt: str,
    model: Optional[str],
    cwd: Optional[str],
    codex_home: Path,
    verbose: bool,
    show_progress: bool,
) -> dict:
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Node.js 18+ is required for KB_LLM_PROVIDER=codex")

    payload = {
        "prompt": prompt,
        "model": model,
        "cwd": cwd or os.getcwd(),
        "sandboxMode": os.environ.get("KB_CODEX_SANDBOX_MODE", "workspace-write"),
        "approvalPolicy": os.environ.get("KB_CODEX_APPROVAL_POLICY", "never"),
        "networkAccessEnabled": _env_flag_default("KB_CODEX_NETWORK", True),
        "webSearchMode": os.environ.get("KB_CODEX_WEB_SEARCH_MODE", "live"),
        "skipGitRepoCheck": _env_flag_default("KB_CODEX_SKIP_GIT_CHECK", True),
        "modelReasoningEffort": (
            os.environ.get("KB_CODEX_REASONING_EFFORT", "").strip() or None
        ),
        "baseUrl": (
            os.environ.get("KB_CODEX_BASE_URL") or os.environ.get("OPENAI_BASE_URL")
        ),
        "apiKey": (
            os.environ.get("CODEX_API_KEY") or os.environ.get("OPENAI_API_KEY")
        ),
        "codexHome": str(codex_home),
        "codexPathOverride": os.environ.get("KB_CODEX_BIN"),
        "showProgress": show_progress,
        "verbose": verbose,
    }

    stop_heartbeat = asyncio.Event()
    heartbeat_task: asyncio.Task[None] | None = None
    if show_progress:
        heartbeat_task = asyncio.create_task(
            _agent_heartbeat(
                stop_heartbeat,
                provider="codex",
                model=model or "codex-default",
                cwd=cwd,
            )
        )

    try:
        process = await asyncio.create_subprocess_exec(
            node,
            str(_CODEX_BRIDGE),
            cwd=str(_REPO_ROOT),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout_bytes, stderr_bytes = await process.communicate(
            json.dumps(payload).encode("utf-8")
        )
    finally:
        if heartbeat_task is not None:
            stop_heartbeat.set()
            heartbeat_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await heartbeat_task

    stderr_text = stderr_bytes.decode("utf-8", errors="replace").strip()
    if stderr_text:
        for line in stderr_text.splitlines():
            observability.event(
                "codex event",
                _preview_text(line),
                visible=show_progress or verbose,
            )

    stdout_text = stdout_bytes.decode("utf-8", errors="replace").strip()
    if process.returncode != 0:
        detail = stderr_text or stdout_text or f"node exited with {process.returncode}"
        raise RuntimeError(detail)

    try:
        data = json.loads(stdout_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Codex bridge returned non-JSON output: {stdout_text[:500]}"
        ) from exc
    if not isinstance(data, dict):
        raise RuntimeError("Codex bridge returned an unexpected payload")
    return data


async def _agent_heartbeat(
    stop: asyncio.Event,
    *,
    provider: str,
    model: str,
    cwd: Optional[str],
) -> None:
    interval = _heartbeat_interval()
    if interval <= 0:
        return
    started = time.monotonic()
    while not stop.is_set():
        try:
            await asyncio.wait_for(stop.wait(), timeout=interval)
        except asyncio.TimeoutError:
            elapsed = int(time.monotonic() - started)
            observability.event(
                "agent running",
                f"elapsed={elapsed}s "
                f"provider={provider} model={model} cwd={cwd or os.getcwd()}",
                visible=True,
            )


def _heartbeat_interval() -> int:
    raw = os.environ.get("KB_AGENT_HEARTBEAT_SECONDS", "30")
    try:
        return max(0, int(raw))
    except ValueError:
        return 30


def _preview_text(text: str, *, limit: int = 280) -> str:
    collapsed = " ".join(text.split())
    if len(collapsed) > limit:
        collapsed = collapsed[: limit - 1].rstrip() + "…"
    return f"text chars={len(text)} preview={collapsed!r}"
