---
title: "HTML to Markdown Conversion"
type: concept
sources: ["[[sources/jina-reader-lm-html-to-markdown]]", "[[sources/crawl4ai-llm-web-crawler]]", "[[sources/trafilatura-web-extraction]]"]
related: ["[[concepts/content-extraction]]", "[[concepts/boilerplate-removal]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/markdown-for-ai-agents]]"]
tags: [html-to-markdown, content-conversion, markdown, llm-data]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Converting extracted HTML content to clean markdown — from rule-based libraries (Turndown, html2text, Pandoc) to neural models (Reader-LM v2, ROUGE-L 0.86) — the format bridge between web content and LLM-consumable knowledge."
---

## Overview

HTML-to-markdown conversion is the format translation step that bridges [[concepts/content-extraction]] (getting clean HTML) and [[concepts/markdown-as-universal-interface]] (the universal substrate for LLM knowledge bases). After boilerplate is removed and article content is identified, the remaining HTML must be converted to markdown to be useful for LLM ingestion, RAG pipelines, and wiki compilation.

This is not a trivial mapping. HTML encodes structure implicitly through nesting, CSS classes, and visual rendering. Markdown encodes structure explicitly through syntax (`#`, `*`, `[]()`, `>`). The conversion must preserve headings, lists, links, emphasis, code blocks, tables, and images while discarding irrelevant HTML attributes, classes, and inline styles.

## Approaches

### Rule-Based Libraries

**Turndown** (JavaScript): The most widely used HTML-to-markdown converter. Used in Jina Reader API pipeline. Processes DOM nodes and applies rules for each element type. Extensible via plugins.

**html2text** (Python): Converts HTML to plain text or markdown. Handles most common elements but struggles with complex tables and nested structures.

**Pandoc** ([[entities/pandoc]]): The universal document converter. Parses HTML into an internal AST and outputs markdown. Most complete but heaviest — designed for document conversion, not high-throughput web scraping.

**Kreuzberg html-to-markdown** (Rust + bindings): High-performance, CommonMark-compliant converter with native bindings for 12+ languages. Performance-oriented for production pipelines.

### Neural Models

**[[entities/reader-lm]]** (Jina AI): 1.5B parameter model treating HTML-to-markdown as a "selective-copy" task. Outperforms rule-based approaches on complex layouts, achieving ROUGE-L 0.86 (ReaderLM v2) compared to 0.69 for Gemini 2.0 Flash. Handles 512K token contexts, 29 languages, and can also extract structured JSON.

**LLM-based conversion**: Using GPT-4o, Claude, or other frontier models. More expensive but handles edge cases. Reader-LM-1.5B actually outperforms GPT-4o (ROUGE-L 0.72 vs 0.43) on this specialized task, demonstrating that specialized small models beat general large ones.

### Integrated Tools

**[[entities/crawl4ai]]**: Produces dual markdown output — raw (complete conversion) and fit (BM25-filtered for relevance). Handles the full pipeline from fetching through conversion.

**[[entities/firecrawl]]**: API service outputting clean markdown with navigation/scripts/boilerplate stripped. 25-75% more token-efficient than raw HTML.

**[[entities/trafilatura]]**: Outputs markdown as one of its formats (alongside TXT, JSON, XML-TEI).

## Quality Dimensions

| Dimension | What It Measures |
|-----------|-----------------|
| Header extraction | Correctly identifying and formatting h1-h6 |
| Main content | Preserving paragraphs, lists, and body text |
| Rich structure | Tables, code blocks, nested lists |
| Links & images | Preserving href/src with correct markdown syntax |
| Markdown syntax | Bold, italic, code, blockquotes |
| Semantic fidelity | Does the markdown convey the same meaning as the HTML? |

## Token Efficiency

Markdown is 25-75% more token-efficient than HTML for LLM consumption (see [[concepts/markdown-for-ai-agents]]). This directly impacts:
- **Cost**: fewer tokens = lower API costs for LLM processing
- **Context window utilization**: more content fits per inference call
- **Retrieval accuracy**: 89% vs 62% RAG retrieval accuracy for markdown vs HTML

## The Conversion Pipeline

For knowledge base ingestion, the complete pipeline is:

```
URL → Fetch (requests/Playwright) → Extract (Readability/Trafilatura) → Convert (Turndown/Reader-LM) → Clean (normalize whitespace, fix links) → Save (raw/*.md)
```

Tools like Crawl4AI, Firecrawl, and Jina Reader API collapse these steps into a single call.

## Sources

- [[sources/jina-reader-lm-html-to-markdown]] — neural approach, benchmark data
- [[sources/crawl4ai-llm-web-crawler]] — dual markdown output with BM25 filtering
- [[sources/trafilatura-web-extraction]] — extraction with markdown output

## Related Concepts

- [[concepts/content-extraction]] — the upstream step (getting clean HTML)
- [[concepts/boilerplate-removal]] — removing noise before conversion
- [[concepts/markdown-as-universal-interface]] — why markdown is the target
- [[concepts/markdown-for-ai-agents]] — why LLMs prefer markdown
