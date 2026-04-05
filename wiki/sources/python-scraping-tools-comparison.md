---
title: "Source: Python Web Scraping — Beautiful Soup vs Scrapy vs Playwright"
type: source-summary
source: "[[raw/python-scraping-tools-comparison]]"
related: ["[[concepts/web-scraping-at-scale]]", "[[entities/playwright]]", "[[entities/scrapy]]", "[[entities/beautiful-soup]]"]
tags: [python, web-scraping, beautiful-soup, scrapy, playwright, comparison]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Systematic comparison: BeautifulSoup (lightweight parsing), Scrapy (2,500 pages/min at scale), Playwright (JS rendering, 800 pages/min) — with performance benchmarks and selection criteria."
---

## Key Points

- BeautifulSoup: lightweight HTML parser, handles malformed markup, lxml parser is 50% faster than html5lib
- Scrapy: 2,500 pages/min, 1,000 concurrent requests, 4GB RAM, built-in retry and rate limiting
- Playwright: full JS rendering, auto-waiting, 800 pages/min, 6GB RAM, 2.8 CPU cores, multi-browser
- Hybrid approach: Playwright for JS rendering → BeautifulSoup for efficient parsing
- Scrapy dominates throughput; Playwright dominates dynamic content; BeautifulSoup is the parser glue

## Detailed Summary

This DasRoot comparison provides the first quantitative benchmarks across all three major Python scraping tools. The numbers are revealing: Scrapy achieves 3x Playwright's throughput for static content, but Playwright handles JavaScript-rendered pages that Scrapy cannot touch.

For [[concepts/web-scraping-at-scale]] in knowledge base construction, the selection matrix is clear:
- **Static blogs, documentation, Wikipedia** → Scrapy for speed
- **Modern web apps, SPAs, interactive sites** → Playwright
- **Quick extraction from known HTML** → BeautifulSoup + requests
- **Mixed content** → Playwright + BeautifulSoup hybrid

The resource consumption numbers (4GB for Scrapy at 1K concurrent vs. 6GB for Playwright at 50 threads) highlight why headless browser scraping is expensive at scale — a key architectural consideration for knowledge base ingest pipelines.

## Concepts Introduced or Discussed

- [[concepts/web-scraping-at-scale]] — tool selection and performance characteristics
- [[concepts/content-extraction]] — parsing and extraction strategies
- [[concepts/anti-bot-evasion]] — Playwright's stealth mode and auto-waiting

## Metadata

- **Author**: DasRoot
- **Date Published**: 2025-12
- **Format**: article
- **URL**: https://dasroot.net/posts/2025/12/python-web-scraping-beautiful-soup/
