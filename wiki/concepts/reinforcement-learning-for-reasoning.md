---
title: "Reinforcement Learning for Reasoning"
type: concept
sources: ["[[sources/adaline-inside-reasoning-models]]", "[[sources/li-system1-system2-reasoning-survey]]"]
related: ["[[concepts/reasoning-models]]", "[[concepts/process-reward-models]]", "[[concepts/llm-reasoning]]"]
last_compiled: 2026-04-05
summary: "Using RL (GRPO, PPO, scaled RL with verifiers) to train LLMs to develop reasoning capabilities -- the core training methodology behind o1, o3, and R1, enabling emergent self-verification and reasoning without supervised fine-tuning."
---

## Overview

Reinforcement learning has emerged as the primary training methodology for [[concepts/reasoning-models|reasoning models]]. Unlike supervised fine-tuning (which teaches models to imitate human reasoning traces), RL trains models to discover effective reasoning strategies through trial and error, rewarded for correct answers and penalized for incorrect ones.

The most striking result: DeepSeek R1-Zero demonstrated that pure RL (with no supervised fine-tuning at all) can produce emergent reasoning, including self-verification and error correction behaviors that were never explicitly taught.

## Key RL Methods

### Group Relative Policy Optimization (GRPO)
Used by DeepSeek R1:
- Sample multiple responses per input.
- Rank responses relative to each other (not against absolute scale).
- Update policy to favor higher-ranked responses.
- Rewards: accuracy (verified via code tests, math solvers), formatting, language consistency.

### Scaled RL with Verifiers
Used by OpenAI o3:
- Generate hundreds/thousands of candidate reasoning paths per problem.
- Evaluator model screens paths for calculation errors.
- Only verified-correct paths drive RL policy updates.
- Requires massive compute (1.2M A100 GPU hours).

### Deliberative Alignment
A safety-specific RL technique:
- Model is trained to "think through" safety considerations within its chain-of-thought.
- Fine-tuned on human feedback about safe vs. unsafe outputs.
- Achieves simultaneous improvements in safety and reasoning quality.

## The AlphaGo Parallel

The analogy to AlphaGo is frequently drawn:
- AlphaGo used RL to achieve superhuman Go play, discovering strategies no human had conceived.
- Reasoning models use RL to develop reasoning strategies beyond what supervised learning on human examples can achieve.
- Both demonstrate that RL can discover novel solutions in complex combinatorial spaces.

## Emergent Behaviors from RL

R1-Zero (pure RL, no SFT) developed several behaviors without being taught:
- **Self-verification**: Checking its own intermediate results.
- **Backtracking**: Abandoning incorrect reasoning paths.
- **Extended deliberation**: Spending more time on harder problems.
- **Error reflection**: Recognizing and correcting mistakes.

These emergent behaviors suggest RL can create genuinely novel reasoning strategies rather than just imitating human patterns.

## Training Pipeline Comparison

| Approach | DeepSeek R1 | OpenAI o3 |
|----------|-------------|-----------|
| Phase 1 | Cold start SFT (~1K samples) | Pre-training with CoT tuples |
| Phase 2 | GRPO (rule-based rewards) | Scaled RL (verifier-screened) |
| Phase 3 | Rejection sampling + SFT | Deliberative alignment |
| Phase 4 | Diverse RL (rule + LLM rewards) | -- |
| Training cost | 2.66M H800 GPU hours | 1.2M A100 GPU hours |

## Sources

- [[sources/adaline-inside-reasoning-models]] -- detailed training pipelines for o3 and R1
- [[sources/li-system1-system2-reasoning-survey]] -- RL in the taxonomy of reasoning approaches

## Related Concepts

- [[concepts/reasoning-models]] -- the systems produced by RL training
- [[concepts/process-reward-models]] -- step-level verifiers used as RL rewards
- [[concepts/llm-reasoning]] -- the capability RL develops
- [[concepts/test-time-compute]] -- inference-time techniques complementing RL training
