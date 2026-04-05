---
title: "Identity Preference Optimization (IPO)"
type: concept
sources: ["[[sources/argilla-rlhf-alternatives-overview]]"]
related: ["[[concepts/dpo]]", "[[concepts/rlhf]]", "[[concepts/kto]]", "[[comparisons/rlhf-alternatives]]"]
last_compiled: 2026-04-05
summary: "A DPO variant that replaces logit functions with identity functions and adds regularization to prevent overfitting -- addressing DPO's tendency to overfit preference data, especially with deterministic preferences."
---

## Overview

Identity Preference Optimization (IPO), along with the related ΨPO framework (Azar et al., 2023), was introduced to address theoretical weaknesses in [[concepts/dpo]]. The IPO paper provides a unifying theoretical framework explaining [[concepts/rlhf]] and DPO through ΨPO, then highlights their shortcomings.

## Key Innovation

IPO replaces logit functions with identity functions in the preference optimization objective and adds an explicit **regularization term** to avoid overfitting. This addresses DPO's tendency to overfit the training preference data, particularly when preference signals are strong or deterministic.

## When to Use IPO

- When preferences in the data are close to deterministic (clear right/wrong answers)
- When DPO shows signs of overfitting (loss continues decreasing but performance degrades)
- When theoretical guarantees about regularization are important

HuggingFace experiments showed mixed results: IPO benefited the Zephyr model but showed different conclusions for OpenHermes, suggesting the advantage is model-dependent.

## Sources
- [[sources/argilla-rlhf-alternatives-overview]] -- IPO in the landscape of methods

## Related Concepts
- [[concepts/dpo]] -- the method IPO improves upon
- [[concepts/kto]] -- another DPO alternative with different assumptions
- [[comparisons/rlhf-alternatives]] -- systematic comparison
