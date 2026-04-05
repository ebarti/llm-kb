---
title: "Firecrawl"
type: entity
entity_type: tool
sources: ["[[sources/firecrawl-web-data-api]]"]
related: ["[[concepts/web-scraping-at-scale]]", "[[concepts/document-processing-pipeline]]", "[[concepts/markdown-as-universal-interface]]", "[[entities/langchain]]", "[[entities/llamaindex]]"]
last_compiled: 2026-04-05
summary: "AI-focused web scraping API by Mendable.ai: converts websites to LLM-ready markdown/JSON via single API call, handles JS rendering and anti-bot, six modes (scrape/crawl/map/search/interact/agent), MCP Server for LLM integration."
---

## Overview

Firecrawl is an AI-powered web crawler and data extraction service that converts websites into clean, LLM-ready data formats. Developed by Mendable.ai, it represents a new category of tools purpose-built for AI data pipelines — abstracting away the complexity of modern [[concepts/web-scraping-at-scale]] behind a simple API.

## Key Features

- **Six modes**: Scrape (single URL), Crawl (entire site), Map (URL discovery), Search (web + content), Interact (dynamic content), Agent (autonomous)
- **LLM-optimized output**: Clean markdown, structured JSON, screenshots
- **Anti-bot handling**: JavaScript rendering, proxy rotation, caching
- **MCP Server**: Direct integration with Claude, Cursor, VS Code
- **SDKs**: Python (`firecrawl-py`), Node.js, CLI

## API

- Base URL: `https://api.firecrawl.dev/v2/`
- Auth: Bearer token (fc-YOUR-API-KEY)
- Core endpoints: `/scrape`, `/search`, `/scrape/{id}/interact`

## Integrations

- [[entities/langchain]] — document loader
- [[entities/llamaindex]] — data connector
- OpenAI — function calling
- CrewAI — agent tool

## Relevance to Knowledge Bases

For LLM knowledge base systems, Firecrawl is the ideal acquisition layer: its markdown output aligns with [[concepts/markdown-as-universal-interface]], and its MCP Server enables LLM agents to directly scrape and ingest web content during research operations.

## Mentioned In
- [[sources/firecrawl-web-data-api]] — documentation and technical details
