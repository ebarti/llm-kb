---
title: "Trafilatura: Python Web Text Extraction"
source: "https://github.com/adbar/trafilatura"
author: "Adrien Barbaresi"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [trafilatura, content-extraction, python, boilerplate-removal, web-scraping]
type: repo
status: raw
discovered_via: search
---

# Trafilatura: Python Web Text Extraction

Trafilatura is a Python package and command-line tool to gather text and metadata on the Web. Published as an ACL 2021 demo paper. Version 2.0.0.

## Core Features

### Web Discovery & Crawling
- Supports sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
- Smart URL management with filtering and deduplication

### Content Extraction
- Main text extraction using pattern matching and algorithms combining jusText and readability approaches
- Metadata capture: title, author, date, site name, categories, tags
- Structural formatting: paragraphs, lists, quotes, code blocks
- Optional: comments, links, images, tables

### Output Formats
- TXT, Markdown, CSV, JSON
- HTML, XML, XML-TEI (Text Encoding Initiative compatible)

### Processing Capabilities
- Handles live URLs and previously downloaded HTML files
- Parallel processing support
- Optional language detection
- Duplicate detection at sentence, paragraph, and document level using LRU cache

## Benchmarks & Recognition

- "Most efficient open-source library" — ScrapingHub article extraction benchmark
- "Best overall tool" — Lejeune & Barbaresi (2020)
- "Best single tool by ROUGE-LSum Mean F1 Page Scores" — Bevendorff et al. (2023)
- Balances precision (noise reduction) with recall (content inclusion)

## Real-World Adoption

Used by HuggingFace, IBM, Microsoft Research, Allen Institute, Stanford, and many academic institutions. Integrated into thousands of projects.

## Installation & Usage

```python
pip install trafilatura
from trafilatura import fetch_url, extract
downloaded = fetch_url('https://example.com')
result = extract(downloaded)  # Returns main text
result = extract(downloaded, output_format='markdown')
```

CLI: `trafilatura -u "https://example.com"`

## License

Apache 2.0 (versions before v1.8.0 used GPLv3+).

## Comparison

Trafilatura combines and improves on jusText (CZ Academy of Sciences boilerplate removal) and Mozilla Readability algorithms, achieving higher accuracy than either alone. It focuses specifically on web text extraction rather than general scraping.
