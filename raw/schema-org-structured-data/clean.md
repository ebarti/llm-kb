---
title: "Schema.org Structured Data: Getting Started"
source: "https://schema.org/docs/gs.html"
author: "Schema.org"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [schema-org, structured-data, json-ld, microdata, rdfa, semantic-web]
type: article
status: raw
discovered_via: search
---

# Schema.org Structured Data

Schema.org provides shared vocabularies for structured data markup on web pages. Over 45 million web domains use Schema.org markup with 450+ billion objects. Supported by Google, Microsoft, Yandex, and Yahoo.

## Three Formats

1. **JSON-LD** (JavaScript Object Notation for Linked Data) — Google-recommended since 2015. Embedded in `<script>` tags, separate from HTML content.
2. **Microdata** — HTML5-based attributes embedded directly in markup: `itemscope`, `itemtype`, `itemprop`
3. **RDFa** (Resource Description Framework in Attributes) — W3C standard, similar to microdata but more expressive

## Why It Matters for Content Extraction

Schema.org markup is a goldmine for automated content extraction because:
- It's **explicitly structured** — the website author has already identified entities, relationships, and types
- It's **machine-readable by design** — no heuristic guessing needed
- It's **standardized** — consistent vocabulary across 45M domains
- Common types: Article, Person, Organization, Product, Event, Review, Recipe, HowTo

## Key Concepts

### Items
Every item has:
- Optional ID
- Array of types (from schema.org vocabulary)
- Properties with URLs as keys and arrays of values

### Nesting
Properties can contain embedded items with their own types and properties. E.g., a Movie item can have a director property containing a Person item.

### Common Types
- **Creative works**: Book, Movie, MusicRecording, Recipe, TVSeries
- **Media**: AudioObject, ImageObject, VideoObject
- **Entities**: Event, Organization, Person, Place, LocalBusiness
- **Commerce**: Product, Offer, Review, AggregateRating

## Extraction Tools

- **extruct** (Python): Extracts JSON-LD, Microdata, RDFa, OpenGraph from HTML
- **Cheerio** (JS): Parse JSON-LD from script tags
- **Web Data Commons**: Large-scale extraction from Common Crawl
- **Apify Structured Data Extractor**: Cloud service for schema.org extraction

## For Knowledge Base Construction

When scraping a web page, checking for Schema.org markup should be the first extraction step — it provides pre-structured, high-confidence data that can be directly ingested into knowledge graphs or wiki articles with minimal processing.
