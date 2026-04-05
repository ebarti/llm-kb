---
title: "Source: Scaling Laws Revisited — The Role of Data Quality"
type: source-summary
source: "[[raw/scaling-laws-data-quality]]"
related: ["[[concepts/scaling-laws]]", "[[concepts/training-data-curation]]", "[[concepts/data-quality-bottleneck]]", "[[entities/chinchilla]]"]
last_compiled: 2026-04-05
summary: "Extends Chinchilla scaling laws with an explicit data quality parameter Q, showing that high-quality data reduces required model size and that quality sensitivity varies by task (gamma 0.17-0.40)."
---

## Key Points

- Proposes quality-aware scaling law: L(N,D,Q) = A/N^alpha + B/(D^beta * Q^gamma) + E
- Q is a dimensionless quality parameter in (0,1] where 1 = fully clean data
- Derived from both effective sample size and information-theoretic perspectives
- Empirical gamma values: ~0.17 (machine translation), ~0.40 (causal language modeling) — models are more robust to moderate corruption than naive theory predicts
- Higher data quality means compute budget should shift toward model scaling
- A billion high-quality tokens can be far more valuable than a billion noisy ones
- Provides a practitioner recipe for estimating Q in real datasets

## Detailed Summary

The [[entities/chinchilla]] scaling laws established that model parameters and training tokens should scale equally for compute-optimal training (~20 tokens per parameter). However, they treated all tokens as equivalent, which the real world violates dramatically.

This work formalizes data quality as a first-class variable in scaling laws. The quality parameter Q modulates the effective dataset size: noisy data behaves as if the dataset were smaller. Two theoretical derivations converge on the same functional form — one from effective sample size reduction, one from information-theoretic mutual information degradation under corruption.

The key practical implication is asymmetric: when data is high-quality, additional compute is best spent on larger models rather than more data. When data is low-quality, no amount of model scaling compensates — quality must be improved first. This provides quantitative backing for the intuition that [[concepts/data-quality-bottleneck]] is often more binding than compute constraints.

## Notable Quotes

> "A billion high-quality tokens may be far more valuable than a billion noisy or redundant ones."

## Related Concepts

- [[concepts/scaling-laws]] — this paper directly extends the Chinchilla framework
- [[concepts/data-quality-bottleneck]] — quantitative evidence that quality dominates scale
- [[concepts/training-data-curation]] — quality estimation as a prerequisite for optimal training
