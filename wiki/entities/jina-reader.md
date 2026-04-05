---
title: "Jina Reader API"
type: entity
entity_type: tool
url: "https://jina.ai/reader/"
related: ["[[concepts/content-extraction]]", "[[concepts/html-to-markdown-conversion]]", "[[entities/reader-lm]]", "[[entities/mozilla-readability]]"]
tags: [jina, reader-api, content-extraction, markdown]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Jina's Reader API converts any URL to LLM-friendly markdown by prefixing r.jina.ai/ — uses headless Chrome + Readability + Turndown, with optional ReaderLM v2 neural engine."
---

## Overview

The Jina Reader API is a web service that converts any URL into clean, LLM-friendly markdown text. It abstracts away the entire content extraction pipeline — headless browser rendering, boilerplate removal, and format conversion — into a single API call.

## Key Facts

- **Type**: Web API
- **URL**: https://jina.ai/reader/
- **Developer**: Jina AI
- **Notable for**: Simplest possible interface — just prefix any URL with `r.jina.ai/`

## How It Works

### Default Pipeline (Heuristic)
1. **Headless Chrome** fetches the source page (renders JavaScript)
2. **[[entities/mozilla-readability]]** extracts the main content
3. **Regex patterns** clean up extraction artifacts
4. **Turndown** (JavaScript library) converts HTML to markdown

### ReaderLM v2 Engine (Neural)
Set `x-engine: readerlm-v2` header to use [[entities/reader-lm]] instead of the heuristic pipeline. Higher quality but 3x token consumption.

## Endpoints

- `r.jina.ai/{url}` — Convert URL to LLM-ready markdown
- `s.jina.ai/{query}` — Web search with full page content extraction

## Response Format

JSON containing: URL, title, content (markdown), timestamp, and metadata.

## Role in Knowledge Base

The Jina Reader API is directly comparable to WebFetch in the wiki's ingest pipeline. Both convert URLs to clean text. The Reader API's advantage is its dedicated optimization for LLM consumption.

## Mentions

- [[sources/jina-reader-lm-html-to-markdown]] — detailed technical analysis
- [[concepts/content-extraction]] — as an integrated extraction tool
- [[concepts/html-to-markdown-conversion]] — as conversion endpoint
