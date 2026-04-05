---
title: "Compute-Optimal vs Inference-Optimal Training"
type: comparison
subjects: ["[[concepts/compute-optimal-training]]", "[[concepts/chinchilla-scaling-laws]]"]
sources: ["[[sources/chinchilla-scaling-laws-explained]]", "[[sources/raschka-pretraining-post-training-paradigms]]"]
last_compiled: 2026-04-05
summary: "Chinchilla-optimal minimizes loss per training FLOP (~20 tokens/param), but inference-optimal overtrains smaller models on far more data (Llama 3: 1,875:1) because training is one-time while inference runs continuously."
---

## Overview

Two competing strategies for allocating compute in LLM training, reflecting different economic objectives.

## Comparison Table

| Dimension | Compute-Optimal (Chinchilla) | Inference-Optimal (Modern Practice) |
|-----------|------------------------------|--------------------------------------|
| **Objective** | Minimize loss per training FLOP | Minimize total cost (training + lifetime inference) |
| **Token/param ratio** | ~20:1 | 100:1 to 60,000:1 |
| **Model size** | Larger for given budget | Smaller, compensated by more data |
| **Training cost** | Minimized relative to performance | Higher than Chinchilla-optimal |
| **Inference cost** | Higher (more parameters to serve) | Lower (fewer parameters) |
| **Data requirement** | Moderate | Extreme (may exhaust high-quality text) |
| **Example** | Chinchilla 70B / 1.4T tokens | Llama 3 8B / 15T tokens |

## The Economic Argument

Training is a **one-time cost**. Inference runs **continuously** across millions of users. For a model that will serve billions of queries, the total cost of ownership is dominated by inference:

```
Total cost = Training cost + (Inference cost per query x Number of queries)
```

A smaller model that costs 2x more to train but 10x less per inference query is dramatically cheaper over its lifetime.

## Evolution of Ratios

| Approach | Year | Ratio | Strategy |
|----------|------|-------|----------|
| GPT-3 (Kaplan) | 2020 | 1.7:1 | Scale parameters, not data |
| Chinchilla | 2022 | 20:1 | Equal scaling (compute-optimal) |
| Llama 2 | 2023 | ~28:1 | Near Chinchilla-optimal |
| Llama 3 8B | 2024 | 1,875:1 | Heavily inference-optimized |
| Qwen3-0.6B | 2025 | 60,000:1 | Extreme overtraining for tiny model |

## When to Use Each

**Compute-optimal**: Research settings where training compute is the bottleneck and the model will be used in limited settings (few inference queries).

**Inference-optimal**: Production settings where the model will serve many users, and per-query cost matters more than training budget.

## Sources

- [[sources/chinchilla-scaling-laws-explained]] — compute-optimal ratios and post-Chinchilla evolution
- [[sources/raschka-pretraining-post-training-paradigms]] — practical token counts in modern models
