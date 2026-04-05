---
title: "Scaling Laws"
type: concept
sources: ["[[sources/chinchilla-scaling-laws]]", "[[sources/scaling-laws-data-quality]]", "[[sources/dclm-datacomp-language-models]]", "[[sources/synthetic-data-llm-pretraining-study]]", "[[sources/nemotron-cc-nvidia]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/mixture-of-experts]]", "[[concepts/training-data-curation]]", "[[concepts/data-quality-bottleneck]]", "[[entities/chinchilla]]"]
last_compiled: 2026-04-05
summary: "Mathematical relationships between model size, dataset size, compute budget, and (recently) data quality that predict LLM performance — from the original Kaplan/Chinchilla laws to quality-aware extensions."
---

## Overview

Scaling laws describe predictable mathematical relationships between training resources and model performance. They enable practitioners to forecast the performance of large, expensive training runs from smaller proxy experiments — a critical capability when frontier training runs cost tens of millions of dollars.

## Historical Development

### Kaplan Scaling Laws (2020)

OpenAI's initial work established that LLM loss follows power laws in model size (N), dataset size (D), and compute (C):

L(N) ~ N^(-0.076)
L(D) ~ D^(-0.095)
L(C) ~ C^(-0.050)

These suggested that model size matters more than data size for a fixed compute budget.

### Chinchilla Scaling Laws (2022)

DeepMind's [[entities/chinchilla]] work revised these relationships, finding that model parameters and training tokens should scale equally for compute-optimal training. The rule of thumb: ~20 tokens per parameter. A 70B model should train on ~1.4T tokens.

This had enormous practical impact — it showed that many existing models (including the original GPT-3) were significantly undertrained relative to their parameter count.

### Quality-Aware Scaling Laws (2025)

[[sources/scaling-laws-data-quality]] extends Chinchilla by adding an explicit data quality parameter:

**L(N,D,Q) = A/N^alpha + B/(D^beta * Q^gamma) + E**

Where Q is a dimensionless quality measure in (0,1]. Key findings:

- gamma ≈ 0.17 for machine translation, ~0.40 for causal language modeling
- Models are more robust to moderate quality corruption than naive theory predicts (sublinear decay)
- When data is high-quality, additional compute is best spent on larger models
- When data is low-quality, no amount of model scaling compensates

## Scaling Laws for Synthetic Data

[[sources/synthetic-data-llm-pretraining-study]] establishes separate scaling dynamics for synthetic data:

- Pure synthetic data is NOT superior to natural web data at any tested scale
- Mixtures (30% synthetic + 70% natural) substantially outperform either pure source
- Synthetic data benefits are stronger for data scaling than model scaling
- Larger models show reduced tolerance for high synthetic data ratios

## Transfer Across Scales

A critical practical finding from [[sources/dclm-datacomp-language-models]]: dataset quality rankings are remarkably consistent across model scales, with Pearson correlations of 0.885-0.919 between small (400M-1B) and large (7B) experiments. This means researchers can evaluate curation strategies at 1/100th the cost of frontier-scale experiments.

## Practical Implications

1. **Compute allocation**: with high-quality data, invest in model size; with noisy data, invest in curation first
2. **Proxy experiments**: small-scale curation experiments reliably predict large-scale outcomes
3. **Data vs parameters**: Chinchilla showed equal scaling; quality-aware laws show quality can shift the optimal ratio
4. **Diminishing returns**: each domain (model scale, data scale, data quality) has diminishing returns — optimization requires balancing all three

## Sources

- [[sources/scaling-laws-data-quality]] — quality-aware extension of Chinchilla
- [[sources/dclm-datacomp-language-models]] — cross-scale transfer of quality rankings
- [[sources/synthetic-data-llm-pretraining-study]] — scaling laws for synthetic data mixtures
- [[sources/nemotron-cc-nvidia]] — long-horizon scaling requires different curation strategy

## Related Concepts

- [[concepts/training-data-curation]] — quality as the highest-leverage scaling factor
- [[concepts/data-quality-bottleneck]] — quality as a binding constraint
- [[entities/chinchilla]] — the foundational compute-optimal scaling work
- [[concepts/synthetic-data-in-pretraining]] — synthetic data has different scaling dynamics
