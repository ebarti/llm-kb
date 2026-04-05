---
title: "IBM Research"
type: entity
entity_type: org
sources: ["[[sources/ibm-llm-routing]]"]
related: ["[[concepts/model-routing]]", "[[concepts/llm-cost-optimization]]"]
last_compiled: 2026-04-05
summary: "IBM's AI research division: developed predictive LLM routing using HELM benchmarks, demonstrating GPT-4-matching quality at 5 cents/query savings through intelligent model selection."
---

## Overview

IBM Research's AI division has contributed to [[concepts/model-routing|LLM routing]] research, developing predictive routers trained on Stanford's HELM benchmark framework.

## Key Contributions

- **RouterBench**: Evaluation framework showing 11 models via IBM router outperformed individual models independently
- **Predictive routing**: Pre-inference routing decisions in under 1ms using benchmark-trained algorithms
- **Key finding**: Several 13B parameter models outperformed 70B Llama-2 on specialized tasks, demonstrating that model size does not determine task-specific quality

## Mentioned In
- [[sources/ibm-llm-routing]] — LLM routing research and RouterBench evaluation
