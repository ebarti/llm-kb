---
title: "Scrapy"
type: entity
entity_type: framework
url: "https://scrapy.org/"
related: ["[[concepts/web-scraping-at-scale]]", "[[entities/playwright]]", "[[entities/beautiful-soup]]"]
tags: [scrapy, python, web-scraping, crawling, framework]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Python's premier web crawling framework — 2,500 pages/min throughput, 1,000 concurrent requests via Twisted async, with built-in pipelines, retry logic, and rate limiting for large-scale scraping."
---

## Overview

Scrapy is a full-featured Python framework for large-scale web crawling and data extraction. It is the standard tool for high-volume static content scraping.

## Key Facts

- **Type**: Python web crawling framework
- **URL**: https://scrapy.org/
- **License**: BSD
- **Notable for**: Highest throughput among Python scraping tools; production-grade pipeline architecture

## Performance

- 2,500 pages/minute throughput
- Up to 1,000 concurrent requests (Twisted async)
- 4GB RAM for 1,000 concurrent requests
- 1.2 CPU cores

## Architecture

- **Engine**: Central data flow manager
- **Spiders**: Define crawling logic and extraction
- **Item Pipelines**: Post-processing, validation, storage
- **Middlewares**: Request/response hooks
- Built-in retry logic, rate limiting, robots.txt compliance

## Limitations

- No JavaScript rendering (static HTML only)
- Steeper learning curve than simpler tools
- Overkill for small scraping tasks

## When to Use

- Static content at massive scale (100K+ pages)
- Distributed crawling across machines
- Enterprise projects requiring proven infrastructure
- When throughput matters more than JS rendering

## Mentions

- [[sources/python-scraping-tools-comparison]] — benchmarked at 2,500 pages/min
- [[concepts/web-scraping-at-scale]] — production-grade crawling
