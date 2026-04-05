---
title: "RAG vs Cache-Augmented Generation (CAG)"
type: comparison
subjects: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/cache-augmented-generation]]"]
sources: ["[[sources/cache-augmented-generation]]", "[[sources/ragflow-rag-review-2025]]"]
last_compiled: 2026-04-05
summary: "CAG preloads all documents into KV cache for 10x faster, more accurate inference on small KBs — but RAG remains necessary for large, dynamic corpora that exceed context window limits."
---

## Overview

[[concepts/cache-augmented-generation]] (CAG) eliminates the retrieval step entirely by preloading all documents into the LLM's extended context and caching KV parameters. [[concepts/retrieval-augmented-generation]] (RAG) selectively retrieves relevant chunks at query time. The choice depends on knowledge base size, update frequency, and latency requirements.

## Comparison Table

| Dimension | RAG | CAG |
|---|---|---|
| **Knowledge base size** | Unlimited | Limited to context window (~128k-1M tokens) |
| **Latency** | 5-10+ seconds (retrieval + generation) | <1 second (cached generation) |
| **Accuracy** | Depends on retrieval quality | Higher (sees all documents, no retrieval errors) |
| **Multi-hop reasoning** | Requires multi-step retrieval | Natural (all context available) |
| **Update frequency** | Easy (add/update documents) | Requires cache recomputation |
| **Infrastructure** | Vector DB, embedding models, retrieval pipeline | Long-context LLM, KV cache storage |
| **Determinism** | Variable (retrieval ranking) | Deterministic (fixed cache) |
| **Cost model** | Per-query retrieval + generation | One-time preload + per-query generation |

## Performance Data

From SQuAD and HotPotQA benchmarks:
- **Speed**: CAG 0.85s vs. RAG 9.24s on HotPotQA-Small (~10x faster)
- **Accuracy**: CAG achieved higher BERTScores across most configurations
- **Reliability**: CAG eliminates retrieval ranking errors entirely

## When to Use Each

### Choose CAG When
- Knowledge base fits within context window (< ~100 pages for 128k models)
- Knowledge is relatively stable (not requiring real-time updates)
- Multi-hop reasoning across documents is important
- Infrastructure simplicity is valued (no vector DB needed)
- Deterministic, reproducible answers are required

### Choose RAG When
- Knowledge base exceeds any context window
- Documents change frequently and must be immediately available
- Cost optimization requires processing only relevant chunks
- The knowledge domain is vast and only small portions are relevant per query

### Hybrid Approach
Emerging architectures combine CAG (preload core knowledge) with selective RAG (retrieve dynamic or overflow content), balancing speed and coverage.

## Relationship to LLM Knowledge Bases

The [[concepts/llm-knowledge-base]] approach occupies a middle ground: it uses structured indexes and summaries for navigation rather than either vector similarity search (RAG) or full preloading (CAG). At personal scale (~100 articles, ~400K words), this index-based approach introduces less latency than "fancy RAG" infrastructure while not requiring the full-context loading of CAG.

## Sources

- [[sources/cache-augmented-generation]] — CAG paper with benchmarks
- [[sources/ragflow-rag-review-2025]] — CAG in context of RAG evolution
