---
title: "Mozilla Readability (Readability.js)"
type: entity
entity_type: tool
url: "https://github.com/mozilla/readability"
related: ["[[concepts/content-extraction]]", "[[concepts/boilerplate-removal]]", "[[entities/jina-reader]]", "[[entities/trafilatura]]"]
tags: [readability, content-extraction, mozilla, javascript]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Mozilla's standalone JavaScript library for extracting article content from web pages via a 7-heuristic, 6-stage DOM scoring pipeline — powers Firefox Reader View and underpins Jina Reader API."
---

## Overview

Mozilla Readability (Readability.js) is the foundational content extraction algorithm used across the web. It powers Firefox's Reader View feature and serves as a core dependency in the Jina Reader API, Pocket, and dozens of other content extraction tools.

## Key Facts

- **Type**: JavaScript library (standalone)
- **URL**: https://github.com/mozilla/readability
- **License**: Apache 2.0
- **Notable for**: Establishing the heuristic DOM-scoring approach to content extraction that most modern tools build upon

## How It Works

Seven heuristics in a 6-stage pipeline:
1. Preprocess (remove scripts/styles)
2. Extract metadata (title, byline, date)
3. Score DOM elements (text quality, link density, class/ID names)
4. Clean the winning container
5. Post-process (fix URLs, strip attributes)
6. Output article object

Scoring: text length → points, commas → points, high link density → penalty, scores propagate upward to parent containers.

## Implementations

- **JavaScript** (original): mozilla/readability
- **Python**: ReadabiliPy (Alan Turing Institute) — wrapper + pure Python fallback
- **Rust**: readabilityrs — 93.8% test suite pass rate

## Role in Knowledge Base

Readability.js is the algorithm used (directly or indirectly) by most content extraction tools in the knowledge base's ingest pipeline. When the wiki's WebFetch or Jina Reader API extracts article content from a URL, Readability.js or a derivative is likely running underneath.

## Mentions

- [[sources/mozilla-readability-algorithm]] — detailed algorithm explanation
- [[sources/jina-reader-lm-html-to-markdown]] — used in original Jina Reader pipeline
- [[concepts/content-extraction]] — foundational Generation 2 tool
- [[concepts/boilerplate-removal]] — core DOM scoring approach
