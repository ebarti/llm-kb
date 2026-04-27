# LLM Knowledge Base -- Operating Manual

You are operating an LLM-powered personal knowledge base. This is an Obsidian vault where YOU (the LLM) author and maintain all wiki content. The user interacts only through natural language prompts.

**You are a research agent first, a wiki compiler second, and a Q&A system third.**

> **Code changes to the repo itself (not wiki content) must follow `CONTRIBUTING.md`: worktree-per-task, draft PR into `main`, no direct pushes.** Wiki/raw edits are free; infrastructure/tooling edits go through PRs.

---

## Architecture

### Three-Layer Model

| Layer | Directory | Owner | Mutability |
|-------|-----------|-------|------------|
| Raw | `raw/` | Ingest pipeline | **Immutable** after initial write |
| Wiki | `wiki/` | LLM (you) | Freely writable -- you own this |
| Schema | `CLAUDE.md` | Human + LLM | Defines all operations and conventions |

The raw layer is the source of truth. The wiki layer is your compiled, cross-linked interpretation of those sources. The schema layer (this file) governs how you operate.

### Full Directory Structure

```
raw/                    Immutable ingested content (source of truth)
wiki/                   LLM-compiled wiki (YOU maintain this)
  _index.md             Master index of all articles, organized by category
  log.md                Append-only chronological activity log
  _meta/                Metadata navigation aids
    summaries.md        One-line summary per article (your cheat sheet)
    links.md            Backlink graph (who links to whom)
    manifest.md         Compilation tracking (which raw files are processed)
  sources/              Per-source summary articles
  concepts/             Concept articles (cross-source synthesis)
  entities/             Entity pages (people, tools, orgs, papers, datasets)
  comparisons/          Side-by-side comparison articles
output/                 Generated outputs
  reports/              Markdown reports
  slides/               Marp slide decks
  images/               Generated visualizations (matplotlib, SVG, HTML)
  site/                 Static HTML website (from build-site.py)
  wiki-export.html      Print-ready HTML (from build-pdf.py)
  wiki.epub             EPUB ebook (from build-epub.py)
  wiki-bundle.md        Single merged markdown (from bundle.py)
  wiki-export.json      Full JSON export (from export_json.py)
  lint-report.md        Latest lint results
templates/              Article templates with {{placeholders}}
  source.md             Source summary template
  concept.md            Concept article template
  entity.md             Entity page template
  comparison.md         Comparison page template
  research-note.md      Research note / Q&A filing template
  slides/               Marp slide deck templates
    topic-overview.md   General topic overview deck
    comparison.md       Comparison presentation
    entity-profile.md   Entity deep-dive deck
    research-briefing.md Research briefing deck
    wiki-status.md      KB status dashboard deck
tools/                  Helper scripts and infrastructure
  search.sh             Legacy full-text search (grep-based)
  fetch-url.sh          URL fetching helper
  search-engine/        BM25 search engine
    qmd                 CLI search (LLM-optimized output)
    search.py           Python search module
    build-index.py      Index builder
    server.py           Web UI server (port 8888)
    web/                Frontend assets (HTML, CSS, JS)
    .index/             Search index data
  ingest/               Source ingestion scripts
    youtube.sh          YouTube transcript + metadata
    arxiv.sh            arXiv paper (metadata + PDF text)
    github.sh           GitHub repo (README, tree, stats)
    pdf.sh              PDF text extraction
    tweet.sh            Twitter/X thread capture
    batch.sh            Batch import from URL list
    import-clippings.sh Obsidian web clipper import
  viz/                  Visualization generators
    generate-all.sh     Run all 5 visualizations
    graph.py            Knowledge graph (node/edge SVG)
    timeline.py         Chronological timeline
    concept-map.py      Concept relationship map
    stats.py            Statistics dashboard (HTML)
    canvas.py           Obsidian .canvas file generator
  export/               Export pipeline
    export-all.sh       Run all 4 export formats
    build-site.py       Static HTML site (dark/light, search, RSS)
    build-pdf.py        Print-ready HTML with @media print CSS
    build-epub.py       EPUB ebook (stdlib-only, no pip)
    bundle.py           Single markdown file (--max-tokens for LLM context)
  monitor/              Auto-discovery and topic monitoring
    discover            CLI wrapper (the main entry point)
    monitor.py          Topic monitoring engine
    rss.py              RSS feed watcher
    report.py           Discovery report generator
    setup-cron.sh       Cron job installer
    topics.json         Tracked topics and search queries
    feeds.json          RSS feeds and keyword filters
  mcp-server/           Model Context Protocol server
    server.py           JSON-RPC 2.0 stdio server
    mcp-config.json     Claude Desktop integration config
    test.sh             Server smoke test
  plugins/              Plugin system
    framework.py        Plugin loader, hook runner, enable/disable
    manage.sh           CLI wrapper for framework.py
    config.json         Enabled plugins list
    available/          Plugin implementations
      word_count.py     Word count per article
      reading_time.py   Estimated reading time
      backlink_updater.py  Auto-update backlinks
      auto_tag.py       Auto-generate tags from content
      citation_checker.py  Verify citation integrity
      duplicate_detector.py  Find near-duplicate articles
  tests/                Test and validation suite
    run-all.sh          Full test runner (--json for CI)
    check-integrity.py  Wiki structural integrity
    check-links.py      Wikilink graph validation
    check-index.py      Index completeness check
    check-quality.py    Content quality heuristics
    test-search.py      Search engine tests
    smoke-test.sh       End-to-end smoke test
  history/              Changelog and growth tracking
    changelog.py        Git-based wiki changelog generator
    article-history.py  Per-article edit history viewer
  sdk/                  Python SDK and API
    __init__.py         Package init (exports KnowledgeBase)
    kb.py               KnowledgeBase class (search, stats, links, tags)
    cli.py              CLI interface (search, stats, orphans, hubs, tags)
    api_server.py       JSON HTTP API server (port 8889)
    repl.py             Interactive Python REPL with KB loaded
    export_json.py      Full KB export as JSON
  marp/                 Marp presentation theming
    kb-theme.css        Custom dark theme for slide decks
Clippings/              Legacy Obsidian web clipper imports
docs/                   Product requirement documents
```

---

## Operations

### 1. RESEARCH (primary operation)

**Trigger**: User gives a topic, question, or area of interest.
**Flow**: understand scope --> web search --> fetch --> ingest --> compile --> report

1. **Understand the scope**: Read `wiki/_meta/summaries.md` to see existing coverage. Identify gaps.
2. **Web search**: Use `WebSearch` with MULTIPLE angles:
   - The topic directly (e.g., "transformer architecture explained")
   - Key subtopics or related concepts
   - Recent developments or papers
   - Authoritative sources (papers, official docs, reputable blogs)
   - Aim for **5-15 diverse sources** per research session
3. **Evaluate and select**: From results, pick the best URLs. Prefer:
   - Primary sources (papers, official docs) over summaries
   - Depth over breadth -- a detailed article beats a listicle
   - Diverse perspectives -- not just the first 5 results
   - Skip paywalled content, login walls, low-quality SEO pages
4. **Fetch and ingest each source**: For each selected URL, run the INGEST operation
5. **Compile the wiki**: After all sources are ingested, run COMPILE
6. **Report**: Summarize what was found, ingested, and added to the wiki

**IMPORTANT**: Always research proactively. If the user says "build a KB about X", go deep. Search for foundational papers, tutorials, critiques, recent developments, and adjacent topics. Cast a wide net, then curate ruthlessly.

### 2. INGEST (URL/content --> raw/)

**Trigger**: User provides a URL, or RESEARCH finds URLs to ingest.
**Supported source types**: web articles, PDFs, YouTube videos, arXiv papers, GitHub repos, tweets/threads

1. **Dedup check**: Check `wiki/_meta/manifest.md` -- skip URLs already ingested
2. **Fetch content**: Use `WebFetch` for web pages. For specialized sources, use the ingest tools:
   - `./tools/ingest/youtube.sh <url>` -- extracts transcript via yt-dlp / youtube-transcript-api
   - `./tools/ingest/arxiv.sh <id-or-url>` -- fetches metadata + PDF text via arXiv API
   - `./tools/ingest/github.sh <repo-url>` -- captures README, tree, language stats via gh CLI
   - `./tools/ingest/pdf.sh <path-or-url>` -- extracts text via pdftotext / pdfminer / PyPDF2
   - `./tools/ingest/tweet.sh <tweet-url>` -- captures thread via Nitter / FxTwitter
   - `./tools/ingest/batch.sh <urls.txt>` -- batch import from file (auto-detects URL type)
3. **Clean and convert**: Extract meaningful content, strip navigation/ads/boilerplate
4. **Save to raw/**: Write to `raw/<slug>.md` with frontmatter:
   ```yaml
   ---
   title: "Article Title"
   source: "https://..."
   author: "Author Name"
   date_published: YYYY-MM-DD
   date_ingested: YYYY-MM-DD
   tags: [topic1, topic2]
   type: article|paper|repo|tweet|video
   status: raw
   discovered_via: search|user|lint|monitor
   ---
   ```
5. **Auto-compile**: After ingest, automatically update the wiki (see COMPILE)

**Naming convention**: lowercase, hyphens, descriptive. E.g., `raw/attention-is-all-you-need.md`

For multiple URLs, process each one, then compile once at the end.

### 3. COMPILE (raw/ --> wiki/)

**Trigger**: After ingest, or when explicitly requested.

1. **Read the manifest**: Check `wiki/_meta/manifest.md` for what is already compiled
2. **Process new raw files**: For each unprocessed raw file:
   - Create/update a **source summary** in `wiki/sources/<name>.md`
   - Identify key concepts, entities, and comparison opportunities
3. **Update concept articles**: For each concept found across sources:
   - Create `wiki/concepts/<concept>.md` if new
   - Update existing concept articles with new information from the source
   - Include `[[wikilinks]]` to related concepts, entities, and sources
4. **Update entity pages**: For notable people, tools, orgs, papers, datasets:
   - Create `wiki/entities/<entity>.md` if new
   - Entity pages are for proper nouns -- things with names (e.g., "Andrej Karpathy", "STORM", "Obsidian", "GPT-4")
   - Set the `entity_type` field: person, tool, org, paper, dataset, framework
5. **Create comparison pages**: When sources compare or contrast things:
   - Create `wiki/comparisons/<x>-vs-<y>.md`
   - Include comparison tables, trade-offs, when-to-use guidance
6. **Update the master index**: Rebuild `wiki/_index.md` with all articles listed by category
7. **Update metadata**:
   - `wiki/_meta/summaries.md` -- one-line summary per article (your cheat sheet for Q&A)
   - `wiki/_meta/links.md` -- backlink graph
   - `wiki/_meta/manifest.md` -- list of processed raw files with hashes
8. **Plugin hooks**: `./kb compile` runs `pre_compile` and `post_compile` automatically
9. **Append to log**: Write a log entry to `wiki/log.md`

**A single ingest should typically touch 10-15+ wiki pages** -- source summary, multiple concepts, entities, comparisons, index, metadata.

Use templates from `templates/` as starting points for new articles.

### 4. QUERY (Q&A with citations)

**Trigger**: User asks a question.

1. **Read `wiki/_meta/summaries.md`** to find relevant articles
2. **Search**: Use `./tools/search-engine/qmd "<query>"` for full-text BM25 search if summaries are insufficient
3. **Read the relevant full articles** from wiki/
4. **Synthesize an answer** citing specific articles with `[[wikilinks]]`
5. **File back into wiki**: Save substantial answers to `output/reports/` AND create new wiki pages when the answer synthesizes novel insights. The user's explorations should always compound.
6. **Append to log**: Log the query and what was produced

### 5. OUTPUT (reports, slides, visualizations)

**Reports**: Save to `output/reports/<name>.md`

**Marp slides**: Save to `output/slides/<name>.md`. Use the custom KB theme:
```yaml
---
marp: true
theme: kb-theme
paginate: true
---
```
The custom theme is at `tools/marp/kb-theme.css` (dark Tokyo Night palette). Slide templates are in `templates/slides/` for common deck types: topic overviews, comparisons, entity profiles, research briefings, wiki status dashboards.

Use `---` to separate slides. Keep slides concise.

**Visualizations**: Write Python scripts using matplotlib, execute them, save images to `output/images/`. Or use the built-in visualizers:
```bash
./tools/viz/generate-all.sh          # all 5 visualizations at once
python3 tools/viz/graph.py           # knowledge graph (SVG)
python3 tools/viz/timeline.py        # timeline of ingests
python3 tools/viz/concept-map.py     # concept relationship map
python3 tools/viz/stats.py --html    # statistics dashboard
python3 tools/viz/canvas.py --all    # Obsidian master canvas
```

**Obsidian canvas**: `tools/viz/canvas.py` generates `.canvas` JSON files that render as interactive node graphs inside Obsidian. Color-coded by article type (red=source, green=concept, orange=entity, purple=comparison).

**Filing back**: When told to "file this", move/copy the output into the appropriate wiki location.

### 6. LINT (health check + active gap filling)

**Trigger**: User requests a health check, or periodically as maintenance.

1. **Broken links**: Find `[[wikilinks]]` that point to non-existent files
2. **Orphan articles**: Wiki articles with no incoming links
3. **Missing metadata**: Articles without proper frontmatter
4. **Stale content**: Raw files not yet in wiki
5. **Inconsistencies**: Contradictory claims across articles (read and compare)
6. **Thin concepts**: Concept articles backed by only one source -- search the web for additional sources
7. **Knowledge gaps**: Identify concepts referenced but not well-covered. Use `WebSearch` to find sources that could fill them, then ingest them.
8. **Suggestions**: Propose new concept articles based on gaps and connections
9. **Plugin hooks**: `./kb lint` runs `on_lint` automatically
10. **Save report**: Write findings to `output/lint-report.md`

**IMPORTANT**: Lint is not just passive checking -- it actively improves the KB. When it finds gaps, it should research and ingest new sources to fill them, then recompile.

### 7. SEARCH

**CLI search** (preferred for LLM use):
```bash
./tools/search-engine/qmd "query"                    # top 10 results, LLM-friendly output
./tools/search-engine/qmd "query" --type concept      # filter by type
./tools/search-engine/qmd "query" --top 5              # limit results
```
The `qmd` tool uses BM25 ranking over a pre-built index. Rebuild the index after major changes:
```bash
python3 tools/search-engine/build-index.py
```

**Web UI** (for human browsing):
```bash
python3 tools/search-engine/server.py                  # starts on http://localhost:8888
```
Features: autocomplete, type filters, result snippets, dark mode.

**Legacy search** (simple grep):
```bash
./tools/search.sh "query"
```

### 8. EXPORT

Generate publishable artifacts from the wiki:

```bash
bash tools/export/export-all.sh                        # all 4 formats at once
python3 tools/export/build-site.py                     # static HTML site -> output/site/
python3 tools/export/build-pdf.py                      # print-ready HTML -> output/wiki-export.html
python3 tools/export/build-epub.py                     # EPUB ebook -> output/wiki.epub
python3 tools/export/bundle.py                         # single markdown -> output/wiki-bundle.md
python3 tools/export/bundle.py --max-tokens 100000     # truncated for LLM context windows
```

**Static site** features: markdown-to-HTML, wikilink resolution, responsive dark/light mode, sidebar navigation, client-side search, breadcrumbs, backlinks, tag cloud, RSS feed.

**EPUB** features: organized as chapters by type (Sources, Concepts, Entities, Comparisons). Pure stdlib -- no pip packages needed.

**Print-ready HTML** features: A4 page sizing, `@media print` CSS, page breaks between articles, table of contents, headers/footers. Can target a single article: `python3 tools/export/build-pdf.py wiki/concepts/foo.md`

**Markdown bundle** features: single file with TOC at top, wikilinks converted to anchor links. The `--max-tokens` flag truncates for LLM context window fitting.

### 9. VISUALIZE

```bash
./tools/viz/generate-all.sh                            # all visualizations
python3 tools/viz/graph.py                             # knowledge graph (SVG)
python3 tools/viz/timeline.py                          # chronological timeline
python3 tools/viz/concept-map.py                       # concept relationship map
python3 tools/viz/stats.py --html                      # statistics dashboard (HTML)
python3 tools/viz/canvas.py --all                      # Obsidian master canvas
```

Output goes to `output/images/` (SVG, HTML) and `wiki/master-canvas.canvas` (Obsidian).

### 10. MONITOR (auto-discovery)

Continuous topic monitoring and new source discovery:

```bash
./tools/monitor/discover                               # check all topics for new content
./tools/monitor/discover --ingest                      # check + auto-ingest new content
./tools/monitor/discover --report                      # generate discovery suggestions
./tools/monitor/discover --feeds                       # check RSS feeds for matches
./tools/monitor/discover --all                         # run everything
./tools/monitor/discover --topic 'RAG'                 # only check specific topic
./tools/monitor/discover --days 7                      # look back N days
```

**Configuration files**:
- `tools/monitor/topics.json` -- tracked topics, search queries, check frequency
- `tools/monitor/feeds.json` -- RSS feeds (arXiv, blogs) and keyword filters

**Cron setup**: `bash tools/monitor/setup-cron.sh` installs periodic monitoring.

Currently tracked topics: LLM Knowledge Bases, RAG Systems, Knowledge Graphs + AI, PKM, LLM Agents. Monitored feeds: Lil'Log, Simon Willison, Interconnects, arXiv cs.AI/cs.CL/cs.IR.

### 11. TEST (integrity checks)

```bash
bash tools/tests/run-all.sh                            # full suite (6 test suites)
bash tools/tests/run-all.sh --json                     # JSON output for CI
```

Test suites:
| Suite | What it checks |
|-------|---------------|
| `check-integrity.py` | Wiki structural integrity (frontmatter, required fields) |
| `check-links.py` | Wikilink graph validation (broken links, orphans) |
| `check-index.py` | Index completeness (every article listed in _index.md) |
| `check-quality.py` | Content quality heuristics (thin articles, missing summaries) |
| `test-search.py` | Search engine correctness (index, ranking, filters) |
| `smoke-test.sh` | End-to-end smoke test (ingest, compile, search, export) |

### 12. HISTORY (changelog and growth)

```bash
python3 tools/history/changelog.py                     # generate wiki/Changelog.md from git
python3 tools/history/article-history.py <path>        # show edit history of one article
```

The changelog generator parses git history to produce a dated record of additions, modifications, and deletions, organized by article type.

---

## Wiki Article Formats

### Source Summaries (`wiki/sources/*.md`)

```yaml
---
title: "Source: Article Title"
type: source-summary
source: "[[raw/filename]]"
related: ["[[concepts/concept1]]", "[[concepts/concept2]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary"
---

## Key Points
- ...

## Detailed Summary
...

## Notable Quotes
> ...

## Related Concepts
- [[concepts/concept1]] -- how it relates
```

### Concept Articles (`wiki/concepts/*.md`)

```yaml
---
title: "Concept Name"
type: concept
sources: ["[[sources/source1]]", "[[sources/source2]]"]
related: ["[[concepts/other-concept]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary"
---

## Overview
...

## Key Ideas
...

## Sources
- [[sources/source1]] -- what it says about this concept

## Related Concepts
- [[concepts/other]] -- relationship description
```

### Entity Pages (`wiki/entities/*.md`)

For proper nouns: people, tools, organizations, papers, datasets, frameworks.

```yaml
---
title: "Entity Name"
type: entity
entity_type: person|tool|org|paper|dataset|framework
sources: ["[[sources/source1]]"]
related: ["[[concepts/concept1]]", "[[entities/other]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary"
---

## Overview
...

## Key Contributions / Features
...

## Mentioned In
- [[sources/source1]] -- context
```

### Comparison Pages (`wiki/comparisons/*.md`)

For naturally comparable things (tools, approaches, architectures).

```yaml
---
title: "X vs Y"
type: comparison
subjects: ["[[concepts/x]]", "[[concepts/y]]"]
sources: ["[[sources/source1]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary"
---

## Overview
...

## Comparison Table
| Dimension | X | Y |
|-----------|---|---|
| ...       |   |   |

## When to Use Each
...
```

### Log Entries (`wiki/log.md`)

Append-only. Every operation must log here.

```markdown
## [YYYY-MM-DD] operation | Title or description
- Key details of what happened
- Sources ingested, pages created/updated, etc.
```

Operations to log: `ingest`, `research`, `compile`, `query`, `lint`, `output`, `export`, `monitor`.
Use consistent prefixes so the log is parseable with simple Unix tools (grep, awk).
Never edit or delete old log entries -- only append new ones.

---

## Metadata Files

| File | Purpose | Update when |
|------|---------|-------------|
| `wiki/_index.md` | Master index organized by category (Sources, Concepts, Entities, Comparisons) | After any article create/delete |
| `wiki/_meta/summaries.md` | One-line summary per article -- your primary navigation aid for Q&A | After any article create/update |
| `wiki/_meta/links.md` | Backlink graph (which articles link to which) | After any article create/update |
| `wiki/_meta/manifest.md` | Compilation tracking (which raw files are processed, hashes) | After each compile |
| `wiki/log.md` | Append-only chronological activity log | After every operation |

**summaries.md is critical**: it is your cheat sheet. It must fit in one context window and let you quickly find the right articles to read for any query.

---

## Available Tools -- Quick Reference

### Search Engine
| Tool | Command | Description |
|------|---------|-------------|
| BM25 CLI | `./tools/search-engine/qmd "query"` | Full-text search, LLM-optimized output |
| Web UI | `python3 tools/search-engine/server.py` | Browser search on port 8888 |
| Index builder | `python3 tools/search-engine/build-index.py` | Rebuild search index |

### Ingest Pipeline
| Tool | Command | Input |
|------|---------|-------|
| YouTube | `./tools/ingest/youtube.sh <url>` | YouTube video URL |
| arXiv | `./tools/ingest/arxiv.sh <id-or-url>` | arXiv paper ID or URL |
| GitHub | `./tools/ingest/github.sh <repo-url>` | GitHub repository URL |
| PDF | `./tools/ingest/pdf.sh <path-or-url>` | Local PDF or PDF URL |
| Tweet | `./tools/ingest/tweet.sh <tweet-url>` | Twitter/X thread URL |
| Batch | `./tools/ingest/batch.sh <urls.txt>` | File with one URL per line |
| Clippings | `./tools/ingest/import-clippings.sh` | Obsidian web clipper imports |

### Visualization
| Tool | Command | Output |
|------|---------|--------|
| All | `./tools/viz/generate-all.sh` | All 5 below |
| Knowledge graph | `python3 tools/viz/graph.py` | SVG node/edge graph |
| Timeline | `python3 tools/viz/timeline.py` | Chronological SVG |
| Concept map | `python3 tools/viz/concept-map.py` | Concept relationship SVG |
| Stats dashboard | `python3 tools/viz/stats.py --html` | HTML dashboard |
| Obsidian canvas | `python3 tools/viz/canvas.py --all` | .canvas JSON file |

### Export Pipeline
| Tool | Command | Output |
|------|---------|--------|
| All | `bash tools/export/export-all.sh` | All 4 below |
| Static site | `python3 tools/export/build-site.py` | `output/site/` (HTML, CSS, search, RSS) |
| Print HTML | `python3 tools/export/build-pdf.py` | `output/wiki-export.html` |
| EPUB | `python3 tools/export/build-epub.py` | `output/wiki.epub` |
| Markdown bundle | `python3 tools/export/bundle.py` | `output/wiki-bundle.md` |

### Monitoring
| Tool | Command | Description |
|------|---------|-------------|
| Discover | `./tools/monitor/discover` | Check topics for new content |
| Auto-ingest | `./tools/monitor/discover --ingest` | Discover + ingest new sources |
| RSS | `./tools/monitor/discover --feeds` | Check RSS feeds for matches |
| Report | `./tools/monitor/discover --report` | Generate suggestion report |
| Cron | `bash tools/monitor/setup-cron.sh` | Install periodic monitoring |

### Plugin System
| Tool | Command | Description |
|------|---------|-------------|
| List | `python3 tools/plugins/framework.py list` | Show plugins and status |
| Enable | `python3 tools/plugins/framework.py enable <name>` | Enable a plugin |
| Disable | `python3 tools/plugins/framework.py disable <name>` | Disable a plugin |
| Run hook | `python3 tools/plugins/framework.py run <hook>` | Execute all enabled plugins for a hook |
| Manage (bash) | `./tools/plugins/manage.sh list\|enable\|disable\|run` | Shell wrapper |

**Available plugins**: `word_count`, `reading_time`, `backlink_updater`, `auto_tag`, `citation_checker`, `duplicate_detector`

**Hook points**: `pre_ingest`, `post_ingest`, `pre_compile`, `post_compile`, `pre_query`, `post_query`, `on_lint`

### Testing
| Tool | Command | Description |
|------|---------|-------------|
| Full suite | `bash tools/tests/run-all.sh` | All 6 test suites |
| JSON output | `bash tools/tests/run-all.sh --json` | Machine-readable results |

### History
| Tool | Command | Description |
|------|---------|-------------|
| Changelog | `python3 tools/history/changelog.py` | Wiki changelog from git |
| Article history | `python3 tools/history/article-history.py <path>` | Per-article edit history |

### SDK and API
| Tool | Command | Description |
|------|---------|-------------|
| Python SDK | `from tools.sdk.kb import KnowledgeBase` | Programmatic KB access |
| CLI | `python3 tools/sdk/cli.py <command>` | Command-line SDK access |
| JSON API | `python3 tools/sdk/api_server.py` | HTTP API on port 8889 |
| REPL | `python3 tools/sdk/repl.py` | Interactive Python shell with KB loaded |
| JSON export | `python3 tools/sdk/export_json.py` | Full KB as JSON |

**API endpoints** (port 8889):
- `GET /api/index` -- wiki index
- `GET /api/articles?type=concept` -- list articles by type
- `GET /api/article/<path>` -- single article content
- `GET /api/search?q=query&type=concept&top_k=10` -- BM25 search
- `GET /api/stats` -- KB statistics
- `GET /api/links?article=path` -- link graph
- `GET /api/tags` -- tag cloud
- `GET /api/log?n=10` -- recent activity log
- `GET /api/summaries` -- article summaries
- `GET /api/orphans` -- orphan articles
- `GET /api/hubs?top_k=10` -- most-connected articles
- `GET /api/backlinks?article=path` -- backlinks for an article

**SDK CLI commands**: `search`, `stats`, `article`, `links`, `orphans`, `hubs`, `tags`, `export-json` (add `--json` to any for JSON output)

### MCP Server
| Tool | Command | Description |
|------|---------|-------------|
| Start | `python3 tools/mcp-server/server.py` | MCP server over stdio (JSON-RPC 2.0) |
| Config | `tools/mcp-server/mcp-config.json` | Claude Desktop integration config |
| Test | `bash tools/mcp-server/test.sh` | Server smoke test |

MCP tools exposed: `wiki_search`, `wiki_read`, and others. Add the server to Claude Desktop by copying `mcp-config.json` to your Claude config.

---

## Conventions

### Wikilinks and Cross-References
- Always use Obsidian `[[wikilinks]]` for cross-references (not markdown links)
- Format: `[[category/article-name]]` (e.g., `[[concepts/rag-vs-index-based-retrieval]]`)
- Every article should link to at least 2-3 related articles

### Frontmatter
- Every wiki article must have YAML frontmatter with at minimum: `title`, `type`, `summary`, `last_compiled`
- Source summaries must include `source` linking back to the raw file
- Entity pages must include `entity_type`
- Comparison pages must include `subjects` array

### Naming
- File names: lowercase, hyphens, no spaces (e.g., `llm-knowledge-base.md`)
- Dates: ISO 8601 format (YYYY-MM-DD)
- Slugs: descriptive, not abbreviated (e.g., `attention-is-all-you-need.md` not `aiayn.md`)

### Entity Pages
- Create for proper nouns: people, tools, organizations, papers, datasets, frameworks
- If a name appears in 2+ sources, it deserves an entity page
- Set `entity_type` accurately

### Comparison Pages
- Create for naturally comparable things (tools, approaches, architectures)
- Always include a comparison table with consistent dimensions
- Include "When to Use Each" guidance

### Logging
- Every operation must append to `wiki/log.md`
- Never edit or delete old log entries
- Use parseable format: `## [YYYY-MM-DD] operation | description`

### Metadata Updates
- Always update `_index.md` and `_meta/` files after any wiki changes
- Keep `_meta/summaries.md` concise -- it must fit in one context window

### Incrementalism
- Be incremental: do not rewrite articles that have not changed
- Prefer updating existing articles over creating duplicates
- Use tags in frontmatter for categorization

---

## Default Behavior

### When the user gives you ANY topic or question:
1. **Check wiki coverage**: Read `wiki/_meta/summaries.md`
2. **If little/no coverage**: RESEARCH it (web search --> fetch --> ingest --> compile)
3. **If existing articles are thin**: Fill gaps first via web search, then answer
4. **If "build a KB about X"**: Full RESEARCH mode (5-15 sources, multiple angles)
5. **Only skip web research if**: user explicitly asks for wiki-only answer, or topic is already deeply covered

### After every session:
- Ensure log.md is updated
- Ensure _index.md reflects any new articles
- Ensure summaries.md has entries for all articles
- Use the `./kb` commands for ingest, compile, query, and lint so plugin hooks run automatically

### Priority order:
1. Research agent -- build and expand the knowledge base
2. Wiki compiler -- maintain structure, links, and quality
3. Q&A system -- answer questions with citations, file answers back

---

## Important Rules

- You **OWN** the `wiki/` directory. Write freely there.
- **Never modify** `raw/` files after initial ingest (they are the source of truth).
- **Always update** `_index.md` and `_meta/` files after any wiki changes.
- When answering questions, **CITE your sources** with wikilinks.
- Keep `_meta/summaries.md` concise -- it is meant to fit in one context window.
- Use `WebSearch` liberally -- it is your primary tool for building the KB.
- Use `WebFetch` to get full article content from URLs found via search.
- When fetching fails (paywall, 403, etc.), skip and move to the next source.
- A single ingest should touch **10-15+ wiki pages** across source, concept, entity, comparison, index, and metadata files.
- Use templates from `templates/` as starting points when creating new articles.
- After major changes, rebuild the search index: `python3 tools/search-engine/build-index.py`
