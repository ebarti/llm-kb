---
title: "Prompt Caching with OpenAI, Anthropic, and Google Models"
source: "https://www.prompthub.us/blog/prompt-caching-with-openai-anthropic-and-google-models"
author: "PromptHub"
date_published: 2025-01-15
date_ingested: 2026-04-05
tags: [prompt-caching, context-caching, cost-optimization, anthropic, openai, google]
type: article
status: raw
discovered_via: search
---

# Prompt Caching Across Major LLM Providers

## Overview

Prompt caching optimizes API requests by reusing static prompt components, reducing both costs and latency. Unlike traditional caching that stores outputs, this caches inputs.

## Provider Comparison

### OpenAI

- **Implementation**: Automatic, no code changes needed.
- **Minimum prompt length**: 1,024 tokens.
- **Cache duration**: 5-10 minutes (up to 1 hour off-peak).
- **Cost savings**: 50% reduction on cached tokens.
- **Latency improvement**: Up to 80% reduction.
- **Supported models**: GPT-4o, GPT-4o Mini, o1-Preview, o1-Mini.
- **Monitoring**: `prompt_tokens_details.cached_tokens` in API responses.

### Anthropic (Claude)

- **Implementation**: Manual configuration via API headers.
- **Minimum prompt length**: 1,024 tokens (Claude 3.5 Sonnet/Opus); 2,048 tokens (other models).
- **Cache duration**: 5 minutes, refreshed on each use.
- **Cache write cost**: 25% surcharge.
- **Cache read discount**: 90% cheaper than standard processing.
- **Up to four cache breakpoints per request**.
- **Implementation**: Add header `anthropic-beta: prompt-caching-2024-07-31` and `cache_control` parameter.

### Google Gemini

- **Implementation**: Manual cache creation via `CachedContent.create`.
- **Minimum context length**: 32,768 tokens.
- **Default cache duration**: 1 hour (customizable).
- **Cache read discount**: 75% cheaper.
- **No creation cost**; storage charges based on token-hours.

## Best Practice

Place static content (system instructions, context, examples) at prompt beginning. Dynamic content (user queries) at end. Use consistent delimiters for reliable cache hits.

## Real-World Impact

- One developer: $8,000/month to $800/month with caching in RAG system.
- Another: $720/month to $72/month (90% reduction).
