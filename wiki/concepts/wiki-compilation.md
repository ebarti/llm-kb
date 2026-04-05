---
title: "Wiki Compilation"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/linting-and-health-checks]]"]
last_compiled: 2026-04-05
summary: "The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source summaries and concept articles."
---

## Overview

Wiki compilation is the process by which an LLM transforms a `raw/` directory of ingested source documents into a structured `wiki/` of markdown files. The process is incremental — only new or changed sources trigger updates to the wiki.

## Key Ideas

- **Source summaries**: Each raw file gets a summary article in `wiki/sources/` covering key points, quotes, and related concepts.
- **Concept articles**: The LLM identifies concepts that appear across multiple sources and synthesizes cross-source articles in `wiki/concepts/`.
- **Cross-linking**: Obsidian-style `[[wikilinks]]` connect concept articles, source summaries, and raw files into a navigable graph.
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

## Related Concepts

- [[concepts/llm-knowledge-base]] — the broader system this pipeline belongs to
- [[concepts/linting-and-health-checks]] — downstream quality checks on the compiled wiki
