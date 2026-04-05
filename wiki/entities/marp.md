---
title: "Marp"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/marp-markdown-presentations]]"]
related: ["[[concepts/obsidian-as-ide]]", "[[concepts/llm-knowledge-base]]", "[[entities/obsidian]]", "[[entities/matplotlib]]"]
last_compiled: 2026-04-06
summary: "A markdown-based presentation framework used within Obsidian to render LLM-generated slide decks as one of the multi-format output options in the knowledge base workflow."
reading_time: "2 min"
---

## Overview

Marp (Markdown Presentation Ecosystem) is an open-source framework that converts markdown files into presentation slides. It supports a simple syntax where slide separators, themes, and layouts are defined within standard markdown, making it trivially easy for an LLM to generate presentation content without requiring proprietary formats like PowerPoint or Google Slides.

In Karpathy's LLM knowledge base workflow, Marp serves as one of the multi-format output channels. When a user asks the LLM a question, the response can be rendered not just as a markdown report but as a Marp-formatted slide deck viewable directly within [[entities/obsidian]] via a plugin.

## Key Features

- **Markdown-native**: Slides are written as plain markdown with `---` separators between slides, headers for titles, and bullet points for content. This means any LLM that can write markdown can write Marp presentations.

- **Obsidian integration**: The Marp plugin for Obsidian renders slide previews inline, keeping all artifacts -- wiki articles, reports, and presentations -- within the same viewing environment.

- **Export formats**: Marp can export to HTML, PDF, and PPTX, making LLM-generated presentations usable outside the Obsidian ecosystem.

- **Theming and directives**: CSS themes and per-slide directives (backgrounds, layouts, sizing) can be embedded in the markdown frontmatter.

## Role in LLM Knowledge Bases

Marp exemplifies the multi-format output principle of the LLM-KB workflow. Rather than restricting LLM output to text responses in a terminal, the system leverages markdown-based tools to produce diverse artifacts: reports (plain markdown), visualizations ([[entities/matplotlib]]), and presentations (Marp). These outputs can then be filed back into the wiki through the filing loop, enriching the knowledge base for future queries.

The choice of Marp over proprietary presentation tools also reinforces the [[concepts/markdown-as-universal-interface]] principle: all content remains in human-readable, version-controllable plain text that any LLM can generate and any editor can display.

## Ecosystem Details

The Marp ecosystem (from [[sources/marp-markdown-presentations]]) consists of four components:

1. **Marp for VS Code** — real-time editing and preview within VS Code
2. **Marp CLI** — command-line batch conversion tool
3. **Marp Core** — the underlying conversion engine
4. **Marpit Framework** — a pluggable HTML/CSS slide deck framework that developers can extend via plugins

Three built-in themes (default, gaia, uncover) are available, with custom themes via CSS. Extended syntax supports directives, math typesetting, image syntax, and auto-scaling. All tools are MIT-licensed open source.

## Mentioned In

- [[sources/marp-markdown-presentations]] — full ecosystem and feature overview
- [[sources/karpathy-llm-knowledge-bases]] -- listed as an Obsidian plugin used for rendering LLM-generated slide decks
- [[sources/antigravity-post-code-ai-workflow]] -- included in the multi-format output step (step 5) of the 6-step workflow
