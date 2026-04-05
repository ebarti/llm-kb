---
title: "Source: Prompt Caching with OpenAI, Anthropic, and Google"
type: source-summary
source: "[[raw/prompt-caching-providers]]"
related: ["[[concepts/prompt-caching]]", "[[concepts/context-windows]]", "[[concepts/context-engineering]]"]
last_compiled: 2026-04-05
summary: "Cross-provider prompt caching comparison: OpenAI (automatic, 50% savings), Anthropic (manual, 90% savings), Google (manual, 75% savings) — all dramatically reduce long-context costs."
---

## Key Points

- **OpenAI**: Automatic caching, 50% cost reduction, up to 80% latency reduction. Min 1,024 tokens. Cache TTL 5-10 min.
- **Anthropic**: Manual via API headers, 90% cost reduction on reads (25% write surcharge). Min 1,024 tokens (Sonnet/Opus). Up to 4 cache breakpoints.
- **Google**: Manual creation, 75% cost reduction. Min 32,768 tokens. Default 1-hour TTL. No creation cost.
- Real-world impact: practitioners report 90% monthly cost reductions ($8K→$800, $720→$72)

## Detailed Summary

Prompt caching is a critical cost optimization for any system using large context windows. Unlike output caching (which stores responses), prompt caching reuses the computed state of static prompt prefixes, avoiding redundant processing of system instructions, examples, and reference documents.

The three major providers take different approaches: OpenAI's automatic caching is zero-configuration but limited to 50% savings. Anthropic offers the deepest discounts (90% on reads) but requires explicit cache breakpoint placement. Google's "context caching" offers 75% savings but has the highest minimum threshold (32K tokens).

For [[concepts/llm-knowledge-base]] systems, prompt caching is particularly valuable: the system instructions, wiki structure, and summaries file are largely static between queries, making them ideal cache candidates. A wiki system making 100+ queries per session against the same knowledge base could see 80-90% cost reduction with proper caching.

## Related Concepts

- [[concepts/prompt-caching]] — the core concept analyzed
- [[concepts/context-windows]] — caching makes large contexts economically viable
- [[concepts/context-engineering]] — cache-aware context design is a key engineering practice
