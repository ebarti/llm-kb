---
title: "Inside Reasoning Models: OpenAI o3 and DeepSeek R1"
source: "https://labs.adaline.ai/p/inside-reasoning-models-openai-o3"
author: "Adaline Labs"
date_published: 2025-03-01
date_ingested: 2026-04-05
tags: [reasoning-models, o3, deepseek-r1, reinforcement-learning, architecture]
type: article
status: raw
discovered_via: search
---

# Inside Reasoning Models: OpenAI o3 and DeepSeek R1

## DeepSeek R1 Training Pipeline

1. **Cold Start**: Initialize with DeepSeek-V3-Base (671B MoE parameters). SFT on ~1,000 high-quality reasoning samples.
2. **GRPO Phase**: Group Relative Policy Optimization. Samples multiple responses per input. Rewards: accuracy (validated through code tests and math verification), formatting compliance, language consistency.
3. **Rejection Sampling**: Generate 600K reasoning samples, filter for correctness and readability. Combine with 200K general-domain examples. 2 SFT epochs.
4. **Diverse RL**: Rule-based rewards for structured tasks + LLM-based reward models for human preferences.

## OpenAI o3 Training Pipeline

1. **Pre-training**: Dense transformer on vast text corpora with prompt-CoT-output tuples.
2. **Scaled RL**: Hundreds/thousands of candidate reasoning paths generated. Evaluator model screens for calculation errors. Only verified paths drive RL training.
3. **Deliberative Alignment**: Model "thinks through" chain-of-thought, checking for errors and unsafe content. Fine-tuning incorporates human feedback.
4. **Test-Time Search**: At inference, generates multiple candidate CoTs evaluated via beam search or Monte Carlo Tree Search. Selects highest-scoring result.

## Architectural Differences

- **DeepSeek R1**: Mixture-of-Experts (MoE) -- gating mechanism activates only relevant expert sub-networks. Efficient but less total context capture.
- **OpenAI o3**: Dense transformer -- all parameters active during processing. Full context capture at higher computational cost.
- **Key difference**: o3 uses "hidden chains of thought" via test-time search; R1 has "explicit CoT visible to users."

## Benchmark Performance

| Benchmark | DeepSeek R1 | OpenAI o3 |
|-----------|------------|-----------|
| AIME 2024 | 79.8% | ~96.7% |
| MATH-500 | 97.3% | >97% |
| Codeforces ELO | ~2000 | ~2727 |
| GPQA Diamond | ~75% | ~87.7% |
| SWE-bench | ~49% | 71.7% |

## Computational Costs

- o3 CoT generation: 3-5x token overhead vs. direct answers.
- o3 training: 1.2M A100 GPU hours.
- DeepSeek R1 training: 2.66M H800 GPU hours.
- o3 high-reasoning mode latency: 7.7 seconds for 100K-token outputs.

## RL as Foundation

"The future of reasoning models will be heavily dependent on Reinforcement Learning." Parallels drawn to AlphaGo's 2016 victory -- RL enables human-level performance in complex domains.

## Limitations

- Simple queries receive unnecessarily resource-intensive reasoning.
- Safety alignment can reduce accuracy (R1's Chinese SimpleQA dropped 12% post-safety RL).
- Multi-turn dialogues fragment logical flow despite 200K-token context windows.
