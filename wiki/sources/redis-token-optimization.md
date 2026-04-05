---
title: "Source: LLM Token Optimization — Cut Costs & Latency"
type: source-summary
source: "[[raw/redis-token-optimization]]"
related: ["[[concepts/semantic-caching]]", "[[concepts/token-optimization]]", "[[concepts/llm-cost-optimization]]", "[[entities/redis]]"]
last_compiled: 2026-04-05
summary: "Redis guide to token optimization: semantic caching achieves 73% cost reduction, output tokens matter more than input for latency, and multi-tier caching eliminates entire inference calls."
---

## Key Points
- Output tokens cost 4-5x more than input tokens ($10-15 vs $2-3 per MTok)
- Flagship vs budget model: 16x cost difference for identical token counts
- Redis LangCache achieved ~73% cost reduction in high-repetition workloads
- 20-turn conversations waste 5,000-10,000 tokens when 500-1,000 would suffice
- Multi-tier caching: exact match → semantic match → fresh inference

## Detailed Summary

Redis's guide identifies where [[concepts/token-optimization|token waste]] occurs in production LLM applications: verbose system prompts repeated across queries, bloated conversation histories, unoptimized function calling, missing max_tokens limits, and oversized RAG context. The decode phase (output generation) is the latency bottleneck since it's sequential and memory-bandwidth bound.

The optimization playbook progresses from foundation techniques (tighter prompts, output constraints, semantic chunking) to advanced strategies ([[concepts/semantic-caching|semantic caching]] with vector embeddings, LLMLingua prompt compression, task-based model selection). Semantic caching stands out: it stores query embeddings alongside LLM responses, retrieving cached answers for semantically similar queries at sub-millisecond latency. Redis LangCache demonstrated 73% cost reduction in high-repetition workloads.

A key insight: production workloads contain far more repetition than expected, making caching disproportionately effective.

## Related Concepts
- [[concepts/semantic-caching]] — the standout optimization technique
- [[concepts/token-optimization]] — broader token efficiency strategies
- [[concepts/llm-cost-optimization]] — cost reduction context
