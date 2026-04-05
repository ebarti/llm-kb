---
title: "ThinkPRM"
type: entity
entity_type: paper
sources: ["[[sources/khalifa-thinkprm]]"]
related: ["[[concepts/process-reward-models]]", "[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]"]
last_compiled: 2026-04-05
summary: "Generative process reward model that verifies reasoning by generating verification CoT, requiring only 1% of PRM800K labels while outperforming discriminative PRMs -- extending the 'thinking' paradigm to verification."
---

## Overview

ThinkPRM (Khalifa et al., 2025) is a process reward model that evaluates reasoning steps by generating its own verification chain-of-thought, rather than producing discriminative scores. It demonstrates that the "thinking" paradigm (extended reasoning via more tokens) applies not just to solution generation but also to solution verification.

## Key Contributions

- **Generative verification**: Instead of scoring steps, ThinkPRM reasons about whether each step is correct.
- **Extreme data efficiency**: Requires only 1% of the labels in PRM800K (the standard [[concepts/process-reward-models|PRM]] training dataset).
- **Scalable verification**: Verification quality improves with more verification tokens, creating an independent axis of [[concepts/test-time-compute]] scaling.
- **Strong out-of-domain generalization**.

## Performance

- Outperforms discriminative PRMs trained on full PRM800K by 8% on GPQA-Diamond.
- Outperforms LLM-as-a-Judge by 7.2% under equivalent token budgets on ProcessBench.
- Improves LiveCodeBench by 4.5%.

## Significance

ThinkPRM creates a recursive structure: reasoning models benefit from verification, and verification benefits from reasoning. Both can scale independently at test time, suggesting a future where both generation and verification engage in extended deliberation.

## Mentioned In

- [[sources/khalifa-thinkprm]] -- the original paper
