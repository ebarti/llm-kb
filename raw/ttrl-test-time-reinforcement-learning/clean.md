---
title: "TTRL: Test-Time Reinforcement Learning"
source: "https://arxiv.org/abs/2504.16084"
author: "Yuxin Zuo, Kaiyan Zhang et al."
date_published: 2025-04-22
date_ingested: 2026-04-05
tags: [test-time-compute, reinforcement-learning, test-time-training, adaptation, reasoning]
type: paper
status: raw
discovered_via: search
---

# TTRL: Test-Time Reinforcement Learning

NeurIPS 2025 paper introducing a method for RL training on unlabeled test data.

## Core Problem
How to perform reinforcement learning at test time when ground-truth labels are unavailable.

## Method
TTRL combines Test-Time Scaling (TTS) and Test-Time Training (TTT):
1. Generate multiple candidate solutions from the model.
2. Use majority voting to determine which answers are likely correct.
3. Use this consensus as a reward signal for RL policy optimization.
4. The model evolves using its own priors from pre-training.

## Key Insight
Common TTS practices like majority voting yield surprisingly effective rewards suitable for driving RL training, even without ground-truth labels.

## Results
- **211% performance boost** for Qwen-2.5-Math-7B on AIME 2024 using only unlabeled test data.
- Performance surpasses the initial model's majority voting ceiling (maj@n metric upper limit).
- Results approach performance levels achieved with supervised learning from labeled data.
- Consistent improvements across a variety of tasks and models.

## Significance
TTRL enables self-evolution of LLMs by utilizing the priors in pre-trained models, suggesting broader applicability across diverse reasoning tasks without requiring expensive labeled datasets for adaptation. Bridges the gap between test-time scaling (inference optimization) and test-time training (model adaptation).
