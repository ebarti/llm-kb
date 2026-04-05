---
title: "Source: Test-Time Scaling Makes Overtraining Compute-Optimal"
type: source-summary
source: "[[raw/roberts-train-to-test-scaling-laws]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/inference-scaling-laws]]", "[[concepts/training-vs-inference-compute]]", "[[concepts/scaling-laws]]"]
tags: [scaling-laws, test-time-compute, overtraining, compute-optimal]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Introduces Train-to-Test (T2) scaling laws jointly optimizing model size, training tokens, and inference samples -- showing overtraining smaller models becomes compute-optimal when accounting for test-time scaling costs."
---

## Key Points

- First framework jointly optimizing training and inference compute under a single budget.
- Traditional Chinchilla scaling laws ignore inference costs; test-time scaling laws ignore training decisions.
- T2 scaling laws bridge this gap.
- Key insight: optimal pretraining shifts into heavy overtraining when inference costs are considered.
- Heavily overtrained models + test-time scaling substantially outperform conventionally-trained alternatives.
- Results hold after post-training, confirming practical relevance.

## Detailed Summary

Roberts et al. (2026) identify a fundamental gap: [[concepts/scaling-laws|Chinchilla scaling laws]] tell us how to train models optimally, and [[concepts/inference-scaling-laws]] tell us how to deploy them optimally, but no prior work optimizes both jointly. The T2 framework fills this gap.

The key result is counterintuitive: when you know a model will use test-time scaling (repeated sampling, best-of-N), it becomes compute-optimal to **overtrain** smaller models rather than following Chinchilla proportions. A 7B model trained on 5x more tokens than Chinchilla prescribes, combined with test-time sampling, outperforms a Chinchilla-optimal 34B model at the same total compute budget.

This has immediate practical implications for [[concepts/training-vs-inference-compute]]: labs should shift training budgets toward smaller, more overtrained models when inference-time scaling is planned.

## Concepts Introduced or Discussed

- [[concepts/inference-scaling-laws]] -- the inference-side scaling relationships
- [[concepts/training-vs-inference-compute]] -- the central paradigm shift
- [[concepts/scaling-laws]] -- how T2 extends Chinchilla

## Metadata

- **Author**: Nicholas Roberts et al.
- **Date Published**: 2026-04-01
- **Format**: paper
- **URL**: https://arxiv.org/abs/2604.01411
