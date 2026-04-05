---
title: "Markdown as Universal Interface"
type: concept
sources: ["[[sources/antigravity-post-code-ai-workflow]]", "[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/obsidian-as-ide]]", "[[concepts/cheap-ontology]]"]
last_compiled: 2026-04-05
summary: "The observation that markdown is simultaneously human-readable, LLM-friendly, version-controllable, tool-agnostic, and future-proof — making it the optimal substrate for LLM-maintained knowledge bases."
---

## Overview

Karpathy's system and its derivatives rely entirely on markdown as the storage and interchange format. This isn't incidental — markdown uniquely satisfies all the competing requirements of a personal knowledge system.

## Why Markdown Works

**Human-readable**: Anyone can open a `.md` file in any text editor and read it. No schema to understand, no database to query.

**LLM-friendly**: Markdown is heavily represented in training data. LLMs generate well-structured markdown natively. Headers, bullets, wikilinks, code blocks — all map naturally to LLM output.

**Version-controllable**: Plain text files work perfectly with Git. Full history, diffing, rollback. Enterprise use cases add version control as a governance mechanism.

**Tool-agnostic**: Obsidian, VS Code, Zed, Cursor, Vim — any editor works. No vendor lock-in to a specific knowledge management platform.

**Future-proof**: `.md` files will be readable in 50 years. Proprietary database formats won't be.

**Wikilinks for structure**: `[[concept-name]]` provides implicit graph structure without a graph database. LLMs can follow wikilinks during compilation to build coherent concept articles.

## The Markdown Workflow

```
raw/source.md          → LLM reads (immutable source of truth)
wiki/concepts/foo.md   → LLM writes (concept articles with [[wikilinks]])
wiki/sources/bar.md    → LLM writes (source summaries)
wiki/_index.md         → LLM writes (master index)
output/report.md       → LLM writes (generated artifacts)
```

All human-readable. All versionable. All processable by any LLM.

## Limitations

- No formal query language (unlike SPARQL for knowledge graphs)
- Implicit structure depends on LLM following conventions consistently
- Wikilinks require filename matching to resolve — broken links are silent failures until linting
- No built-in temporal tracking (unlike Graphiti's time windows)

## Sources
- [[sources/antigravity-post-code-ai-workflow]] — articulates "markdown as universal interface" explicitly
- [[sources/karpathy-llm-knowledge-bases]] — the system that embodies this principle

## Related Concepts
- [[concepts/llm-knowledge-base]] — uses markdown as substrate
- [[concepts/obsidian-as-ide]] — the viewer/navigator for the markdown files
- [[concepts/cheap-ontology]] — markdown replacing formal ontology schemas
- [[concepts/knowledge-graph]] — the structured alternative
