---
title: "Obsidian as IDE"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — with the LLM as the actual author."
---

## Overview

In the LLM knowledge base workflow, Obsidian serves as the human-facing IDE: a viewer for raw data, the compiled wiki, and generated outputs. Crucially, the human uses Obsidian primarily to *read* — the LLM writes all content.

## Key Ideas

- **Read-only for humans**: The LLM writes and maintains wiki content; humans rarely edit files directly in Obsidian.
- **Web Clipper**: The Obsidian Web Clipper browser extension converts web articles to markdown for ingestion into `raw/`.
- **Image downloads**: A hotkey workflow downloads referenced images locally so the LLM can reference them during compilation.
- **Plugin ecosystem**: Plugins like Marp enable rendering of LLM-generated slide decks directly in Obsidian.
- **Unified view**: Raw sources, wiki articles, reports, slides, and matplotlib images are all viewable within the same Obsidian vault.

## Why Obsidian

Obsidian's native support for markdown, `[[wikilinks]]`, and backlink graphs makes it a natural fit for a wiki structured around interconnected `.md` files. The graph view and backlinks panel expose the link structure the LLM builds during compilation.

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's description of Obsidian as the frontend IDE

## Related Concepts

- [[concepts/llm-knowledge-base]] — the broader system
- [[concepts/wiki-compilation]] — the pipeline that produces the wiki Obsidian displays
