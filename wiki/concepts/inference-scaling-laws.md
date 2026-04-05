---
title: "Inference Scaling Laws"
type: concept
sources: ["[[sources/wu-inference-scaling-laws]]", "[[sources/roberts-train-to-test-scaling-laws]]", "[[sources/snell-test-time-compute-scaling]]", "[[sources/agarwal-art-of-scaling-test-time-compute]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/scaling-laws]]", "[[concepts/training-vs-inference-compute]]", "[[concepts/adaptive-compute-allocation]]", "[[concepts/best-of-n-sampling]]"]
last_compiled: 2026-04-05
summary: "Formal mathematical relationships governing how LLM performance scales with inference-time compute -- the deployment-side counterpart to Chinchilla training scaling laws, establishing inference compute as an independently optimizable axis."
---

## Overview

Inference scaling laws describe how LLM performance improves as more computation is allocated at inference time. They are the deployment-side counterpart to training scaling laws ([[concepts/scaling-laws|Chinchilla]], Kaplan et al.), establishing that inference compute is an independent, optimizable axis of AI system design.

## The Core Equation

[[sources/wu-inference-scaling-laws|Wu et al. (ICLR 2025)]] establish the empirical relationship:

**log10(C) = 1.19 * log10(N) + 2.03**

where C is the compute-optimal inference FLOPs and N is the model size. This allows estimation of optimal inference compute allocation for a given model.

## Key Results

### Smaller Models Can Win
Llemma-7B with a novel tree search algorithm consistently outperforms Llemma-34B across all inference strategies on the MATH benchmark. The computational resources are better invested in inference algorithms than in model parameter scaling alone.

### Adaptive Allocation
A compute-optimal strategy that allocates test-time compute per prompt based on difficulty achieves **4x efficiency improvement** over uniform [[concepts/best-of-n-sampling|best-of-N]] allocation ([[sources/snell-test-time-compute-scaling|Snell et al., 2024]]).

### Generation Over Verification
Compute-optimal inference favors scaling solution generation more aggressively than scaling the number of verifications. The bottleneck is diversity of solutions, not verification quality.

### No Universal Strategy
[[sources/agarwal-art-of-scaling-test-time-compute|Agarwal et al. (2025)]] show no single strategy universally dominates -- the optimal approach depends on problem difficulty, model type, and compute budget.

## Train-to-Test (T2) Scaling Laws

[[sources/roberts-train-to-test-scaling-laws|Roberts et al. (2026)]] bridge the gap between training and inference scaling:

- Jointly optimize model size, training tokens, and inference samples under one budget.
- **Key insight**: When inference costs are accounted for, optimal training shifts into heavy **overtraining** of smaller models.
- A 7B model trained 5x beyond Chinchilla optimum + test-time sampling outperforms a Chinchilla-optimal 34B model.

This has immediate practical implications: labs planning to deploy with [[concepts/test-time-compute]] should train smaller, more overtrained models.

## Relationship to Training Scaling Laws

| Dimension | Training Scaling (Chinchilla) | Inference Scaling (Wu et al.) | Joint (T2, Roberts et al.) |
|-----------|------------------------------|-------------------------------|---------------------------|
| Optimizes | Model size + training tokens | Inference compute + strategy | All three jointly |
| Key insight | Scale data and params equally | Inference compute is independently optimizable | Overtraining becomes optimal |
| Published | 2022 | 2024/2025 | 2026 |

## Open Questions

- How do inference scaling laws change with post-training (RLHF, DPO)?
- Do inference scaling laws transfer across domains, or are they domain-specific?
- What is the interaction between inference scaling and model architecture (MoE vs. dense)?

## Sources

- [[sources/wu-inference-scaling-laws]] -- ICLR 2025 foundational paper
- [[sources/roberts-train-to-test-scaling-laws]] -- T2 joint training-inference laws
- [[sources/snell-test-time-compute-scaling]] -- adaptive allocation results
- [[sources/agarwal-art-of-scaling-test-time-compute]] -- large-scale empirical validation

## Related Concepts

- [[concepts/test-time-compute]] -- the paradigm these laws govern
- [[concepts/scaling-laws]] -- the training-side counterpart (Chinchilla)
- [[concepts/training-vs-inference-compute]] -- the macro paradigm shift
- [[concepts/adaptive-compute-allocation]] -- optimal allocation strategies
- [[concepts/best-of-n-sampling]] -- baseline inference scaling technique
