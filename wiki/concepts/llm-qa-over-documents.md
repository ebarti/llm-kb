---
title: "LLM Q&A Over Documents"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "Using an LLM agent to answer complex questions over a compiled wiki by reading index files and summaries to navigate to relevant full articles, without needing a vector database."
reading_time: "2 min"
---

## Overview

Once a wiki is compiled and large enough, an LLM agent can answer complex research questions by navigating the wiki's index and summary files to find relevant articles, reading them in full, and synthesizing answers.

## Key Ideas

- **Index-first navigation**: The LLM reads `_meta/summaries.md` (one-line summaries of all articles) to identify relevant documents before reading full articles.
- **No vector DB required**: At ~small scale (~100 articles, ~400K words), LLM-maintained summaries and indexes are sufficient — no RAG pipeline needed.
- **Self-improving**: Query outputs (reports, slides, images) are filed back into the wiki, so every Q&A session enhances the knowledge base for future queries.
- **CLI tool integration**: Custom search tools can be handed to the LLM via CLI for larger or more complex queries.
- **Output formats**: Answers are rendered as markdown reports, Marp slide decks, or matplotlib visualizations — not just text in a terminal.

## Workflow

1. User asks a question in natural language
2. LLM reads `_meta/summaries.md` to find relevant articles
3. LLM reads full relevant articles from `wiki/`
4. LLM synthesizes answer, citing sources with wikilinks
5. (Optional) LLM saves substantial answers to `output/reports/` or files them into the wiki

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's description of Q&A over a compiled wiki

## Related Concepts

- [[concepts/llm-knowledge-base]] — the system this Q&A operates over
- [[concepts/rag-vs-index-based-retrieval]] — comparison of index-based vs. vector retrieval approaches
- [[concepts/wiki-compilation]] — the compilation process that makes Q&A possible
