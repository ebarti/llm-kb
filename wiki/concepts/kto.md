---
title: "Kahneman-Tversky Optimization (KTO)"
type: concept
sources: ["[[sources/argilla-kto-kahneman-tversky]]", "[[sources/argilla-rlhf-alternatives-overview]]"]
related: ["[[concepts/dpo]]", "[[concepts/rlhf]]", "[[concepts/preference-data]]", "[[concepts/prospect-theory-in-alignment]]", "[[comparisons/rlhf-alternatives]]"]
last_compiled: 2026-04-05
summary: "A prospect-theory-based alignment method that uses binary desirable/undesirable signals instead of pairwise preferences, outperforming DPO on noisy real-world data and matching SFT+DPO combined on Llama models."
---

## Overview

Kahneman-Tversky Optimization (KTO), introduced by Ethayarajh et al. (2024), takes a fundamentally different approach to preference optimization. Instead of modeling preferences through the [[concepts/bradley-terry-model]] (as in [[concepts/rlhf]] and [[concepts/dpo]]), KTO grounds its loss function in **prospect theory** -- the Nobel Prize-winning model of how humans actually evaluate gains and losses.

The key insight: humans are **loss-averse**. The pain of a loss is felt more strongly than the pleasure of an equivalent gain. KTO incorporates this asymmetry into the alignment objective, producing a method that is more robust to noisy, real-world data.

## The HALO Framework

KTO emerged from the HALO (Human-Aware Loss functions) framework, which classifies alignment methods by whether they model human cognitive biases:

- **HALOs** (like KTO): Model human decision-making biases (loss aversion, reference dependence)
- **Non-HALOs** (like DPO): Use idealized preference models (Bradley-Terry)

At 13B+ parameters, HALOs matched or outperformed non-HALOs, suggesting that accounting for human psychology improves alignment.

## How KTO Works

### Data Requirements
KTO requires only **binary feedback**: each response is labeled as either desirable (+1) or undesirable (-1). No pairwise comparisons needed.

This is a dramatic simplification over DPO (which requires preference pairs) and is far cheaper to collect:
- Thumbs up/down buttons are ubiquitous in deployed systems
- Binary signals are more abundant than pairwise comparisons
- Works well even with **imbalanced data** (e.g., 1:10 desirable:undesirable ratio)

### Loss Function
KTO directly maximizes the **utility** of generations using Kahneman-Tversky value functions rather than maximizing the log-likelihood of preferences. Key components:
- A KL penalty that rises when the model increases reward for desirable examples generically (prevents learning a trivial "everything is good" policy)
- Asymmetric weighting of desirable vs. undesirable examples, reflecting loss aversion
- Forces the model to learn what specifically makes outputs desirable

## Key Results

| Finding | Detail |
|---------|--------|
| **Data efficiency** | KTO-aligned Llama-7B outperformed DPO even with 90% of desirable examples discarded |
| **Without SFT** | DPO models rambled and hallucinated; KTO remained stable |
| **Matching combined methods** | KTO alone matched SFT + DPO combined on Llama models |
| **Noise robustness** | Better than DPO on noisy, publicly available datasets |
| **Scale independence** | Superior or comparable to DPO across 1B-30B parameters |

## When to Use KTO vs. DPO

| Scenario | Recommended |
|----------|-------------|
| Binary feedback available (thumbs up/down) | **KTO** |
| Noisy, real-world datasets | **KTO** |
| No prior SFT step | **KTO** |
| Imbalanced desirable/undesirable data | **KTO** |
| Clean, transitive preference pairs | **DPO** |
| Risk of underfitting is a concern | **DPO** |
| High-quality curated preference datasets | **DPO** |

The key theoretical insight: DPO works better with clean, transitive data, but KTO's worst-case guarantees excel when noise is present -- which matches most real-world deployment scenarios.

## Sources
- [[sources/argilla-kto-kahneman-tversky]] -- detailed overview and experimental results
- [[sources/argilla-rlhf-alternatives-overview]] -- KTO in the landscape of methods

## Related Concepts
- [[concepts/dpo]] -- the primary comparison point
- [[concepts/rlhf]] -- the baseline method
- [[concepts/preference-data]] -- KTO's relaxed data requirements
- [[concepts/prospect-theory-in-alignment]] -- the theoretical foundation
- [[comparisons/rlhf-alternatives]] -- systematic method comparison
