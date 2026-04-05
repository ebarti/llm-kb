---
title: "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens"
source: "https://arxiv.org/abs/2602.13517"
author: "Wei-Lin Chen, Liqian Peng, Tian Tan, Chao Zhao, Blake JianHang Chen, Ziqian Lin, Alec Go, Yu Meng"
date_published: 2026-02-19
date_ingested: 2026-04-05
tags: [reasoning-tokens, test-time-compute, overthinking, reasoning-quality, evaluation]
type: paper
status: raw
discovered_via: search
---

# Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens

## Core Contribution
Introduces the concept of "deep-thinking tokens" -- tokens where the model's internal predictions undergo significant revisions in deeper layers prior to convergence. These are distinct from tokens generated through superficial processing.

## Key Finding: Token Count is Unreliable
Increased generation length does not consistently correlate with accuracy and may instead signal "overthinking," leading to performance degradation. Raw token counts are poor proxies for reasoning quality.

## Deep-Thinking Ratio
The proportion of deep-thinking tokens within generated sequences. Evaluated across AIME 24/25, HMMT 25, and GPQA-diamond on GPT-OSS, DeepSeek-R1, and Qwen3.

## Results
- Deep-thinking ratio demonstrates a robust and consistently positive correlation with accuracy.
- Substantially outperforms length-based and confidence-based alternatives as a reasoning quality metric.

## Practical Application: Think@n
A test-time scaling strategy that prioritizes samples with high deep-thinking ratio, achieving comparable self-consistency performance while reducing computational costs through early rejection of unpromising generations.

## Significance
Provides a principled metric for understanding when models are genuinely reasoning vs. generating verbose but shallow text. Challenges the "more tokens = better reasoning" assumption.
