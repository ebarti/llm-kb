---
title: "Reinforcement Learning from Human Feedback (RLHF)"
type: concept
sources: ["[[sources/huggingface-rlhf-illustrated]]", "[[sources/argilla-rlhf-alternatives-overview]]", "[[sources/dpo-vs-ppo-comprehensive-study]]", "[[sources/wolfe-reward-models-llm]]", "[[sources/rlhf-preference-data-collection]]"]
related: ["[[concepts/reward-model]]", "[[concepts/ppo-for-llms]]", "[[concepts/dpo]]", "[[concepts/constitutional-ai]]", "[[concepts/rlaif]]", "[[concepts/preference-data]]", "[[concepts/reward-hacking]]", "[[concepts/ai-alignment]]"]
last_compiled: 2026-04-05
summary: "The dominant technique for aligning LLMs with human preferences: train a reward model on human preference data, then fine-tune the LLM using PPO to maximize that reward while staying close to the reference policy."
---

## Overview

Reinforcement Learning from Human Feedback (RLHF) is the technique that transformed raw language models into useful assistants like ChatGPT, Claude, and Gemini. It bridges the gap between a model that predicts the next token and one that produces outputs humans actually prefer -- helpful, harmless, and honest responses rather than merely statistically likely text.

The core insight is that human preferences are easier to express through comparison ("response A is better than response B") than through explicit reward functions. RLHF collects these comparisons, distills them into a [[concepts/reward-model]], and uses reinforcement learning to steer the language model toward higher-reward outputs.

## The Three-Step Pipeline

### Step 1: Supervised Fine-Tuning (SFT)
Begin with a pretrained language model and fine-tune it on high-quality instruction-following demonstrations. This produces a model that can follow instructions but may not align with nuanced human preferences. SFT establishes the behavioral foundation that RLHF refines.

### Step 2: Reward Model Training
Collect [[concepts/preference-data]] by having human annotators compare pairs of model outputs and indicate which is better. Train a [[concepts/reward-model]] to predict these preferences, converting relative rankings into scalar scores via the [[concepts/bradley-terry-model]]:

```
P(y_w > y_l) = σ(r(x, y_w) - r(x, y_l))
Loss = -log(sigmoid(r_chosen - r_rejected))
```

Typical scale: ~50k labeled preference samples. The reward model is often a smaller LLM (e.g., OpenAI used 6B for a 175B policy) with a linear head replacing the language modeling head.

### Step 3: RL Fine-Tuning with PPO
Use [[concepts/ppo-for-llms]] to fine-tune the language model against the reward model. The optimization objective balances reward maximization with staying close to the original model:

```
r = r_θ(x, y) - λ · KL(π_θ || π_ref)
```

The KL divergence penalty is critical: without it, the model degenerates into producing gibberish that exploits the reward model (see [[concepts/reward-hacking]]). The frozen reference policy `π_ref` anchors the optimization.

## Why RLHF Works

1. **Preference comparison is natural**: Humans find it much easier to say "A is better than B" than to assign absolute quality scores
2. **Captures tacit knowledge**: Many preferences (tone, helpfulness, safety) are hard to specify in rules but easy to demonstrate through comparison
3. **Iterative refinement**: The model generates, humans evaluate, the reward model updates, and the policy improves in a virtuous cycle

## Key Challenges

- **Cost**: Human preference annotation is expensive (~$10-50/hour for annotators, requiring 50K+ comparisons)
- **Annotator disagreement**: Humans disagree on preferences, adding variance without ground truth
- **[[concepts/reward-hacking]]**: The policy can exploit imperfections in the reward model, achieving high proxy reward while actual quality degrades
- **Complexity**: PPO requires 4 model copies (policy, value function, reward model, reference) and careful hyperparameter tuning
- **Scaling**: As models grow, the RL optimization becomes increasingly expensive and unstable

## Historical Development

| Year | Milestone |
|------|-----------|
| 2017 | Christiano et al. -- Deep RL from Human Preferences (Atari) |
| 2019 | Ziegler et al. -- Fine-Tuning LMs from Human Preferences |
| 2020 | Stiennon et al. -- Learning to Summarize with Human Feedback |
| 2022 | [[entities/instructgpt]] (OpenAI) -- first major RLHF success on LLMs |
| 2022 | [[entities/anthropic]] -- Training a Helpful and Harmless Assistant |
| 2022 | DeepMind Sparrow -- targeted human judgements for dialogue |
| 2023 | Meta Llama 2 -- detailed RLHF at scale (>1M human annotations) |
| 2023 | [[concepts/dpo]] -- reward-free alternative achieves comparable results |

## Alternatives and Evolution

RLHF spawned a family of alignment techniques that simplify, extend, or replace its components:

- **[[concepts/dpo]]**: Eliminates the reward model and RL entirely via implicit reward learning
- **[[concepts/kto]]**: Uses binary signals instead of pairwise preferences, grounded in prospect theory
- **[[concepts/constitutional-ai]]**: Replaces human harmlessness labels with AI feedback
- **[[concepts/rlaif]]**: Fully automates preference annotation using LLMs
- **[[concepts/orpo]]**: Combines SFT and preference alignment in a single step
- **RLVR**: Uses verifiable rewards (e.g., code correctness) to eliminate the reward model

The trend is toward simpler, more efficient methods -- but PPO-based RLHF remains the gold standard for production systems requiring maximum performance (see [[comparisons/ppo-vs-dpo]]).

## Sources
- [[sources/huggingface-rlhf-illustrated]] -- definitive RLHF tutorial with pipeline details
- [[sources/argilla-rlhf-alternatives-overview]] -- positions RLHF among 9+ alternatives
- [[sources/dpo-vs-ppo-comprehensive-study]] -- empirical evidence for PPO's superiority
- [[sources/wolfe-reward-models-llm]] -- deep dive into the reward model component

## Related Concepts
- [[concepts/reward-model]] -- the learned preference function at RLHF's core
- [[concepts/ppo-for-llms]] -- the RL algorithm used in step 3
- [[concepts/preference-data]] -- the human feedback that drives everything
- [[concepts/ai-alignment]] -- the broader goal RLHF serves
- [[concepts/reward-hacking]] -- the primary failure mode
- [[concepts/instruction-tuning]] -- the SFT step that precedes RLHF
