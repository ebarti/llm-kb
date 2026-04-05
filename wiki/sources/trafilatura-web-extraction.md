---
title: "Source: Trafilatura — Python Web Text Extraction"
type: source-summary
source: "[[raw/trafilatura-web-extraction]]"
related: ["[[concepts/content-extraction]]", "[[concepts/boilerplate-removal]]", "[[entities/trafilatura]]"]
tags: [trafilatura, content-extraction, python, benchmarks]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Trafilatura: the most accurate open-source web text extraction library — combines jusText and Readability algorithms, outputs to markdown/JSON/XML-TEI, used by HuggingFace, IBM, Microsoft Research."
---

## Key Points

- Combines jusText and Readability approaches for best-in-class extraction accuracy
- Outperforms competitors across multiple benchmarks (ScrapingHub, Lejeune & Barbaresi 2020, Bevendorff 2023)
- Outputs to TXT, Markdown, CSV, JSON, HTML, XML, XML-TEI formats
- Built-in crawling (sitemaps, feeds), deduplication (sentence/paragraph/document level), and language detection
- Used by HuggingFace, IBM, Microsoft Research, Allen Institute, Stanford
- Apache 2.0 license, published as ACL 2021 demo paper

## Detailed Summary

Trafilatura occupies the sweet spot in the content extraction landscape: it's more accurate than [[entities/mozilla-readability]] alone, more focused than general-purpose scrapers like Scrapy, and lighter-weight than LLM-based approaches like [[entities/jina-reader]].

Its key innovation is combining two complementary extraction algorithms: jusText (from the Czech Academy of Sciences, focused on boilerplate removal via block-level classification) and Mozilla Readability (focused on article identification via DOM scoring). This hybrid approach achieves both high precision (rejecting noise) and high recall (capturing content).

For [[concepts/document-processing-pipeline]] workflows in knowledge bases, Trafilatura is the ideal first-pass extraction tool: feed it a URL, get clean text with metadata (title, author, date, site name, categories, tags). Its markdown output format integrates directly into markdown-based KB pipelines.

The built-in crawling capabilities (sitemap parsing, feed discovery, URL deduplication) also make it useful as a lightweight discovery engine — finding URLs to scrape before extracting their content.

## Concepts Introduced or Discussed

- [[concepts/content-extraction]] — Trafilatura's core capability
- [[concepts/boilerplate-removal]] — hybrid jusText + Readability approach
- [[concepts/html-to-markdown-conversion]] — one of Trafilatura's output formats

## Quotes & Evidence

> "Most efficient open-source library" — ScrapingHub benchmark
> "Best single tool by ROUGE-LSum Mean F1 Page Scores" — Bevendorff et al. 2023

## Metadata

- **Author**: Adrien Barbaresi
- **Date Published**: 2024 (v2.0.0)
- **Format**: repository / documentation
- **URL**: https://github.com/adbar/trafilatura
