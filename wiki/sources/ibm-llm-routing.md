---
title: "Source: LLM Routing for Quality, Low-Cost Responses"
type: source-summary
source: "[[raw/ibm-llm-routing]]"
related: ["[[concepts/model-routing]]", "[[concepts/llm-cost-optimization]]", "[[entities/ibm-research]]"]
last_compiled: 2026-04-05
summary: "IBM Research on LLM routing: predictive routers trained on HELM benchmarks matched GPT-4 quality while saving 5 cents/query; 13B models outperformed 70B Llama-2 on specialized tasks."
---

## Key Points
- Predictive routers make routing decisions in under 1 millisecond
- IBM router matched GPT-4 performance while saving 5 cents per query
- Several 13B models outperformed 70B Llama-2 on specialized tasks
- Premium vs lightweight model pricing gap: 60-300x
- Organizations report 30-70% cost reductions while maintaining quality

## Detailed Summary

IBM Research presents two primary [[concepts/model-routing|routing]] approaches: nonpredictive routers (testing multiple models simultaneously and selecting the best response) and predictive routers (making pre-inference routing decisions trained on benchmark data). IBM's predictive approach leverages Stanford's HELM benchmark framework to identify specialized model capabilities and route domain-specific queries to optimal performers.

The key finding: model size does not determine task-specific quality. Several 13-billion parameter models outperformed Meta's 70-billion parameter Llama-2 by measurable margins on specific tasks. The RouterBench evaluation showed 11 models via IBM's router outperformed individual models working independently.

Cascading routers represent a hybrid: test smallest/cheapest models first, escalating only when quality is insufficient. This achieves up to 85% cost reduction by directing simpler queries to smaller models.

## Related Concepts
- [[concepts/model-routing]] — the core technique
- [[concepts/llm-cost-optimization]] — cost reduction context
- [[concepts/llm-inference-optimization]] — routing as part of the optimization stack
