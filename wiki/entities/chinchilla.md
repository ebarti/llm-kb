---
title: "Chinchilla"
type: entity
entity_type: paper
sources: ["[[sources/scaling-laws-data-quality]]", "[[sources/chinchilla-scaling-laws-explained]]"]
related: ["[[concepts/scaling-laws]]", "[[concepts/training-data-curation]]", "[[concepts/chinchilla-scaling-laws]]", "[[concepts/compute-optimal-training]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "DeepMind's 2022 paper establishing compute-optimal scaling laws: model parameters and training tokens should scale equally (~20 tokens per parameter), showing many existing LLMs were significantly undertrained."
---

## Overview

"Training Compute-Optimal Large Language Models" (Hoffmann et al., 2022) — commonly called the Chinchilla paper — is one of the most influential papers in LLM scaling. Published by DeepMind, it established that for a given compute budget, model parameters and training tokens should be scaled roughly equally.

## Key Finding

The compute-optimal ratio is approximately **20 tokens per parameter**. A 70B model should train on ~1.4T tokens to be compute-optimal. This was a significant correction to earlier Kaplan scaling laws (OpenAI, 2020) that suggested prioritizing model size over data.

## Impact

- Showed that GPT-3 (175B params, 300B tokens) was severely undertrained — it should have seen ~3.5T tokens
- Chinchilla (70B params, 1.4T tokens) outperformed the much larger Gopher (280B params, 300B tokens)
- Fundamentally changed how labs budget compute: invest in data, not just parameters
- Drove the shift toward larger training datasets (FineWeb, DCLM, etc.)

## Limitations

The Chinchilla framework treats all tokens as equivalent — it has no notion of data quality. [[sources/scaling-laws-data-quality]] extends it with an explicit quality parameter Q, showing that the optimal compute allocation depends on data quality: high-quality data favors larger models, low-quality data means quality improvement outweighs scaling.

Subsequent work has also challenged the exact coefficient (~20 tokens/param) and suggested that in practice, "over-training" smaller models on more data (beyond Chinchilla-optimal) can be preferable when inference cost matters more than training cost.

## Mentioned In

- [[sources/scaling-laws-data-quality]] — extended with quality-aware framework
