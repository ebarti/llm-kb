---
title: "Redis"
type: entity
entity_type: tool
sources: ["[[sources/redis-token-optimization]]"]
related: ["[[concepts/semantic-caching]]", "[[concepts/vector-databases]]", "[[concepts/llm-cost-optimization]]"]
last_compiled: 2026-04-05
summary: "In-memory data platform used for LLM semantic caching: Redis LangCache stores query embeddings alongside responses, achieving 73% cost reduction with sub-millisecond vector search across millions of entries."
---

## Overview

Redis is an in-memory data platform that has become a key infrastructure component for LLM application optimization, particularly through its [[concepts/semantic-caching|semantic caching]] capabilities.

## LLM-Relevant Features

- **LangCache**: Semantic caching layer storing query vector embeddings alongside LLM responses
- **Vector search**: Cosine similarity, Euclidean distance, inner product at sub-millisecond latency
- **Scale**: Handles millions of vectors with consistent performance
- **Consolidation**: Replaces need for separate vector database, cache, and session store

## Performance

- ~73% cost reduction in high-repetition LLM workloads
- Sub-millisecond cache hit latency vs seconds for fresh LLM inference
- Supports multi-tier caching: exact match → semantic match → fresh inference

## Mentioned In
- [[sources/redis-token-optimization]] — semantic caching architecture and optimization results
