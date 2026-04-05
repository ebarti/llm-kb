---
title: "Structured Data Extraction (Schema.org)"
type: concept
sources: ["[[sources/schema-org-structured-data]]"]
related: ["[[concepts/content-extraction]]", "[[concepts/information-extraction]]", "[[concepts/structured-output-extraction]]"]
tags: [schema-org, structured-data, json-ld, semantic-web, extraction]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Extracting pre-structured data (JSON-LD, Microdata, RDFa) from web pages using Schema.org vocabularies — 45M+ domains provide machine-readable entities and metadata that bypass heuristic extraction entirely."
---

## Overview

While [[concepts/content-extraction]] typically involves heuristic or neural analysis to identify article content in messy HTML, structured data extraction takes a fundamentally different approach: it reads the **explicitly marked-up, machine-readable data** that website authors have already embedded using Schema.org vocabularies.

Over 45 million web domains use Schema.org markup, with 450+ billion marked-up objects. This means a significant fraction of web pages already contain high-confidence structured data that can be extracted without any heuristic guessing.

## How It Works

### JSON-LD (Preferred)
The most common format. Embedded in `<script type="application/ld+json">` tags, completely separate from HTML content. Easy to extract: parse the script tag, decode JSON, walk the schema.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Web Scraping Best Practices",
  "author": {"@type": "Person", "name": "Jane Doe"},
  "datePublished": "2025-12-01",
  "publisher": {"@type": "Organization", "name": "ScraperAPI"}
}
```

### Microdata
HTML5 attributes embedded directly in markup: `itemscope`, `itemtype`, `itemprop`. Requires DOM parsing to extract.

### RDFa
W3C standard attributes (about, typeof, property). More expressive than Microdata but less common.

## Why It Matters for Knowledge Bases

Schema.org data is a goldmine for the ingest pipeline because:

1. **Pre-structured**: The website author has already identified entities, types, and relationships
2. **High confidence**: No heuristic errors — the data is explicitly declared
3. **Standardized**: Consistent vocabulary across 45M domains
4. **Rich metadata**: Author, date, publisher, categories — exactly what raw/ frontmatter needs
5. **Entity-oriented**: Maps directly to [[concepts/named-entity-recognition]] and [[concepts/entity-linking]] tasks

## Extraction Priority

For a [[concepts/document-processing-pipeline]], the optimal strategy:

1. **First**: Extract Schema.org / JSON-LD for metadata and entities
2. **Second**: Extract RSS/Atom feed content if available
3. **Third**: Apply heuristic extraction ([[entities/trafilatura]], [[entities/mozilla-readability]])
4. **Fourth**: Fall back to neural extraction ([[entities/reader-lm]])

The Schema.org data populates raw/ frontmatter (title, author, date, tags), while heuristic/neural extraction captures the article body text.

## Tools

- **extruct** (Python): Extracts JSON-LD, Microdata, RDFa, OpenGraph, Dublin Core
- **Cheerio** (JavaScript): Parse JSON-LD from script tags
- **Web Data Commons**: Large-scale extraction from Common Crawl
- **Any JSON parser**: JSON-LD is just JSON in a script tag

## Sources

- [[sources/schema-org-structured-data]] — Schema.org overview and implementation

## Related Concepts

- [[concepts/content-extraction]] — heuristic/neural complement to structured extraction
- [[concepts/information-extraction]] — extracting entities from unstructured text
- [[concepts/structured-output-extraction]] — forcing LLM outputs into structured formats
