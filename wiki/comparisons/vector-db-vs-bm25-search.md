---
title: "Vector Database vs. BM25 Keyword Search"
type: comparison
subjects: ["[[concepts/vector-databases]]", "[[concepts/rag-vs-index-based-retrieval]]"]
sources: ["[[sources/hn-vector-database-debate]]", "[[sources/graphiti-temporal-knowledge-graphs]]"]
last_compiled: 2026-04-06
summary: "Comparing dense vector semantic search with sparse keyword-based BM25 retrieval -- and why hybrid approaches combining both outperform either alone."
---

## Overview

The choice between vector-based semantic search and keyword-based BM25 retrieval is a core infrastructure decision for knowledge base Q&A systems that have outgrown simple index-based navigation. Vector databases excel at finding semantically similar content even when exact keywords differ, while BM25 excels at precise keyword matching and handling technical terminology. Modern best practice, exemplified by [[entities/graphiti]]'s hybrid retrieval and [[entities/vespa]]'s integrated engine, increasingly favors combining both methods.

This comparison matters for LLM knowledge bases that grow beyond the ~400K word threshold where Karpathy's index-based approach suffices. At that scale, the system needs a retrieval backend, and the choice between vector search, keyword search, or a hybrid of both has significant implications for answer quality.

## Comparison Table

| Dimension | Vector Database (Dense Retrieval) | BM25 Keyword Search (Sparse Retrieval) |
|-----------|----------------------------------|--------------------------------------|
| Core approach | Embed text into dense vectors, find nearest neighbors by cosine similarity | Score documents by term frequency and inverse document frequency |
| Semantic understanding | High (finds conceptually related content) | None (requires exact keyword overlap) |
| Technical terminology | Poor (rare terms get weak embeddings) | Excellent (exact match on domain-specific terms) |
| Synonyms/paraphrases | Handles well | Misses entirely |
| Computational cost | High (embedding generation + ANN search) | Low (inverted index lookup) |
| Infrastructure | Vector DB or embedding library required | Standard text search (Elasticsearch, Postgres full-text) |
| Accuracy at scale | Approximate (ANN algorithms) | Exact (returns all matching documents) |
| Multi-language | Possible with multilingual embeddings | Language-specific stemming/tokenization |
| Best for | Exploratory queries, conceptual similarity | Known-item search, technical terms, exact phrases |

## Detailed Analysis

**The vocabulary mismatch problem**: Vector search solves the fundamental limitation of keyword search: vocabulary mismatch. A user asking about "knowledge management" should retrieve articles about "PKM" and "second brain" even though the keywords differ. Vector embeddings capture this semantic relationship; BM25 does not.

**The specificity problem**: Conversely, vector search struggles with highly specific technical terms. A query about "pgvector HNSW" should prioritize documents containing those exact terms, but dense embeddings may dilute these specific signals among semantically similar but irrelevant content. BM25 handles this perfectly.

**The hybrid advantage**: [[entities/graphiti]] combines semantic search, BM25, and graph traversal in its retrieval pipeline. The [[sources/hn-vector-database-debate]] discussion and [[entities/vespa]]'s architecture both point to the same conclusion: the best retrieval combines multiple signals. A typical hybrid approach uses BM25 to find exact matches and vector search to find semantically related content, then fuses the results using reciprocal rank fusion or learned re-ranking.

**Relevance to LLM-KB**: For a markdown wiki that has outgrown index-based navigation, the practical recommendation is: start with BM25 (easier to implement, no embedding infrastructure), add vector search when vocabulary mismatch becomes a problem, and eventually implement hybrid retrieval if retrieval quality is critical. Most personal-scale knowledge bases will never need to go beyond BM25; most team-scale bases benefit from hybrid.

## When to Use Each

**Use BM25 keyword search when:**
- Your knowledge base uses consistent terminology
- Queries involve specific technical terms, names, or identifiers
- You want minimal infrastructure (Elasticsearch or Postgres full-text search)
- Precision matters more than recall

**Use vector search when:**
- Users phrase queries in natural language that differs from document terminology
- You need cross-language retrieval
- The knowledge base covers broad topics where vocabulary varies
- Exploratory discovery ("find articles related to this concept") is a primary use case

**Use hybrid when:**
- Both use cases apply (most real-world scenarios)
- Retrieval quality is critical to downstream LLM answer quality
- You can afford the additional infrastructure and complexity

## Sources

- [[sources/hn-vector-database-debate]] -- practitioner debate on vector DB necessity, including BM25 alternatives
- [[sources/graphiti-temporal-knowledge-graphs]] -- implements hybrid retrieval (semantic + BM25 + graph)
