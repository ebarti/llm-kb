---
title: "Semantic Search"
type: concept
sources: ["[[sources/redis-semantic-vs-keyword-search]]", "[[sources/weaviate-hybrid-search-explained]]", "[[sources/superlinked-hybrid-search-reranking]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/vector-search]]", "[[concepts/keyword-search]]", "[[concepts/hybrid-search]]", "[[comparisons/semantic-vs-keyword-search]]"]
last_compiled: 2026-04-05
summary: "Search based on meaning rather than exact terms: transformer models encode text into dense vectors, enabling retrieval of conceptually related content even when queries and documents share no common words."
---

## Overview

Semantic search uses [[concepts/text-embeddings]] to find content based on meaning rather than exact word matches. A query like "how to prevent memory issues" will retrieve documents about "eviction policies," "maxmemory configuration," and "OOM prevention" — even though none of these share the query's exact terms.

This contrasts with [[concepts/keyword-search]], which relies on lexical matching through inverted indexes and algorithms like [[concepts/bm25]].

## How It Works

1. **Offline**: Encode all documents into dense vector embeddings using a transformer model (BERT, E5, etc.)
2. **At query time**: Encode the query into a vector using the same model
3. **Retrieve**: Find the k-nearest document vectors using [[concepts/vector-search]] (cosine similarity)
4. **Rank**: Return documents ordered by similarity score

## Strengths

- **Synonym handling**: "car repairs" matches "automotive maintenance"
- **Conceptual matching**: "database slowdowns" finds "performance optimization"
- **Natural language queries**: Users can express queries conversationally
- **Multilingual**: Some models capture meaning across languages without translation
- **Intent understanding**: Captures what users mean, not just what they type

## Weaknesses

- **Exact-match blind spots**: Cannot reliably match product codes ("SKU-2847-B"), error identifiers ("OOM-2024-047"), or string-literal patterns
- **Higher latency**: Especially on CPU; GPU acceleration substantially helps
- **Significant memory**: Dense embeddings require more storage than sparse inverted indexes
- **Non-deterministic**: Results can change with model updates or retraining (problematic for regulatory compliance)
- **Training data dependence**: Quality depends on the embedding model's training distribution

## Optimal Use Cases

- RAG implementations
- Question-answering systems
- Conversational AI and chatbots
- Multilingual applications
- Content-rich platforms where users express queries naturally
- E-commerce product discovery (beyond exact product codes)

## Why Hybrid Is Better

Semantic search's failure modes are complementary to those of keyword search. This is why production systems combine both approaches into [[concepts/hybrid-search]] — capturing the precision of exact-term matching alongside the recall of meaning-based retrieval. See [[comparisons/semantic-vs-keyword-search]] for a detailed tradeoff analysis.

## Sources

- [[sources/redis-semantic-vs-keyword-search]] — comprehensive comparison with failure mode analysis
- [[sources/weaviate-hybrid-search-explained]] — semantic component in hybrid architecture
- [[sources/superlinked-hybrid-search-reranking]] — semantic search in RAG pipelines

## Related Concepts

- [[concepts/text-embeddings]] — the representation that enables semantic search
- [[concepts/vector-search]] — the retrieval mechanism
- [[concepts/keyword-search]] — the complementary approach
- [[concepts/hybrid-search]] — combining both for production use
- [[comparisons/semantic-vs-keyword-search]] — detailed tradeoff comparison
