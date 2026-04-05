---
title: "V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning"
source: "https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/"
author: "Meta AI"
date_published: 2025-06-12
date_ingested: 2026-04-05
tags: [V-JEPA, world-models, self-supervised-learning, robotics, Meta]
type: article
status: raw
discovered_via: search
---

# V-JEPA 2: Meta's Self-Supervised World Model

## Architecture & Scale
- 1.2 billion parameters (ViT-g/16 backbone, up from ViT-H/16 in V-JEPA 1)
- Encoder processes raw video into semantic embeddings
- Predictor generates predictions based on video embeddings and contextual information

## Training Data
- Stage 1 (Pre-training): 1M+ hours video + 1M images from diverse sources (22M videos including YT-Temporal-1B)
- Stage 2 (Action-conditioned): Only 62 hours of robot data (Droid dataset)

## Key Improvements Over V-JEPA 1
- Action prediction and world modeling for robotics
- Progressive-resolution training: 16 frames initial, 64 frames cooldown
- Action-conditioned training using teacher-forcing and rollout losses

## Performance Benchmarks
- Something-Something v2: 77.3 top-1 accuracy (motion understanding)
- Epic-Kitchens-100: 39.7 recall-at-5 (human action anticipation) — SOTA
- Video QA: SOTA at 8B parameter scale when aligned with LLM

## Robotic Planning
- Zero-shot robot planning in new environments
- Short-horizon tasks: encoder compares current/goal states, model-predictive control
- Longer tasks: visual subgoals sequentially, 65-80% success on novel pick-and-place
- Uses Cross Entropy Method to optimize action sequences

## New Physical Reasoning Benchmarks
1. IntPhys 2: Violation-of-expectations paradigm; humans 85-95%, current models near chance
2. MVPBench: Minimal video pairs preventing superficial visual cues
3. CausalVQA: Cause-and-effect reasoning including counterfactuals
