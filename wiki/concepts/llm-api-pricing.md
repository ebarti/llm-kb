---
title: "LLM API Pricing"
type: concept
sources: ["[[sources/premai-llm-cost-optimization-guide]]", "[[sources/ibm-llm-routing]]", "[[sources/redis-token-optimization]]", "[[sources/anthropic-prompt-caching]]"]
related: ["[[concepts/llm-cost-optimization]]", "[[concepts/model-routing]]", "[[concepts/prompt-caching]]"]
last_compiled: 2026-04-05
summary: "LLM API pricing landscape in 2026: prices dropped ~80% since early 2025; output tokens cost 3-5x more than input; premium-to-lightweight gap is 60-300x; batch APIs offer 50% discounts."
---

## Overview

LLM API pricing determines the economics of running LLM-powered applications. Understanding the pricing structure — asymmetric input/output costs, tiered models, caching discounts, and batch pricing — is essential for [[concepts/llm-cost-optimization|cost optimization]].

## Market Trends

LLM API prices dropped approximately **80%** between early 2025 and early 2026:
- GPT-4o input: $5.00 → $2.50 per million tokens
- Newer models like o4 Mini: $0.55/MTok input
- Price compression continues as competition intensifies

## Pricing Tiers (Early 2026)

| Tier | Examples | Input $/MTok | Output $/MTok | Notes |
|------|----------|-------------|--------------|-------|
| Premium | GPT-4, Claude Opus | $15-30 | $60-75 | Complex reasoning |
| Mid-tier | GPT-4o, Claude Sonnet | $2.50-3 | $10-15 | General purpose |
| Lightweight | GPT-4o-mini, Haiku | $0.15-0.50 | $0.60-1.25 | Simple tasks |
| Small/Open | Llama, Mistral API | $0.10-0.50 | $0.10-0.50 | Commodity |
| Self-hosted | Any open model | ~$0.0001 | ~$0.0001 | Infrastructure cost |

## Key Pricing Asymmetries

1. **Output > Input**: Output tokens cost **3-5x** more than input tokens. Cutting response length yields outsized savings.
2. **Premium > Lightweight**: The gap is **60-300x**. This makes [[concepts/model-routing|model routing]] enormously impactful.
3. **Cache hits > Fresh tokens**: Anthropic charges 10% for cached reads; OpenAI 50%. [[concepts/prompt-caching|Prompt caching]] can save 50-90%.
4. **Batch > Real-time**: Batch APIs offer 50% discounts for non-urgent workloads.

## Practical Example

Customer support chatbot, 1M conversations/month (500 input + 200 output tokens each):
- Flagship model ($2.50/$10.00): **$3,250/month**
- Budget-tier model ($0.15/$0.60): **$195/month**
- **16x difference** for identical token counts and conversation quality

## Sources
- [[sources/premai-llm-cost-optimization-guide]] — 2026 pricing tables and market trends
- [[sources/ibm-llm-routing]] — premium vs lightweight pricing gap
- [[sources/redis-token-optimization]] — input/output cost asymmetry
- [[sources/anthropic-prompt-caching]] — cache pricing tiers

## Related Concepts
- [[concepts/llm-cost-optimization]] — strategies for managing these costs
- [[concepts/model-routing]] — exploiting pricing tier differences
- [[concepts/prompt-caching]] — exploiting cache pricing discounts
