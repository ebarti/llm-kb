# llm-kb

> A personal knowledge base you operate in natural language. You drop sources (URLs, PDFs, repos, tweets); Claude fetches, summarises, cross-links, and maintains an Obsidian-browsable wiki. You ask questions; it answers with citations and files the answers back.

`llm-kb` is a small CLI that turns `claude` into a research agent over a set of markdown notes. You never edit the wiki by hand — it is written, linted, and extended by the LLM. You read it (in Obsidian, a browser, an EPUB) and you ask it things.

---

## What it does

Three operations cover 90% of use:

| Operation | You say | It does |
|-----------|---------|---------|
| **Research** | `kb research "mixture of experts"` | Web-searches 5–15 angles, fetches the good sources, ingests them, compiles summaries + concept pages + entity pages + comparisons. One prompt → 10–15 new wiki pages. |
| **Ingest** | `kb ingest https://arxiv.org/abs/...` | Handles URLs, arXiv, YouTube, GitHub, PDFs, tweets. Cleans, frontmatters, indexes. |
| **Ask** | `kb ask "what's the tradeoff between softmax and linear attention?"` | Reads summaries to find relevant articles, answers with `[[wikilinks]]`, optionally files the answer back as a new wiki page. |

Plus: lint (find gaps and fill them from the web), search (BM25), compare, slides (Marp), report, visualise (knowledge graph, timeline, concept map, Obsidian canvas), export (static site / PDF / EPUB / bundle), monitor (RSS + topic watch), MCP server, Python SDK.

The core idea: **raw data is immutable; the wiki is the LLM's compiled, cross-linked interpretation of it; your queries compound back into the wiki.**

---

## Quickstart

Requirements:
- `claude` CLI installed and authenticated ([Claude Code](https://docs.claude.com/claude-code))
- Python 3.9+ (stdlib only for core tools — no `pip install` needed)
- Optional: `yt-dlp`, `pdftotext`, `gh` (for YouTube / PDF / GitHub ingest)
- Optional: [Obsidian](https://obsidian.md) to browse the vault

```bash
git clone git@github.com:ebarti/llm-kb.git ~/Github/llm-kb
cd ~/Github/llm-kb

# Create your first workspace (data lives outside the repo):
./kb new ai                       # → ~/kb-workspaces/ai/

# Kick off your first research session:
./kb --dir ai research "transformer architecture"

# Ask a question once the wiki has content:
./kb --dir ai ask "what is a mixture of experts?"

# Open the workspace in Obsidian:
open ~/kb-workspaces/ai
```

First-run tips:
- `./kb workspaces` lists every workspace and shows which one is active.
- `./kb --dir <name>` auto-creates the workspace if it does not exist.
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
  kb                        # CLI
  tools/                    # search engine, ingest, viz, export, plugins, MCP, SDK
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

`./kb` refuses to run with `KB_DIR` pointing at the install dir — data never lives inside this repo.

---

## Command reference

Run `./kb --help` for the full list. A useful subset:

```bash
# Core
./kb research "<topic>"           # web research + ingest + compile
./kb ingest <url> [urls...]       # ingest specific sources
./kb compile                      # recompile wiki from raw/
./kb ask "<question>"             # Q&A with citations
./kb lint                         # health check + fill gaps from the web

# Search & browse
./kb search "<query>"             # BM25 full-text search
./kb serve                        # web UI on :8888
./kb stats                        # quick counts and tags
./kb log [n]                      # recent activity log

# Generate
./kb slides "<topic>"             # Marp deck in output/slides/
./kb report "<topic>"             # long-form markdown report
./kb compare "<x>" "<y>"          # comparison article
./kb entity "<name>"              # entity page

# Export & visualize
./kb export [site|pdf|epub|bundle]
./kb viz    [graph|timeline|stats|canvas]

# Maintenance & ops
./kb discover                     # auto-discover new sources via RSS + topic queries
./kb test                         # run the integrity test suite
./kb mcp                          # MCP server over stdio (for Claude Desktop)
./kb -i                           # interactive Claude session in this workspace

# Workspaces
./kb new <name>                   # create ~/kb-workspaces/<name>
./kb workspaces                   # list all workspaces
./kb --dir <name> <command>       # target a specific workspace
```

Flags: `--dir / -d`, `--model`, `--budget`, `--no-commit`, `--dry-run`, `--verbose`.
Env: `KB_DIR`, `KB_WORKSPACES`, `KB_MODEL`, `KB_BUDGET`, `KB_PERMISSION_MODE`, `KB_NO_COMMIT`.

---

## What's in the repo

```
kb                    The CLI (bash, ~1200 lines)
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
- `.canvas` files from `kb viz canvas` render as interactive node graphs
- The Marp community plugin renders `output/slides/*.md` as live slide decks
- Dataview works on the frontmatter (every article has `title`, `type`, `summary`, `last_compiled`, etc.)

A minimal `.obsidian/` config is created automatically by `kb init`.

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
