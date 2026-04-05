---
title: "Bradley-Terry Model"
type: concept
sources: ["[[sources/wolfe-direct-preference-optimization]]", "[[sources/wolfe-reward-models-llm]]", "[[sources/huggingface-rlhf-illustrated]]"]
related: ["[[concepts/reward-model]]", "[[concepts/rlhf]]", "[[concepts/dpo]]", "[[concepts/preference-data]]"]
last_compiled: 2026-04-05
summary: "The statistical model underlying both RLHF reward models and DPO: converts pairwise preference comparisons into probability estimates via the sigmoid of reward differences."
---

## Overview

The Bradley-Terry model (1952) is the statistical foundation that connects human preference judgments to trainable reward functions in LLM alignment. It provides the mathematical bridge between "humans prefer response A over response B" and a scalar reward model that can be optimized with RL.

## The Model

Given two items i and j with strengths (rewards) r_i and r_j, the probability that i is preferred over j is:

```
P(i > j) = exp(r_i) / (exp(r_i) + exp(r_j)) = σ(r_i - r_j)
```

where σ is the sigmoid function. This elegantly converts scalar reward differences into preference probabilities.

## Application in LLM Alignment

### Reward Model Training
The [[concepts/reward-model]] loss function derives directly from the Bradley-Terry model:
```
Loss = -log(sigmoid(r_chosen - r_rejected))
```
This is minimized when the reward model correctly assigns higher scores to human-preferred responses.

### DPO Derivation
[[concepts/dpo]] reparameterizes the reward as an implicit function of policy probabilities, then plugs this into the Bradley-Terry model. The partition function Z(x) cancels in pairwise comparisons, yielding a clean supervised loss.

### Preference Data Interpretation
The model assumes preferences follow a logistic distribution -- items with higher "strength" are preferred more often, but not deterministically. This captures the reality that human preferences are noisy and probabilistic.

## Limitations

- Assumes transitivity (if A > B and B > C, then A > C), which human preferences sometimes violate
- Assumes independence of irrelevant alternatives (adding a third option doesn't change the A vs B probability)
- [[concepts/kto]] argues these assumptions are too idealized and proposes prospect theory instead

## Sources
- [[sources/wolfe-direct-preference-optimization]] -- Bradley-Terry in DPO derivation
- [[sources/wolfe-reward-models-llm]] -- Bradley-Terry for reward model training
- [[sources/huggingface-rlhf-illustrated]] -- Bradley-Terry in the RLHF pipeline

## Related Concepts
- [[concepts/reward-model]] -- trained using Bradley-Terry loss
- [[concepts/dpo]] -- reparameterizes Bradley-Terry with implicit rewards
- [[concepts/preference-data]] -- the data Bradley-Terry models
- [[concepts/kto]] -- prospect-theory alternative to Bradley-Terry
