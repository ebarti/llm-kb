---
title: "Prometheus"
type: entity
entity_type: tool
sources: ["[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/eugeneyan-llm-evaluators]]"]
related: ["[[concepts/llm-as-judge]]", "[[concepts/llm-evaluation-metrics]]", "[[entities/deepeval]]"]
last_compiled: 2026-04-05
summary: "Open-source LLM evaluator fine-tuned on 100K GPT-4 feedback samples (based on Llama-2-Chat); achieves 0.897 Pearson correlation with human judgments using explicit rubrics and reference answers."
---

## Overview

Prometheus is an open-source LLM fine-tuned specifically for evaluation tasks. Based on Llama-2-Chat and trained on 100,000 GPT-4 feedback samples, it provides a cost-effective alternative to using GPT-4 directly as a judge.

## Key Properties

- **Base model**: Llama-2-Chat
- **Training data**: 100K GPT-4 feedback examples
- **Correlation**: 0.897 Pearson with human judgments
- **Requirement**: Explicit rubrics and reference answers
- **Prometheus 2**: Updated version with fine-grained rubrics

## Trade-offs

Compared to using GPT-4 directly as a judge:
- **Advantage**: Much lower cost (runs locally or on smaller hardware)
- **Advantage**: No API dependency
- **Limitation**: Less flexible (requires explicit rubrics)
- **Limitation**: May not generalize as well outside training distribution

## Mentioned In

- [[sources/confident-ai-llm-evaluation-metrics]] — as an open-source LLM-as-Judge option
- [[sources/eugeneyan-llm-evaluators]] — effectiveness data (0.897 Pearson correlation)
