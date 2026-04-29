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
from pathlib import Path
import subprocess
import sys
from typing import Callable, Optional, Sequence

from kb import observability
from kb.budget import BudgetExceeded, BudgetTracker
from kb.git_util import auto_commit
from kb.models import (
    EXIT_ABORT,
    EXIT_BUDGET,
    EXIT_ERROR,
    EXIT_NOOP,
    EXIT_SUCCESS,
    LLMInvocationResult,
    TokenUsage,
)
from kb.runner import invoke_llm
from kb.workspace import Workspace
from tools.compile.review import ReviewerConfig, review_wiki_writes, snapshot_articles


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
    workspace_source: str = "unknown"
    run_log_path: Path | None = None
    show_progress: bool = False

    def new_budget(self) -> BudgetTracker:
        return BudgetTracker(limit=self.budget_limit)

    def should_show_progress(self) -> bool:
        return not self.json_output and (self.show_progress or self.verbose)


@dataclass
class PluginHookResult:
    """Result from invoking one plugin hook through the framework CLI."""

    hook: str
    ok: bool
    exit_code: int = 0
    output: str = ""
    skipped: bool = False

    def as_detail(self) -> dict[str, object]:
        return {
            "hook": self.hook,
            "ok": self.ok,
            "exit_code": self.exit_code,
            "output": self.output,
            "skipped": self.skipped,
        }


# --------------------------------------------------------------------------- #
#  LLM command helper
# --------------------------------------------------------------------------- #


PromptBuilder = Callable[[], str]
HookArgs = Sequence[str] | Callable[[], Sequence[str]]


def _resolve_hook_args(args: HookArgs | None) -> list[str]:
    if args is None:
        return []
    resolved = args() if callable(args) else args
    return [str(arg) for arg in resolved]


def _append_message(existing: Optional[str], extra: str) -> str:
    if existing:
        return f"{existing.rstrip()}\n{extra}"
    return extra


def run_plugin_hook(
    ctx: CommandContext,
    hook_name: str,
    args: HookArgs | None = None,
) -> PluginHookResult:
    """Run one plugin hook against the active workspace.

    The plugin framework computes its root from the location of
    ``framework.py``, so invoke the workspace copy rather than importing the
    install copy. Capturing output keeps ``--json`` callers parseable; normal
    terminal callers still see plugin output before the command result.
    """
    hook_args = _resolve_hook_args(args)
    if ctx.dry_run:
        return PluginHookResult(hook=hook_name, ok=True, skipped=True)

    framework = ctx.workspace.kb_dir / "tools" / "plugins" / "framework.py"
    if not framework.exists():
        output = f"[plugin] Framework not found at {framework}; skipped {hook_name}"
        if not ctx.json_output:
            print(output, file=sys.stderr)
        return PluginHookResult(
            hook=hook_name,
            ok=True,
            skipped=True,
            output=output,
        )

    proc = subprocess.run(
        [sys.executable or "python3", str(framework), "run", hook_name, *hook_args],
        cwd=str(ctx.workspace.kb_dir),
        capture_output=True,
        text=True,
        check=False,
    )
    output = "\n".join(
        part.rstrip()
        for part in (proc.stdout, proc.stderr)
        if part and part.strip()
    )
    if output and not ctx.json_output:
        print(output)
    return PluginHookResult(
        hook=hook_name,
        ok=proc.returncode == 0,
        exit_code=proc.returncode,
        output=output,
    )


def _plugin_hook_failed_message(hook_result: PluginHookResult) -> str:
    message = f"plugin hook '{hook_result.hook}' failed"
    if hook_result.output:
        message += f":\n{hook_result.output}"
    return message


def run_llm_command(
    ctx: CommandContext,
    *,
    command: str,
    topic: Optional[str],
    prompt_builder: PromptBuilder,
    commit_label: str,
    pre_hook: str | None = None,
    pre_hook_args: HookArgs | None = None,
    post_hook: str | None = None,
    post_hook_args: HookArgs | None = None,
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

    observability.event(
        "workspace",
        f"ready path={ctx.workspace.kb_dir} source={ctx.workspace_source}",
        visible=ctx.should_show_progress(),
    )
    ctx.workspace.ensure_dirs()
    hook_details: list[dict[str, object]] = []
    if pre_hook:
        observability.event(
            "hook",
            f"running {pre_hook}",
            visible=ctx.should_show_progress(),
        )
        pre_result = run_plugin_hook(ctx, pre_hook, pre_hook_args)
        hook_details.append(pre_result.as_detail())
        if not pre_result.ok:
            observability.event(
                "hook",
                f"failed {pre_hook} exit_code={pre_result.exit_code}",
                visible=ctx.should_show_progress(),
            )
            return LLMInvocationResult(
                command=command,
                topic=topic,
                ok=False,
                exit_code=EXIT_ERROR,
                budget_limit=ctx.budget_limit,
                model=ctx.model,
                message=_plugin_hook_failed_message(pre_result),
                details={"hooks": hook_details},
            )

    article_snapshot = snapshot_articles(ctx.workspace.wiki_dir)
    budget = ctx.new_budget()
    observability.event(
        "llm",
        f"command={command} workspace={ctx.workspace.kb_dir}",
        visible=ctx.should_show_progress(),
    )

    try:
        observability.event(
            "prompt",
            f"building command={command}",
            visible=ctx.verbose and not ctx.json_output,
        )
        prompt = prompt_builder()
        observability.event(
            "agent",
            f"starting command={command} model={ctx.model} budget={ctx.budget_limit}",
            visible=ctx.should_show_progress(),
        )
        llm_result = invoke_llm(
            prompt=prompt,
            model=ctx.model,
            budget=budget,
            dry_run=False,
            permission_mode=ctx.permission_mode,
            verbose=ctx.verbose,
            show_progress=ctx.should_show_progress(),
            cwd=str(ctx.workspace.kb_dir),
        )
    except BudgetExceeded as exc:
        return LLMInvocationResult(
            command=command,
            topic=topic,
            ok=False,
            exit_code=EXIT_BUDGET,
            budget_limit=ctx.budget_limit,
            # Rebuild from explicit fields rather than ``**usage.__dict__``:
            # pydantic v2 keeps private attrs (``__pydantic_*``) on __dict__
            # and those leak into the constructor and trip validation.
            usage=TokenUsage(
                input_tokens=exc.usage.input_tokens,
                output_tokens=exc.usage.output_tokens,
                cache_creation_input_tokens=exc.usage.cache_creation_input_tokens,
                cache_read_input_tokens=exc.usage.cache_read_input_tokens,
            ),
            model=ctx.model,
            message=str(exc),
            details={"hooks": hook_details} if hook_details else {},
        )

    # Route raw LLM text: keep it in ``message`` for non-JSON users (the CLI
    # renderer falls back to printing ``message`` for LLM commands), but in
    # --json mode stash it under ``details["raw_output"]`` so the structured
    # payload stays structured. ``details["backend"]`` is always populated.
    raw_text = llm_result.text if llm_result.text else None
    details: dict[str, object] = {"backend": llm_result.backend}
    if ctx.json_output and raw_text is not None:
        details["raw_output"] = raw_text
        rendered_message: Optional[str] = f"{command}: backend={llm_result.backend}"
    else:
        rendered_message = raw_text

    observability.event(
        "review",
        "scanning changed wiki writes",
        visible=ctx.should_show_progress(),
    )
    review_outcome = review_wiki_writes(
        ctx.workspace.kb_dir,
        before_snapshot=article_snapshot,
        config=ReviewerConfig.from_env(),
    )
    observability.event(
        "review",
        f"candidates={review_outcome.candidates} "
        f"accepted={len(review_outcome.accepted)} "
        f"rejected={len(review_outcome.rejected)} "
        f"quarantine={review_outcome.quarantine_batch or 'none'}",
        visible=ctx.should_show_progress(),
    )
    if review_outcome.candidates:
        details["compile_review"] = review_outcome.as_dict()

    result = LLMInvocationResult(
        command=command,
        topic=topic,
        prompt=(prompt[:400] if ctx.verbose else None),
        budget_limit=ctx.budget_limit,
        usage=TokenUsage(
            input_tokens=budget.usage.input_tokens,
            output_tokens=budget.usage.output_tokens,
            cache_creation_input_tokens=budget.usage.cache_creation_input_tokens,
            cache_read_input_tokens=budget.usage.cache_read_input_tokens,
        ),
        model=ctx.model,
        ok=(
            llm_result.returncode == 0
            and not llm_result.budget_exceeded
            and review_outcome.ok
        ),
        exit_code=(
            EXIT_BUDGET
            if llm_result.budget_exceeded
            else (
                EXIT_SUCCESS
                if llm_result.returncode == 0 and review_outcome.ok
                else EXIT_ERROR
            )
        ),
        message=rendered_message,
        details=details,
    )
    if hook_details:
        result.details["hooks"] = hook_details

    if result.ok and post_hook:
        observability.event(
            "hook",
            f"running {post_hook}",
            visible=ctx.should_show_progress(),
        )
        post_result = run_plugin_hook(ctx, post_hook, post_hook_args)
        hook_details.append(post_result.as_detail())
        result.details["hooks"] = hook_details
        if not post_result.ok:
            observability.event(
                "hook",
                f"failed {post_hook} exit_code={post_result.exit_code}",
                visible=ctx.should_show_progress(),
            )
            result.ok = False
            result.exit_code = EXIT_ERROR
            result.message = _append_message(
                result.message,
                _plugin_hook_failed_message(post_result),
            )

    if not review_outcome.ok:
        review_message = (
            "compile review rejected wiki writes:\n"
            + review_outcome.rejection_summary()
        )
        result.message = (
            f"{rendered_message}\n\n{review_message}"
            if rendered_message
            else review_message
        )

    # Auto-commit on success
    if result.ok and not ctx.no_commit and not ctx.dry_run:
        observability.event(
            "git",
            f"auto-commit label={commit_label!r}",
            visible=ctx.should_show_progress(),
        )
        committed = auto_commit(ctx.workspace.kb_dir, commit_label, dry_run=False)
        result.committed = committed
        result.commit_label = commit_label if committed else None
        observability.event(
            "git",
            f"auto-commit committed={committed}",
            visible=ctx.should_show_progress(),
        )

    observability.event(
        "result",
        f"command={command} ok={result.ok} exit_code={result.exit_code} "
        f"tokens={result.usage.total}",
        visible=ctx.should_show_progress(),
    )

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
    "PluginHookResult",
    "run_plugin_hook",
    "run_llm_command",
]
