---
title: "Mozilla Readability Algorithm (Readability.js) Explained"
source: "https://webcrawlerapi.com/blog/mozilla-readability-algorithm-readabilityjs"
author: "WebcrawlerAPI"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [readability, content-extraction, mozilla, dom-analysis, boilerplate-removal]
type: article
status: raw
discovered_via: search
---

# Mozilla Readability Algorithm (Readability.js) Explained

Mozilla Readability is a standalone JavaScript library that extracts article content from web pages, removing navigation, ads, and sidebars. It powers Firefox's Reader View.

## Seven Key Heuristics

1. **Unlikely Candidates Removal** — Eliminates sidebars, ads, and widgets with obvious class/id names
2. **Class/ID Weighting** — Applies bonuses for positive names (article, content, body), penalties for negative indicators (sidebar, comment, footer)
3. **Link Density Analysis** — Identifies navigation blocks by measuring link saturation (navigation is mostly links)
4. **Text Quality Signals** — Scores based on length and punctuation patterns (commas indicate real sentences)
5. **Parent Score Propagation** — Pushes scores upward since articles live in container elements
6. **Sibling Merging** — Combines fragmented content across multiple DOM blocks
7. **Conditional Cleanup** — Removes forms, embeds, and suspicious lists when appropriate

## Pipeline Architecture

The `Readability.parse()` method executes six sequential stages:

1. **Preprocessing** — Removes obvious noise (scripts, styles) and normalizes DOM structure
2. **Metadata Extraction** — Captures title, byline, excerpt, site name, publish time
3. **Article Container Identification** — Core scoring via `_grabArticle()` method. Finds many small blocks (p, pre, td, headings, some divs) and assigns scores
4. **Content Cleaning** — Junk removal and simplification through `_prepArticle()`
5. **Post-Processing** — URL conversion (relative to absolute), wrapper elimination, attribute stripping
6. **Output Generation** — Returns article object with HTML, text, and metadata

## Scoring Mechanism

- Short text (<25 chars) is ignored
- Longer text receives bonuses capped at 3 points per 100 characters
- Commas are counted as sentence indicators
- Scores propagate upward through the DOM tree with diminishing intensity
- Parent containers accumulate points from multiple children
- Text blocks with real sentences get points; blocks with too many links lose points

## Output Structure

Returns: title, byline, excerpt, siteName, publishedTime, content (HTML), textContent (plain text), length, lang, dir

## Implementations

- **JavaScript (original)**: github.com/mozilla/readability
- **Python (ReadabiliPy)**: Python wrapper for Readability.js + pure Python fallback by Alan Turing Institute
- **Rust (readabilityrs)**: Passes 93.8% of Mozilla's test suite

## Common Failure Scenarios

- Insufficient text content
- Navigation blocks overwhelming real content
- Fragmented content across numerous small elements
- Malformed DOM structure
- Heavy page "chrome" exceeding article text volume
- Empty JavaScript application shells (SPAs)

## Significance

The Readability algorithm is the foundational content extraction approach used by Firefox Reader View, Jina Reader API, Pocket, and many other tools. Its heuristic approach — scoring DOM elements by text quality rather than using fixed selectors — makes it generalizable across millions of different website layouts.
