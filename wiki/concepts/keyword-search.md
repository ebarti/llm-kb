---
title: "Keyword Search"
type: concept
sources: ["[[sources/redis-semantic-vs-keyword-search]]", "[[sources/weaviate-hybrid-search-explained]]"]
related: ["[[concepts/bm25]]", "[[concepts/semantic-search]]", "[[concepts/hybrid-search]]", "[[comparisons/semantic-vs-keyword-search]]"]
last_compiled: 2026-04-05
summary: "Lexical search using inverted indexes and BM25 ranking: fast, deterministic, and precise for exact terms, but blind to synonyms and conceptual relationships."
---

## Overview

Keyword search (also called lexical search) finds documents by matching exact terms between queries and documents. It uses **inverted indexes** — data structures mapping terms to the documents that contain them — combined with ranking algorithms like [[concepts/bm25]] to score relevance.

## Processing Pipeline

1. **Tokenization**: Break text into individual words
2. **Lowercasing**: Normalize case for consistent matching
3. **Stop word removal**: Filter common words ("the", "is", "and")
4. **Stemming**: Reduce words to root forms ("running" → "run", "ran" → "run")
5. **Indexing**: Build inverted index mapping stemmed terms to document IDs with positions

## Strengths

- **Exact-match precision**: Reliably finds product codes, SKUs, error identifiers, legal citations
- **Determinism**: Identical queries always produce identical results (critical for compliance and debugging)
- **Speed**: Fast for large collections using efficient inverted index structures
- **Low memory**: Sparse representations require minimal storage compared to dense vectors
- **Boolean operations**: Supports complex AND/OR/NOT queries with field filtering and phrase matching
- **Interpretability**: Users can see exactly which terms matched

## Weaknesses

- **Synonym blindness**: "car repairs" will not match "automotive maintenance"
- **Concept gap**: "database slowdowns" misses "performance optimization"
- **Vocabulary mismatch**: Users must guess the exact terminology used in documents
- **No intent understanding**: Cannot distinguish between different meanings of the same word

## Optimal Use Cases

- Highly specialized content where users know exact terms
- Product catalogs, SKU lookups, technical code repositories
- Regulatory/compliance scenarios requiring deterministic results
- Small to medium datasets where infrastructure simplicity matters
- Boolean search with complex field filtering

## Sources

- [[sources/redis-semantic-vs-keyword-search]] — comprehensive comparison and failure mode analysis
- [[sources/weaviate-hybrid-search-explained]] — BM25 component of hybrid search

## Related Concepts

- [[concepts/bm25]] — the standard ranking algorithm for keyword search
- [[concepts/semantic-search]] — the meaning-based alternative
- [[concepts/hybrid-search]] — combining keyword and semantic approaches
- [[comparisons/semantic-vs-keyword-search]] — detailed tradeoff comparison
