---
title: "Content Extraction"
type: concept
sources: ["[[sources/mozilla-readability-algorithm]]", "[[sources/trafilatura-web-extraction]]", "[[sources/jina-reader-lm-html-to-markdown]]", "[[sources/crawl4ai-llm-web-crawler]]", "[[sources/schema-org-structured-data]]"]
related: ["[[concepts/boilerplate-removal]]", "[[concepts/html-to-markdown-conversion]]", "[[concepts/web-scraping-at-scale]]", "[[concepts/structured-data-extraction]]", "[[concepts/document-processing-pipeline]]", "[[concepts/markdown-as-universal-interface]]"]
tags: [content-extraction, web-scraping, ingest-pipeline]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The discipline of extracting meaningful content from messy web pages — from DOM-scoring heuristics (Readability) through hybrid algorithms (Trafilatura) to neural models (Reader-LM) — the critical first step in any knowledge base ingest pipeline."
---

## Overview

Content extraction is the process of separating meaningful article content from the surrounding noise on a web page — navigation, ads, sidebars, footers, cookie banners, social widgets, and boilerplate. It is the critical bottleneck in any [[concepts/document-processing-pipeline]] that ingests web content into a knowledge base.

The quality of content extraction directly determines the quality of everything downstream: if boilerplate leaks through, it contaminates summaries, concept articles, and search results. If real content is dropped, the knowledge base has gaps. The field has evolved through three generations of approaches, each trading off generality, accuracy, and computational cost.

## Three Generations of Content Extraction

### Generation 1: Rule-Based (2000s)
Manual CSS selectors or XPath expressions targeting specific page elements. Works perfectly for known sites but requires per-site rules. Used in early web scrapers and RSS readers.

**Tools**: BeautifulSoup + custom selectors, XPath extractors
**Strength**: Perfect precision on known sites
**Weakness**: Zero generalizability — breaks when sites change

### Generation 2: Heuristic/Statistical (2010s)
DOM-scoring algorithms that analyze text density, link density, class/ID names, and structural patterns to identify article containers. Generalizable across millions of sites without per-site rules.

**Tools**: [[entities/mozilla-readability]] (7 heuristics, 6-stage pipeline), [[entities/trafilatura]] (hybrid jusText + Readability), jusText, Goose, newspaper3k
**Strength**: Works on most websites without configuration
**Weakness**: Fails on SPAs, heavy navigation, fragmented layouts

### Generation 3: Neural (2024+)
Specialized language models trained on HTML-to-markdown conversion as a "selective-copy" task. The model learns to skip markup and boilerplate, retaining only meaningful content.

**Tools**: [[entities/reader-lm]] (1.5B params, ROUGE-L 0.86), Crawl4AI with LLM extraction
**Strength**: Handles complex, multilingual, and unusual layouts
**Weakness**: Higher computational cost, requires GPU for real-time processing

## The Extraction Stack for Knowledge Bases

The optimal approach combines all three generations in a priority cascade:

1. **Check for Schema.org / JSON-LD** — pre-structured, high-confidence data (see [[concepts/structured-data-extraction]])
2. **Check for RSS/Atom feeds** — clean content in standardized format
3. **Apply heuristic extraction** — [[entities/trafilatura]] for best accuracy, [[entities/mozilla-readability]] for speed
4. **Fall back to neural extraction** — [[entities/reader-lm]] or LLM-based extraction for difficult pages
5. **Last resort: headless browser + DOM analysis** — [[entities/playwright]] for JS-heavy SPAs

## Key Metrics

Content extraction quality is measured by:
- **Precision**: fraction of extracted content that is actually article content (not boilerplate)
- **Recall**: fraction of article content that was successfully extracted
- **ROUGE-L**: n-gram overlap between extracted text and ground truth
- **Token Error Rate (TER)**: measures hallucinated content not in the original

## Why It Matters for This Wiki

This knowledge base's entire raw/ layer depends on content extraction. Every `WebFetch` call, every `./tools/ingest/*.sh` script, and every URL processed during RESEARCH operations goes through content extraction. The quality of extraction determines whether the wiki is built on clean signal or contaminated with navigation menus and cookie notices.

## Sources

- [[sources/mozilla-readability-algorithm]] — foundational heuristic algorithm
- [[sources/trafilatura-web-extraction]] — best-in-class hybrid extraction
- [[sources/jina-reader-lm-html-to-markdown]] — neural approach outperforming heuristics
- [[sources/crawl4ai-llm-web-crawler]] — BM25-filtered extraction for relevance
- [[sources/schema-org-structured-data]] — pre-structured extraction source

## Related Concepts

- [[concepts/boilerplate-removal]] — the noise-filtering sub-problem
- [[concepts/html-to-markdown-conversion]] — the format conversion step after extraction
- [[concepts/web-scraping-at-scale]] — content extraction at production scale
- [[concepts/markdown-as-universal-interface]] — why markdown is the extraction target format
