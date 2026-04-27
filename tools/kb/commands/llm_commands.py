"""
LLM-invoking subcommand dispatchers.

Each function here is a thin shim that builds the prompt and delegates
to :func:`tools.kb.commands._common.run_llm_command`. The actual prompt
text lives in :mod:`tools.kb.commands.prompts` so it can be reviewed /
updated without touching runtime logic.
"""

from __future__ import annotations

import dataclasses
import subprocess
from pathlib import Path

from ...compile.review import ReviewerConfig, review_wiki_writes, snapshot_articles
from ..git_util import auto_commit
from ..models import EXIT_ERROR, LLMInvocationResult
from . import prompts
from ._common import CommandContext, run_llm_command, run_plugin_hook


def _raw_snapshot(ctx: CommandContext) -> set[Path]:
    raw_dir = ctx.workspace.raw_dir
    if not raw_dir.exists():
        return set()
    return {path for path in raw_dir.rglob("*.md") if path.is_file()}


def _relative_workspace_paths(ctx: CommandContext, paths: set[Path]) -> list[str]:
    relpaths: list[str] = []
    for path in sorted(paths):
        try:
            relpaths.append(str(path.relative_to(ctx.workspace.kb_dir)))
        except ValueError:
            relpaths.append(str(path))
    return relpaths


def _new_raw_file_args(ctx: CommandContext, before: set[Path]) -> list[str]:
    after = _raw_snapshot(ctx)
    new_files = after - before
    return _relative_workspace_paths(ctx, new_files)


def _append_hook_detail(result: LLMInvocationResult, hook_result) -> None:
    hooks = list(result.details.get("hooks", []))
    hooks.append(hook_result.as_detail())
    result.details["hooks"] = hooks


def _mark_hook_failure(result: LLMInvocationResult, hook_result) -> LLMInvocationResult:
    result.ok = False
    result.exit_code = EXIT_ERROR
    message = f"plugin hook '{hook_result.hook}' failed"
    if hook_result.output:
        message += f":\n{hook_result.output}"
    result.message = f"{result.message.rstrip()}\n{message}" if result.message else message
    return result


def research(ctx: CommandContext, topic: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="research",
        topic=topic,
        prompt_builder=lambda: prompts.RESEARCH_PROMPT.format(topic=topic),
        commit_label=f"research — {topic}",
    )


def ingest(ctx: CommandContext, urls: list[str]) -> LLMInvocationResult:
    urls_str = " ".join(urls)
    commit_label = f"ingest — {urls[0] if urls else 'urls'}"
    before_raw = _raw_snapshot(ctx)
    no_commit_ctx = dataclasses.replace(ctx, no_commit=True)
    result = run_llm_command(
        no_commit_ctx,
        command="ingest",
        topic=urls_str,
        prompt_builder=lambda: prompts.INGEST_PROMPT.format(urls=urls_str),
        commit_label=commit_label,
        pre_hook="pre_ingest",
        post_hook="post_ingest",
        post_hook_args=lambda: _new_raw_file_args(ctx, before_raw),
    )

    if not result.ok or ctx.dry_run:
        return result

    post_compile = run_plugin_hook(ctx, "post_compile")
    _append_hook_detail(result, post_compile)
    if not post_compile.ok:
        return _mark_hook_failure(result, post_compile)

    if not ctx.no_commit:
        committed = auto_commit(ctx.workspace.kb_dir, commit_label, dry_run=False)
        result.committed = committed
        result.commit_label = commit_label if committed else None

    return result


def compile_wiki(ctx: CommandContext) -> LLMInvocationResult:
    # Run the LLM compile step without auto-committing so we can run the
    # decoration-page generators first and include their output in the same
    # commit.
    no_commit_ctx = dataclasses.replace(ctx, no_commit=True)
    result = run_llm_command(
        no_commit_ctx,
        command="compile",
        topic=None,
        prompt_builder=lambda: prompts.COMPILE_PROMPT,
        commit_label="compile wiki",
        pre_hook="pre_compile",
    )

    if not result.ok or ctx.dry_run:
        return result

    decoration_snapshot = snapshot_articles(ctx.workspace.wiki_dir)

    # Run decoration-page generators (Dashboard, Graph, Tags, Glossary,
    # Changelog) using the workspace copy so --dir <workspace> writes to the
    # right place.
    generate_all = ctx.workspace.kb_dir / "tools" / "compile" / "pages" / "generate_all.py"
    proc = subprocess.run(
        ["python3", str(generate_all)],
        cwd=str(ctx.workspace.kb_dir),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        result.ok = False
        result.exit_code = EXIT_ERROR
        diag = (proc.stderr or proc.stdout or "").strip()
        result.message = (
            f"generate_all.py failed; decoration pages not updated"
            + (f":\n{diag}" if diag else "")
        )

    review_outcome = review_wiki_writes(
        ctx.workspace.kb_dir,
        before_snapshot=decoration_snapshot,
        config=ReviewerConfig.from_env(),
    )
    if review_outcome.candidates:
        result.details["post_decoration_review"] = review_outcome.as_dict()
    if not review_outcome.ok:
        result.ok = False
        result.exit_code = EXIT_ERROR
        review_message = (
            "post-decoration compile review rejected wiki writes:\n"
            + review_outcome.rejection_summary()
        )
        result.message = (
            f"{result.message}\n\n{review_message}"
            if result.message
            else review_message
        )
        return result
    if not result.ok:
        return result

    post_hook = run_plugin_hook(ctx, "post_compile")
    _append_hook_detail(result, post_hook)
    if not post_hook.ok:
        return _mark_hook_failure(result, post_hook)

    # Auto-commit the full compile output (LLM changes + decoration pages).
    if not ctx.no_commit:
        committed = auto_commit(ctx.workspace.kb_dir, "compile wiki", dry_run=False)
        result.committed = committed
        result.commit_label = "compile wiki" if committed else None

    return result


def ask(ctx: CommandContext, question: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="ask",
        topic=question,
        prompt_builder=lambda: prompts.ASK_PROMPT.format(question=question),
        commit_label=f"query — {question[:50]}",
        pre_hook="pre_query",
        pre_hook_args=[question],
        post_hook="post_query",
        post_hook_args=[question],
    )


def lint(ctx: CommandContext) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="lint",
        topic=None,
        prompt_builder=lambda: prompts.LINT_PROMPT,
        commit_label="lint + gap fill",
        post_hook="on_lint",
    )


def slides(ctx: CommandContext, topic: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="slides",
        topic=topic,
        prompt_builder=lambda: prompts.SLIDES_PROMPT.format(topic=topic),
        commit_label=f"generate slides — {topic}",
    )


def report(ctx: CommandContext, topic: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="report",
        topic=topic,
        prompt_builder=lambda: prompts.REPORT_PROMPT.format(topic=topic),
        commit_label=f"report — {topic}",
    )


def compare(ctx: CommandContext, x: str, y: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="compare",
        topic=f"{x} vs {y}",
        prompt_builder=lambda: prompts.COMPARE_PROMPT.format(x=x, y=y),
        commit_label=f"compare — {x} vs {y}",
    )


def entity(ctx: CommandContext, name: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="entity",
        topic=name,
        prompt_builder=lambda: prompts.ENTITY_PROMPT.format(name=name),
        commit_label=f"entity — {name}",
    )


def discover(ctx: CommandContext) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="discover",
        topic=None,
        prompt_builder=lambda: prompts.DISCOVER_PROMPT,
        commit_label="discover — auto-fill gaps",
    )


def freeform(ctx: CommandContext, prompt: str) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="freeform",
        topic=prompt,
        prompt_builder=lambda: prompt,
        commit_label=prompt[:60],
    )
