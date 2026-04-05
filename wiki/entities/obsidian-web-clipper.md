---
title: "Obsidian Web Clipper"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/dairai-llm-knowledge-bases-architecture]]", "[[sources/antigravity-post-code-ai-workflow]]"]
related: ["[[entities/obsidian]]", "[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-06
summary: "A browser extension for converting web articles into markdown files for ingestion into the raw/ directory of an LLM knowledge base."
reading_time: "2 min"
---

## Overview

The Obsidian Web Clipper is a browser extension that converts web pages into markdown files and saves them directly into an [[entities/obsidian]] vault. In Karpathy's LLM knowledge base workflow, it serves as the primary ingestion tool for web-based content, converting articles, blog posts, and documentation pages into the `.md` format that the LLM can then process during [[concepts/wiki-compilation]].

The Web Clipper extracts the main content of a web page, strips navigation and advertising elements, converts HTML to clean markdown, and preserves structural elements like headers, lists, code blocks, and links. It saves the resulting `.md` file into a user-configured directory -- in the LLM-KB workflow, this is typically the `raw/` directory that serves as the immutable source of truth.

## Key Features

- **HTML to markdown conversion**: Automatically extracts and converts web page content to clean, readable markdown.

- **Configurable save location**: Files can be directed to specific vault directories (e.g., `raw/`) with customizable naming templates.

- **Metadata preservation**: Captures URL, page title, author, and capture date as YAML frontmatter, providing provenance information for the LLM.

- **Image handling**: Combined with a hotkey for downloading referenced images locally, the Web Clipper enables the LLM to access visual content during compilation.

## Role in LLM Knowledge Bases

The Web Clipper is the entry point of the LLM-KB pipeline. Every article, paper, or documentation page that enters the knowledge base typically passes through the Web Clipper first, being converted from HTML to markdown and deposited in `raw/`. The quality of this conversion directly affects the downstream [[concepts/data-quality-bottleneck]]: poorly converted content (missing sections, broken formatting, lost images) produces lower-quality wiki articles during compilation.

In the minimum viable setup described by [[sources/antigravity-post-code-ai-workflow]], installing Obsidian + Web Clipper is the first step. This tool, combined with the LLM API, is the minimum infrastructure required to begin building an LLM-maintained knowledge base.

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] -- described as the tool used to convert web articles to markdown for ingestion
- [[sources/dairai-llm-knowledge-bases-architecture]] -- listed as a core implementation requirement for the ingestion phase
- [[sources/antigravity-post-code-ai-workflow]] -- included in the minimum viable setup instructions
