---
title: "Obsidian as IDE"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/nxcode-obsidian-ai-second-brain-2026]]", "[[sources/stephango-vault-organization]]", "[[sources/dsebastien-obsidian-plugins-2026]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/obsidian-ai-integration]]", "[[concepts/obsidian-graph-view]]", "[[concepts/obsidian-frontmatter-properties]]", "[[concepts/file-over-app]]"]
last_compiled: 2026-04-05
summary: "Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — with the LLM as the actual author and 2,700+ plugins extending the viewer."
reading_time: "2 min"
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

Obsidian's native support for markdown, `[[wikilinks]]`, and backlink graphs makes it a natural fit for a wiki structured around interconnected `.md` files. The [[concepts/obsidian-graph-view]] and backlinks panel expose the link structure the LLM builds during compilation. The [[concepts/file-over-app]] philosophy ensures the vault is accessible to external LLM agents via the file system.

Key IDE-like features for LLM-KB work:

- **[[concepts/obsidian-graph-view]]**: Visualize the entire wiki's link structure — see clusters, orphans, and compilation quality at a glance
- **[[concepts/obsidian-frontmatter-properties]]**: Structured metadata queryable via [[entities/dataview]] — the LLM writes properties, the human queries them
- **[[concepts/obsidian-plugin-ecosystem]]**: 2,700+ plugins extend the viewer (Marp for slides, Dataview for queries, Excalidraw for diagrams, Canvas for spatial layouts)
- **[[concepts/obsidian-canvas]]**: Spatial boards for mapping concept relationships visually
- **Search**: Full-text and property-based search across the entire vault

## Two Modes of AI Interaction

Obsidian now supports two complementary AI interaction modes (see [[concepts/obsidian-ai-integration]]):

1. **LLM-KB mode** (Karpathy's approach): The LLM operates externally via file system or MCP, writing and maintaining all wiki content. Obsidian is purely a viewer. This is the paradigm this knowledge base uses.

2. **Plugin-AI mode**: AI runs inside Obsidian via plugins like [[entities/obsidian-copilot]] and [[entities/smart-connections]]. Users interact with AI through chat interfaces within Obsidian.

These modes can coexist: the external LLM maintains the wiki structure, while plugin-based AI assists with ad-hoc queries and note editing.

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's description of Obsidian as the frontend IDE
- [[sources/nxcode-obsidian-ai-second-brain-2026]] — Obsidian as AI-powered second brain platform
- [[sources/stephango-vault-organization]] — how the CEO uses Obsidian
- [[sources/dsebastien-obsidian-plugins-2026]] — plugins that extend IDE capabilities

## Related Concepts

- [[concepts/llm-knowledge-base]] — the broader system
- [[concepts/wiki-compilation]] — the pipeline that produces the wiki Obsidian displays
- [[concepts/obsidian-plugin-ecosystem]] — plugins extending the IDE
- [[concepts/obsidian-ai-integration]] — AI capabilities within the IDE
- [[concepts/obsidian-graph-view]] — visual verification of compilation quality
- [[concepts/file-over-app]] — the philosophy enabling external LLM access

## Related Entities

- [[entities/obsidian]] — the application itself
- [[entities/obsidian-web-clipper]] — browser extension for ingesting web content
- [[entities/marp]] — slide deck plugin
- [[entities/dataview]] — structured query plugin for frontmatter
- [[entities/steph-ango]] — Obsidian CEO who recommended [[concepts/vault-separation]]
- [[entities/obsidian-copilot]] — AI assistant plugin
- [[entities/smart-connections]] — RAG-based vault QA plugin

## Related Comparisons

- [[comparisons/obsidian-vs-graph-database]] — file-based vs. database storage
- [[comparisons/obsidian-vs-logseq-vs-notion]] — platform comparison
