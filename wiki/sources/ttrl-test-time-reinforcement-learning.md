---
title: "Source: TTRL: Test-Time Reinforcement Learning"
type: source-summary
source: "[[raw/ttrl-test-time-reinforcement-learning]]"
related: ["[[concepts/test-time-training]]", "[[concepts/test-time-compute]]", "[[concepts/reinforcement-learning-for-reasoning]]", "[[concepts/self-consistency]]"]
tags: [test-time-training, reinforcement-learning, self-evolution, reasoning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NeurIPS 2025 paper showing majority voting can serve as RL reward signal on unlabeled test data, achieving 211% improvement on AIME -- bridging test-time scaling and test-time training."
---

## Key Points

- Uses majority voting from test-time scaling as a reward signal for RL training.
- No ground-truth labels needed -- the model generates its own training signals.
- 211% performance boost for Qwen-2.5-Math-7B on AIME 2024.
- Surpasses the initial model's majority voting ceiling.
- Bridges [[concepts/test-time-compute|test-time scaling]] and [[concepts/test-time-training|test-time training]].

## Detailed Summary

TTRL (Zuo, Zhang et al., NeurIPS 2025) introduces an elegant solution to a fundamental challenge: how to continue improving models at deployment time without labeled data. The key insight is that majority voting -- a standard [[concepts/test-time-compute]] technique -- provides a surprisingly effective reward signal for reinforcement learning.

The method: (1) generate multiple solutions from the model, (2) use majority voting to identify likely-correct answers, (3) use this consensus as reward for RL policy optimization. This creates a virtuous cycle where the model's own collective predictions drive further improvement.

The 211% improvement on AIME 2024 is remarkable because it surpasses the model's own maj@n ceiling -- the model improves beyond what simple test-time scaling alone could achieve. This demonstrates that [[concepts/test-time-training]] and [[concepts/test-time-compute|test-time scaling]] are complementary, not alternative, strategies.

## Concepts Introduced or Discussed

- [[concepts/test-time-training]] -- weight adaptation at inference time
- [[concepts/test-time-compute]] -- the scaling component (majority voting)
- [[concepts/reinforcement-learning-for-reasoning]] -- RL as the training mechanism

## Metadata

- **Author**: Yuxin Zuo, Kaiyan Zhang et al.
- **Date Published**: 2025-04-22
- **Format**: paper (NeurIPS 2025)
- **URL**: https://arxiv.org/abs/2504.16084
