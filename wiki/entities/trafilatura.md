---
title: "Trafilatura"
type: entity
entity_type: tool
url: "https://github.com/adbar/trafilatura"
related: ["[[concepts/content-extraction]]", "[[concepts/boilerplate-removal]]", "[[entities/mozilla-readability]]"]
tags: [trafilatura, python, content-extraction, web-scraping]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The most accurate open-source web text extraction library — Python package combining jusText and Readability algorithms, outputting to markdown/JSON/XML-TEI, used by HuggingFace, IBM, Microsoft Research."
---

## Overview

Trafilatura is a Python package and command-line tool for web text extraction, published as an ACL 2021 demo paper. It consistently outperforms competing libraries in academic benchmarks.

## Key Facts

- **Type**: Python library + CLI
- **URL**: https://github.com/adbar/trafilatura
- **Author**: Adrien Barbaresi
- **License**: Apache 2.0 (v1.8.0+; earlier versions GPLv3+)
- **Version**: 2.0.0
- **Notable for**: Best accuracy among open-source extraction tools across multiple independent benchmarks

## Technical Approach

Combines two complementary algorithms:
- **jusText** (Czech Academy of Sciences): Block-level text classification for boilerplate removal using stop-word density
- **Readability**: DOM scoring for article container identification (inspired by [[entities/mozilla-readability]])

This hybrid achieves both high precision (rejecting noise) and high recall (capturing content).

## Capabilities

- Content extraction with metadata (title, author, date, categories, tags)
- Output formats: TXT, Markdown, CSV, JSON, HTML, XML, XML-TEI
- Built-in crawling: sitemap/feed parsing, URL deduplication
- Parallel processing support
- Language detection
- Duplicate detection at sentence/paragraph/document level (LRU cache)

## Benchmark Results

- "Most efficient open-source library" — ScrapingHub
- "Best overall tool" — Lejeune & Barbaresi (2020)
- "Best single tool by ROUGE-LSum Mean F1" — Bevendorff et al. (2023)

## Adoption

Used by HuggingFace, IBM, Microsoft Research, Allen Institute, Stanford, and thousands of other projects.

## Role in Knowledge Base

Trafilatura is the recommended first-choice extraction tool for the KB ingest pipeline when WebFetch is unavailable or when higher accuracy is needed. Its markdown output integrates directly into the raw/ layer.

## Mentions

- [[sources/trafilatura-web-extraction]] — detailed feature and benchmark analysis
- [[concepts/content-extraction]] — benchmark leader in Generation 2 tools
- [[concepts/boilerplate-removal]] — hybrid approach
