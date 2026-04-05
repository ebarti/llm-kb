---
title: "Source: A Recipe for Training Neural Networks"
type: source-summary
source: "[[raw/karpathy-recipe-training-neural-networks]]"
related: ["[[entities/andrej-karpathy]]", "[[concepts/fine-tuning]]", "[[concepts/data-quality-bottleneck]]"]
tags: [karpathy, training, neural-networks, best-practices]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's 2019 practical guide to training neural networks: six-stage recipe from data inspection through squeezing performance, emphasizing 'patience and attention to detail' over clever tricks."
---

## Key Points

- Neural nets are "leaky abstractions" — you cannot treat them as plug-and-play
- Training "fails silently" — correct code can produce degraded results without errors
- Six-stage recipe: (1) know your data, (2) establish infrastructure, (3) overfit, (4) regularize, (5) tune, (6) squeeze
- "Don't be a hero" — copy proven architectures instead of inventing new ones
- Data inspection is step zero — outlier visualization "almost always uncover[s] bugs in data quality"
- Adam at 3e-4 is the safe default optimizer/learning rate
- Random search beats grid search for hyperparameters
- "Patience and attention to detail" correlate most strongly with success

## Detailed Summary

This widely-cited 2019 blog post offers Karpathy's accumulated practical wisdom for training neural networks. It is notable for its blunt honesty about the difficulty of the craft and its systematic, hypothesis-driven approach that prevents the accumulation of unverified complexity.

The essay opens with two uncomfortable truths: neural networks cannot be treated as black boxes (they are "leaky abstractions"), and they fail silently (no exceptions, just quietly worse performance). The remedy is a disciplined six-stage process that moves from understanding data through establishing baselines to incrementally adding complexity.

The post has become required reading in many ML courses and teams, functioning as a practitioner's checklist. Its influence extends beyond technical advice — the "don't be a hero" philosophy and the emphasis on data quality over model cleverness anticipated the broader [[concepts/data-quality-bottleneck]] insight that would crystallize in later years.

## Concepts Introduced or Discussed

- [[concepts/data-quality-bottleneck]] — Data inspection as the essential first step
- [[concepts/fine-tuning]] — Practical approach to model adaptation

## Quotes & Evidence

> "The most common mistake I see people make is to dive into a complicated framework right away."

> "Don't be a hero. Copy paste architectures from related papers."

> "Patience and attention to detail" correlate most strongly with deep learning success.

## Metadata

- **Author**: Andrej Karpathy
- **Date Published**: 2019-04-25
- **Format**: blog post
- **URL**: https://karpathy.github.io/2019/04/25/recipe/
