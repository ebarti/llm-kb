---
title: "Reward Models for LLM Alignment"
source: "https://cameronrwolfe.substack.com/p/reward-models"
author: "Cameron R. Wolfe"
date_published: 2024-11-01
date_ingested: 2026-04-05
tags: [reward-model, alignment, rlhf, bradley-terry, rewardbench]
type: article
status: raw
discovered_via: search
---

# Reward Models for LLM Alignment

## Architecture
- Specialized LLMs with modified architecture
- Base: LLM decoder with added linear classification head
- Final token vector passes through linear head to produce scalar score
- Parameters typically initialized from existing policy (SFT model)

## Bradley-Terry Model Foundation
Given two completions i and j:
P(i > j) = exp(r_i)/(exp(r_i) + exp(r_j))

## Training Process
- Data: Preference datasets with (prompt, chosen, rejected) triplets
- Loss: -log(sigmoid(r_chosen - r_rejected))
- Post-training: Normalize rewards to mean zero

## Reward Model Types
1. **Classifier-based RMs**: Standard approach with linear head. Best for structured tasks.
2. **LLM-as-a-Judge**: Prompts foundation models for scores. Competitive with classifier models for frontier models.
3. **DPO models**: Implicit rewards without explicit RM. Policy becomes the reward model.
4. **Outcome Reward Models (ORMs)**: Per-token correctness probability for reasoning tasks.
5. **Process Reward Models (PRMs)**: Scores after each reasoning step. Requires step-level supervision.

## Challenges
- **Reward hacking**: RMs assign high scores to low-quality outputs through exploitation
- **Distribution mismatch**: Degrades when RL policy and RM from different model lineages
- **Complexity costs**: Separate model hosting/inference during training
- **Evaluation gap**: RM benchmark accuracy doesn't reliably predict downstream performance

## Best Practices (RewardBench)
- Data quality dominates over other factors
- Base model matters: RM performance correlates with base model capabilities
- Model lineage alignment: RM and policy should derive from same model family
- Two training epochs can outperform single epoch
- Length bias avoidance: ensure similar-length preference pairs
- Larger RMs benefit only on challenging data (reasoning, coding)

## Alternative Approaches
- **RLVR**: Uses deterministic, verifiable rewards. Eliminates RM requirement. Enables extended training without reward hacking.
- **DPO**: Aligns without explicit RM or RL via implicit reward learning.
