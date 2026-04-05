---
title: "Source: Schema.org Structured Data"
type: source-summary
source: "[[raw/schema-org-structured-data]]"
related: ["[[concepts/structured-data-extraction]]", "[[concepts/content-extraction]]"]
tags: [schema-org, structured-data, json-ld, semantic-web]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Schema.org provides structured data vocabularies used by 45M+ domains — JSON-LD, Microdata, and RDFa formats that enable high-confidence automated content extraction without heuristics."
---

## Key Points

- 45 million web domains use Schema.org markup, with 450+ billion marked-up objects
- Three formats: JSON-LD (Google-recommended), Microdata (HTML5 attributes), RDFa (W3C standard)
- Pre-structured data: the website author has already identified entities, types, and relationships
- Common types: Article, Person, Organization, Product, Event, Review, Recipe, HowTo
- For content extraction, Schema.org markup should be the first thing checked — it provides high-confidence data requiring minimal processing
- Extraction tools: extruct (Python), Cheerio (JS), Web Data Commons (large-scale), Apify

## Detailed Summary

Schema.org structured data represents a fundamentally different approach to content extraction compared to heuristic methods like [[entities/mozilla-readability]] or [[entities/trafilatura]]. Instead of analyzing DOM structure to guess what's content vs. boilerplate, Schema.org markup provides **explicit, author-declared** structured data.

The scale is massive: 45 million domains and 450 billion objects mean that a significant fraction of web pages encountered during knowledge base construction will have some Schema.org markup. JSON-LD (embedded in `<script>` tags) is the most common format and is separate from the HTML content, making it trivial to extract.

For knowledge base [[concepts/document-processing-pipeline]] design, the optimal strategy is a two-pass approach: (1) extract Schema.org data for high-confidence entities and metadata, (2) fall back to heuristic content extraction (Readability/Trafilatura) for article text.

## Concepts Introduced or Discussed

- [[concepts/structured-data-extraction]] — Schema.org as structured data source
- [[concepts/content-extraction]] — Schema.org as complement to heuristic extraction

## Metadata

- **Author**: Schema.org
- **Date Published**: 2024
- **Format**: documentation
- **URL**: https://schema.org/docs/gs.html
