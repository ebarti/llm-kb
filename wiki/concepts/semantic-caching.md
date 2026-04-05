---
title: "Semantic Caching"
type: concept
sources: ["[[sources/redis-token-optimization]]", "[[sources/premai-llm-cost-optimization-guide]]"]
related: ["[[concepts/llm-cost-optimization]]", "[[concepts/prompt-caching]]", "[[concepts/token-optimization]]", "[[entities/redis]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Caching LLM responses keyed by semantic similarity rather than exact string match, using vector embeddings to identify similar queries and return pre-computed answers in milliseconds — achieving 61-73% cost reduction."
---

## Overview

Semantic caching stores LLM responses alongside vector embeddings of the input queries. When a new query arrives, the system converts it to an embedding and searches for semantically similar cached queries. If similarity exceeds a threshold, the cached response is returned immediately — eliminating the LLM inference call entirely.

Unlike exact-match caching, semantic caching catches paraphrases and near-duplicates: "What's the weather like today?" and "How's the weather right now?" would hit the same cache entry. This is critical because production workloads contain far more repetition than developers typically expect.

## How It Works

1. **Query arrives** → convert to vector embedding
2. **Vector search** against cache (cosine similarity, Euclidean distance, or inner product)
3. **If match exceeds threshold** → return cached response (milliseconds)
4. **If no match** → call LLM, store query embedding + response in cache

## Multi-Tier Strategy

Production systems typically implement layered caching:
1. **Exact match** — identical queries at sub-millisecond latency
2. **Semantic match** — similar queries at slightly higher latency
3. **Fresh inference** — cache miss, full LLM call (seconds)

## Performance Results

- **Redis LangCache**: ~73% cost reduction in high-repetition workloads
- **Customer service**: 61-68% cache hit rates
- **API call reduction**: 68.8% documented in production
- **Latency**: cache hits return in **milliseconds** vs **seconds** for fresh inference

## Comparison with Prompt Caching

| Dimension | Semantic Caching | [[concepts/prompt-caching|Prompt Caching]] |
|-----------|-----------------|----------------|
| What's cached | Full responses | KV cache state of prompt prefix |
| Match type | Semantic similarity | Exact prefix match |
| Provider | Application-level | API provider |
| Cost saving | 30-73% | 50-90% on cached input |
| Latency saving | Seconds → milliseconds | 31-79% faster |
| Complementary? | Yes — they stack | Yes — they stack |

These techniques are complementary: prompt caching reduces cost of cache misses, while semantic caching eliminates inference calls entirely for cache hits.

## Infrastructure

[[entities/redis|Redis]] has emerged as the standard platform, consolidating semantic caching, vector search, session management, and operational data in a single system. It handles millions of vectors with sub-millisecond latency.

## Sources
- [[sources/redis-token-optimization]] — semantic caching architecture and Redis LangCache results
- [[sources/premai-llm-cost-optimization-guide]] — semantic caching as one of 8 cost strategies

## Related Concepts
- [[concepts/llm-cost-optimization]] — semantic caching as a high-impact cost technique
- [[concepts/prompt-caching]] — complementary provider-level caching
- [[concepts/vector-databases]] — underlying infrastructure for similarity search
- [[concepts/token-optimization]] — reducing token usage through caching
