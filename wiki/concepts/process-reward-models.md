---
title: "Process Reward Models"
type: concept
sources: ["[[sources/lightman-lets-verify-step-by-step]]", "[[sources/snell-test-time-compute-scaling]]", "[[sources/raschka-state-of-reasoning-inference]]", "[[sources/khalifa-thinkprm]]", "[[sources/zhang-test-time-scaling-survey]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]", "[[concepts/llm-reasoning]]", "[[concepts/chain-of-thought]]"]
last_compiled: 2026-04-05
summary: "Trained verifier models that evaluate each step in a reasoning chain (not just the final answer), enabling selection of the best reasoning path -- a key building block of test-time compute scaling and reasoning models."
---

## Overview

Process Reward Models (PRMs) are specialized models trained to evaluate the quality of individual reasoning steps within a chain-of-thought solution. Unlike Outcome Reward Models (ORMs) that only judge the final answer, PRMs provide step-level feedback: each reasoning step is scored as helpful or unhelpful toward the correct solution.

PRMs were introduced by [[sources/lightman-lets-verify-step-by-step|Lightman et al. (2023)]] at OpenAI and are widely believed to be a core component of [[concepts/reasoning-models|reasoning models]] like o1 and o3.

## Process vs. Outcome Supervision

| Dimension | Outcome Supervision (ORM) | Process Supervision (PRM) |
|-----------|--------------------------|--------------------------|
| Feedback granularity | Final answer only | Each reasoning step |
| Error localization | Cannot identify where reasoning went wrong | Pinpoints exact error location |
| Interpretability | Low -- only knows if answer is right | High -- can explain why reasoning failed |
| Alignment | Rewards correct answers via any reasoning | Rewards endorsed reasoning chains |
| Data requirements | Cheaper to label (just correct/incorrect) | Requires step-level human annotation |
| Performance | Good | Significantly better (78% vs. lower on MATH) |

## How PRMs Work

1. **Training data**: Human annotators label each step in reasoning chains as correct (+) or incorrect (-). The [[sources/lightman-lets-verify-step-by-step|PRM800K dataset]] contains 800,000 such labels.
2. **Model training**: A model is fine-tuned to predict step-level correctness, learning what constitutes valid vs. flawed reasoning.
3. **Inference-time use**: When generating solutions, the PRM scores candidate reasoning paths. The path with the highest step-level scores is selected.

## Applications

### Test-Time Compute Scaling
PRMs are central to [[concepts/test-time-compute|test-time compute scaling]]:
- Generate multiple candidate solutions.
- Score each solution's reasoning steps with the PRM.
- Select the solution with the best process-level scores.
- Snell et al. (2024) showed this approach enables 4x efficiency gains and can outperform 14x larger models.

### Reinforcement Learning Training
In [[concepts/reasoning-models|reasoning model]] training (o3, R1), PRMs serve as reward signals for RL:
- OpenAI o3 uses evaluator models to screen candidate reasoning paths during RL training.
- Only paths with verified reasoning drive policy updates.

### Self-Correction
PRMs can detect errors mid-generation, enabling models to backtrack and revise reasoning steps.

## Recent Advances

- **[[sources/khalifa-thinkprm|ThinkPRM]] (2025)**: Generative PRMs that produce verification chains-of-thought, requiring only 1% of PRM800K labels while outperforming discriminative PRMs by 8% on GPQA-Diamond. Extends the "thinking" paradigm to verification itself -- verification compute can be scaled independently at test time.
- **Math-Shepherd** (2023): Automated step-level verification without human annotations.
- **Generalizable PRMs**: Using formally verified training data for broader applicability.

## Scaling Challenges

[[sources/introl-inference-time-scaling-paradigm-shift|Crosley (2025)]] notes that DeepSeek-R1 explicitly found PRMs and MCTS less effective than pure RL with extended outputs. [[sources/wu-inference-scaling-laws|Wu et al. (ICLR 2025)]] find that compute-optimal inference favors scaling solution generation more aggressively than scaling verifications. This suggests PRM-based selection is most valuable in the low-sample regime, with advantages eroding at scale (16-32+ samples).

## AI Alignment Connection

Process supervision has significant alignment implications:
- It rewards models for reasoning correctly, not just for getting right answers.
- A model that reaches the correct answer via flawed reasoning is penalized under process supervision.
- This makes reasoning more interpretable and auditable.
- It more directly enforces "thinking the right way" rather than "getting the right result."

## Sources

- [[sources/lightman-lets-verify-step-by-step]] -- the foundational paper introducing PRMs
- [[sources/snell-test-time-compute-scaling]] -- PRMs as a key mechanism for test-time compute
- [[sources/raschka-state-of-reasoning-inference]] -- PRMs in the inference-time scaling landscape

## Related Concepts

- [[concepts/test-time-compute]] -- PRMs enable efficient test-time scaling
- [[concepts/reasoning-models]] -- PRMs are a core training and inference component
- [[concepts/chain-of-thought]] -- the reasoning chains that PRMs evaluate
- [[concepts/llm-reasoning]] -- the broader capability being improved
