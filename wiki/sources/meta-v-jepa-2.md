---
title: "Source: V-JEPA 2 — Self-Supervised World Models for Understanding, Prediction and Planning"
type: source-summary
source: "[[raw/meta-v-jepa-2-world-model]]"
related: ["[[concepts/jepa]]", "[[concepts/world-models]]", "[[concepts/self-supervised-learning]]", "[[entities/meta-ai]]", "[[entities/yann-lecun]]"]
tags: [V-JEPA, world-models, self-supervised-learning, robotics, Meta]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Meta's V-JEPA 2: 1.2B-param self-supervised world model trained on 1M+ hours of video; achieves SOTA on action anticipation; enables zero-shot robot planning with only 62 hours of robot data; introduces three new physical reasoning benchmarks."
---

## Key Points

- 1.2 billion parameter model (ViT-g/16), up from 630M in V-JEPA 1
- Pre-trained on 1M+ hours of video and 1M images; only 62 hours of robot data for action conditioning
- SOTA on Epic-Kitchens-100 action anticipation (39.7 recall-at-5) and strong motion understanding (77.3 on SSv2)
- Zero-shot robot planning: 65-80% success on novel pick-and-place without any data from target robots
- Three new benchmarks reveal current models (including V-JEPA 2) are far below human physical reasoning
- Progressive-resolution training mirrors LLM long-context training approach

## Detailed Summary

V-JEPA 2 represents Meta's most complete realization of [[entities/yann-lecun]]'s [[concepts/jepa]] vision. The model follows a two-stage training: massive self-supervised pre-training on internet video (22M videos from YT-Temporal-1B), followed by a lightweight action-conditioned post-training phase using just 62 hours of unlabeled robot video from the Droid dataset.

The architectural upgrade from ViT-H/16 (630M params) to ViT-g/16 (1B params) combined with progressive-resolution training (16 frames initially, 64 frames in cooldown) yields strong visual understanding. When aligned with an LLM, V-JEPA 2 achieves SOTA on multiple video QA tasks at the 8B parameter scale.

The robotic application is particularly striking: V-JEPA 2-AC (action-conditioned variant) deploys zero-shot on Franka arms in two different labs for pick-and-place tasks, using model-predictive control with Cross Entropy Method optimization. This demonstrates that [[concepts/self-supervised-learning]] from internet video can transfer directly to robotic planning.

Meta also introduced three physical reasoning benchmarks — IntPhys 2, MVPBench, and CausalVQA — revealing that even V-JEPA 2 falls substantially short of human physical reasoning (humans 85-95% on IntPhys 2 vs. near-chance for models).

## Concepts Introduced or Discussed

- [[concepts/jepa]] — the underlying architectural philosophy
- [[concepts/self-supervised-learning]] — learning without explicit labels
- [[concepts/world-models]] — internal representations enabling prediction and planning
- [[concepts/embodied-ai]] — deploying AI in physical environments

## Metadata

- **Author**: Meta AI (Assran et al.)
- **Date Published**: 2025-06-12
- **Format**: research paper + blog
- **URL**: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
