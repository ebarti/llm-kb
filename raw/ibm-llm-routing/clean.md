---
title: "LLM Routing for Quality, Low-Cost Responses"
source: "https://research.ibm.com/blog/LLM-routers"
author: "IBM Research"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [model-routing, cost-optimization, llm-selection, inference]
type: article
status: raw
discovered_via: search
---

# LLM Routing for Quality, Low-Cost Responses — IBM Research

## What is LLM Routing?
LLM routers function as intelligent dispatchers for language model queries. Rather than sending every request to a single large model, routers analyze incoming queries and direct them to the most appropriate model. Works like "an air traffic controller" directing traffic to optimize outcomes.

## Two Primary Approaches

### Nonpredictive Routers (Audition Method)
- Test multiple models simultaneously on each query
- Select model generating best response
- Advantage: immediate feedback on model selection
- Drawback: multiple inferences create latency and increased costs

### Predictive Routers
- Make routing decisions using pre-inference analysis
- Train algorithms on benchmark data to identify model strengths/weaknesses
- IBM's approach leverages publicly available LLM evaluation data (Stanford HELM)
- Faster and more cost-effective than audition methods

### Cascading Routers
- Hybrid variant testing smallest/cheapest models first
- Escalate until quality answer emerges

## Cost-Quality Tradeoffs
- Cut inferencing costs by up to 85% by directing simpler queries to smaller models
- Several 13B parameter models outperformed Meta's 70B Llama-2 on specialized tasks
- If 60% of queries use small model, 30% medium, 10% large: average costs drop 50-70%

## IBM Router Results (RouterBench)
- 11 models via IBM router outperformed individual models working independently
- IBM router matched GPT-4 performance while saving 5 cents per query

## Pricing Context (Early 2026)
- Premium models (GPT-4, Claude Opus): $30-60/MTok
- Mid-tier: $10-15/MTok
- Lightweight: $0.50-2/MTok
- Small models: $0.10-0.50/MTok
- Local deployment: $0.0001/MTok
- Difference between premium and lightweight: 60-300x

## Practical Implementation
- Router operates in three stages: analysis, selection, execution (under 1ms)
- Organizations report 30-70% cost reductions while maintaining quality
- Up to 98% savings on specific workloads
