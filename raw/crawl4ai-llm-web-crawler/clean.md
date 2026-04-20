---
title: "Crawl4AI: Open-Source LLM-Friendly Web Crawler"
source: "https://github.com/unclecode/crawl4ai"
author: "unclecode"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [crawl4ai, web-scraping, llm, markdown, content-extraction, open-source]
type: repo
status: raw
discovered_via: search
---

# Crawl4AI: Open-Source LLM-Friendly Web Crawler

Crawl4AI is the #1 trending open-source web crawler on GitHub (63K+ stars). It transforms web content into clean, structured Markdown for RAG, agents, and data pipelines. Apache 2.0 licensed.

## Core Architecture

Built on Playwright (async), providing:
- Persistent browser profiles with saved authentication states
- Session management for multi-step crawling
- Full control over headers, cookies, user agents
- Multi-browser support (Chromium, Firefox, WebKit)
- Stealth mode to mimic legitimate users

## Markdown Generation

Dual-output system:
- **Raw Markdown**: Complete, unfiltered content conversion
- **Fit Markdown**: Intelligently filtered output using heuristic-based noise removal + BM25-based filtering for extracting core information

## Data Extraction Methods

### LLM-Driven Extraction
Compatible with open-source and proprietary LLMs for structured data recovery. Implements chunking:
- Topic-based chunking for semantic coherence
- Regex-based chunking for structured data
- Sentence-level chunking for granular processing
- Cosine similarity matching for semantic relevance

### CSS/XPath Extraction
Fast schema-based extraction using XPath and CSS selectors — no AI overhead. Custom schemas for structured JSON from repetitive patterns.

### Media Handling
Extracts images, audio, videos, responsive image formats (srcset, picture).

## Content Filtering

- **Pruning Content Filter**: Fixed-threshold removal of low-value content
- **BM25 Content Filter**: Relevance-based filtering aligned with user queries
- Custom strategy support

## Advanced Features

- JavaScript execution and async/sync waiting for dynamic content
- Automatic 3-tier anti-bot detection with proxy escalation (v0.8.5)
- Shadow DOM flattening
- Consent popup removal
- Crash recovery with resume_state callbacks
- Lazy load handling (simulated scrolling)
- Deep crawl with 5-10x faster URL discovery via prefetch mode

## Deployment

```bash
pip install -U crawl4ai
crawl4ai-setup
```

Docker: `docker run -d -p 11235:11235 unclecode/crawl4ai:latest`
- Real-time monitoring dashboard
- Browser pooling with pre-warming
- Interactive playground
- Multi-architecture (AMD64/ARM64)

## Significance for LLM Knowledge Bases

Crawl4AI represents the convergence of web scraping and AI: it's built from the ground up to produce LLM-consumable output. Its BM25 content filtering is particularly relevant for knowledge base construction — it can extract only the content relevant to a specific query, reducing noise before ingestion.
