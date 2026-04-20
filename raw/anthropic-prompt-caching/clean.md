---
title: "Prompt Caching - Anthropic Claude"
source: "https://claude.com/blog/prompt-caching"
author: "Anthropic"
date_published: 2024-08-14
date_ingested: 2026-04-05
tags: [prompt-caching, anthropic, claude, cost-optimization, latency]
type: article
status: raw
discovered_via: search
---

# Prompt Caching — Anthropic Claude

## How It Works
Prompt caching allows developers to cache frequently used context between API calls. The system caches large blocks of input tokens that are reused across multiple requests, reducing computational overhead on subsequent calls that reference the same cached content.

## Pricing Structure
Claude implements a tiered pricing model for cached prompts:
- Cache Write: 25% premium over base input token pricing (initial caching cost)
- Cache Read: 10% of base input token pricing (significantly discounted reuse cost)

### Model-Specific Rates
- Claude 3.5 Sonnet: $3/MTok input | $3.75/MTok write | $0.30/MTok read | $15/MTok output
- Claude 3 Opus: $15/MTok input | $18.75/MTok write | $1.50/MTok read | $75/MTok output
- Claude 3 Haiku: $0.25/MTok input | $0.30/MTok write | $0.03/MTok read | $1.25/MTok output

## Supported Models
- Claude 3.5 Sonnet (200K context window)
- Claude 3 Opus (200K context window)
- Claude 3 Haiku (200K context window)

## Primary Use Cases
1. Conversational agents with extended instructions or document uploads
2. Coding assistants maintaining codebase summaries for Q&A
3. Large document processing incorporating complete long-form material
4. Extensive instruction sets including dozens of high-quality examples
5. Agentic systems requiring multiple tool-use rounds
6. Knowledge base interactions embedding entire documents for user queries

## Performance Improvements
- Chat with 100K-token books: 79% latency reduction (11.5s → 2.4s) + 90% cost reduction
- 10,000-token many-shot prompting: 31% latency reduction (1.6s → 1.1s) + 86% cost savings
- 10-turn conversations: 75% latency reduction (~10s → ~2.5s) + 53% cost reduction

## Cache Lifetime
Default 5-minute cache lifetime. Optional 1-hour cache duration available at additional cost.

## Availability
Generally Available on the Anthropic API (since December 17, 2024). Available in preview on Amazon Bedrock and Google Cloud Vertex AI.
