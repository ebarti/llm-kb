---
title: "Semantic Search vs. Keyword Search: When to Use Each"
source: "https://redis.io/blog/semantic-search-vs-keyword-search/"
author: "Redis"
date_published: 2024-09-15
date_ingested: 2026-04-05
tags: [semantic-search, keyword-search, BM25, embeddings, hybrid-search, comparison]
type: article
status: raw
discovered_via: search
---

# Semantic Search vs. Keyword Search — Redis

## How Each Works

### Semantic Search
- Uses transformer models (BERT) to convert text into dense vector embeddings
- Cosine similarity scoring (-1 to 1)
- Ranks by semantic proximity in embedding space

### Keyword Search
- Inverted index structures mapping terms to documents
- BM25 probabilistic ranking
- Pipeline: tokenization, lowercasing, stop word removal, stemming

## BM25 Parameters

- k1: Controls term frequency saturation
- b: Handles length normalization

## Comparative Analysis

| Aspect | Keyword | Semantic |
|--------|---------|----------|
| Matching | Lexical (exact) | Dense vectors |
| Memory | Minimal (sparse) | Significant |
| Latency | Fast | Higher (esp. CPU) |
| GPU | N/A | Substantially faster |
| Failure Mode | Misses synonyms | Misses exact codes |
| Ranking | BM25 (deterministic) | Neural (varies) |

## Failure Modes

Semantic fails: error codes ("OOM-2024-047"), product IDs ("SKU-2847-B").
Keyword fails: "database slowdowns" won't match "performance optimization"; "car repairs" misses "automotive maintenance".

## When to Use Semantic

- RAG implementations
- Question-answering systems
- Multilingual applications
- Conversational AI

## When to Use Keyword

- Exact term matching (product codes, SKUs, legal codes)
- Boolean operations (AND/OR/NOT)
- Deterministic results (regulatory compliance)
- Small/medium datasets

## Hybrid Architecture

Parallel indexes: HNSW vector index + BM25 inverted index. Same document collection, no duplication. Merge via RRF. Redis supports both HNSW and FLAT indexes natively.
