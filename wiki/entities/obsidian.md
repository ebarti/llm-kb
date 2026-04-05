---
title: "Obsidian"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/dairai-llm-knowledge-bases-architecture]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/stephango-file-over-app]]", "[[sources/stephango-vault-organization]]", "[[sources/stephango-dialectic-interview]]", "[[sources/nxcode-obsidian-ai-second-brain-2026]]", "[[sources/dsebastien-obsidian-plugins-2026]]", "[[sources/pkm-comparison-obsidian-notion-logseq]]"]
related: ["[[concepts/obsidian-as-ide]]", "[[concepts/vault-separation]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/file-over-app]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/obsidian-ai-integration]]", "[[concepts/vault-organization]]", "[[concepts/obsidian-frontmatter-properties]]", "[[concepts/obsidian-graph-view]]", "[[concepts/obsidian-canvas]]", "[[concepts/digital-garden]]", "[[entities/andrej-karpathy]]", "[[entities/steph-ango]]", "[[entities/dataview]]", "[[entities/marp]]", "[[entities/obsidian-copilot]]", "[[entities/smart-connections]]", "[[entities/templater]]", "[[entities/excalidraw]]", "[[entities/logseq]]", "[[comparisons/obsidian-vs-logseq-vs-notion]]"]
last_compiled: 2026-04-05
summary: "A local-first, markdown-based knowledge management platform with 1.5M users, 2,700+ plugins, and a 'file over app' philosophy — serves as the frontend IDE for LLM-maintained wikis."
reading_time: "3 min"
---

## Overview

Obsidian is a desktop and mobile application for managing knowledge bases built on local markdown files. It supports `[[wikilinks]]` for cross-referencing, a graph view that visualizes link structures, and a rich plugin ecosystem. In the LLM knowledge base workflow, Obsidian serves as the human-facing IDE -- a viewer and navigator for the raw data, compiled wiki, and generated artifacts that the LLM produces. Crucially, the human uses Obsidian primarily to read, while the LLM performs all writing and maintenance.

Obsidian was founded by Steph Ango and Shida Li. Its core philosophy of local-first, plain-text storage aligns perfectly with the LLM-KB approach: files remain human-readable, version-controllable, and independent of any proprietary format. This portability is a major reason Karpathy chose it as the frontend for his workflow.

## Key Features (Relevant to LLM-KB)

- **Wikilinks and backlinks**: Native `[[wikilink]]` support creates an implicit graph structure that mirrors how the LLM cross-links concept articles during compilation. The backlinks panel shows all articles referencing the current file.

- **Graph view**: Visualizes the entire link graph of the wiki, making it possible to see clusters of related concepts and identify orphan articles at a glance.

- **Web Clipper**: A browser extension that converts web articles into markdown files, serving as the primary ingestion tool for adding new raw sources to the `raw/` directory.

- **Local image storage**: A hotkey workflow downloads referenced images locally, enabling the LLM to reference visual content during compilation.

- **Plugin ecosystem**: Plugins like [[entities/marp]] (slide deck rendering) and [[entities/dataview]] (structured queries over frontmatter metadata) extend Obsidian's capabilities for viewing LLM-generated artifacts.

- **Vault system**: Obsidian organizes files into "vaults" (directories). [[entities/steph-ango]] recommended maintaining separate vaults for human-curated and agent-generated content to prevent [[concepts/hallucination-contamination]].

## Role in LLM Knowledge Bases

Obsidian is the default viewing layer in Karpathy's architecture and in most derivative implementations. It provides the bridge between the LLM's markdown output and human comprehension. The wiki directory structure (`wiki/sources/`, `wiki/concepts/`, `wiki/_meta/`) maps directly to Obsidian's file-and-folder navigation. The graph view and backlinks surface the link structure the LLM builds during [[concepts/wiki-compilation]].

Gallagher initially used Obsidian for his personal knowledge management but found it insufficient for structural reasoning, leading him to develop the Knowledge Graph Kit with [[entities/sqlite]] and [[entities/chromadb]] instead. This contrast illustrates Obsidian's sweet spot: excellent for reading and navigating text-based knowledge, less suited for formal graph operations or task management.

## Platform Statistics (2026)

- **1.5 million** active users with 22% year-over-year growth
- **2,700+** community plugins, **100+** AI-related extensions
- **Free** for personal and business use (commercial license removed early 2025)
- **Optional paid services**: Sync ($5/month), Publish ($10/month)
- **Team size**: 7-12 people, no venture capital, funded entirely by users
- **Performance**: 95% responsiveness, <200ms latency at 20,000 notes

## Philosophy: File over App

[[entities/steph-ango]]'s [[concepts/file-over-app]] philosophy is Obsidian's foundational design principle: files in open formats outlast any application. Five manifesto principles: independence, user-only funding, small team, privacy, data durability. Ango states: "The company is secondary to my personal goals of using the tool I want."

## Plugin Ecosystem

The [[concepts/obsidian-plugin-ecosystem]] transforms Obsidian from a markdown editor into a programmable knowledge platform. Key plugins: [[entities/dataview]] (SQL-like queries), [[entities/templater]] (JS-powered automation), [[entities/obsidian-copilot]] (100K+ user AI assistant), [[entities/smart-connections]] (RAG vault QA), [[entities/excalidraw]] (most-downloaded, diagramming). See also [[concepts/obsidian-canvas]], [[concepts/obsidian-graph-view]].

## AI Integration

Two paradigms (see [[concepts/obsidian-ai-integration]]): plugin-based AI (Copilot, Smart Connections, Sonar, SystemSculpt) running inside Obsidian, and external agent AI (Claude Code + MCP) operating on the vault via the file system. The external approach is architecturally identical to this knowledge base.

## Key 2025-2026 Developments

- **Bases** (November 2025): Native database feature with table/list views
- **Commercial license removal** (early 2025): Free for all use
- **Claude Code + MCP integration**: External LLM agents operating on vaults
- **Properties system**: YAML frontmatter with typed properties, vault-wide rename ([[concepts/obsidian-frontmatter-properties]])

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] -- described as the IDE frontend for viewing raw data, wiki, and visualizations
- [[sources/dairai-llm-knowledge-bases-architecture]] -- listed as a core implementation requirement
- [[sources/antigravity-post-code-ai-workflow]] -- included in the minimum viable setup; Steph Ango's vault separation recommendation
- [[sources/gallagher-second-brain-knowledge-graphs]] -- Gallagher's initial tool before switching to graph-based approach
- [[sources/stephango-file-over-app]] -- the "file over app" manifesto
- [[sources/stephango-vault-organization]] -- CEO's personal vault structure
- [[sources/stephango-dialectic-interview]] -- company principles and design philosophy
- [[sources/nxcode-obsidian-ai-second-brain-2026]] -- AI integration guide with platform statistics
- [[sources/dsebastien-obsidian-plugins-2026]] -- comprehensive 75+ plugin guide
- [[sources/pkm-comparison-obsidian-notion-logseq]] -- three-way PKM comparison
