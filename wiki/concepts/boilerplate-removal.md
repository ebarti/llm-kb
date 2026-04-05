---
title: "Boilerplate Removal"
type: concept
sources: ["[[sources/mozilla-readability-algorithm]]", "[[sources/trafilatura-web-extraction]]", "[[sources/jina-reader-lm-html-to-markdown]]"]
related: ["[[concepts/content-extraction]]", "[[concepts/html-to-markdown-conversion]]", "[[concepts/data-quality-bottleneck]]"]
tags: [boilerplate-removal, content-extraction, web-scraping]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The sub-problem of content extraction focused on removing navigation, ads, footers, sidebars, and other non-content elements from web pages — solved via DOM scoring (Readability), block classification (jusText), or neural filtering (Reader-LM)."
---

## Overview

Boilerplate removal is the noise-filtering component of [[concepts/content-extraction]]. A typical web page is 60-80% boilerplate: navigation bars, sidebars, ads, footers, cookie banners, related article links, social sharing widgets, comment sections, and repetitive structural markup. Only 20-40% is the actual article content a knowledge base needs.

Failing to remove boilerplate is a form of [[concepts/data-quality-bottleneck]] — if navigation menus and ad text leak into raw/ files, they propagate into summaries, concept articles, and search indexes, reducing quality across the entire wiki.

## Approaches

### DOM Scoring (Readability Family)
[[entities/mozilla-readability]] scores DOM elements based on text quality signals: length, punctuation density (commas indicate sentences), link density (high link density = navigation). Scores propagate upward through the tree, and the highest-scoring container is selected as the article.

**Heuristics used**: unlikely candidate removal (class/ID names like "sidebar", "ad", "nav"), link density thresholds, text length minimums (25 chars), parent score propagation with diminishing returns.

### Block Classification (jusText Family)
jusText classifies each text block as "good" (content), "near-good" (probably content), "bad" (boilerplate), or "short" (ambiguous). Uses stop-word density and surrounding block context. Originally developed at the Czech Academy of Sciences.

[[entities/trafilatura]] combines both approaches for best results.

### Neural Filtering
[[entities/reader-lm]] and [[entities/crawl4ai]] use learned models to identify and skip boilerplate. Reader-LM treats it as a selective-copy task (copy content, skip noise). Crawl4AI applies BM25 relevance filtering to remove content that doesn't match the target query.

## Common Boilerplate Types

| Type | Detection Method | Difficulty |
|------|-----------------|------------|
| Navigation menus | High link density | Easy |
| Sidebars | Class/ID names, position | Easy |
| Cookie banners | Class names, fixed position | Easy |
| Ads | Class names, iframe detection | Medium |
| Related articles | Link density, "related" keywords | Medium |
| Comments sections | Class names, form elements | Medium |
| Social widgets | iframe, known domains | Medium |
| Inline promotions | Context-dependent | Hard |
| Author bios | Variable position and format | Hard |
| Pagination controls | Numbered links, "next/prev" | Hard |

## Impact on Knowledge Base Quality

Every boilerplate element that survives extraction becomes noise in the knowledge base:
- Navigation text pollutes [[concepts/information-extraction]] results
- Ad copy introduces irrelevant entities and claims
- Comment text introduces unvetted opinions
- Cookie notices add legal boilerplate to every source summary

## Sources

- [[sources/mozilla-readability-algorithm]] — DOM scoring approach
- [[sources/trafilatura-web-extraction]] — hybrid block classification + DOM scoring
- [[sources/jina-reader-lm-html-to-markdown]] — neural selective-copy approach

## Related Concepts

- [[concepts/content-extraction]] — the parent discipline
- [[concepts/data-quality-bottleneck]] — boilerplate as a quality contaminant
- [[concepts/html-to-markdown-conversion]] — the step after boilerplate removal
