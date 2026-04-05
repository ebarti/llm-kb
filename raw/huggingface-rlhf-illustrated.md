---
title: "Illustrating Reinforcement Learning from Human Feedback (RLHF)"
source: "https://huggingface.co/blog/rlhf"
author: "Nathan Lambert, Louis Castricato, Leandro von Werra, Alex Havrilla"
date_published: 2022-12-09
date_ingested: 2026-04-05
tags: [rlhf, alignment, reinforcement-learning, reward-model, ppo, human-feedback]
type: article
status: raw
discovered_via: search
---

# Illustrating Reinforcement Learning from Human Feedback (RLHF)

## Three-Step RLHF Pipeline

### 1. Pretraining Language Models
- Start with a pretrained language model using classical pretraining objectives (next-token prediction with cross-entropy loss)
- Examples: OpenAI used smaller GPT-3, Anthropic used 10M-52B parameter models, DeepMind used up to 280B parameter Gopher
- Optional: Fine-tune on augmented data (human-generated text or context clues)
- Critical requirement: Model must respond well to diverse instructions

### 2. Reward Model Training
The reward model (preference model) takes text sequences and returns a scalar reward representing human preference.

**Architecture Choices:**
- Can be a fine-tuned LM or LM trained from scratch on preference data
- Varying sizes relative to generation LM (e.g., OpenAI: 175B LM with 6B reward model; Anthropic: 10B-52B for both)
- Anthropic used Preference Model Pretraining (PMP) for improved sample efficiency

**Data Collection:**
- Sample prompts from predefined datasets (e.g., Amazon Mechanical Turk, user API submissions)
- Generate multiple text outputs from the base LM for each prompt
- Human annotators rank outputs (not score them directly)

**Ranking Methodology:**
- Head-to-head comparison: Compare outputs from two models on the same prompt
- Elo ranking system: Use matchup results to generate relative rankings and ratings
- Normalization: Convert rankings into scalar reward signal for training
- Avoids uncalibrated/noisy individual scores from varying human values

**Training Dataset Scale:**
- Typically ~50k labeled preference samples
- Only one large-scale general dataset: Anthropic's hh-rlhf

### 3. Fine-Tuning with Reinforcement Learning (PPO)

**Policy**: Language model that takes a prompt and returns token sequence probability distributions

**Action Space**: Vocabulary tokens (~50k tokens typically)

**Reward Function**: Combined metric:
```
r = r_θ - λ * r_KL
where:
- r_θ = scalar reward from preference model
- r_KL = KL divergence penalty
- λ = scaling coefficient
```

**KL Divergence Penalty:**
- Compares per-token probability distributions between RL policy and initial pretrained model (frozen reference)
- Penalizes substantial policy deviation from original model
- Prevents reward model exploitation (generating gibberish that fools reward but produces incoherent text)

**PPO Update Rule:**
- Proximal Policy Optimization: policy-gradient RL algorithm
- On-policy: Parameters updated only with current batch of prompt-generation pairs
- Trust region optimization using gradient constraints to prevent training destabilization

## Open-Source Tools
- TRL (Transformers Reinforcement Learning): Fine-tune pretrained LMs with PPO in Hugging Face ecosystem
- TRLX: Fork by CarperAI for larger models (33B+)
- RL4LMs (Allen AI): Building blocks including PPO, NLPO, A2C, TRPO

## Key Challenges
- Expensive human annotation
- Annotator disagreement adds variance
- Reward model overoptimization
- KL divergence tuning complexity
- Models still output harmful or factually inaccurate text
- Scaling properties of preference models not fully understood

## Foundational Papers
- Christiano et al. (2017): Deep Reinforcement Learning from Human Preferences
- Zieglar et al. (2019): Fine-Tuning Language Models from Human Preferences
- Stiennon et al. (2020): Learning to summarize with human feedback
- OpenAI (2022): InstructGPT
- Anthropic (2022): Training a Helpful and Harmless Assistant with RLHF
- DeepMind (2022): Sparrow
