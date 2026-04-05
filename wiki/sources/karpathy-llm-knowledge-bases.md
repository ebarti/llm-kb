---
title: "Source: Thread by @karpathy — LLM Knowledge Bases"
type: source-summary
source: "[[raw/karpathy-llm-knowledge-bases]]"
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]", "[[concepts/obsidian-as-ide]]", "[[concepts/llm-qa-over-documents]]", "[[concepts/linting-and-health-checks]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Karpathy describes using LLMs to build and maintain personal markdown wikis from raw ingested sources, with Obsidian as the viewing IDE and LLM-driven Q&A, output generation, and linting."
---

## Key Points

- LLMs are increasingly useful for **manipulating knowledge** (markdown/images), not just code
- Architecture: `raw/` directory → LLM compiles → `wiki/` of `.md` files with summaries, backlinks, and concept articles
- **Obsidian** serves as the frontend IDE to view raw data, the compiled wiki, and visualizations
- The LLM writes and maintains the wiki; the human rarely edits it directly
- **Q&A** works without fancy RAG at ~small scale (~100 articles, ~400K words): LLM auto-maintains index files and brief summaries to navigate efficiently
- **Outputs**: markdown reports, Marp slideshows, matplotlib images — all viewable in Obsidian; outputs get "filed back" into the wiki
- **Linting**: LLM health checks find inconsistencies, impute missing data via web search, suggest new article candidates
- **Extra tools**: custom CLI search engine handed off to LLM as a tool for larger queries
- **Future direction**: synthetic data generation + finetuning so the LLM "knows" the corpus in its weights
- Karpathy sees potential for a polished product rather than a collection of scripts

## Detailed Summary

Karpathy outlines a workflow where an LLM acts as the author and maintainer of a personal knowledge base. Source documents (articles, papers, repos, datasets) are ingested into a `raw/` directory using tools like the Obsidian Web Clipper. An LLM then incrementally "compiles" these into a structured wiki of markdown files, producing per-source summaries, concept articles with cross-links, and backlink graphs.

Obsidian is used purely as a viewer/IDE — the human does not write wiki content directly. Plugins like Marp allow viewing LLM-generated slide decks inside Obsidian.

For Q&A, Karpathy found that simple index files and one-line summaries maintained by the LLM were sufficient to navigate a ~400K word corpus without needing a vector database or RAG pipeline. The LLM reads the summaries index, selects relevant articles, and synthesizes answers.

Output formats include markdown reports, Marp slides, and matplotlib visualizations. These outputs are often filed back into the wiki, making the knowledge base self-reinforcing.

LLM-driven linting runs health checks: detecting inconsistencies, filling gaps with web searches, and proposing new concept articles based on observed gaps.

## Notable Quotes

> "You rarely ever write or edit the wiki manually, it's the domain of the LLM."

> "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents."

> "I think there is room here for an incredible new product instead of a hacky collection of scripts."

> "My own explorations and queries always 'add up' in the knowledge base."

## Related Concepts

- [[concepts/llm-knowledge-base]] — the core system described in this thread
- [[concepts/wiki-compilation]] — the raw→wiki compilation pipeline
- [[concepts/obsidian-as-ide]] — use of Obsidian as a read-only frontend
- [[concepts/llm-qa-over-documents]] — Q&A without RAG via index+summaries
- [[concepts/linting-and-health-checks]] — LLM-driven wiki health checks
- [[concepts/rag-vs-index-based-retrieval]] — why simple indexing beats RAG at small scale
