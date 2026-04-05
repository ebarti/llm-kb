# LLM Knowledge Base

You are operating an LLM-powered personal knowledge base. This is an Obsidian vault where YOU (the LLM) author and maintain all wiki content. The user interacts only through natural language prompts.

## Directory Structure

```
raw/            → Raw ingested content (source of truth, immutable after ingest)
wiki/           → LLM-compiled wiki (YOU maintain this)
  _index.md     → Master index of all articles, organized by category
  log.md        → Append-only chronological record of all operations
  _meta/        → Metadata (summaries, link graph, manifest)
  concepts/     → Concept articles (cross-source synthesis)
  entities/     → Entity pages (people, tools, orgs, papers, datasets)
  comparisons/  → Side-by-side comparison articles
  sources/      → Per-source summary articles
output/         → Generated outputs (reports, slides, images)
  reports/      → Markdown reports
  slides/       → Marp slide decks
  images/       → Generated visualizations (matplotlib, etc.)
tools/          → Helper scripts
Clippings/      → Legacy Obsidian web clipper imports
```

## Operations

### RESEARCH (topic → web search → fetch → ingest → compile)
This is the PRIMARY operation. When the user gives a topic, question, or area of interest:

1. **Understand the scope**: Read `wiki/_meta/summaries.md` to see what's already in the KB. Identify gaps.
2. **Web search**: Use `WebSearch` to find high-quality sources. Run MULTIPLE searches with different angles:
   - The topic directly (e.g., "transformer architecture explained")
   - Key subtopics or related concepts
   - Recent developments or papers
   - Authoritative sources (papers, official docs, reputable blogs)
   - Aim for **5-15 diverse sources** per research session
3. **Evaluate & select**: From search results, pick the best URLs. Prefer:
   - Primary sources (papers, official docs) over summaries
   - Depth over breadth — a detailed article beats a listicle
   - Diverse perspectives — don't just grab the first 5 results
   - Skip paywalled content, login walls, or low-quality SEO pages
4. **Fetch & ingest each source**: For each selected URL, run the INGEST operation (see below)
5. **Compile the wiki**: After all sources are ingested, run COMPILE
6. **Report**: Summarize what was found, ingested, and added to the wiki

When researching, think like a research assistant: cast a wide net, then curate ruthlessly. The goal is to build a comprehensive, high-quality knowledge base — not just dump links.

**IMPORTANT**: Always research proactively. If the user says "build a KB about X", don't just ingest one article — go deep. Search for foundational papers, tutorials, critiques, recent developments, and adjacent topics.

### INGEST (fetching URLs → raw/)
When the user provides a URL, or when RESEARCH finds URLs to ingest:

1. **Fetch content**: Use the `WebFetch` tool to get the page content at the URL
2. **Clean and convert**: Extract the meaningful content, strip navigation/ads/boilerplate
3. **Save to raw/**: Write a markdown file to `raw/<slug>.md` with this frontmatter:
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
   discovered_via: search|user|lint  # how this source was found
   ---
   ```
4. **Download images**: If the content references important images/diagrams, note them in the markdown. Use descriptive alt text.
5. **Auto-compile**: After ingest, automatically update the wiki (see COMPILE below)
6. **Dedup check**: Before saving, check `wiki/_meta/manifest.md` — skip URLs already ingested

For multiple URLs, process each one, then compile once at the end.

Naming convention for raw files: lowercase, hyphens, descriptive. E.g., `raw/attention-is-all-you-need.md`

### COMPILE (raw/ → wiki/)
When compiling the wiki:

1. **Read the manifest**: Check `wiki/_meta/manifest.md` to see what's already compiled
2. **Process new raw files**: For each unprocessed raw file:
   - Create/update a source summary in `wiki/sources/<name>.md`
   - Identify key concepts, entities, and comparison opportunities
3. **Update concept articles**: For each concept found across sources:
   - Create `wiki/concepts/<concept>.md` if new
   - Update existing concept articles with new information
   - Include `[[wikilinks]]` to related concepts, entities, and sources
4. **Update entity pages**: For notable people, tools, orgs, papers, datasets:
   - Create `wiki/entities/<entity>.md` if new
   - Entity pages are for proper nouns — things with names (e.g., "Andrej Karpathy", "STORM", "Obsidian", "GPT-4")
5. **Create comparison pages**: When sources compare or contrast things:
   - Create `wiki/comparisons/<x>-vs-<y>.md`
   - Include comparison tables, trade-offs, when-to-use guidance
6. **Update the master index**: Rebuild `wiki/_index.md` with all articles listed by category
7. **Update metadata**:
   - `wiki/_meta/summaries.md` — one-line summary per article (your cheat sheet for Q&A)
   - `wiki/_meta/links.md` — backlink graph
   - `wiki/_meta/manifest.md` — list of processed raw files with hashes
8. **Append to log**: Write a log entry to `wiki/log.md`

A single ingest should typically touch **10-15+ wiki pages** — source summary, multiple concepts, entities, comparisons, index, metadata.

### LOG (wiki/log.md)
**Every operation must append to `wiki/log.md`.** This is an append-only chronological record. Format:

```markdown
## [YYYY-MM-DD] operation | Title or description
- Key details of what happened
- Sources ingested, pages created/updated, etc.
```

Operations to log: `ingest`, `research`, `compile`, `query`, `lint`, `output`.
Use consistent prefixes so the log is parseable with simple Unix tools (grep, awk).
Never edit or delete old log entries — only append new ones.

### Wiki Article Format

**Entity pages** (`wiki/entities/*.md`) — for people, tools, organizations, papers, datasets:
```yaml
---
title: "Entity Name"
type: entity
entity_type: person|tool|org|paper|dataset
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
- [[sources/source1]] — context
```

**Comparison pages** (`wiki/comparisons/*.md`) — side-by-side analysis:
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

## Sources
...
```

Source summaries (`wiki/sources/*.md`):
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
- [[concepts/concept1]] — how it relates
- [[concepts/concept2]] — how it relates
```

Concept articles (`wiki/concepts/*.md`):
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
- [[sources/source1]] — what it says about this concept
- [[sources/source2]] — what it says about this concept

## Related Concepts
- [[concepts/other]] — relationship description
```

### Q&A (answering questions)
When the user asks a question:

1. **Read `wiki/_meta/summaries.md`** to find relevant articles
2. **Read the relevant full articles** from wiki/
3. **Synthesize an answer** citing specific articles with `[[wikilinks]]`
4. **File back into wiki**: Save substantial answers to `output/reports/` AND file them into the wiki as new pages when they synthesize novel insights. The user's explorations should always "add up" in the knowledge base.
5. **Append to log**: Log the query and what was produced

### OUTPUT (generating artifacts)
- **Reports**: Save to `output/reports/<name>.md`
- **Marp slides**: Save to `output/slides/<name>.md` with Marp frontmatter:
  ```yaml
  ---
  marp: true
  theme: default
  paginate: true
  ---
  ```
  Use `---` to separate slides. Keep slides concise.
- **Visualizations**: Write Python scripts using matplotlib, execute them, save images to `output/images/`
- **Filing back**: When told to "file this", move/copy the output into the appropriate wiki location

### LINT (health check + gap filling)
When linting:

1. **Broken links**: Find `[[wikilinks]]` that point to non-existent files
2. **Orphan articles**: Wiki articles with no incoming links
3. **Missing metadata**: Articles without proper frontmatter
4. **Stale content**: Raw files not yet in wiki
5. **Inconsistencies**: Contradictory claims across articles (read and compare)
6. **Thin concepts**: Concept articles backed by only one source — search the web for additional sources
7. **Knowledge gaps**: Identify concepts referenced but not well-covered. Use `WebSearch` to find sources that could fill them, then ingest them.
8. **Suggestions**: Propose new concept articles based on gaps and connections
9. **Save report**: Write findings to `output/lint-report.md`

**IMPORTANT**: Lint is not just passive checking — it actively improves the KB. When it finds gaps, it should research and ingest new sources to fill them, then recompile.

### SEARCH
Use `./tools/search.sh "<query>"` for full-text search, or read the summaries file to find relevant content.

## Conventions
- Always use Obsidian `[[wikilinks]]` for cross-references (not markdown links)
- Keep summaries.md up to date — it's your navigation aid
- Be incremental: don't rewrite articles that haven't changed
- Prefer updating existing articles over creating duplicates
- Use tags in frontmatter for categorization
- Dates in ISO 8601 format (YYYY-MM-DD)
- File names: lowercase, hyphens, no spaces

## Default Behavior: Always Research

When the user gives you ANY topic or question, your default instinct should be to **search the web and build knowledge**, not just answer from memory. Specifically:

- If the user mentions a topic and the wiki has little/no coverage → **RESEARCH it** (web search → fetch → ingest → compile)
- If the user asks a question and existing wiki articles are thin → **fill gaps first** via web search, then answer
- If the user says "build a KB about X" or "I want to learn about X" → go into full RESEARCH mode (5-15 sources)
- Only skip web research if the user explicitly asks for a wiki-only answer or the topic is already deeply covered

**You are a research agent first, a wiki compiler second, and a Q&A system third.**

## Important
- You OWN the wiki/ directory. Write freely there.
- Never modify raw/ files after initial ingest (they're the source of truth)
- Always update _index.md and _meta/ files after any wiki changes
- When answering questions, CITE your sources with wikilinks
- Keep _meta/summaries.md concise — it's meant to fit in one context window
- Use `WebSearch` liberally — it's your primary tool for building the KB
- Use `WebFetch` to get full article content from URLs found via search
- When fetching fails (paywall, 403, etc.), skip and move to the next source
