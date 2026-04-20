"""
Shared helpers for typed kb subcommands.

Every command receives a :class:`CommandContext` built in ``cli.py`` and
returns a pydantic result. The :func:`run_llm_command` helper centralises
budget enforcement, dry-run handling, commit labelling and exit codes for
the family of LLM-invoking subcommands (research, ingest, compile, ask,
lint, slides, report, compare, entity, discover, freeform).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from ..budget import BudgetExceeded, BudgetTracker
from ..git_util import auto_commit
from ..models import (
    EXIT_ABORT,
    EXIT_BUDGET,
    EXIT_ERROR,
    EXIT_NOOP,
    EXIT_SUCCESS,
    LLMInvocationResult,
    TokenUsage,
)
from ..runner import invoke_llm
from ..workspace import Workspace


@dataclass
class CommandContext:
    """Per-invocation runtime settings shared by every subcommand."""

    workspace: Workspace
    model: str = "opus"
    budget_limit: Optional[int] = None
    dry_run: bool = False
    no_commit: bool = False
    verbose: bool = False
    json_output: bool = False
    permission_mode: str = "bypassPermissions"
    force_backend: Optional[str] = None

    def new_budget(self) -> BudgetTracker:
        return BudgetTracker(limit=self.budget_limit)


# --------------------------------------------------------------------------- #
#  LLM command helper
# --------------------------------------------------------------------------- #


PromptBuilder = Callable[[], str]


def run_llm_command(
    ctx: CommandContext,
    *,
    command: str,
    topic: Optional[str],
    prompt_builder: PromptBuilder,
    commit_label: str,
) -> LLMInvocationResult:
    """Boilerplate used by every LLM-invoking subcommand.

    Handles:
      - Dry-run short-circuit (no LLM call, no filesystem writes)
      - Budget tracking via :class:`BudgetTracker`
      - ``BudgetExceeded`` -> exit code 2
      - Auto-commit on success
    """
    if ctx.dry_run:
        # Do NOT create workspace dirs on dry-run — keep it fully side-effect
        # free so users can preview commands against arbitrary paths.
        return LLMInvocationResult(
            command=command,
            topic=topic,
            prompt=prompt_builder()[:400],
            dry_run=True,
            budget_limit=ctx.budget_limit,
            model=ctx.model,
            message=f"[dry-run] {command}: would run LLM prompt",
            exit_code=EXIT_SUCCESS,
        )

    ctx.workspace.ensure_dirs()
    budget = ctx.new_budget()

    try:
        prompt = prompt_builder()
        llm_result = invoke_llm(
            prompt=prompt,
            model=ctx.model,
            budget=budget,
            dry_run=False,
            permission_mode=ctx.permission_mode,
            force_backend=ctx.force_backend,
            verbose=ctx.verbose,
        )
    except BudgetExceeded as exc:
        return LLMInvocationResult(
            command=command,
            topic=topic,
            ok=False,
            exit_code=EXIT_BUDGET,
            budget_limit=ctx.budget_limit,
            usage=TokenUsage(**exc.usage.__dict__),
            model=ctx.model,
            message=str(exc),
        )

    result = LLMInvocationResult(
        command=command,
        topic=topic,
        prompt=(prompt[:400] if ctx.verbose else None),
        budget_limit=ctx.budget_limit,
        usage=TokenUsage(**budget.usage.__dict__),
        model=ctx.model,
        ok=llm_result.returncode == 0 and not llm_result.budget_exceeded,
        exit_code=(
            EXIT_BUDGET
            if llm_result.budget_exceeded
            else (EXIT_SUCCESS if llm_result.returncode == 0 else EXIT_ERROR)
        ),
        # Do not truncate LLM output here — downstream rendering consumes the
        # full text (progress updates, file paths, etc.). Any serialization
        # bounds should be applied at the serialization site, not here.
        message=llm_result.text if llm_result.text else None,
        details={"backend": llm_result.backend},
    )

    # Auto-commit on success
    if result.ok and not ctx.no_commit and not ctx.dry_run:
        committed = auto_commit(ctx.workspace.kb_dir, commit_label, dry_run=False)
        result.committed = committed
        result.commit_label = commit_label if committed else None

    return result


# --------------------------------------------------------------------------- #
#  Exit-code helpers for non-LLM commands
# --------------------------------------------------------------------------- #


def noop(command: str, message: str) -> LLMInvocationResult:
    return LLMInvocationResult(
        command=command,
        ok=True,
        exit_code=EXIT_NOOP,
        message=message,
    )


def error(command: str, message: str, exit_code: int = EXIT_ERROR) -> LLMInvocationResult:
    return LLMInvocationResult(
        command=command,
        ok=False,
        exit_code=exit_code,
        message=message,
    )


__all__ = [
    "CommandContext",
    "EXIT_ABORT",
    "EXIT_BUDGET",
    "EXIT_ERROR",
    "EXIT_NOOP",
    "EXIT_SUCCESS",
    "auto_commit",
    "error",
    "noop",
    "run_llm_command",
]
