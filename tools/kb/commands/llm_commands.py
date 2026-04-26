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

from tools.compile import manifest as compile_manifest

from ..git_util import auto_commit
from ..models import EXIT_ERROR, EXIT_SUCCESS, LLMInvocationResult
from . import prompts
from ._common import CommandContext, run_llm_command


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
    return run_llm_command(
        ctx,
        command="ingest",
        topic=urls_str,
        prompt_builder=lambda: prompts.INGEST_PROMPT.format(urls=urls_str),
        commit_label=f"ingest — {urls[0] if urls else 'urls'}",
    )


def compile_wiki(ctx: CommandContext) -> LLMInvocationResult:
    regen_meta = ctx.workspace.kb_home / "tools" / "compile" / "regen_meta.py"
    if not regen_meta.exists():
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_ERROR,
            dry_run=ctx.dry_run,
            budget_limit=ctx.budget_limit,
            model=ctx.model,
            message=f"Missing regen_meta script: {regen_meta}",
        )

    plan = compile_manifest.plan_compile(ctx.workspace.kb_dir)

    if plan.is_noop:
        manifest_written = False
        if not ctx.dry_run and (plan.sources or plan.manifest):
            manifest_written = compile_manifest.save_manifest_if_changed(
                ctx.workspace.kb_dir,
                compile_manifest.build_current_manifest(plan),
            )

        details = compile_manifest.describe_plan(plan)
        details.update(
            {
                "noop": True,
                "llm_skipped": True,
                "manifest_written": manifest_written,
            }
        )
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=True,
            exit_code=EXIT_SUCCESS,
            dry_run=ctx.dry_run,
            budget_limit=ctx.budget_limit,
            model=ctx.model,
            message="compile: no changed raw sources; LLM skipped",
            details=details,
        )

    # Run the LLM compile step without auto-committing so we can run the
    # decoration-page generators first and include their output in the same
    # commit.
    no_commit_ctx = dataclasses.replace(ctx, no_commit=True)
    before_outputs = compile_manifest.snapshot_wiki_outputs(ctx.workspace.kb_dir)
    result = run_llm_command(
        no_commit_ctx,
        command="compile",
        topic=None,
        prompt_builder=lambda: compile_manifest.scoped_compile_prompt(
            plan.changed_sources
        ),
        commit_label="compile wiki",
    )
    result.details = {
        **(result.details or {}),
        **compile_manifest.describe_plan(plan),
        "noop": False,
        "llm_skipped": False,
    }

    if not result.ok or ctx.dry_run:
        return result

    after_llm_outputs = compile_manifest.snapshot_wiki_outputs(ctx.workspace.kb_dir)
    output_paths = compile_manifest.changed_outputs(before_outputs, after_llm_outputs)

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
        return result

    manifest_written = compile_manifest.save_manifest_if_changed(
        ctx.workspace.kb_dir,
        compile_manifest.build_updated_manifest(
            plan,
            compiled_sources=plan.changed_sources,
            changed_output_paths=output_paths,
            available_output_paths=list(after_llm_outputs),
            compiled_at=compile_manifest.utc_now(),
        ),
    )
    result.details.update(
        {
            "outputs": output_paths,
            "manifest_written": manifest_written,
        }
    )

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
    )


def lint(ctx: CommandContext) -> LLMInvocationResult:
    return run_llm_command(
        ctx,
        command="lint",
        topic=None,
        prompt_builder=lambda: prompts.LINT_PROMPT,
        commit_label="lint + gap fill",
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
