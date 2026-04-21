"""User-facing entrypoint for the Python ``kb`` CLI."""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from typing import Callable, Sequence

from .commands import export as export_cmd
from .commands import init as init_cmd
from .commands import llm_commands, log as log_cmd, search as search_cmd
from .commands import serve as serve_cmd
from .commands import stats as stats_cmd
from .commands import test_cmd, viz as viz_cmd, workspaces as workspaces_cmd
from .commands._common import CommandContext, error
from .models import (
    CommandResult,
    EXIT_ERROR,
    ExportResult,
    InitResult,
    LLMInvocationResult,
    LogResult,
    SearchResult,
    ServeResult,
    StatsResult,
    TestResult,
    VizResult,
    WorkspacesResult,
)
from .workspace import Workspace


_URL_RE = re.compile(r"https?://\S+")
_QUESTION_RE = re.compile(
    r"^(who|what|when|where|why|how|can|could|should|would|is|are|do|does|did)\b",
    re.IGNORECASE,
)


@dataclass
class GlobalOptions:
    json_output: bool = False
    verbose: bool = False
    dry_run: bool = False
    no_commit: bool = False
    model: str | None = None
    budget: int | None = None
    dir_flag: str | None = None
    permission_mode: str | None = None


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    opts, remaining = _parse_global_options(args)

    if not remaining or remaining[0] in {"help", "-h", "--help"}:
        _print_help()
        return 0

    ctx = _build_context(opts)
    command = remaining[0]
    command_args = remaining[1:]

    try:
        if command in {"-i", "--interactive"}:
            result = _run_interactive(ctx)
        else:
            handler = _COMMANDS.get(command)
            result = (
                handler(ctx, command_args)
                if handler is not None
                else _smart_route(ctx, " ".join(remaining).strip())
            )
    except SystemExit as exc:
        if isinstance(exc.code, int):
            return int(exc.code)
        if exc.code is not None:
            print(exc.code, file=sys.stderr)
        return EXIT_ERROR

    _render_result(result, json_output=ctx.json_output)
    return int(result.exit_code)


def _parse_budget_value(value: str, *, source: str) -> int:
    try:
        budget = int(value)
    except ValueError as exc:
        raise SystemExit(f"invalid {source} value: expected integer") from exc
    if budget <= 0:
        raise SystemExit(f"invalid {source} value: expected a positive integer")
    return budget


def _parse_global_options(argv: Sequence[str]) -> tuple[GlobalOptions, list[str]]:
    opts = GlobalOptions()
    remaining: list[str] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--json":
            opts.json_output = True
        elif arg in {"--verbose", "-v"}:
            opts.verbose = True
        elif arg == "--dry-run":
            opts.dry_run = True
        elif arg == "--no-commit":
            opts.no_commit = True
        elif arg in {"--model", "--budget", "--dir", "-d", "--permission-mode"}:
            if i + 1 >= len(argv):
                raise SystemExit(f"missing value for {arg}")
            value = argv[i + 1]
            if arg == "--model":
                opts.model = value
            elif arg == "--budget":
                opts.budget = _parse_budget_value(value, source="--budget")
            elif arg in {"--dir", "-d"}:
                opts.dir_flag = value
            else:
                opts.permission_mode = value
            i += 1
        elif arg.startswith("--model="):
            opts.model = arg.split("=", 1)[1]
        elif arg.startswith("--budget="):
            opts.budget = _parse_budget_value(
                arg.split("=", 1)[1],
                source="--budget",
            )
        elif arg.startswith("--dir="):
            opts.dir_flag = arg.split("=", 1)[1]
        elif arg.startswith("--permission-mode="):
            opts.permission_mode = arg.split("=", 1)[1]
        else:
            remaining.append(arg)
        i += 1
    return opts, remaining


def _build_context(opts: GlobalOptions) -> CommandContext:
    env_budget = os.environ.get("KB_TOKEN_BUDGET")
    budget_limit = opts.budget
    if budget_limit is None and env_budget:
        budget_limit = _parse_budget_value(env_budget, source="KB_TOKEN_BUDGET")

    return CommandContext(
        workspace=Workspace.resolve(
            kb_home=None, kb_dir=None, dir_flag=opts.dir_flag, dry_run=opts.dry_run,
        ),
        model=opts.model or os.environ.get("KB_MODEL", "opus"),
        budget_limit=budget_limit,
        dry_run=opts.dry_run,
        no_commit=opts.no_commit or os.environ.get("KB_NO_COMMIT") == "1",
        verbose=opts.verbose,
        json_output=opts.json_output,
        permission_mode=opts.permission_mode
        or os.environ.get("KB_PERMISSION_MODE", "bypassPermissions"),
        force_backend=os.environ.get("KB_FORCE_BACKEND"),
    )


def _parse_command(
    prog: str,
    args: Sequence[str],
    setup: Callable[[argparse.ArgumentParser], None],
) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=prog)
    setup(parser)
    return parser.parse_args(list(args))


def _run_research(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb research", args, lambda p: p.add_argument("topic", nargs="+"))
    return llm_commands.research(ctx, " ".join(ns.topic))


def _run_ingest(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb ingest", args, lambda p: p.add_argument("urls", nargs="+"))
    return llm_commands.ingest(ctx, ns.urls)


def _run_compile(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    _parse_command("kb compile", args, lambda p: None)
    return llm_commands.compile_wiki(ctx)


def _run_ask(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb ask", args, lambda p: p.add_argument("question", nargs="+"))
    return llm_commands.ask(ctx, " ".join(ns.question))


def _run_lint(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    _parse_command("kb lint", args, lambda p: None)
    return llm_commands.lint(ctx)


def _run_search(ctx: CommandContext, args: Sequence[str]) -> SearchResult:
    def setup(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("query", nargs="+")
        parser.add_argument("--top", type=int, default=10)

    ns = _parse_command("kb search", args, setup)
    return search_cmd.run(ctx, " ".join(ns.query), top_k=ns.top)


def _run_slides(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb slides", args, lambda p: p.add_argument("topic", nargs="+"))
    return llm_commands.slides(ctx, " ".join(ns.topic))


def _run_report(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb report", args, lambda p: p.add_argument("topic", nargs="+"))
    return llm_commands.report(ctx, " ".join(ns.topic))


def _run_compare(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    def setup(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("x")
        parser.add_argument("y")

    ns = _parse_command("kb compare", args, setup)
    return llm_commands.compare(ctx, ns.x, ns.y)


def _run_entity(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb entity", args, lambda p: p.add_argument("name", nargs="+"))
    return llm_commands.entity(ctx, " ".join(ns.name))


def _run_export(ctx: CommandContext, args: Sequence[str]) -> ExportResult:
    ns = _parse_command(
        "kb export",
        args,
        lambda p: p.add_argument("format", nargs="?", default="site"),
    )
    return export_cmd.run(ctx, ns.format)


def _run_viz(ctx: CommandContext, args: Sequence[str]) -> VizResult:
    ns = _parse_command(
        "kb viz",
        args,
        lambda p: p.add_argument("viz_type", nargs="?", default="stats"),
    )
    return viz_cmd.run(ctx, ns.viz_type)


def _run_discover(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    _parse_command("kb discover", args, lambda p: None)
    return llm_commands.discover(ctx)


def _run_test(ctx: CommandContext, args: Sequence[str]) -> TestResult:
    _parse_command("kb test", args, lambda p: None)
    return test_cmd.run(ctx)


def _run_log(ctx: CommandContext, args: Sequence[str]) -> LogResult:
    def setup(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("n", nargs="?", type=int, default=10)
        parser.add_argument("--all", action="store_true")

    ns = _parse_command("kb log", args, setup)
    return log_cmd.run(ctx, n=ns.n, all_entries=ns.all)


def _run_stats(ctx: CommandContext, args: Sequence[str]) -> StatsResult:
    _parse_command("kb stats", args, lambda p: None)
    return stats_cmd.run(ctx)


def _run_serve(ctx: CommandContext, args: Sequence[str]) -> ServeResult:
    def setup(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("port", nargs="?", type=int, default=8765)

    ns = _parse_command("kb serve", args, setup)
    return serve_cmd.run_serve(ctx, port=ns.port)


def _run_mcp(ctx: CommandContext, args: Sequence[str]) -> ServeResult:
    return serve_cmd.run_mcp(ctx, args=list(args))


def _run_init(ctx: CommandContext, args: Sequence[str]) -> InitResult:
    ns = _parse_command(
        "kb init",
        args,
        lambda p: p.add_argument("target", nargs="?"),
    )
    return init_cmd.run_init(ctx, target=ns.target, dry_run=ctx.dry_run)


def _run_new(ctx: CommandContext, args: Sequence[str]) -> InitResult:
    def setup(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("name")
        parser.add_argument("base", nargs="?")

    ns = _parse_command("kb new", args, setup)
    return init_cmd.run_new(ctx, ns.name, base=ns.base, dry_run=ctx.dry_run)


def _run_workspaces(ctx: CommandContext, args: Sequence[str]) -> WorkspacesResult:
    ns = _parse_command(
        "kb workspaces",
        args,
        lambda p: p.add_argument("base", nargs="?"),
    )
    return workspaces_cmd.run(ctx, base=ns.base)


def _run_interactive(ctx: CommandContext) -> CommandResult:
    if ctx.json_output or ctx.dry_run:
        return CommandResult(
            command="interactive",
            ok=True,
            exit_code=0,
            dry_run=ctx.dry_run,
            message="interactive session descriptor (not started in --json/--dry-run mode)",
        )

    try:
        os.execvp(
            "claude",
            [
                "claude",
                "--permission-mode",
                ctx.permission_mode,
                "--model",
                ctx.model,
                "--effort",
                "max",
            ],
        )
    except OSError as exc:
        return error(
            "interactive",
            f"failed to launch Claude CLI ({exc}); is `claude` installed on PATH?",
        )
    # Unreachable on success — execvp replaces this process.
    return error("interactive", "failed to launch Claude CLI")


def _smart_route(ctx: CommandContext, text: str) -> LLMInvocationResult:
    if not text:
        return error("freeform", "empty input")

    urls = _URL_RE.findall(text)
    if urls:
        return llm_commands.ingest(ctx, urls)
    if text.endswith("?") or _QUESTION_RE.match(text):
        return llm_commands.ask(ctx, text)
    if len(text.split()) <= 6:
        return llm_commands.research(ctx, text)
    return llm_commands.freeform(ctx, text)


def _model_dump_json(result: CommandResult) -> str:
    if hasattr(result, "model_dump_json"):
        return result.model_dump_json(indent=2)
    return result.json(indent=2)


def _render_result(result: CommandResult, *, json_output: bool) -> None:
    if json_output:
        print(_model_dump_json(result))
        return

    if isinstance(result, SearchResult):
        if result.message and not result.hits:
            print(result.message.strip())
            return
        if not result.hits:
            print(f'No results for "{result.query}"')
            return
        print(f'Search results for "{result.query}" ({result.backend})')
        for idx, hit in enumerate(result.hits, start=1):
            title = hit.title or hit.path
            score = f" score={hit.score:.4f}" if hit.score is not None else ""
            print(f"{idx}. {title}{score}")
            print(f"   file: {hit.path}")
            if hit.snippet:
                print(f"   {hit.snippet}")
        return

    if isinstance(result, StatsResult):
        print(
            f"Wiki files: {result.total_wiki_files} | "
            f"Wiki words: {result.total_wiki_words} | "
            f"Raw words: {result.total_raw_words}"
        )
        for section in result.sections:
            print(
                f"{section.name} files={section.files} words={section.words}"
                + (
                    f" last_modified={section.last_modified}"
                    if section.last_modified
                    else ""
                )
            )
        return

    if isinstance(result, LogResult):
        if not result.entries:
            print("No log entries found.")
            return
        print("\n\n".join(result.entries))
        return

    if isinstance(result, TestResult):
        print(
            f"Test suites: total={result.total} passed={result.passed} failed={result.failed}"
        )
        for suite in result.suites:
            status = "PASS" if suite.passed else "FAIL"
            print(f"{status} {suite.name} (rc={suite.returncode})")
        if result.message:
            print(result.message.strip())
        return

    if isinstance(result, WorkspacesResult):
        for entry in result.workspaces:
            default = " (default)" if entry.is_default else ""
            print(f"{entry.name}{default}: {entry.path} [{entry.articles} articles]")
        return

    if isinstance(result, InitResult):
        if result.message:
            print(result.message)
        for path in result.created_files:
            print(path)
        return

    if result.message:
        print(result.message.strip())


def _print_help() -> None:
    print(
        """kb — Python CLI for the LLM knowledge base

Usage:
  kb <command> [args] [--json] [--verbose] [--dry-run] [--no-commit]
  kb "<natural language prompt>"

Commands:
  research <topic>
  ingest <url> [urls...]
  compile
  ask <question>
  lint
  search <query> [--top N]
  slides <topic>
  report <topic>
  compare <x> <y>
  entity <name>
  export [site|pdf|epub|bundle]
  viz [graph|timeline|stats|concept-map|canvas|all]
  discover
  test
  log [n] [--all]
  stats
  init [path]
  new <name> [base]
  workspaces
  serve [port]
  mcp [args...]
  -i | --interactive

Global flags:
  --dir, -d <name|path>
  --model <model>
  --budget <tokens>
  --permission-mode <mode>
  --json
  --verbose, -v
  --dry-run
  --no-commit
"""
    )


_COMMANDS: dict[str, Callable[[CommandContext, Sequence[str]], CommandResult]] = {
    "research": _run_research,
    "ingest": _run_ingest,
    "compile": _run_compile,
    "ask": _run_ask,
    "lint": _run_lint,
    "search": _run_search,
    "slides": _run_slides,
    "report": _run_report,
    "compare": _run_compare,
    "entity": _run_entity,
    "export": _run_export,
    "viz": _run_viz,
    "discover": _run_discover,
    "test": _run_test,
    "log": _run_log,
    "stats": _run_stats,
    "serve": _run_serve,
    "mcp": _run_mcp,
    "init": _run_init,
    "new": _run_new,
    "workspaces": _run_workspaces,
    "ws": _run_workspaces,
}


if __name__ == "__main__":
    raise SystemExit(main())
