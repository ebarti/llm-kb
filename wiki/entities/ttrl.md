---
title: "TTRL (Test-Time Reinforcement Learning)"
type: entity
entity_type: paper
sources: ["[[sources/ttrl-test-time-reinforcement-learning]]"]
related: ["[[concepts/test-time-training]]", "[[concepts/test-time-compute]]", "[[concepts/reinforcement-learning-for-reasoning]]"]
last_compiled: 2026-04-05
summary: "NeurIPS 2025 paper demonstrating RL training on unlabeled test data using majority voting as reward signal, achieving 211% improvement on AIME -- bridging test-time scaling and test-time training."
---

## Overview

TTRL (Test-Time Reinforcement Learning) by Zuo, Zhang et al. (NeurIPS 2025) demonstrates that majority voting from standard [[concepts/test-time-compute|test-time scaling]] can serve as an effective reward signal for reinforcement learning, enabling model self-improvement without labeled data.

## Key Result

211% improvement for Qwen-2.5-Math-7B on AIME 2024 using only unlabeled test data, surpassing the model's own majority voting ceiling.

## Significance

TTRL bridges two previously separate paradigms: test-time scaling (spend more compute) and [[concepts/test-time-training]] (modify model weights). It shows these are complementary -- the scaling provides training signal that drives improvement beyond what scaling alone achieves.

## Mentioned In

- [[sources/ttrl-test-time-reinforcement-learning]] -- the original paper
