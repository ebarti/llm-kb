---
title: "Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models"
source: "https://arxiv.org/abs/2408.00724"
author: "Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang"
date_published: 2024-08-01
date_ingested: 2026-04-05
tags: [inference-scaling, scaling-laws, compute-optimal, test-time-compute, reasoning]
type: paper
status: raw
discovered_via: search
---

# Inference Scaling Laws

Published at ICLR 2025. Establishes concrete inference scaling relationships.

## Core Finding
Scaling inference compute with inference strategies can be more computationally efficient than scaling model parameters. Smaller models combined with advanced inference algorithms offer Pareto-optimal trade-offs in cost and performance.

## Inference Strategies Analyzed
- Greedy search
- Majority voting
- Best-of-N sampling
- Weighted voting
- Two tree search algorithms

## Key Empirical Result
Regression analysis on inference FLOPs and model sizes yields:
log10(C) = 1.19 log10(N) + 2.03

This allows estimation of optimal inference model sizes.

## Specific Demonstration
Llemma-7B with novel tree search consistently outperforms Llemma-34B across all tested inference strategies on MATH benchmark. Computational resources are better invested in inference algorithms rather than model parameter scaling alone.

## Compute-Optimal Inference
A "compute-optimal" scaling strategy allocates test-time compute per prompt adaptively, improving efficiency by 4x compared to best-of-N baseline. Inference scaling laws reveal that compute-optimal inference favors scaling solution generation more aggressively than scaling verifications.

## Significance
Provides the inference-time counterpart to Chinchilla training scaling laws. Establishes that inference compute is an independent, optimizable axis of AI system design.
