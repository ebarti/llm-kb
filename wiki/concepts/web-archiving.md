---
title: "Web Archiving"
type: concept
sources: ["[[sources/web-archiving-warc-tools]]"]
related: ["[[concepts/content-extraction]]", "[[concepts/plain-text-longevity]]", "[[concepts/file-over-app]]", "[[concepts/document-processing-pipeline]]"]
tags: [web-archiving, warc, preservation, provenance]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Preserving web content in standardized WARC (ISO 28500) format for permanence and provenance — from institutional tools (Heritrix, Wayback Machine) to personal archiving (ArchiveBox, SingleFile) — critical for knowledge base source integrity."
---

## Overview

Web archiving is the practice of preserving web content for future access. For knowledge base construction, it addresses the fundamental problem of **link rot**: the sources that underpin your knowledge base may disappear at any time. Studies consistently show that ~50% of URLs are dead within 5 years.

The standard approach in most knowledge base systems (including this wiki) is to extract text content and save it in raw/ files. This preserves the text but loses the full context: HTTP headers, linked resources, visual layout, JavaScript state. WARC archiving preserves everything.

## WARC Format

WARC (Web ARChive) is the ISO 28500:2017 international standard. A WARC file contains:
- HTTP request and response (including headers)
- Full page content (HTML, CSS, images, JS)
- Metadata (timestamps, URLs, content types)
- Redirect chains

Used by: Library of Congress, British Library, Internet Archive, Bibliothèque Nationale de France, national libraries worldwide.

## Tool Categories

### Institutional Crawlers
- **Heritrix**: Internet Archive's open-source archival-quality crawler
- **Browsertrix Crawler**: Docker-based high-fidelity crawling with Chromium

### Personal Archiving
- **ArchiveBox**: Self-hosted, creates archives from RSS feeds, bookmarks, and links (wget + Chrome headless)
- **SingleFile**: Browser extension + CLI for single-file HTML archives
- **ArchiveWeb.Page**: Chrome plugin for interactive archiving with WARC/WACZ export

### Replay Tools
- **OpenWayback**: Open-source Wayback Machine
- **PYWB**: Python web archive replay
- **ReplayWeb.page**: Client-side WARC/WACZ replay

## Relevance to LLM Knowledge Bases

Web archiving strengthens the raw/ layer of an LLM knowledge base:

1. **Permanence**: Archived pages persist even when URLs die
2. **Provenance**: Full HTTP context for source verification
3. **Reproducibility**: Others can verify your sources against archived originals
4. **Legal defense**: Archived copies prove what content was publicly available when you scraped it

The ideal ingest pipeline would be: **fetch → archive (WARC) → extract (Readability/Trafilatura) → convert (markdown) → save (raw/)**. The WARC file serves as ground truth; the markdown extraction is a derived view.

## ArchiveBox for Knowledge Bases

ArchiveBox is the most relevant tool for personal knowledge bases:
- Takes RSS feeds, bookmarks, and URL lists as input (matching KB discovery patterns)
- Creates WARC archives automatically
- Also saves SingleFile HTML, PDF, screenshots, and plain text
- Self-hosted, SQLite-based, Docker-ready
- Could be integrated alongside the raw/ directory as a preservation layer

## Common Crawl

Common Crawl provides petabytes of WARC-format web data, crawled monthly, freely available. This is the same data used to train most LLMs. For knowledge base research, it enables:
- Historical analysis of how web content has changed
- Large-scale structured data extraction (via Web Data Commons project)
- Building training datasets for content extraction models

## Sources

- [[sources/web-archiving-warc-tools]] — comprehensive tool and format overview

## Related Concepts

- [[concepts/content-extraction]] — extracting article text from archived pages
- [[concepts/plain-text-longevity]] — archiving as longevity strategy
- [[concepts/file-over-app]] — WARC files outlast any single replay tool
- [[concepts/document-processing-pipeline]] — archiving as pipeline step
