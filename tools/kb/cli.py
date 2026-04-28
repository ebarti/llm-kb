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
from .commands import queue as queue_cmd
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
    QueueResult,
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

_ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[0;34m",
    "magenta": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[1;37m",
}


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


@dataclass(frozen=True)
class TerminalTheme:
    enabled: bool
    ok: str
    fail: str
    warn: str
    info: str
    bullet: str
    arrow: str
    spark: str

    def color(self, text: object, *styles: str) -> str:
        value = str(text)
        if not self.enabled:
            return value
        prefix = "".join(_ANSI[style] for style in styles if style in _ANSI)
        if not prefix:
            return value
        return f"{prefix}{value}{_ANSI['reset']}"

    def heading(self, text: str) -> str:
        return self.color(text, "bold", "white")

    def dim(self, text: object) -> str:
        return self.color(text, "dim")


def _color_enabled(stream: object | None = None) -> bool:
    stream = sys.stdout if stream is None else stream
    setting = os.environ.get("KB_COLOR", "auto").strip().lower()
    if setting in {"1", "always", "force", "on", "true", "yes"}:
        return True
    if setting in {"0", "never", "off", "false", "no"}:
        return False
    if os.environ.get("NO_COLOR") is not None:
        return False
    isatty = getattr(stream, "isatty", None)
    return bool(isatty and isatty())


def _theme(stream: object | None = None) -> TerminalTheme:
    enabled = _color_enabled(stream)
    return TerminalTheme(
        enabled=enabled,
        ok="✓" if enabled else "[ok]",
        fail="✗" if enabled else "[fail]",
        warn="⚠" if enabled else "[warn]",
        info="ℹ" if enabled else "[info]",
        bullet="•" if enabled else "*",
        arrow="→" if enabled else "->",
        spark="⚡" if enabled else "[!]",
    )


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


def _rebuild_graph_store(ctx: CommandContext, result: LLMInvocationResult) -> LLMInvocationResult:
    """Rebuild the typed graph store after a successful LLM compile.

    Mirrors the bash ``kb compile`` graph-rebuild block:
    - If ``tools/graph/gq`` is absent, skip silently.
    - If the build fails and a last-good ``.graph.db`` exists, warn and continue.
    - If the build fails and no ``.graph.db`` exists, emit an error and return a
      failed result so ``kb compile`` propagates a non-zero exit code.
    """
    import subprocess
    import tempfile
    from pathlib import Path

    kb_dir = Path(ctx.workspace.kb_dir)
    gq = kb_dir / "tools" / "graph" / "gq"

    if not gq.exists():
        return result

    had_graph_db = (kb_dir / ".graph.db").exists()

    fd, graph_err_name = tempfile.mkstemp(prefix="kb-graph-build.")
    graph_err_path = Path(graph_err_name)
    os.close(fd)

    try:
        with graph_err_path.open("w") as graph_err_fh:
            proc = subprocess.run(
                [sys.executable, str(gq), "build"],
                cwd=str(kb_dir),
                stdout=subprocess.DEVNULL,
                stderr=graph_err_fh,
            )
    except (OSError, subprocess.SubprocessError) as exc:  # pragma: no cover
        proc = None
        graph_err_path.write_text(str(exc))

    stderr_text = graph_err_path.read_text().strip()
    try:
        graph_err_path.unlink()
    except OSError:
        pass

    if proc is not None and proc.returncode == 0:
        return result

    if stderr_text:
        print(stderr_text, file=sys.stderr)

    if had_graph_db:
        print(
            "Graph store build failed (non-fatal; keeping existing .graph.db)",
            file=sys.stderr,
        )
        return result

    print(
        "Graph store build failed and no existing .graph.db is available",
        file=sys.stderr,
    )
    from .models import EXIT_ERROR as _EXIT_ERROR

    result.ok = False
    result.exit_code = _EXIT_ERROR
    return result


def _run_compile(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    _parse_command("kb compile", args, lambda p: None)
    result = llm_commands.compile_wiki(ctx)
    raw_noop = result.details.get("noop") and result.details.get("raw_sources", 0) > 0
    empty_install_noop = (
        result.details.get("noop")
        and result.details.get("raw_sources", 0) == 0
        and not any(ctx.workspace.wiki_dir.rglob("*.md"))
    )
    if result.ok and not ctx.dry_run and not raw_noop and not empty_install_noop:
        result = _rebuild_graph_store(ctx, result)
    return result


def _run_ask(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb ask", args, lambda p: p.add_argument("question", nargs="+"))
    return llm_commands.ask(ctx, " ".join(ns.question))


def _run_query(ctx: CommandContext, args: Sequence[str]) -> LLMInvocationResult:
    ns = _parse_command("kb query", args, lambda p: p.add_argument("question", nargs="+"))
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


def _run_queue(ctx: CommandContext, args: Sequence[str]) -> QueueResult:
    return queue_cmd.run(ctx, args)


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

    theme = _theme()

    if isinstance(result, SearchResult):
        if result.message and not result.hits:
            if result.ok:
                print(f"{theme.color(theme.info, 'yellow')} {result.message.strip()}")
            else:
                print(_format_message(result.message.strip(), result.ok, theme))
            return
        if not result.hits:
            print(
                f"{theme.color(theme.info, 'yellow')} "
                f"No results for {theme.color(result.query, 'green')}"
            )
            return
        print(
            f"{theme.heading('Search Results')} "
            f"{theme.dim(f'backend: {result.backend}')}"
        )
        print(f"  Query: {theme.color(result.query, 'green')}")
        for idx, hit in enumerate(result.hits, start=1):
            title = hit.title or hit.path
            score = f" score={hit.score:.4f}" if hit.score is not None else ""
            print(
                f"{theme.color(str(idx) + '.', 'cyan')} "
                f"{theme.color(title, 'bold')}{theme.color(score, 'yellow')}"
            )
            print(f"   {theme.dim('file:')} {hit.path}")
            if hit.snippet:
                print(f"   {hit.snippet}")
        return

    if isinstance(result, StatsResult):
        print(theme.heading("Wiki Stats"))
        print(
            f"  {theme.color('wiki files', 'cyan')}: {result.total_wiki_files} | "
            f"{theme.color('wiki words', 'cyan')}: {result.total_wiki_words} | "
            f"{theme.color('raw words', 'cyan')}: {result.total_raw_words}"
        )
        for section in result.sections:
            section_padding = " " * max(2, 22 - len(section.name))
            print(
                f"  {theme.color(section.name, 'green')}{section_padding}"
                f"files={section.files} words={section.words}"
                + (
                    f" {theme.dim(f'last_modified={section.last_modified}')}"
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
            f"{theme.heading('Test Suites')} "
            f"total={result.total} "
            f"{theme.color(f'passed={result.passed}', 'green')} "
            f"{theme.color(f'failed={result.failed}', 'red' if result.failed else 'green')}"
        )
        for suite in result.suites:
            if suite.passed:
                status = theme.color("PASS", "green")
            else:
                status = theme.color("FAIL", "red")
            print(f"{status} {suite.name} {theme.dim(f'(rc={suite.returncode})')}")
        if result.message:
            print(_format_message(result.message.strip(), result.ok, theme))
        return

    if isinstance(result, QueueResult):
        if result.action == "list":
            if not result.items:
                print(f"{theme.color(theme.info, 'cyan')} Queue is empty.")
                return
            print(f"{theme.heading('Queued Candidates')} {theme.dim(f'({len(result.items)})')}")
            for item in result.items:
                title = item.title or "(untitled)"
                topic = (
                    f" {theme.color(f'[{item.topic}]', 'magenta')}"
                    if item.topic
                    else ""
                )
                print(f"{theme.color(item.id, 'cyan')}{topic} {title}")
                if item.url:
                    print(f"   {theme.dim('url:')} {item.url}")
                if item.content_hash:
                    print(f"   {theme.dim('hash:')} {item.content_hash}")
                if item.preview:
                    print(f"   {item.preview[:180]}")
            return
        if result.message:
            print(_format_message(result.message.strip(), result.ok, theme))
        return

    if isinstance(result, WorkspacesResult):
        print(theme.heading("Workspaces"))
        for entry in result.workspaces:
            name = theme.color(entry.name, "green" if entry.is_default else "cyan")
            default = f" {theme.color('(default)', 'yellow')}" if entry.is_default else ""
            print(
                f"  {name}{default}: "
                f"{theme.dim(entry.path)} [{entry.articles} articles]"
            )
        return

    if isinstance(result, InitResult):
        if result.message:
            print(_format_message(result.message, result.ok, theme))
        for path in result.created_files:
            print(f"{theme.color(theme.ok, 'green')} {path}")
        return

    if result.message:
        print(_format_message(result.message.strip(), result.ok, theme))


def _print_help() -> None:
    theme = _theme()
    model_default = os.environ.get("KB_MODEL", "opus")
    permission_default = os.environ.get("KB_PERMISSION_MODE", "bypassPermissions")

    logo = r"""
    ██╗  ██╗██████╗
    ██║ ██╔╝██╔══██╗
    █████╔╝ ██████╔╝
    ██╔═██╗ ██╔══██╗
    ██║  ██╗██████╔╝
    ╚═╝  ╚═╝╚═════╝
"""
    print(theme.color(logo.rstrip("\n"), "cyan"))
    print(f"  {theme.dim('LLM Knowledge Base CLI')}\n")

    _help_section(theme, "SETUP")
    print(
        f"  {theme.color('python3 -m pip install -r requirements.txt', 'green')}"
    )
    print(f"  {theme.color('export ANTHROPIC_API_KEY=<key>', 'green')}")
    print(f"  {theme.dim('LLM commands use claude-agent-sdk; kb -i uses claude CLI.')}")
    print(
        f"  {theme.dim('Default workspace: $KB_WORKSPACES/default unless --dir or KB_DIR is set.')}"
    )
    print("")

    _help_section(theme, "USAGE")
    print(f"  {theme.color('kb', 'green')} <command> [args...] [flags]")
    print(f"  {theme.color('kb', 'green')} \"<natural language prompt>\"")
    print("")

    _help_section(theme, "CORE COMMANDS")
    _help_row(theme, "research", "\"<topic>\"", "Deep web research + ingest + compile")
    _help_row(theme, "ingest", "<url> [urls...]", "Ingest specific URLs into raw/")
    _help_row(theme, "compile", "", "Recompile wiki from raw sources")
    _help_row(theme, "ask", "\"<question>\"", "Q&A over the wiki")
    _help_row(theme, "query", "\"<question>\"", "Alias for ask")
    _help_row(theme, "lint", "", "Health check + active gap filling")
    print("")

    _help_section(theme, "SEARCH & BROWSE")
    _help_row(theme, "search", "\"<query>\" [--top N]", "Full-text search")
    _help_row(theme, "serve", "[port]", "Start search web UI (default: 8765)")
    print("")

    _help_section(theme, "GENERATE")
    _help_row(theme, "slides", "\"<topic>\"", "Generate a Marp slide deck")
    _help_row(theme, "report", "\"<topic>\"", "Generate a detailed report")
    _help_row(theme, "compare", "\"<x>\" \"<y>\"", "Generate a comparison article")
    _help_row(theme, "entity", "\"<name>\"", "Create/update an entity page")
    print("")

    _help_section(theme, "QUEUE")
    _help_row(theme, "queue list", "", "Show discovered candidates awaiting review")
    _help_row(theme, "queue approve", "<id>", "Promote a candidate through ingest")
    _help_row(theme, "queue reject", "<id> [reason]", "Archive a candidate")
    print("")

    _help_section(theme, "EXPORT & VISUALIZE")
    _help_row(theme, "export", "[format]", "Export wiki: site, pdf, epub, or bundle")
    _help_row(
        theme,
        "viz",
        "[type]",
        "Generate graph, timeline, stats, concept-map, canvas, or all",
    )
    print("")

    _help_section(theme, "MAINTENANCE")
    _help_row(theme, "discover", "", "Auto-discover new sources")
    _help_row(theme, "test", "", "Run integrity tests")
    _help_row(theme, "stats", "", "Quick wiki statistics")
    _help_row(theme, "log", "[n] [--all]", "Show recent log entries")
    _help_row(theme, "init", "[path]", "Initialize a new knowledge base")
    _help_row(theme, "new", "<name> [base]", "Create a named workspace")
    _help_row(theme, "workspaces", "[base]", "List all workspaces (alias: ws)")
    print("")

    _help_section(theme, "INFRASTRUCTURE")
    _help_row(theme, "mcp", "[args...]", "Start MCP server")
    _help_row(theme, "-i", "| --interactive", "Interactive Claude session")
    print("")

    _help_section(theme, "FLAGS")
    _help_flag(
        theme,
        "--dir, -d",
        "<name|path>",
        "Target a workspace; names resolve under $KB_WORKSPACES and auto-init if new",
    )
    _help_flag(
        theme,
        "--model",
        "<model>",
        f"Override Claude model (default: {model_default})",
    )
    _help_flag(
        theme,
        "--budget",
        "<tokens>",
        "Stop when aggregate token usage exceeds this",
    )
    _help_flag(
        theme,
        "--permission-mode",
        "<mode>",
        f"Claude permission mode (default: {permission_default})",
    )
    _help_flag(theme, "--json", "", "Emit machine-readable output")
    _help_flag(theme, "--verbose, -v", "", "Show detailed output and prompt previews")
    _help_flag(theme, "--dry-run", "", "Preview what would happen without side effects")
    _help_flag(theme, "--no-commit", "", "Skip git auto-commit after successful wiki writes")
    print("")

    _help_section(theme, "ENVIRONMENT")
    _help_env(theme, "KB_MODEL", f"Claude model default (current: {model_default})")
    _help_env(
        theme,
        "KB_PERMISSION_MODE",
        f"Permission mode default (current: {permission_default})",
    )
    _help_env(
        theme,
        "KB_WORKSPACES",
        "Base dir for named workspaces (default: ~/kb-workspaces)",
    )
    _help_env(theme, "KB_DIR", "Active workspace override")
    _help_env(theme, "KB_NO_COMMIT", "Skip git commits when set to 1")
    _help_env(theme, "KB_TOKEN_BUDGET", "Default token budget for LLM commands")
    _help_env(theme, "KB_COLOR", "auto|always|never terminal color control")
    _help_env(theme, "NO_COLOR", "Disable color when KB_COLOR is auto")
    _help_env(theme, "ANTHROPIC_API_KEY", "Required by claude-agent-sdk for LLM commands")
    print("")

    _help_section(theme, "SMART ROUTING")
    print(f"  If no command matches, {theme.color('kb', 'green')} routes by input shape:")
    _help_bullet(theme, "URLs", "ingest")
    _help_bullet(theme, "Questions", "ask")
    _help_bullet(theme, "Short phrases", "research")
    _help_bullet(theme, "Anything else", "free-form LLM prompt")
    print("")

    _help_section(theme, "EXAMPLES")
    _help_example(theme, "kb new agents")
    _help_example(theme, "kb --dir agents research \"LLM agents with memory\"")
    _help_example(theme, "kb ingest https://arxiv.org/abs/2401.00001")
    _help_example(theme, "kb \"what are the key themes?\"")
    _help_example(theme, "kb compare \"RLHF\" \"DPO\"")
    _help_example(theme, "kb search \"attention\" --top 5")


def _format_message(message: str, ok: bool, theme: TerminalTheme) -> str:
    if ok:
        return message
    return f"{theme.color(theme.fail, 'red')} {message}"


def _help_section(theme: TerminalTheme, title: str) -> None:
    print(theme.heading(title))


def _help_row(theme: TerminalTheme, command: str, args: str, description: str) -> None:
    left_plain = f"{command} {args}".strip()
    left = theme.color(command, "cyan")
    if args:
        left = f"{left} {args}"
    padding = " " * max(2, 30 - len(left_plain))
    print(f"  {left}{padding}{description}")


def _help_flag(theme: TerminalTheme, flag: str, arg: str, description: str) -> None:
    left_plain = f"{flag} {arg}".strip()
    left = theme.color(flag, "yellow")
    if arg:
        left = f"{left} {arg}"
    padding = " " * max(2, 34 - len(left_plain))
    print(f"  {left}{padding}{description}")


def _help_env(theme: TerminalTheme, name: str, description: str) -> None:
    print(f"  {theme.dim(f'{name:<22}')} {description}")


def _help_bullet(theme: TerminalTheme, label: str, target: str) -> None:
    print(
        f"  {theme.dim(theme.bullet)} {label:<14} "
        f"{theme.color(theme.arrow, 'magenta')} {target}"
    )


def _help_example(theme: TerminalTheme, command: str) -> None:
    print(f"  {theme.color(command, 'green')}")


_COMMANDS: dict[str, Callable[[CommandContext, Sequence[str]], CommandResult]] = {
    "research": _run_research,
    "ingest": _run_ingest,
    "compile": _run_compile,
    "ask": _run_ask,
    "query": _run_query,
    "lint": _run_lint,
    "search": _run_search,
    "slides": _run_slides,
    "report": _run_report,
    "compare": _run_compare,
    "entity": _run_entity,
    "export": _run_export,
    "viz": _run_viz,
    "discover": _run_discover,
    "queue": _run_queue,
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
