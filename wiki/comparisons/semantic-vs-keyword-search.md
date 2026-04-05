---
title: "Semantic Search vs Keyword Search"
type: comparison
subjects: ["[[concepts/semantic-search]]", "[[concepts/keyword-search]]"]
sources: ["[[sources/redis-semantic-vs-keyword-search]]", "[[sources/weaviate-hybrid-search-explained]]"]
last_compiled: 2026-04-05
summary: "Complementary retrieval approaches: semantic search captures meaning via dense vectors but misses exact identifiers; keyword search matches precise terms via inverted indexes but misses synonyms — production systems combine both."
---

## Overview

[[concepts/semantic-search]] and [[concepts/keyword-search]] are the two fundamental approaches to information retrieval. They have **complementary failure modes**, which is why production systems combine them into [[concepts/hybrid-search]] rather than choosing one over the other.

## Comparison Table

| Dimension | Semantic Search | Keyword Search |
|-----------|----------------|----------------|
| **How it works** | Dense vectors via transformer models | Inverted indexes with BM25 ranking |
| **Matching** | Meaning-based (cosine similarity) | Lexical (exact terms) |
| **Handles synonyms** | Yes ("car" matches "automobile") | No (misses if different word used) |
| **Handles exact codes** | Poorly (may conflate similar codes) | Perfectly (SKU-2847-B matched exactly) |
| **Memory** | Significant (dense vectors) | Minimal (sparse inverted index) |
| **Latency** | Higher (especially on CPU) | Fast for large collections |
| **GPU benefit** | Substantial acceleration | Not applicable |
| **Determinism** | Non-deterministic (varies with retraining) | Deterministic (same query = same results) |
| **Boolean logic** | Limited | Full AND/OR/NOT support |
| **Multilingual** | Some models handle cross-language | Requires per-language indexes |
| **Setup cost** | Embedding model + vector index | Simpler (standard search infrastructure) |

## Failure Mode Analysis

### Semantic Search Fails When:
- Searching for error codes: "OOM-2024-047"
- Looking up product identifiers: "SKU-2847-B"
- Needing exact phrase matches in legal/regulatory contexts
- String-literal patterns must be matched precisely

### Keyword Search Fails When:
- "database slowdowns" should match "performance optimization"
- "car repairs" should find "automotive maintenance"
- "How do I prevent memory issues?" should find documents about "eviction policies" and "maxmemory configuration"
- Users don't know the exact terminology used in documents

## When to Use Each

### Choose Keyword Search When:
- Users search by exact identifiers (product codes, legal citations, error codes)
- Results must be deterministic and reproducible (regulatory compliance)
- Complex boolean queries are needed (AND/OR/NOT with field filtering)
- Dataset is small-medium and infrastructure simplicity is valued
- Exact phrase matching is critical

### Choose Semantic Search When:
- Users express queries in natural language
- Content uses varied terminology for the same concepts
- Building RAG, QA, or conversational AI systems
- Multilingual matching is needed
- Intent and meaning matter more than specific words

### Choose Hybrid (Both) When:
- Building a production system (almost always the right answer)
- Queries mix natural language with specific identifiers
- Maximum retrieval recall is needed before [[concepts/reranking]]

## The Hybrid Solution

```
Query → BM25 (inverted index) → Ranked List A
      → Vector Search (HNSW)   → Ranked List B
      → RRF Fusion              → Merged Results
      → Cross-Encoder Reranking → Final Top-N
```

See [[concepts/hybrid-search]] for implementation details. Default alpha of 0.75 in [[entities/weaviate]] reflects that most queries benefit more from semantic understanding, with keyword matching as a safety net for exact terms.

## Sources

- [[sources/redis-semantic-vs-keyword-search]] — comprehensive failure mode analysis
- [[sources/weaviate-hybrid-search-explained]] — hybrid architecture details
