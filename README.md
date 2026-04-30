# llm-kb

> A personal knowledge base you operate in natural language. You drop sources (URLs, PDFs, repos, tweets); Claude fetches, summarises, cross-links, and maintains an Obsidian-browsable wiki. You ask questions; it answers with citations and files the answers back.

`llm-kb` is a small CLI that turns Claude into a research agent over a set of markdown notes. You never edit the wiki by hand — it is written, linted, and extended by the LLM. You read it (in Obsidian, a browser, an EPUB) and you ask it things.

---

## What it does

Three operations cover 90% of use:

| Operation | You say | It does |
|-----------|---------|---------|
| **Research** | `uv run kb research "mixture of experts"` | Web-searches 5–15 angles, fetches the good sources, ingests them, compiles summaries + concept pages + entity pages + comparisons. One prompt → 10–15 new wiki pages. |
| **Ingest** | `uv run kb ingest https://arxiv.org/abs/...` | Handles URLs, arXiv, YouTube, GitHub, PDFs, tweets. Cleans, frontmatters, indexes. |
| **Ask** | `uv run kb ask "what's the tradeoff between softmax and linear attention?"` | Reads summaries to find relevant articles, answers with `[[wikilinks]]`, optionally files the answer back as a new wiki page. |

Plus: lint (find gaps and fill them from the web), search (BM25), compare, slides (Marp), report, visualise (knowledge graph, timeline, concept map, Obsidian canvas), export (static site / PDF / EPUB / bundle), monitor (RSS + topic watch), MCP server, Python SDK.

The core idea: **raw data is immutable; the wiki is the LLM's compiled, cross-linked interpretation of it; your queries compound back into the wiki.**

---

## Quickstart

Requirements:
- [uv](https://docs.astral.sh/uv/) with Python 3.10+
- Either direct Anthropic API auth (`ANTHROPIC_API_KEY`) or Vertex AI auth (`KB_LLM_PROVIDER=vertex` / `CLAUDE_CODE_USE_VERTEX=1` plus Google Cloud credentials)
- Optional: `claude` CLI installed and authenticated for `uv run kb -i` interactive sessions ([Claude Code](https://docs.claude.com/claude-code))
- Optional: `yt-dlp`, `pdftotext`, `gh` (for YouTube / PDF / GitHub ingest)
- Optional: [Obsidian](https://obsidian.md) to browse the vault

```bash
git clone git@github.com:ebarti/llm-kb.git ~/Github/llm-kb
cd ~/Github/llm-kb
uv sync

# Choose one auth path.

# Option A: Anthropic API
export ANTHROPIC_API_KEY="your-api-key"

# Option B: Vertex AI
export KB_LLM_PROVIDER=vertex
export ANTHROPIC_VERTEX_PROJECT_ID="your-gcp-project"
export CLOUD_ML_REGION="global"

# Create your first workspace (data lives outside the repo):
uv run kb new ai                  # → ~/kb-workspaces/ai/

# Kick off your first research session:
uv run kb --dir ai research "transformer architecture"

# Ask a question once the wiki has content:
uv run kb --dir ai ask "what is a mixture of experts?"

# Open the workspace in Obsidian:
open ~/kb-workspaces/ai
```

First-run tips:
- LLM-backed commands use the Claude Agent SDK by default. If you see a `claude-agent-sdk is required` error, run `uv sync` from the repo root.
- Anthropic API mode requires `ANTHROPIC_API_KEY`.
- Vertex AI mode does not require `ANTHROPIC_API_KEY`; set `KB_LLM_PROVIDER=vertex` or `CLAUDE_CODE_USE_VERTEX=1`, configure `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION`, then provide Google credentials in your environment, such as `GOOGLE_APPLICATION_CREDENTIALS`.
- If you omit `--dir`/`KB_DIR`, `uv run kb research "<topic>"` creates a topic-named workspace.
- Non-research commands without `--dir`/`KB_DIR` target `$KB_WORKSPACES/default`.
- `uv run kb workspaces` lists every workspace and shows which one is active.
- `uv run kb --dir <name>` auto-creates the workspace if it does not exist.
- The `--dir` flag accepts a bare name (resolved to `$KB_WORKSPACES/<name>`) or an absolute path.

---

## Core concepts

### Three layers

| Layer | Directory | Owner | Mutability |
|-------|-----------|-------|------------|
| **Raw** | `raw/` | Ingest pipeline | Immutable after write — source of truth |
| **Wiki** | `wiki/` | Claude (the LLM) | Freely rewritten on every compile |
| **Schema** | `CLAUDE.md` | Human + LLM | Defines conventions and operations |

The wiki contains four kinds of articles (`wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/comparisons/`), plus an `_index.md` and a `_meta/` dir with summaries, a backlink graph, and a compile manifest. A single ingest typically touches 10–15 pages across these.

### Workspaces

A **workspace** is a self-contained directory with its own `raw/`, `wiki/`, `output/`, tools, and git history. The repo itself is code only — workspaces live under `$KB_WORKSPACES` (default: `~/kb-workspaces/`).

```
~/Github/llm-kb/            # this repo — tooling only
  pyproject.toml            # uv project + CLI entrypoint
  kb/                       # Python CLI package (`kb.*`)
  tools/                    # operational scripts: ingest, viz, export, plugins, MCP, SDK
  templates/                # article + slide templates
  CLAUDE.md                 # Claude's operating manual (copied into workspaces)

~/kb-workspaces/
  ai/                       # your AI research workspace
    raw/                    # ingested sources
    wiki/                   # Claude-maintained articles
    output/                 # reports, slides, images, exports
    tools/                  # per-workspace copy (with its own search index)
  biology-genai/
  my-other-topic/
```

Research commands auto-create a topic-named workspace when `--dir` and `KB_DIR` are unset. Other commands use `$KB_WORKSPACES/default` unless you pass `--dir <name|path>` or set `KB_DIR`.

---

## Command reference

Run `uv run kb --help` for the full list. A useful subset:

```bash
# Core
uv run kb research "<topic>"           # web research + ingest + compile
uv run kb ingest <url> [urls...]       # ingest specific sources
uv run kb compile                      # recompile wiki from raw/
uv run kb ask "<question>"             # Q&A with citations
uv run kb lint                         # health check + fill gaps from the web

# Search & browse
uv run kb search "<query>"             # BM25 full-text search
uv run kb serve                        # web UI on :8765
uv run kb stats                        # quick counts and tags
uv run kb log [n]                      # recent activity log

# Generate
uv run kb slides "<topic>"             # Marp deck in output/slides/
uv run kb report "<topic>"             # long-form markdown report
uv run kb compare "<x>" "<y>"          # comparison article
uv run kb entity "<name>"              # entity page

# Export & visualize
uv run kb export [site|pdf|epub|bundle]
uv run kb viz    [graph|timeline|stats|canvas]

# Maintenance & ops
uv run kb discover                     # auto-discover new sources via RSS + topic queries
uv run kb test                         # run the integrity test suite
uv run kb mcp                          # MCP server over stdio (for Claude Desktop)
uv run kb -i                           # interactive Claude session in this workspace

# Workspaces
uv run kb new <name>                   # create ~/kb-workspaces/<name>
uv run kb workspaces                   # list all workspaces
uv run kb --dir <name> <command>       # target a specific workspace
uv run kb research "<topic>"           # auto-creates a topic-named workspace if --dir/KB_DIR is unset
```

Flags: `--dir / -d`, `--model`, `--budget`, `--no-commit`, `--dry-run`, `--verbose`.
Env: `ANTHROPIC_API_KEY`, `KB_LLM_PROVIDER`, `CLAUDE_CODE_USE_VERTEX`, `ANTHROPIC_VERTEX_PROJECT_ID`, `CLOUD_ML_REGION`, `GOOGLE_APPLICATION_CREDENTIALS`, `KB_DIR`, `KB_WORKSPACES`, `KB_MODEL`, `KB_TOKEN_BUDGET`, `KB_AGENT_HEARTBEAT_SECONDS`, `KB_LOG_DIR`, `KB_RUN_LOG`, `KB_REVIEW_AUTO_REPAIR`, `KB_PERMISSION_MODE`, `KB_NO_COMMIT`, `KB_COLOR`.

LLM-backed commands print timestamped progress and tee stdout/stderr to
`<workspace>/output/logs/*.log` by default. Set `KB_LOG_DIR` to move run logs or
`KB_RUN_LOG=0` to disable log files.
Compile review auto-repairs common draft schema/link issues by default; set
`KB_REVIEW_AUTO_REPAIR=0` to disable that safety net.

---

## What's in the repo

```
pyproject.toml        uv project metadata and `kb` console script
kb/                   Python package for the CLI (`kb.*`)
tools/
  search-engine/      BM25 search (Python stdlib) + web UI on :8888
  ingest/             One shell script per source type (youtube, arxiv, github, pdf, tweet, batch)
  viz/                Knowledge graph, timeline, concept map, stats dashboard, Obsidian canvas
  export/             Static site, print-ready HTML, EPUB, single-markdown bundle
  monitor/            RSS + topic-query auto-discovery, optional cron
  plugins/            Hook system (post-compile, on-lint, etc.) with 10+ built-in plugins
  mcp-server/         MCP server exposing the KB as tools to Claude Desktop
  sdk/                Python SDK + CLI + JSON HTTP API (:8889) + REPL + full-JSON export
  tests/              Integrity, link graph, index, quality, search, and smoke tests
  history/            Git-based changelog + per-article edit history
  marp/               Custom Marp theme for slide decks
templates/            Article + slide templates with {{placeholders}}
docs/                 PRDs (01-core, 02-advanced)
CLAUDE.md             Claude's operating manual (authoritative layout + conventions)
CONTRIBUTING.md       Worktree-per-task workflow for contributors
```

The operating manual (`CLAUDE.md`) is the authoritative description of how Claude is supposed to behave inside a workspace. Read it if you want to know the conventions in detail — article frontmatter, wikilink style, when to create an entity page vs. a concept article, how compilation is supposed to work, etc.

---

## Obsidian integration

Workspaces are plain markdown, so any editor works — but Obsidian is the intended frontend:
- `[[wikilinks]]` resolve natively
- `.canvas` files from `uv run kb viz canvas` render as interactive node graphs
- The Marp community plugin renders `output/slides/*.md` as live slide decks
- Dataview works on the frontmatter (every article has `title`, `type`, `summary`, `last_compiled`, etc.)

A minimal `.obsidian/` config is created automatically by `uv run kb init`.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: every change lands via a worktree + draft PR into `main`. No direct pushes.

```bash
cd ~/Github/llm-kb
git worktree add ../llm-kb-feat-foo -b feat/foo origin/main
cd ../llm-kb-feat-foo
# ... edit ...
bash tools/tests/run-all.sh       # must be green before marking ready-for-review
git push -u origin feat/foo
gh pr create --draft --base main
```

**Wiki content itself is not reviewed** — it is authored by the LLM inside workspaces, which live outside this repo. PRs here are for the tooling (`kb`, `tools/`, `templates/`, `CLAUDE.md`, docs).

---

## Status

This is a personal tool, open-sourced because several people asked. Expect rough edges. No backwards-compat promises between commits — pin a SHA if you depend on a behavior. Issues and PRs are welcome, but please read `CONTRIBUTING.md` first.

No license has been set yet. Treat as all-rights-reserved until that changes; if you want to use or fork it, open an issue and I'll sort the license out.
