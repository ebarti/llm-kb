---
title: "Linting and Health Checks"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "LLM-driven health checks over the compiled wiki to find inconsistencies, fill data gaps, detect broken links, identify orphan articles, and suggest new content."
reading_time: "1 min"
---

## Overview

Wiki linting is the process of running LLM-powered health checks over the compiled wiki to maintain data integrity, surface inconsistencies, and suggest improvements. It is an incremental, ongoing process rather than a one-time step.

## Key Ideas

- **Inconsistency detection**: The LLM compares claims across articles to find contradictions.
- **Missing data imputation**: Gaps in knowledge can be filled using web search tools during a lint pass.
- **Broken link detection**: Find `[[wikilinks]]` pointing to non-existent files.
- **Orphan detection**: Identify wiki articles with no incoming links.
- **New article suggestions**: The LLM identifies concepts mentioned across sources that don't yet have dedicated articles.
- **Stale content detection**: Raw files not yet compiled into the wiki.
- **LLM-generated questions**: The LLM suggests further questions to explore and look into, driving future research directions.

## Output

Lint results are saved to `output/lint-report.md` and can be filed back into the wiki to track outstanding issues.

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's description of LLM health checks over the wiki

## Related Concepts

- [[concepts/llm-knowledge-base]] — the system being linted
- [[concepts/wiki-compilation]] — the pipeline that produces the wiki being checked
