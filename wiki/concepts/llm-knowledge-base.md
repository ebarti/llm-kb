---
title: "LLM Knowledge Base"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/wiki-compilation]]", "[[concepts/obsidian-as-ide]]", "[[concepts/llm-qa-over-documents]]", "[[concepts/linting-and-health-checks]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "A personal knowledge base where an LLM authors and maintains all wiki content from raw ingested sources, with humans interacting only via natural language."
reading_time: "2 min"
---

## Overview

An LLM knowledge base is a system where source documents are ingested into a `raw/` directory and an LLM incrementally compiles them into a structured wiki of markdown files. The human owner interacts with the system only through natural language prompts — the LLM writes, updates, and maintains all wiki content directly.

## Key Ideas

- **LLM as author**: The LLM owns the wiki directory and writes all content. Humans rarely edit wiki files manually.
- **Incremental compilation**: New raw sources are compiled into the wiki without rewriting unchanged articles.
- **Structured output**: The wiki contains source summaries, concept articles with cross-links, backlink graphs, and index files.
- **Self-reinforcing**: Queries and explorations produce outputs (reports, slides, images) that get filed back into the wiki, compounding knowledge over time.
- **Scalable without RAG**: At ~small scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries are sufficient for effective Q&A without a vector database.
- **Product opportunity**: Karpathy notes this workflow could become a polished product rather than a collection of scripts.

## Architecture

```
raw/          ← ingested source documents (source of truth)
wiki/         ← LLM-compiled and maintained
  _index.md   ← master article index
  _meta/      ← summaries, link graph, manifest
  sources/    ← per-source summary articles
  concepts/   ← cross-source concept articles
output/       ← reports, slides, images (filed back into wiki)
```

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — original description of the workflow by Andrej Karpathy

## Related Concepts

- [[concepts/wiki-compilation]] — the pipeline from raw → wiki
- [[concepts/obsidian-as-ide]] — the viewing frontend
- [[concepts/llm-qa-over-documents]] — Q&A over the compiled wiki
- [[concepts/linting-and-health-checks]] — maintaining wiki integrity
- [[concepts/rag-vs-index-based-retrieval]] — why simple indexing can beat RAG

## Related Entities

- [[entities/andrej-karpathy]] — originator of this methodology
- [[entities/obsidian]] — the IDE/viewer
- [[entities/marp]], [[entities/matplotlib]] — multi-format output tools
- [[entities/obsidian-web-clipper]] — primary ingestion tool

## Related Comparisons

- [[comparisons/storm-vs-karpathy-workflow]] — single-shot vs. accumulating KB
- [[comparisons/knowledge-graph-vs-wiki]] — graphs vs. markdown
- [[comparisons/manual-pkm-vs-llm-pkm]] — manual vs. AI-maintained PKM
- [[comparisons/fine-tuning-vs-context-window]] — weights vs. context
