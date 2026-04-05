---
title: "Prompt Caching"
type: concept
sources: ["[[sources/prompt-caching-providers]]", "[[sources/redis-rag-vs-long-context]]", "[[sources/anthropic-prompt-caching]]", "[[sources/premai-llm-cost-optimization-guide]]"]
related: ["[[concepts/context-windows]]", "[[concepts/context-engineering]]", "[[concepts/long-context-models]]", "[[concepts/kv-cache]]", "[[concepts/llm-cost-optimization]]"]
last_compiled: 2026-04-05
summary: "Provider-level optimization caching computed state of static prompt prefixes: Anthropic (90% savings), OpenAI (50%), Google (75%) — making large contexts economically viable."
---

## Overview

Prompt caching is an infrastructure-level optimization that reuses the computed internal state (KV cache) of static prompt prefixes across multiple API calls. Unlike output caching (storing responses), prompt caching avoids redundant computation of system instructions, examples, and reference documents that remain constant between requests.

This is a critical enabler for systems using large [[concepts/context-windows]], reducing both cost and latency. For [[concepts/llm-knowledge-base]] systems that repeatedly query against the same knowledge base, prompt caching can reduce per-query costs by 50-90%.

## Provider Comparison

| Feature | Anthropic (Claude) | OpenAI (GPT) | Google (Gemini) |
|---------|-------------------|--------------|-----------------|
| Implementation | Manual (API headers) | Automatic | Manual (API method) |
| Cost reduction (reads) | **90%** | **50%** | **75%** |
| Write surcharge | 25% | None | None |
| Min tokens | 1,024 (Sonnet/Opus) | 1,024 | 32,768 |
| Cache TTL | 5 min (refreshed on use) | 5-10 min (up to 1hr off-peak) | 1 hour (customizable) |
| Cache breakpoints | Up to 4 per request | N/A (automatic) | N/A |
| Storage charges | None | None | Token-hours |

## Implementation Best Practices

### Optimal Prompt Structure
```
[STATIC — cached]
  System instructions
  Reference documents / knowledge base
  Few-shot examples
  Tool definitions

[DYNAMIC — not cached]
  User query
  Session-specific context
```

Place all static content at the beginning, dynamic content at the end. Cache hits require exact prefix matching.

### Anthropic-Specific
Add header `anthropic-beta: prompt-caching-2024-07-31` and mark cacheable sections with `cache_control` parameter. Up to 4 breakpoints per request.

### Cost-Benefit Analysis
- **Break-even**: Typically 2-3 requests with the same prefix to offset any write surcharge
- **Ideal for**: Repeated queries against stable context (chatbots, wiki Q&A, coding assistants)
- **Not ideal for**: One-off queries with unique context each time

## Real-World Impact

- Developer report: **$8,000/month → $800/month** with caching in RAG system (90% reduction)
- Another report: **$720/month → $72/month** (90% reduction)
- Semantic caching (Redis): **73% reduction** in high-repetition workloads

## Relevance to Wiki Systems

For [[concepts/llm-knowledge-base]] systems, prompt caching is particularly valuable because:
1. System instructions and wiki structure are constant across queries
2. The summaries file changes infrequently and is loaded every query
3. Only the user's question and loaded articles change between requests
4. With 4 Anthropic breakpoints: system prompt, summaries, loaded articles, user query

## Technical Foundation: KV Cache

Prompt caching is built on [[concepts/kv-cache]] infrastructure. When a provider caches a prompt prefix, they store the computed KV cache state from the prefill phase. Subsequent requests with the same prefix skip prefill computation entirely, explaining both the cost savings (no GPU compute for cached tokens) and latency reduction (skip directly to decoding).

## Anthropic Claude Performance Benchmarks

From [[sources/anthropic-prompt-caching]]:
- **100K-token book chat**: 11.5s → 2.4s (79% latency reduction) + 90% cost reduction
- **10,000-token many-shot prompting**: 1.6s → 1.1s (31% latency) + 86% cost savings
- **10-turn conversations**: ~10s → ~2.5s (75% latency) + 53% cost reduction

## Sources

- [[sources/prompt-caching-providers]] — cross-provider comparison and implementation details
- [[sources/redis-rag-vs-long-context]] — semantic caching as complementary approach
- [[sources/anthropic-prompt-caching]] — Anthropic's official documentation with performance benchmarks
- [[sources/premai-llm-cost-optimization-guide]] — prompt caching as one of 8 cost optimization strategies

## Related Concepts

- [[concepts/context-windows]] — caching makes large contexts economically viable
- [[concepts/context-engineering]] — cache-aware design is a key engineering practice
- [[concepts/long-context-models]] — caching is essential for cost-effective use of large windows
- [[concepts/kv-cache]] — the underlying infrastructure that prompt caching abstracts
- [[concepts/llm-cost-optimization]] — prompt caching as a key cost lever
