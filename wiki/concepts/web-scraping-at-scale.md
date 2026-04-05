---
title: "Web Scraping at Scale"
type: concept
sources: ["[[sources/firecrawl-web-data-api]]", "[[sources/web-scraping-best-practices-2026]]", "[[sources/python-scraping-tools-comparison]]", "[[sources/crawl4ai-llm-web-crawler]]", "[[sources/web-scraping-legality-ethics-2025]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/content-extraction]]", "[[concepts/anti-bot-evasion]]", "[[concepts/web-scraping-ethics-and-law]]", "[[concepts/html-to-markdown-conversion]]", "[[entities/firecrawl]]", "[[entities/crawl4ai]]", "[[entities/scrapy]]", "[[entities/playwright]]"]
last_compiled: 2026-04-05
summary: "Modern web scraping for AI pipelines: async concurrency, proxy rotation, headless browsers for JS, API-based services (Firecrawl, Crawl4AI) that output LLM-ready markdown, and scaling from scripts to microservice architectures."
---

## Overview

Web scraping is stage 0 of any [[concepts/document-processing-pipeline]] that ingests web content. At scale — thousands to millions of pages — it transforms from a simple script into a distributed system requiring concurrency management, anti-bot evasion, error handling, and output normalization.

For LLM knowledge bases, web scraping is the primary acquisition mechanism: finding, fetching, and converting web pages into clean text for ingestion. This wiki itself depends on web scraping (via WebFetch) to acquire raw sources.

## Key Technical Challenges

### Concurrency and Throughput
Modern websites are slow and content-heavy. Sequential fetching is inadequate at scale. Solutions:
- **Async I/O**: aiohttp, httpx for concurrent HTTP requests
- **Job queues**: Celery, RabbitMQ for distributed task management
- **Serverless**: AWS Lambda, Cloud Functions for elastic scaling
- **Frameworks**: Scrapy (Python) — built for large-scale crawling with async support

### Anti-Bot Detection
Websites increasingly deploy protections:
- **IP rotation**: Residential proxies, rotating datacenter IPs
- **User-Agent randomization**: Rotate browser fingerprints
- **Request throttling**: Respect Crawl-delay, randomize intervals
- **Realistic headers**: Accept, Accept-Language, Referer headers

### JavaScript-Heavy Sites
Content rendered client-side requires headless browsers:
- **Playwright**: Modern, fast, supports Chromium/Firefox/WebKit
- **Puppeteer**: Node.js, Chrome/Chromium only
- **Selenium**: Oldest, broadest browser support

### Output Normalization
Raw HTML must be converted to clean, structured content. The ideal output for LLM consumption is markdown — see [[concepts/markdown-as-universal-interface]].

## AI-Focused Web Scraping

[[entities/firecrawl]] represents the new category of AI-optimized scraping services:
- Single API call → clean markdown, JSON, or screenshots
- Handles JavaScript, anti-bot, proxies automatically
- Modes: scrape (single URL), crawl (entire site), map (URL discovery), search (web search + content)
- MCP Server integration for direct LLM agent access
- Integrates with LangChain, LlamaIndex, CrewAI

This is a paradigm shift: instead of building scraping infrastructure, AI developers consume a "web data API" that outputs LLM-ready content.

## Architecture at Scale

**Small scale (100s of pages)**: Simple scripts with requests + BeautifulSoup. Adequate for personal knowledge bases.

**Medium scale (10K-100K pages)**: Scrapy framework with rotating proxies and retry logic. Job queue for parallelization.

**Large scale (1M+ pages)**: Microservice architecture with separate services for URL management, fetching, rendering, parsing, and storage. Kubernetes for orchestration. Message queues between stages.

## Legal and Ethical Considerations

- Always check robots.txt before scraping
- Respect Crawl-delay directives
- Avoid overloading servers with aggressive request rates
- Be aware of Terms of Service restrictions
- Consider the Computer Fraud and Abuse Act (US) and similar legislation

## Tool Selection Guide

Based on benchmarks from [[sources/python-scraping-tools-comparison]]:

| Tool | Best For | Throughput | JS Support |
|------|----------|-----------|------------|
| [[entities/scrapy]] | High-volume static crawling | 2,500 pages/min | No |
| [[entities/playwright]] | JS-heavy sites, SPAs | 800 pages/min | Full |
| [[entities/beautiful-soup]] | Simple parsing, prototyping | N/A (parser only) | No |
| [[entities/crawl4ai]] | LLM-ready markdown output | Async parallel | Full |
| [[entities/firecrawl]] | Managed API, no infrastructure | API-managed | Full |

## Sources

- [[sources/firecrawl-web-data-api]] — AI-focused web scraping API
- [[sources/web-scraping-best-practices-2026]] — comprehensive 2026 best practices
- [[sources/python-scraping-tools-comparison]] — quantitative tool benchmarks
- [[sources/crawl4ai-llm-web-crawler]] — open-source LLM-focused crawler
- [[sources/web-scraping-legality-ethics-2025]] — legal framework

## Related Concepts

- [[concepts/document-processing-pipeline]] — web scraping is stage 0
- [[concepts/content-extraction]] — extracting clean content from fetched pages
- [[concepts/html-to-markdown-conversion]] — converting extracted HTML to markdown
- [[concepts/anti-bot-evasion]] — avoiding detection at scale
- [[concepts/web-scraping-ethics-and-law]] — legal constraints
- [[concepts/markdown-as-universal-interface]] — markdown as scraping output format
- [[entities/firecrawl]] — leading AI-focused scraping service
- [[entities/crawl4ai]] — leading open-source scraping tool
