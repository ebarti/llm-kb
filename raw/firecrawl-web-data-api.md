---
title: "Firecrawl: The Web Data API for AI"
source: "https://docs.firecrawl.dev/introduction"
author: "Mendable.ai / Firecrawl"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [web-scraping, crawling, firecrawl, markdown, llm-data, api]
type: repo
status: raw
discovered_via: search
---

# Firecrawl: The Web Data API for AI

AI-powered web crawler that converts websites into clean, LLM-ready data (markdown, JSON). Developed by Mendable.ai.

## Core Modes

1. **Scrape**: Extract content from a single URL as markdown, HTML, or structured JSON
2. **Crawl**: Recursively scrape entire websites
3. **Map**: URL discovery — find all URLs on a website
4. **Search**: Search the web and get full page content from results in one call
5. **Interact**: Click buttons, fill forms, extract dynamic content, navigate
6. **Agent**: Autonomous web data gathering

## API

Base URL: `https://api.firecrawl.dev/v2/`
Authentication: Bearer token (fc-YOUR-API-KEY)

Key endpoints:
- `/scrape` — Extract content from URLs
- `/search` — Search web and get full content
- `/scrape/{scrapeId}/interact` — Interactive page sessions

## Output Formats
- Markdown (primary — optimized for LLMs)
- HTML
- Structured JSON
- Screenshots
- Links extraction

Responses include metadata: title, description, source URL, status code, content type.

## Technical Capabilities
- JavaScript rendering for dynamic content
- Rotating proxies for anti-bot bypass
- Built-in caching mechanisms
- High-throughput performance
- Browser automation (clicking, typing)

## LLM Framework Integrations
- LangChain
- LlamaIndex
- OpenAI
- CrewAI
- MCP Server (Claude, Cursor, Windsurf, VS Code)

## SDKs
- Python: `firecrawl-py`
- Node.js: `@mendable/firecrawl-js`
- CLI: `firecrawl-cli`
- Community SDKs available

## MCP Server
Model Context Protocol Server adds web scraping capabilities directly to LLM clients like Claude and Cursor.
