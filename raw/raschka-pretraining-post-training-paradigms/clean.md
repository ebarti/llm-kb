---
title: "New LLM Pre-training and Post-training Paradigms"
source: "https://magazine.sebastianraschka.com/p/new-llm-pre-training-and-post-training"
author: "Sebastian Raschka"
date_published: 2024-09-01
date_ingested: 2026-04-05
tags: [pretraining, post-training, qwen, llama, gemma, apple-afm, multi-stage-training, knowledge-distillation]
type: article
status: raw
discovered_via: search
---

# New LLM Pre-training and Post-training Paradigms

## Models Analyzed

### Alibaba's Qwen 2
- 7 trillion tokens, four dense model sizes (0.5B, 1.5B, 7B, 72B) plus MoE variant
- 151,642-token vocabulary, 30 languages
- Two-stage pre-training: regular + long-context (4,096 to 32,768 tokens)
- Used previous-gen Qwen models to synthesize additional training data
- Post-training: SFT on 500K examples (2 epochs) + DPO (offline and online)

### Apple Intelligence Foundation Models (AFM)
- 3B device model + larger server model
- Three-stage pre-training:
  1. Core: 6.3 trillion tokens
  2. Continued: 1 trillion tokens with down-weighted web, up-weighted math/code
  3. Context lengthening: 100 billion tokens with synthetic long-context data
- Smaller model used knowledge distillation from 6.4B teacher
- Post-training: rejection sampling fine-tuning + mirror descent policy optimization

### Google's Gemma 2
- 2B, 9B, 27B configurations
- 27B trained on 13 trillion tokens from scratch
- Smaller variants used knowledge distillation
- Reward model 10x larger than policy model
- WARP (weight-averaged reward models) for policy averaging

### Meta's Llama 3.1
- 405B model + 8B and 70B
- 15.6 trillion token dataset (up from 2T in Llama 2)
- Three-stage pre-training: standard (8k context) -> gradual context lengthening (6 stages to 128k) -> annealing on high-quality benchmarks
- Post-training: iterative SFT + DPO with model averaging

## Emerging Trends

1. Data Quality Over Quantity: All models emphasize filtering and curation
2. Multi-Stage Pre-training: Initial pre-training + context extension + quality annealing
3. Knowledge Distillation: Larger teachers improve smaller variants
4. Preference Optimization: DPO and rejection sampling largely replacing pure RLHF/PPO
5. Synthetic Data: Previous-gen LLMs generate training data
6. Model Averaging: Merging checkpoints to stabilize and improve performance
