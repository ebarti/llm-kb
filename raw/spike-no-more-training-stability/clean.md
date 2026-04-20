---
title: "Spike No More: Stabilizing the Pre-training of Large Language Models"
source: "https://arxiv.org/html/2312.16903v2"
author: "Various (arXiv)"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [training-stability, loss-spikes, gradient-explosion, layer-normalization, initialization]
type: paper
status: raw
discovered_via: search
---

# Spike No More: Stabilizing the Pre-training of Large Language Models

## Core Problem

Loss spikes during large language model pre-training cause catastrophic training failures. The paper identifies two fundamental causes of exploding gradients.

## Two Sources of Gradient Explosion

### 1. Shortcut-Based Explosion
Residual connections in transformer layers can amplify gradient norms exponentially during forward propagation. With standard initialization, the standard deviation of FFN outputs grows unbounded, causing gradient explosion during backpropagation.

### 2. Layer Normalization (LN) Explosion
LN gradient magnitudes follow: ||dLN(x)/dx||_2 = O(sqrt(d)/||x||_2). When input vectors have very small standard deviations (common in scaled initialization), LN gradients become inversely proportional and explode, particularly in shallow layers.

## Key Finding on Initialization Methods

Plain initialization (standard He initialization) causes shortcut explosion but not LN explosion. Scaled initialization (reducing W2 and Wo parameters) prevents shortcut explosion but actually enables LN explosion — creating a critical stability problem overlooked in prior work.

## Proposed Solutions

- Embed LN: Apply layer normalization directly to embedding vectors
- Scaled Embed: Multiply embeddings by sqrt(d) to increase their standard deviation toward 1.0

These modifications ensure input vectors to LN layers maintain appropriate magnitudes.

## Experimental Validation

Testing on 350M and 1.7B parameter models using C4 dataset:
- Vanilla (scaled init only) showed frequent loss spikes
- Embed Detach (gradient shrinking) provided incomplete protection
- Embed LN and Scaled Embed completely eliminated spikes
- Methods preventing spikes enabled training with 2x larger learning rates
- Performance improvements increased substantially with model scale

## Practical Recommendations

1. Combine scaled initialization with embedding modifications
2. Use larger learning rates than conventionally assumed safe
3. Apply shorter sequences during early training stages
4. Monitor gradient norms in shallow layers as spike indicators
