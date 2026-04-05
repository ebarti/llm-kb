---
title: "LLM Cost Optimization"
type: concept
sources: ["[[sources/premai-llm-cost-optimization-guide]]", "[[sources/redis-token-optimization]]", "[[sources/ibm-llm-routing]]", "[[sources/anthropic-prompt-caching]]"]
related: ["[[concepts/model-routing]]", "[[concepts/prompt-caching]]", "[[concepts/semantic-caching]]", "[[concepts/token-optimization]]", "[[concepts/llm-api-pricing]]", "[[concepts/llm-inference-optimization]]", "[[concepts/batch-inference]]"]
last_compiled: 2026-04-05
summary: "Strategies for reducing LLM API and infrastructure costs by 50-85%: prompt optimization, caching (prompt + semantic), model routing, batching, output constraints, and self-hosting at scale."
---

## Overview

LLM cost optimization is the discipline of reducing the financial cost of running LLM-powered applications while maintaining output quality. A 2025 analysis of 86,000 developers found that 40-60% of LLM budgets go to operational inefficiencies rather than necessary model usage. For the [[concepts/llm-knowledge-base|LLM-KB system]], where every compilation, Q&A query, and lint operation involves LLM calls, cost management directly determines sustainability.

## The Cost Landscape (2026)

LLM API prices dropped approximately 80% between early 2025 and early 2026. Current pricing:

| Tier | Examples | Input Price | Output Price |
|------|----------|-------------|--------------|
| Premium | GPT-4, Claude Opus | $15-30/MTok | $60-75/MTok |
| Mid-tier | GPT-4o, Claude Sonnet | $2.50-3/MTok | $10-15/MTok |
| Lightweight | GPT-4o-mini, Haiku | $0.15-0.50/MTok | $0.60-1.25/MTok |
| Small/Open | Llama, Mistral | $0.10-0.50/MTok | $0.10-0.50/MTok |
| Self-hosted | Any open model | ~$0.0001/MTok | ~$0.0001/MTok |

Key asymmetry: output tokens cost 3-5x more than input tokens. A customer support chatbot at 1M conversations/month costs $3,250/month on a flagship model vs $195/month on a budget model — a 16x difference for identical token counts.

## Eight-Strategy Framework

### Tier 1: Quick Wins (Hours)
1. **Prompt Optimization** (20-40% savings): Compress system prompts, remove redundancy, constrain output length. One case showed 85% token reduction (847 → 127 tokens) with improved results.
2. **Output Constraints**: Set max_tokens limits; include length constraints in instructions ("Answer in 50 words"). Output tokens cost 3-5x more, so cutting response length yields outsized savings.

### Tier 2: Infrastructure (Days)
3. **[[concepts/prompt-caching|Prompt Caching]]** (50-90% on cached portions): Anthropic charges 10% of normal rate for cache hits; OpenAI offers 50% discount. Critical for applications with repeated system prompts.
4. **[[concepts/semantic-caching|Semantic Caching]]** (30-70% savings): Cache LLM responses keyed by semantic similarity. Redis LangCache achieved 73% cost reduction. Hit rates of 61-68% documented in customer service.
5. **[[concepts/batch-inference|Batch APIs]]** (20-50% savings): OpenAI Batch API offers 50% discount for jobs that can wait up to 24 hours. Anthropic's Batch API halves Sonnet pricing.

### Tier 3: Architecture (Weeks)
6. **[[concepts/model-routing]]** (40-60% savings): Route 70% of queries to cheap models, 25% to mid-tier, 5% to premium. IBM's router matched GPT-4 quality while saving 5 cents per query.
7. **Context Optimization** (20-40% savings): Conversation summarization, selective RAG retrieval, semantic chunking. 20-turn conversations waste 5,000-10,000 tokens when 500-1,000 would suffice.

### Tier 4: Scale (Months)
8. **Self-Hosting** (60-90% savings at scale): Practical above 1M monthly queries. Requires GPU infrastructure, [[concepts/llm-serving-frameworks|serving frameworks]], and [[concepts/quantization|quantized models]].

## Real-World Case Study

A fintech compliance analyzer achieved 80% cost reduction ($12,000 → $2,400/month) by stacking:
- Prompt compression (30% token reduction)
- Semantic caching (45% hit rate)
- Model routing (70% GPT-3.5, 25% mini, 5% GPT-4)
- Output constraints (50% fewer tokens)

## Relevance to LLM-KB System

The [[concepts/llm-knowledge-base|LLM-KB]] system incurs costs at every stage: RESEARCH (web search + multi-source ingestion), COMPILE (cross-referencing dozens of articles), Q&A (reading summaries + full articles), and LINT (scanning entire wiki). Key applicable strategies:
- **Prompt caching**: System prompts and the CLAUDE.md instructions are repeated across every operation
- **Model routing**: Use lightweight models for simple classification/tagging, premium for synthesis
- **Semantic caching**: Similar queries about the same topic area can reuse cached answers
- **Batch processing**: Bulk compilation operations can use batch APIs

## Sources
- [[sources/premai-llm-cost-optimization-guide]] — comprehensive 8-strategy framework with fintech case study
- [[sources/redis-token-optimization]] — token waste identification and semantic caching architecture
- [[sources/ibm-llm-routing]] — model routing research and RouterBench results
- [[sources/anthropic-prompt-caching]] — Anthropic's prompt caching pricing and performance

## Related Concepts
- [[concepts/llm-inference-optimization]] — technical optimization underlying cost reduction
- [[concepts/llm-api-pricing]] — market pricing context
- [[concepts/cheap-ontology]] — cost reduction enabling democratized knowledge management
