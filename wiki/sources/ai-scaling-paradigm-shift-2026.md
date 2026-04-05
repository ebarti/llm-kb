---
title: "Source: The AI Scaling Paradigm Shift — From Pre-Training to Test-Time Compute"
type: source-summary
source: "[[raw/ai-scaling-paradigm-shift-2026]]"
related: ["[[concepts/compute-scaling]]", "[[concepts/test-time-compute]]", "[[concepts/path-to-agi]]", "[[entities/ilya-sutskever]]"]
tags: [scaling-laws, test-time-compute, post-training, reasoning-models, inference]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The meaning of 'scaling' has fundamentally shifted: from pre-training scale (2018-2023) to post-training (2023-2025) to test-time compute (2024+), with DeepSeek-R1 proving RL alone produces reasoning."
---

## Key Points

- Three eras of scaling: pre-training (Chinchilla), post-training (RLHF/DPO), test-time compute (o1/R1)
- Frontier models have shown diminishing returns from pre-training scale for over a year
- DeepSeek-R1 proved pure RL produces reasoning capabilities matching OpenAI o1
- Test-time compute: spending 10-100x more tokens per query for better answers
- Field shifts from "does scaling reduce loss?" to "which scaling translates to economic utility?"
- Sutskever: "The age of scaling is ending... back to the age of research"
- Data wall: high-quality text data may be exhausted by 2026-2028

## Detailed Summary

This composite source tracks the most significant paradigm shift in AI since the transformer architecture: the transition from raw pre-training scale as the primary driver of progress to a multi-dimensional scaling landscape.

### The Pre-Training Plateau

The Kaplan (2020) and Chinchilla (2022) scaling laws established that more compute + more data = predictably better models. This powered the GPT-2 → GPT-3 → GPT-4 progression. However, by late 2024, this approach began hitting diminishing returns. GPT-5 delays, marginal improvements from massive cost increases, and private acknowledgments of a ceiling have shifted the industry's approach.

### The Three Eras

**Era 1: Pre-Training (2018-2023)** — Bigger models, more data, predictable improvement.

**Era 2: Post-Training (2023-2025)** — RLHF, instruction tuning, DPO improve behavior without larger base models. [[entities/ilya-sutskever]]'s shift away from pure scaling reflects this transition.

**Era 3: Test-Time Compute (2024-present)** — Spending more compute at inference via deliberation and search strategies. OpenAI o1/o3, DeepSeek-R1, Gemini 2.0 Flash Thinking. See [[concepts/test-time-compute]].

### The Data Wall

A critical forcing function: high-quality text data (~300T tokens) may be fully utilized by 2026-2032. Synthetic data offers partial relief but risks [[concepts/model-collapse]]. Microsoft's SynthLLM and human-anchored approaches attempt to bridge the gap.

### Competing Narratives

Nadella: Post-training represents "emergence of new scaling laws" — scaling evolves, not dies.
Apple ML Research: Reasoning models may be "illusion of thinking."
The truth likely lies between: scaling continues but along different, less predictable dimensions.

## Concepts Introduced or Discussed

- [[concepts/compute-scaling]] — The multi-dimensional scaling landscape
- [[concepts/test-time-compute]] — Inference-time scaling as new frontier
- [[concepts/data-wall]] — Training data exhaustion
- [[concepts/model-collapse]] — Risks of synthetic data training

## Metadata

- **Author**: Multiple sources
- **Date Published**: 2026-01-01
- **Format**: Compiled analysis
- **URL**: https://www.hec.edu/en/dare/tech-ai/ai-beyond-scaling-laws
