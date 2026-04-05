---
title: "Crawl4AI"
type: entity
entity_type: tool
url: "https://github.com/unclecode/crawl4ai"
related: ["[[concepts/web-scraping-at-scale]]", "[[concepts/content-extraction]]", "[[entities/firecrawl]]", "[[entities/playwright]]"]
tags: [crawl4ai, web-scraping, open-source, llm, markdown]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The #1 trending open-source web crawler (63K+ GitHub stars) — Playwright-based async crawler producing LLM-ready markdown with BM25 relevance filtering, multi-strategy extraction, and anti-bot detection."
---

## Overview

Crawl4AI is an open-source web crawler and scraper built specifically for LLM applications. It produces clean, structured markdown optimized for RAG pipelines, AI agents, and data ingestion.

## Key Facts

- **Type**: Open-source Python library + Docker service
- **URL**: https://github.com/unclecode/crawl4ai
- **License**: Apache 2.0
- **Stars**: 63,000+ (GitHub)
- **Notable for**: Open-source alternative to Firecrawl; BM25-filtered "fit markdown" output

## Key Features

### Dual Markdown Output
- **Raw Markdown**: Complete, unfiltered content conversion
- **Fit Markdown**: BM25-filtered to extract only content relevant to a specific query

### Multi-Strategy Extraction
- LLM-driven extraction (any open-source or proprietary model)
- CSS/XPath schema-based extraction (fast, no AI overhead)
- Media extraction (images, audio, video, srcset, picture)

### Production Features
- Playwright-based async architecture (Chromium, Firefox, WebKit)
- 3-tier anti-bot detection with automatic proxy escalation
- Shadow DOM flattening, consent popup removal
- Crash recovery with resume_state callbacks
- Docker deployment with real-time monitoring dashboard
- Browser pooling with pre-warming

### Chunking
- Topic-based, regex-based, sentence-level
- Cosine similarity matching for semantic relevance

## Comparison with Firecrawl

| Feature | Crawl4AI | [[entities/firecrawl]] |
|---------|----------|-----------|
| Type | Open-source library | SaaS API |
| Cost | Free | Per-credit pricing |
| BM25 filtering | Yes (fit markdown) | No |
| Self-hosted | Yes (Docker) | Yes (self-hosted option) |
| LLM extraction | Built-in | Built-in |
| Anti-bot | 3-tier escalation | Rotating proxies |

## Mentions

- [[sources/crawl4ai-llm-web-crawler]] — detailed feature analysis
- [[concepts/web-scraping-at-scale]] — as leading open-source solution
- [[concepts/content-extraction]] — BM25-filtered relevance extraction
