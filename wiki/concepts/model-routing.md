---
title: "Model Routing"
type: concept
sources: ["[[sources/ibm-llm-routing]]", "[[sources/premai-llm-cost-optimization-guide]]"]
related: ["[[concepts/llm-cost-optimization]]", "[[concepts/llm-inference-optimization]]", "[[concepts/llm-api-pricing]]"]
last_compiled: 2026-04-05
summary: "Intelligent dispatching of LLM queries to appropriately-sized models based on complexity, achieving 40-85% cost reduction while maintaining 95%+ quality through predictive routing, cascading, or benchmark-trained classifiers."
---

## Overview

Model routing is the technique of directing LLM queries to different models based on query complexity, required quality, latency constraints, or cost targets. Instead of sending every request to a single expensive model, a router analyzes incoming queries and dispatches them to the most cost-effective model that can handle each task adequately.

This is the single most impactful architectural decision for [[concepts/llm-cost-optimization|cost optimization]] at the application level. The price difference between premium and lightweight models is **60-300x** (as of early 2026), making routing decisions enormously consequential.

## Routing Strategies

### Predictive Routers
Make routing decisions using pre-inference analysis, typically trained on benchmark data:
- IBM's approach trains on Stanford HELM benchmark data to identify specialized model capabilities
- Decisions take **under 1 millisecond**
- Found that several 13B models outperformed 70B Llama-2 on specialized tasks
- IBM's RouterBench: 11 models via router outperformed individual models independently

### Cascading Routers
Start with the smallest/cheapest model and escalate only when quality is insufficient:
- Test smallest model first
- If response quality fails a threshold, try next tier
- Continue until acceptable quality or reach premium tier
- Effective when most queries are simple (common in production)

### Nonpredictive Routers (Audition)
Test multiple models simultaneously and select the best response:
- Provides immediate quality feedback
- Drawback: multiplies inference cost and latency
- Useful for offline evaluation and router training

## Cost Impact

Typical enterprise distribution:
- **70%** of queries → budget model ($0.10-0.50/MTok)
- **20%** of queries → mid-tier model ($2.50-3/MTok)
- **10%** of queries → premium model ($15-30/MTok)

This reduces average per-query cost by **60-80%** compared to routing all traffic through a premium model. Organizations report 30-70% cost reductions in practice, with some achieving up to 98% savings on specific workloads.

## Real-World Results

- IBM router matched **GPT-4 performance** while saving 5 cents per query
- Hybrid query routing: 37-46% less LLM usage, 32-38% latency improvement, 39% cost reduction
- Fintech case study: routing 70% to GPT-3.5, 25% to mini, 5% to GPT-4 was a key component of 80% total cost reduction

## Relevance to LLM-KB System

The [[concepts/llm-knowledge-base|LLM-KB]] system has natural routing opportunities:
- **Simple tasks** (metadata extraction, tag assignment, link validation): lightweight model
- **Moderate tasks** (source summarization, index updates): mid-tier model
- **Complex tasks** (cross-source synthesis, concept article creation, nuanced Q&A): premium model

## Sources
- [[sources/ibm-llm-routing]] — IBM Research on predictive routing with HELM benchmarks
- [[sources/premai-llm-cost-optimization-guide]] — routing as one of 8 cost strategies

## Related Concepts
- [[concepts/llm-cost-optimization]] — routing as the highest-impact cost technique
- [[concepts/llm-api-pricing]] — pricing tiers that make routing valuable
- [[concepts/llm-inference-optimization]] — routing at the application level
