"""
LLM runner for kb.

Backend: the **Claude Agent SDK** (``claude-agent-sdk`` on PyPI). It gives
us agentic behaviour (tool use, permission modes, working directory, etc.)
like the old ``claude`` CLI subprocess path did, *and* it reports token
usage via ``ResultMessage.usage`` so :class:`~tools.kb.budget.BudgetTracker`
can hard-enforce budgets on every invocation.

The old two-backend split (raw ``anthropic`` SDK vs ``claude`` CLI
subprocess) existed only because the CLI could not report tokens. The
Agent SDK closes that gap, so this module now has a single code path.
"""

from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass, field
from typing import Optional

from .budget import BudgetExceeded, BudgetTracker
from .models import TokenUsage


@dataclass
class LLMResult:
    text: str = ""
    backend: str = "agent"  # 'agent' | 'dry-run'
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
    cwd: Optional[str] = None,
) -> LLMResult:
    """Run ``prompt`` through the Claude Agent SDK.

    Parameters
    ----------
    prompt
        The user prompt.
    model
        Model alias (``opus``/``sonnet``/``haiku``) or a full model id
        (e.g. ``claude-opus-4-7``). Aliases are expanded below.
    budget
        A :class:`~tools.kb.budget.BudgetTracker`. The ``ResultMessage``
        usage is fed into it; if the response crosses the cap, the
        returned :class:`LLMResult` has ``budget_exceeded=True``.
    dry_run
        When true, return an :class:`LLMResult` describing what would be
        run without touching the SDK.
    permission_mode
        Forwarded to ``ClaudeAgentOptions.permission_mode``. Matches the
        CLI's ``--permission-mode`` values: ``default``, ``acceptEdits``,
        ``plan``, ``dontAsk``, ``bypassPermissions``.
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


def _resolve_model(name: str) -> str:
    return _MODEL_ALIASES.get(name, name)


def _missing_sdk_error() -> Optional[Exception]:
    try:
        import claude_agent_sdk  # noqa: F401
    except Exception as exc:  # noqa: BLE001
        return exc
    return None


def _invoke_agent(
    *,
    prompt: str,
    model: str,
    budget: BudgetTracker,
    permission_mode: str,
    verbose: bool,
    cwd: Optional[str],
) -> LLMResult:
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

    if not os.environ.get("ANTHROPIC_API_KEY"):
        return LLMResult(
            text=(
                "ERROR: ANTHROPIC_API_KEY is not set. Export it before "
                "running LLM-backed commands, for example: "
                "`export ANTHROPIC_API_KEY=<key>`."
            ),
            backend="agent",
            returncode=1,
        )

    resolved_model = _resolve_model(model)

    remaining = budget.remaining()
    if remaining is not None and remaining <= 0:
        return LLMResult(
            text="ERROR: token budget exhausted before agent call",
            backend="agent",
            returncode=1,
            budget_exceeded=True,
        )

    if verbose:
        print(
            f"[kb] agent backend | model={resolved_model} "
            f"permission_mode={permission_mode} budget={budget.limit}"
        )

    try:
        text, budget_exceeded, had_error, error_subtype = asyncio.run(
            _stream_agent(
                prompt=prompt,
                model=resolved_model,
                budget=budget,
                permission_mode=permission_mode,
                cwd=cwd,
            )
        )
    except Exception as exc:  # noqa: BLE001
        return LLMResult(
            text=f"ERROR: claude-agent-sdk call failed: {exc}",
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

    async for msg in query(prompt=prompt, options=options):
        if isinstance(msg, AssistantMessage):
            for block in getattr(msg, "content", None) or []:
                block_text = getattr(block, "text", None)
                if block_text:
                    assistant_text_parts.append(block_text)
        elif isinstance(msg, ResultMessage):
            final_result_text = getattr(msg, "result", None)
            if getattr(msg, "is_error", False):
                had_error = True
                error_subtype = getattr(msg, "subtype", None)
            try:
                budget.add_from_response(msg)
            except BudgetExceeded:
                budget_exceeded = True

    text = final_result_text if final_result_text else "".join(assistant_text_parts)
    return text, budget_exceeded, had_error, error_subtype
