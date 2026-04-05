---
title: "Proximal Policy Optimization (PPO) for LLMs"
type: concept
sources: ["[[sources/huggingface-rlhf-illustrated]]", "[[sources/dpo-vs-ppo-comprehensive-study]]", "[[sources/argilla-rlhf-alternatives-overview]]"]
related: ["[[concepts/rlhf]]", "[[concepts/reward-model]]", "[[concepts/dpo]]", "[[comparisons/ppo-vs-dpo]]"]
last_compiled: 2026-04-05
summary: "The dominant RL algorithm for RLHF: a policy-gradient method using trust-region optimization to fine-tune LLMs against reward models while maintaining training stability via clipped objectives and KL penalties."
---

## Overview

Proximal Policy Optimization (PPO), originally developed by Schulman et al. (2017) at OpenAI, is the workhorse RL algorithm behind [[concepts/rlhf]]. It fine-tunes language models to maximize reward model scores while staying within a "trust region" of the current policy, preventing the catastrophic instability that plagues unconstrained RL.

PPO was chosen for RLHF not because it is optimal, but because it is well-understood, stable, and has decades of engineering tooling. Despite its age, it remains the highest-performing alignment method in comprehensive evaluations.

## How PPO Works for LLMs

### RL Formulation
- **Policy**: The language model π_θ(y|x) -- maps prompts to response distributions
- **Action space**: Vocabulary tokens (~50k tokens)
- **Reward**: Combined signal from reward model and KL penalty:
  ```
  r = r_RM(x, y) - λ · KL(π_θ || π_ref)
  ```
- **Reference policy**: Frozen copy of the initial SFT model

### The PPO Update
PPO uses a clipped surrogate objective that prevents excessively large policy updates:
```
L_CLIP = min(r_t(θ) · A_t, clip(r_t(θ), 1-ε, 1+ε) · A_t)
```
where r_t(θ) is the probability ratio between new and old policy, A_t is the advantage estimate, and ε is the clipping parameter.

This is an **on-policy** algorithm: each update uses only the current batch of prompt-generation pairs. The policy generates new text, evaluates it against the reward model, and updates.

### Required Infrastructure
PPO-based RLHF requires **four model copies** simultaneously:
1. **Policy model** (being trained)
2. **Value function** (estimates expected future reward)
3. **Reward model** (provides training signal)
4. **Reference model** (frozen, for KL penalty)

This makes it significantly more resource-intensive than offline methods like [[concepts/dpo]].

## Why PPO Outperforms DPO

Xu et al. (2024) found PPO consistently outperforms DPO across all experimental settings (see [[comparisons/ppo-vs-dpo]]). The key reasons:

1. **Online learning**: PPO generates new samples during training, allowing it to explore the response space and learn from its own mistakes. DPO is limited to a fixed dataset.
2. **Distribution robustness**: PPO handles distribution shifts between training data and the policy's current outputs. DPO is sensitive to mismatches.
3. **Complex task performance**: PPO excels on challenging tasks (code competitions, complex reasoning) where the fixed preference data in DPO may not cover edge cases.

## Challenges

- **Computational cost**: 4 model copies + generation during training = high GPU requirements
- **Hyperparameter sensitivity**: Requires tuning of learning rate, KL coefficient λ, clipping ε, batch size, and more
- **Implementation complexity**: Correct PPO-for-LLMs implementation requires RL engineering expertise
- **[[concepts/reward-hacking]]**: Extended PPO training can exploit reward model imperfections
- **Training instability**: Without careful tuning, PPO training can diverge or produce degenerate policies

## Alternatives
- **A2C**: DeepMind used Synchronous Advantage Actor-Critic for Sparrow
- **NLPO**: Natural Language Policy Optimization (Allen AI)
- **ILQL**: Implicit Language Q-Learning -- offline RL, avoiding costly forward passes
- **[[concepts/dpo]]**: Eliminates RL entirely via supervised learning

## Sources
- [[sources/huggingface-rlhf-illustrated]] -- PPO in the RLHF pipeline
- [[sources/dpo-vs-ppo-comprehensive-study]] -- PPO vs DPO empirical comparison
- [[sources/argilla-rlhf-alternatives-overview]] -- PPO as the baseline

## Related Concepts
- [[concepts/rlhf]] -- the pipeline PPO serves
- [[concepts/reward-model]] -- provides the training signal
- [[concepts/dpo]] -- the reward-free alternative
- [[comparisons/ppo-vs-dpo]] -- detailed comparison
