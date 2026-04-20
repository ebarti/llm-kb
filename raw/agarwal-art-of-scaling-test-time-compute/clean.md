---
title: "The Art of Scaling Test-Time Compute for Large Language Models"
source: "https://arxiv.org/abs/2512.02008"
author: "Aradhye Agarwal, Ayan Sengupta, Tanmoy Chakraborty"
date_published: 2025-12-01
date_ingested: 2026-04-05
tags: [test-time-compute, inference-scaling, empirical-study, reasoning, scaling-laws]
type: paper
status: raw
discovered_via: search
---

# The Art of Scaling Test-Time Compute for Large Language Models

First large-scale empirical study of test-time scaling (TTS), spanning over 30 billion tokens generated across 8 open-source LLMs (7B to 235B parameters) and 4 reasoning datasets.

## Key Contributions
- First systematic comparison of TTS strategies at scale.
- Practical recipe for selecting the best TTS strategy, considering problem difficulty, model type, and compute budget.

## Three Consistent Trends

1. **No Universal Dominance**: Different test-time scaling strategies excel under different conditions. No single approach works best universally.

2. **Distinct Model Patterns**: Reasoning models demonstrate varying performance characteristics, categorized into "short-horizon" and "long-horizon" groups based on problem difficulty and trace length.

3. **Monotonic Scaling**: For any given model type, performance improvements scale predictably with increased compute allocation.

## Practical Guidance
Actionable recommendations for practitioners implementing inference-time scaling optimization, based on matching strategy to problem difficulty and model type.
