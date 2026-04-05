---
title: "Source: Illustrating Reinforcement Learning from Human Feedback (RLHF)"
type: source-summary
source: "[[raw/huggingface-rlhf-illustrated]]"
related: ["[[concepts/rlhf]]", "[[concepts/reward-model]]", "[[concepts/preference-data]]", "[[concepts/ppo-for-llms]]", "[[entities/instructgpt]]"]
last_compiled: 2026-04-05
summary: "HuggingFace's foundational RLHF tutorial covering the three-step pipeline (pretrain, reward model, PPO fine-tuning), with practical guidance on data collection, KL penalties, and open-source tooling."
---

## Key Points
- RLHF aligns LLMs with human preferences through a three-step pipeline: pretraining, reward model training on human preference data, and RL fine-tuning with PPO
- The reward model converts pairwise human rankings into scalar preference scores using the Bradley-Terry model
- A KL divergence penalty prevents the policy from diverging too far from the reference model, avoiding reward exploitation
- Typical scale: ~50k labeled preference samples for reward model training
- PPO uses trust-region optimization with gradient constraints to prevent training destabilization

## Detailed Summary

The article provides the canonical walkthrough of the RLHF pipeline as applied to large language models. The process begins with a pretrained language model (e.g., GPT-3 scale) that is optionally fine-tuned on curated instruction data.

In the second step, a [[concepts/reward-model]] is trained. Human annotators compare multiple model outputs for a given prompt and rank them by preference. These rankings are normalized into scalar rewards using the [[concepts/bradley-terry-model]]. Architecture choices vary: OpenAI used a 6B reward model for a 175B LM, while [[entities/anthropic]] used matched sizes (10B-52B) and introduced Preference Model Pretraining (PMP) for better sample efficiency.

The third step applies [[concepts/ppo-for-llms]] to fine-tune the language model. The reward function combines the preference model's score with a KL divergence penalty: `r = r_θ - λ * r_KL`. The KL term compares per-token probability distributions between the RL policy and the frozen reference model, preventing the policy from generating gibberish that exploits the reward model.

The article highlights open-source tools: TRL (HuggingFace), TRLX (CarperAI, for 33B+ models), and RL4LMs (Allen AI, supporting PPO, NLPO, A2C, TRPO).

## Notable Quotes
> "Human annotators rank outputs (not score them directly)" -- emphasizing that relative rankings are more reliable than absolute scores
> "Without KL penalty, model generates gibberish maximizing reward" -- the critical role of regularization

## Related Concepts
- [[concepts/rlhf]] -- this is the definitive tutorial on the technique
- [[concepts/reward-model]] -- detailed coverage of architecture and training
- [[concepts/preference-data]] -- discussion of data collection methodology
- [[concepts/ppo-for-llms]] -- PPO as the RL algorithm of choice
- [[concepts/reward-hacking]] -- identified as a key challenge
