# PRD-01: LLM Knowledge Base — Core System

## Vision
A personal knowledge base system where the user submits natural language prompts and Claude CLI autonomously fetches, ingests, compiles, and maintains a structured wiki of markdown files — all viewable in Obsidian.

## Problem
Building a knowledge base manually is tedious. Karpathy described the ideal workflow: raw data goes in, an LLM compiles it into a navigable wiki, and the user interacts only through prompts. Current tooling requires manual web clipping, manual organization, and custom scripts. We want a single `kb` command that does everything.

## Architecture

```
agentic-ai/
├── CLAUDE.md              # Claude's operating manual for this vault
├── kb                     # Main CLI entry point (wraps claude CLI)
├── raw/                   # Raw ingested content (markdown + images)
├── wiki/                  # LLM-compiled wiki
│   ├── _index.md          # Master index with all articles
│   ├── _meta/             # Metadata files (summaries, link graph)
│   ├── concepts/          # Concept articles (LLM-authored)
│   └── sources/           # Per-source summaries
├── output/                # Generated outputs (slides, reports, images)
├── tools/                 # Helper scripts
│   ├── fetch-url.sh       # Fetch URL → markdown + images
│   └── search.sh          # Full-text search over wiki
├── Clippings/             # Obsidian web clipper imports (legacy)
└── docs/                  # PRDs and documentation
```

## Core Components

### 1. `kb` CLI Wrapper
- Single entry point: `./kb "your prompt here"`
- Wraps `claude` CLI with the project directory as context
- No API keys needed — uses Claude Code directly
- Supports all operations via natural language

### 2. Web Content Fetcher (`tools/fetch-url.sh`)
- Given a URL, fetches the page content
- Converts HTML to clean markdown using Claude
- Downloads referenced images to `raw/<source>/images/`
- Stores result in `raw/<source-name>.md` with YAML frontmatter
- Handles articles, papers, GitHub repos, tweets

### 3. Wiki Compiler
- Triggered by prompt: "compile wiki" or automatically after ingest
- Reads all `raw/` content
- For each source: creates a summary in `wiki/sources/`
- Identifies concepts across sources → creates `wiki/concepts/` articles
- Maintains `wiki/_index.md` with full article listing + brief descriptions
- Maintains `wiki/_meta/summaries.md` — one-line summary per article (for LLM context loading)
- Maintains `wiki/_meta/links.md` — backlink graph
- Uses Obsidian `[[wikilinks]]` for cross-references
- Incremental: only processes new/changed raw content

### 4. CLAUDE.md Operating Manual
- Teaches Claude the vault structure
- Defines conventions (frontmatter format, linking style, naming)
- Provides instructions for each operation type
- Includes the meta-index so Claude can navigate efficiently

## Frontmatter Format

### Raw files (`raw/*.md`)
```yaml
---
title: "Article Title"
source: "https://..."
author: "Author Name"
date_published: 2026-01-01
date_ingested: 2026-04-05
tags: [topic1, topic2]
type: article|paper|repo|tweet|video
---
```

### Wiki articles (`wiki/**/*.md`)
```yaml
---
title: "Concept Name"
type: concept|source-summary
sources: ["[[raw/source1]]", "[[raw/source2]]"]
related: ["[[concepts/other-concept]]"]
last_compiled: 2026-04-05
summary: "One-line summary for index"
---
```

## User Interaction Examples
```bash
# RESEARCH — the primary operation (web search → fetch → ingest → compile)
./kb research "transformer architecture"
./kb "build a KB about RLHF"
./kb "I want to learn about mixture of experts"

# Ingest specific URLs
./kb ingest https://arxiv.org/abs/2401.00001
./kb "ingest these: https://url1.com https://url2.com"

# Compile/update the wiki
./kb compile

# Ask a question (will research gaps if wiki coverage is thin)
./kb ask "what are the main differences between transformers and SSMs?"

# Generate output
./kb slides "top 5 concepts in the KB"

# Lint + auto-fill gaps from the web
./kb lint

# Full-text search
./kb search "attention mechanism"

# Interactive session
./kb -i
```

## Success Criteria
- User can go from URL → searchable wiki article in a single prompt
- Wiki is browsable in Obsidian with working links
- Claude can efficiently navigate the wiki via index files
- System works with just `claude` CLI installed — no API keys or external services
