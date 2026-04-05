---
title: "Source: Prompt Caching — Anthropic Claude"
type: source-summary
source: "[[raw/anthropic-prompt-caching]]"
related: ["[[concepts/prompt-caching]]", "[[entities/anthropic]]", "[[entities/claude]]", "[[concepts/llm-cost-optimization]]"]
last_compiled: 2026-04-05
summary: "Anthropic's official prompt caching documentation: 90% cost reduction and 79% latency improvement for repeated context, with tiered write/read pricing across Claude model family."
---

## Key Points
- Cache reads cost 10% of base input token pricing (90% discount)
- Cache writes cost 25% premium over base pricing (amortized over reuse)
- 100K-token book chat: 11.5s → 2.4s (79% latency reduction) + 90% cost reduction
- Default 5-minute cache lifetime, optional 1-hour at additional cost
- Generally Available since December 2024 on Anthropic API, preview on Bedrock/Vertex

## Detailed Summary

[[entities/anthropic|Anthropic's]] prompt caching allows developers to cache frequently used context between API calls, dramatically reducing both cost and latency for workloads with repeated prompt prefixes. The pricing model is tiered: writing to cache costs a 25% premium over standard input tokens, but reading from cache costs only 10% of the standard rate — a net 90% discount on cached portions when reused.

The feature is particularly powerful for [[concepts/llm-knowledge-base|knowledge base]] applications: embedding entire documents into prompts for Q&A, maintaining codebase summaries for coding assistants, and running multi-turn agent workflows. Performance benchmarks show dramatic improvements: a 100K-token book drops from 11.5s to 2.4s response time, and 10-turn conversations see 75% latency reduction with 53% cost savings.

All Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku models support caching with 200K context windows. The 5-minute default cache lifetime means high-frequency applications benefit most, though a 1-hour option exists.

## Notable Quotes
> "Prompt caching is particularly effective for conversational agents with extended instructions or uploaded documents"

## Related Concepts
- [[concepts/prompt-caching]] — the core mechanism
- [[concepts/llm-cost-optimization]] — prompt caching as a key cost lever
- [[concepts/kv-cache]] — underlying infrastructure that makes prompt caching possible
