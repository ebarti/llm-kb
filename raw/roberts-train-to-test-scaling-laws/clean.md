---
title: "Test-Time Scaling Makes Overtraining Compute-Optimal"
source: "https://arxiv.org/abs/2604.01411"
author: "Nicholas Roberts, Sungjun Cho, Zhiqi Gao, Tzu-Heng Huang, Albert Wu, Gabriel Orlanski, Avi Trost, Kelly Buchanan, Aws Albarghouthi, Frederic Sala"
date_published: 2026-04-01
date_ingested: 2026-04-05
tags: [test-time-compute, scaling-laws, overtraining, compute-optimal, training-inference-tradeoff]
type: paper
status: raw
discovered_via: search
---

# Test-Time Scaling Makes Overtraining Compute-Optimal

## Core Contribution
Introduces Train-to-Test (T2) scaling laws that jointly optimize model size, training tokens, and number of inference samples under a single end-to-end compute budget.

## The Gap Addressed
- Traditional scaling laws (Chinchilla) optimize training compute only, ignoring inference costs.
- Test-time scaling laws optimize inference only, ignoring how models were trained.
- No prior work jointly optimized both training and inference under a unified budget.

## Key Insight
When accounting for inference cost, optimal pretraining decisions shift radically into the overtraining regime. Heavily overtrained smaller models are more compute-efficient when combined with test-time scaling (repeated sampling, best-of-N) than conventionally Chinchilla-optimal models.

## Methodology
- Uses pass@k modeling for test-time scaling.
- Jointly optimizes three variables: model size N, training tokens D, number of inference samples k.
- Tests across 8 downstream tasks.

## Key Findings
- Overtrained models matching T2 forecasts substantially outperformed conventionally-trained alternatives.
- Results hold after post-training, indicating practical relevance for deployed systems.
- The shift toward overtraining is more pronounced as inference budgets increase.

## Significance
This paper bridges the gap between training-time and inference-time scaling laws, providing the first unified framework for compute-optimal decisions spanning the full lifecycle from training to deployment.
