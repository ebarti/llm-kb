---
title: "Compute-Optimal Training"
type: concept
sources: ["[[sources/chinchilla-scaling-laws-explained]]"]
related: ["[[concepts/chinchilla-scaling-laws]]", "[[concepts/llm-pretraining]]", "[[concepts/llm-training-costs]]"]
last_compiled: 2026-04-05
summary: "Allocating a fixed compute budget optimally between model size and training data — Chinchilla showed equal scaling is optimal, but modern practice shifts toward inference-optimal overtraining of smaller models."
---

## Overview

Compute-optimal training asks: given a fixed FLOP budget, how should it be divided between model parameters and training tokens to minimize loss?

The [[concepts/chinchilla-scaling-laws]] answered this definitively: scale both equally. A 70B model trained on 1.4T tokens beats a 280B model trained on fewer tokens, given the same total compute.

## Compute-Optimal vs. Inference-Optimal

In practice, labs no longer train at the Chinchilla-optimal point. The economic reality is that inference costs dominate over the model's lifetime:

- **Compute-optimal**: Minimizes training loss for a given training budget. Results in larger models.
- **Inference-optimal**: Minimizes total cost (training + lifetime inference). Results in smaller models trained on much more data.

Llama 3 8B trained on 15T tokens (1,875:1 ratio vs Chinchilla's 20:1) exemplifies the inference-optimal approach. The training cost is higher than Chinchilla prescribes for an 8B model, but the resulting model is cheap to serve and competitive with much larger models.

## Implications

1. **Data is the bottleneck**: At extreme overtraining ratios, high-quality text data becomes scarce, driving interest in synthetic data generation
2. **Small models can be powerful**: With enough training data, even sub-1B models can be surprisingly capable
3. **Training cost is a one-time investment**: Amortized over millions of inference queries, overtraining is economically rational

## Sources

- [[sources/chinchilla-scaling-laws-explained]] — the foundational scaling analysis

## Related Concepts

- [[concepts/chinchilla-scaling-laws]] — the specific scaling law
- [[concepts/llm-pretraining]] — the training process
- [[concepts/llm-training-costs]] — the economic framework
