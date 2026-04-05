---
title: "Self-Supervised Learning"
type: concept
sources: ["[[sources/jepa-deep-dive]]", "[[sources/meta-v-jepa-2]]"]
related: ["[[concepts/jepa]]", "[[concepts/world-models]]", "[[concepts/latent-world-models]]"]
tags: [self-supervised-learning, representation-learning, pretraining, JEPA]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Learning representations from unlabeled data via pretext tasks — from contrastive learning (SimCLR, CLIP) to joint embedding prediction (JEPA) — the foundational training paradigm for world models that learn from millions of hours of internet video."
---

## Overview

Self-supervised learning (SSL) trains models on unlabeled data by creating supervision signals from the data itself — predicting masked patches, matching augmented views, or forecasting future states. In the context of [[concepts/world-models]], SSL enables learning physical world representations from massive unlabeled video datasets without the prohibitive cost of manual annotation.

The field has evolved through three major paradigms: contrastive learning (push apart different examples), generative pretraining (predict raw data), and joint embedding prediction ([[concepts/jepa]] — predict representations). V-JEPA 2 demonstrates the power of the JEPA approach: pre-training on 1M+ hours of unlabeled video produces representations sufficient for zero-shot robotic planning with only 62 hours of robot-specific data.

## Key Ideas

### Three SSL Paradigms for Vision

| Paradigm | Method | Strength | Weakness |
|----------|--------|----------|----------|
| Contrastive | SimCLR, CLIP, MoCo | Strong representations | Needs exponentially many negatives |
| Generative | MAE, VideoGPT | Captures fine detail | Wastes capacity on pixel-level prediction |
| Joint Embedding | I-JEPA, V-JEPA | Efficient, avoids collapse | Requires careful regularization |

### The Collapse Problem

All embedding-based SSL methods face representational collapse — trivial constant outputs that minimize prediction error without learning. Solutions include:
- **Contrastive**: Negative samples push representations apart (expensive)
- **Distillation**: EMA target encoder (BYOL, V-JEPA) — asymmetric architecture prevents collapse
- **Regularization**: Isotropic Gaussian constraint (LeWorldModel) — mathematically elegant

### From SSL to World Models

The key insight is that SSL on video naturally produces [[concepts/world-models]]: predicting what comes next in a video requires understanding physics, object permanence, and causality. V-JEPA 2 scales this to 22M videos and 1B parameters, producing representations that transfer to robotic planning without explicit physics training.

## How It Connects

SSL is the training paradigm underlying [[concepts/jepa]] and modern [[concepts/world-models]]. It connects to [[concepts/latent-world-models]] through representation learning. The success of SSL for world models validates the broader thesis that sufficient data and scale can bootstrap physical understanding from passive observation.

## Sources

- [[sources/jepa-deep-dive]] — SSL paradigms and collapse prevention
- [[sources/meta-v-jepa-2]] — V-JEPA 2 as scaled SSL for world models
