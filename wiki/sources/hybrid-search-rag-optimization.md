---
title: "Source: Optimizing RAG with Hybrid Search & Reranking"
type: source-summary
source: "[[raw/hybrid-search-rag-optimization]]"
related: ["[[concepts/hybrid-search]]", "[[concepts/bm25]]", "[[concepts/reranking]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "VectorHub guide to hybrid search: combining BM25 keyword matching with vector semantic search via RRF fusion, plus transformer-based reranking — with practical database implementation notes."
reading_time: "1 min"
---

## Key Points

- Vector search excels at semantic meaning but struggles with exact keywords, abbreviations, proper names
- BM25 captures exact terms but misses semantic relationships
- Weighted balancing formula: H=(1-α)K+αV adjusts the blend
- Reciprocal Rank Fusion (RRF) combines by position, ignoring raw scores
- Transformer-based reranking reorders retrieved results by relevance confidence
- Native hybrid support: Weaviate, Pinecone, Elasticsearch; manual for ChromaDB
- Testing on National Security Strategy: hybrid outperformed pure semantic for geographic references and proper nouns

## Detailed Summary

This practical guide demonstrates why neither [[concepts/bm25]] nor vector search alone suffices for production [[concepts/retrieval-augmented-generation]]. The article provides concrete examples: vector search finds semantically similar content but misses exact product SKUs or legal clause numbers; keyword search finds exact matches but can't connect "automobile maintenance" with "car repair."

The recommended approach combines both via [[concepts/hybrid-search]], with two main fusion strategies: weighted balancing (simple but requires tuning α) and RRF (parameter-free rank fusion). Post-retrieval [[concepts/reranking]] with transformer models further improves precision.

## Related Concepts

- [[concepts/hybrid-search]] — the core technique
- [[concepts/bm25]] — keyword retrieval component
- [[concepts/reranking]] — post-retrieval quality improvement
- [[concepts/vector-databases]] — infrastructure for vector search
