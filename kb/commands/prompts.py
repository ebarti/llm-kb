"""
Prompt templates extracted from the bash kb.

Kept separate so the prompt text is easy to review and the command
dispatchers in :mod:`llm_commands` stay short.
"""

from __future__ import annotations


RESEARCH_PROMPT = """RESEARCH this topic for the knowledge base: {topic}

You are a research agent running a ReAct loop. Do NOT plan a fixed number of
sources upfront. Instead, iteratively discover what you need.

## Progress reporting

You MUST print structured progress updates so the user can track what's happening. Use this exact format:

At the start:
```
═══ RESEARCH: <topic> ═══
```

At the start of each iteration:
```
─── Iteration <N> ──────────────────────────
  Coverage so far:  <X> sources ingested | <Y> wiki pages | <Z> subtopics covered
  Gaps identified:  <list of gaps/thin areas to fill this iteration>
  Search plan:      <list of queries to run>
```

After each source is ingested:
```
  ✓ Ingested: <source title> (<url>)
```

When a fetch fails or is skipped:
```
  ✗ Skipped: <reason> (<url>)
```

After compiling each iteration:
```
  Compiled: +<N> sources, +<N> concepts, +<N> entities, +<N> comparisons
```

At the end:
```
═══ RESEARCH COMPLETE ═══
  Total sources:     <N>
  Wiki pages:        <N> (sources: <n>, concepts: <n>, entities: <n>, comparisons: <n>)
  Iterations:        <N>
  Subtopics covered: <bulleted list>
  Known gaps:        <any remaining gaps, or 'None identified'>
```

## Loop: repeat until convergence

### REASON
- What subtopics exist within this topic?
- What do I already have? (Read wiki/_meta/summaries.md)
- What gaps remain? What subtopics are uncovered or thin?
- What angles haven't I searched yet? (foundational work, recent breakthroughs, key papers, key people, critiques, industry applications, tutorials, adjacent topics, datasets, tools, benchmarks)

### ACT
- Run WebSearch queries targeting the identified gaps (multiple queries per iteration)
- For each quality result: fetch with WebFetch, clean to markdown, save to raw/
- Compile what you've ingested so far: source summaries, concept articles, entity pages, comparison pages

### ASSESS
- Re-read wiki/_meta/summaries.md to see updated coverage
- List remaining gaps and thin areas
- If significant gaps remain → loop back to REASON
- If coverage is comprehensive and new searches return mostly duplicates → stop

## Stopping condition
Stop ONLY when:
- All major subtopics have at least 2-3 sources backing them
- New searches are returning content you've already covered
- You cannot identify meaningful gaps remaining

Do NOT stop after a single pass. Expect 3-5+ iterations of this loop for any non-trivial topic. Each iteration should discover new angles the previous ones missed.

## After the loop
- Do a final compile pass ensuring all wiki pages are cross-linked
- Update the index and all metadata files
- Print the final RESEARCH COMPLETE progress report

## Wiki write contract

The compile review gate validates every changed wiki markdown file after you
finish. Treat these as hard requirements:

Use this exact frontmatter shape before writing files under wiki/:

Source summaries in wiki/sources/*.md:
```
---
title: "Source: Descriptive Source Title"
type: source-summary
source: "[[raw/raw-file-slug]]"
related: ["[[concepts/example-concept]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary."
---
```

Concept articles in wiki/concepts/*.md:
```
---
title: "Concept Name"
type: concept
sources: ["[[sources/source-summary-slug]]"]
related: ["[[concepts/related-concept]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary."
---
```

Entity pages in wiki/entities/*.md:
```
---
title: "Entity Name"
type: entity
entity_type: person|tool|org|paper|dataset|framework
sources: ["[[sources/source-summary-slug]]"]
related: ["[[concepts/related-concept]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary."
---
```

Comparison pages in wiki/comparisons/*.md:
```
---
title: "X vs Y"
type: comparison
subjects: ["[[concepts/x]]", "[[concepts/y]]"]
sources: ["[[sources/source-summary-slug]]"]
last_compiled: YYYY-MM-DD
summary: "One-line summary."
---
```

Review constraints:
- Use YYYY-MM-DD for last_compiled.
- Every source-summary body must contain at least 80 words.
- Every concept body must contain at least 80 words.
- Every entity body must contain at least 60 words.
- Every comparison body must contain at least 100 words.
- Do not use bare wikilinks like [[memgpt]] or [[agentic-memory]].
  Always include the category path, such as [[entities/memgpt]],
  [[sources/memgpt]], [[concepts/agentic-memory]], or
  [[comparisons/memory-architecture-comparison]].
- Before finishing, check that every wikilink resolves to a file you wrote or
  an existing file in wiki/.
"""


INGEST_PROMPT = (
    "Ingest the following URLs into the knowledge base. For each URL: fetch the "
    "content, convert to clean markdown, save to raw/, then update the wiki. URLs: {urls}"
)


COMPILE_PROMPT = (
    "Compile/update the wiki from all raw sources. Process any new or changed "
    "raw files, update source summaries, concept articles, and the master index."
)


ASK_PROMPT = "Answer this question using the knowledge base: {question}"


LINT_PROMPT = """Run a comprehensive health check on the wiki AND actively fill gaps:
1. Check for broken links, orphan articles, missing summaries, stale content, inconsistencies
2. Identify thin concepts (backed by only 1 source) and knowledge gaps
3. For each gap found: use WebSearch to find sources that could fill it, then WebFetch + ingest them into raw/
4. Recompile the wiki with the new sources
5. Save the full report to output/lint-report.md"""


SLIDES_PROMPT = (
    "Create a Marp slide deck about: {topic}. Save it to the output/slides/ "
    "directory. Use the wiki as the source material. Use proper Marp "
    "frontmatter with theme, paginate, etc."
)


REPORT_PROMPT = (
    "Write a comprehensive, detailed report about: {topic}. Use the knowledge "
    "base as the primary source. Include citations with [[wikilinks]]. Save "
    "the report to output/reports/. Structure it with executive summary, "
    "sections, and conclusions."
)


COMPARE_PROMPT = """Create a detailed comparison article: '{x}' vs '{y}'. Include:
- Overview of each
- Comparison table with key dimensions
- Pros/cons of each
- When to use each
- Sources and citations
Use comparison frontmatter with `type: comparison` and `subjects`, not `items`.
Save to wiki/comparisons/ and update the index. If the wiki lacks coverage of either topic, research them first using WebSearch."""


ENTITY_PROMPT = (
    "Create or update an entity page for: '{name}'. Determine the entity "
    "type (person, tool, org, paper, dataset). Research it using the wiki "
    "and, if needed, WebSearch. Save to wiki/entities/ with proper "
    "frontmatter. Update the index and metadata."
)


DISCOVER_PROMPT = """Analyze the current knowledge base and discover new sources to improve it:
1. Read wiki/_meta/summaries.md to understand current coverage
2. Identify topics that are thinly covered or have only 1-2 sources
3. Use WebSearch to find high-quality new sources for those gaps
4. Ingest the best 3-5 new sources found
5. Recompile the wiki
6. Report what was discovered and added"""
