---
title: "Wiki Compilation"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/linting-and-health-checks]]", "[[concepts/information-extraction]]", "[[concepts/named-entity-recognition]]", "[[concepts/relation-extraction]]", "[[concepts/structured-output-extraction]]", "[[concepts/claim-extraction]]", "[[concepts/llm-summarization]]", "[[concepts/entity-linking]]", "[[concepts/document-processing-pipeline]]", "[[concepts/incremental-etl]]", "[[concepts/document-chunking-strategies]]"]
last_compiled: 2026-04-05
summary: "The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source summaries and concept articles."
reading_time: "2 min"
---

## Overview

Wiki compilation is the process by which an LLM transforms a `raw/` directory of ingested source documents into a structured `wiki/` of markdown files. The process is incremental — only new or changed sources trigger updates to the wiki.

## Key Ideas

- **Source summaries**: Each raw file gets a summary article in `wiki/sources/` covering key points, quotes, and related concepts.
- **Concept articles**: The LLM identifies concepts that appear across multiple sources and synthesizes cross-source articles in `wiki/concepts/`.
- **Cross-linking**: Obsidian-style wikilinks connect concept articles, source summaries, and raw files into a navigable graph.
- **Index and metadata**: The LLM maintains `_index.md` (master article list), `_meta/summaries.md` (one-line summaries), `_meta/links.md` (backlink graph), and `_meta/manifest.md` (compiled file tracking).
- **Incrementalism**: The manifest tracks which raw files have been processed so compilation only touches what's new.

## Compilation Steps

1. Read `_meta/manifest.md` to identify unprocessed raw files
2. For each new raw file: create/update `wiki/sources/<name>.md`
3. Identify key concepts; create/update `wiki/concepts/<concept>.md`
4. Rebuild `wiki/_index.md`
5. Update `_meta/summaries.md`, `_meta/links.md`, `_meta/manifest.md`

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's description of the raw→wiki pipeline

## Information Extraction in Compilation

Wiki compilation is fundamentally an [[concepts/information-extraction]] pipeline. Each compilation step involves specific IE subtasks:

| Compilation Step | IE Subtask | Tool/Approach |
|-----------------|------------|---------------|
| Extract title, author, date, tags | [[concepts/structured-output-extraction]] | Pydantic schema / [[entities/instructor]] |
| Identify people, tools, papers | [[concepts/named-entity-recognition]] | Zero-shot NER via LLM prompting |
| Connect entities to concepts | [[concepts/relation-extraction]] | Subject-predicate-object triple extraction |
| Deduplicate entity mentions | [[concepts/entity-linking]] | LLM-based clustering (KGGen pattern) |
| Create source summaries | [[concepts/llm-summarization]] | Hybrid extract-then-abstract |
| Verify extracted claims | [[concepts/claim-extraction]] | Atomic decomposition (Claimify pattern) |

The wiki compiler currently uses an implicit lightweight schema (entity types: person, tool, org, paper, dataset). [[concepts/schema-guided-extraction]] research suggests this could evolve toward a dynamic schema that expands as new entity types emerge.

## Related Concepts

- [[concepts/llm-knowledge-base]] — the broader system this pipeline belongs to
- [[concepts/linting-and-health-checks]] — downstream quality checks on the compiled wiki
- [[concepts/information-extraction]] — the foundational capability powering compilation
- [[concepts/structured-output-extraction]] — ensures schema-conformant extraction output
- [[concepts/llm-summarization]] — drives source summary creation
- [[concepts/entity-linking]] — deduplicates entity mentions across sources
- [[concepts/claim-extraction]] — enables fact verification of wiki content

## Related Entities

- [[entities/andrej-karpathy]] — defined the compilation pipeline
- [[entities/obsidian-web-clipper]] — primary ingestion tool feeding raw/
