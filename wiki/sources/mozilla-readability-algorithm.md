---
title: "Source: Mozilla Readability Algorithm Explained"
type: source-summary
source: "[[raw/mozilla-readability-algorithm]]"
related: ["[[concepts/content-extraction]]", "[[concepts/boilerplate-removal]]", "[[entities/mozilla-readability]]"]
tags: [readability, content-extraction, dom-analysis, boilerplate-removal]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Deep technical explanation of Mozilla's Readability.js — the 7-heuristic, 6-stage pipeline that powers Firefox Reader View and underpins most modern content extraction tools."
---

## Key Points

- Readability.js uses 7 heuristics to score and identify article content in arbitrary web pages
- The algorithm operates as a 6-stage pipeline: preprocess → metadata → score → clean → post-process → output
- Scoring is based on text quality signals: length, punctuation (commas indicate sentences), link density
- Scores propagate upward through the DOM with diminishing intensity, letting parent containers accumulate child scores
- "Unlikely candidates" removal (elements with sidebar/ad/nav class names) is what makes the algorithm work on most pages
- The algorithm fails on SPAs, extremely fragmented content, and pages where navigation outweighs article text

## Detailed Summary

Mozilla's Readability.js is the foundational content extraction algorithm used across the web content extraction ecosystem. It powers Firefox Reader View and serves as a core dependency in [[entities/jina-reader]], [[entities/trafilatura]] (partially), and many other tools.

The algorithm's genius is its heuristic generality: rather than using page-specific CSS selectors (which would break across millions of sites), it scores DOM elements based on universal signals. Text blocks with real sentences (detected by commas and length) get points; blocks dominated by links (navigation) lose points. Scores propagate upward so that the article's wrapper `div` accumulates the highest score.

The 7 heuristics work in concert: unlikely candidate removal handles obvious noise (sidebars, ads via class/ID names), link density analysis catches navigation sections, text quality signals find the real content, parent score propagation identifies the container, and sibling merging handles fragmented layouts.

Available in JavaScript (original), Python (ReadabiliPy by Alan Turing Institute), and Rust (readabilityrs, 93.8% test suite pass rate).

## Concepts Introduced or Discussed

- [[concepts/content-extraction]] — the core problem Readability solves
- [[concepts/boilerplate-removal]] — Readability's primary function
- [[concepts/html-to-markdown-conversion]] — downstream step after extraction

## Quotes & Evidence

> "Text blocks with real sentences get points, blocks with too many links lose points, and scores are pushed to parent containers."
> "Unlikely candidates removal is what makes the algorithm work most of the time."

## Metadata

- **Author**: WebcrawlerAPI
- **Date Published**: 2025
- **Format**: article
- **URL**: https://webcrawlerapi.com/blog/mozilla-readability-algorithm-readabilityjs
