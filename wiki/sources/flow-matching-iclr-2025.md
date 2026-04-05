---
title: "Source: Flow With What You Know (ICLR 2025)"
type: source-summary
source: "[[raw/flow-matching-iclr-2025]]"
related: ["[[concepts/flow-matching]]", "[[concepts/diffusion-models]]", "[[concepts/rectified-flow]]"]
tags: [flow-matching, rectified-flow, generative-models, mathematical-foundations]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "ICLR 2025 blog post providing physics-grounded explanation of flow matching: velocity field estimation via ODE solving, rectified flows as straight-line transport paths, reflow for few-step generation, and connection to optimal transport via Benamou-Brenier formulation."
---

## Key Points

- [[concepts/flow-matching]] learns velocity fields transforming probability distributions via the ODE dr = v(r,t) dt
- Training: random source-target pairing, linear interpolation, velocity prediction by neural network, averaging produces smooth non-crossing flows
- [[concepts/rectified-flow]] is the natural outcome: trajectories automatically straighten through training
- Reflow (teacher-student distillation) further straightens paths for few-step generation
- Key difference from [[concepts/diffusion-models]]: flow models are deterministic; diffusion injects stochastic noise
- Smooth trajectories benefit from higher-order integration (RK4 dramatically improves over Euler)
- Time warping optimizes by concentrating integration steps where curvature peaks
- Connection to optimal transport: reflowed paths approximate Benamou-Brenier constant-velocity geodesics in Wasserstein space
- Over 30 flow matching papers accepted at NeurIPS 2025; 150+ submissions to ICLR 2026

## Detailed Summary

This ICLR 2025 blog post provides the most accessible explanation of [[concepts/flow-matching]] available, grounding the mathematics in physics intuition. The core idea is learning a velocity field that transports samples from a noise distribution to a data distribution along straight-line paths.

The training process begins with random pairing of source (noise) and target (data) points, connected by linear interpolation at constant velocity. A neural network learns to predict the correct velocity at each position and time. Despite individual training trajectories crossing, the learned field averages these to produce smooth, non-crossing flows.

Rectified flows emerge naturally: the straightening of trajectories is an inherent property of the training process. The reflow extension uses a teacher model to generate synthetic endpoints, then trains a student on these straighter trajectories -- enabling one-step or few-step generation.

The connection to optimal transport theory is elegant: reflowed paths approximate the Benamou-Brenier formulation, where optimal mass transport follows constant-velocity geodesics in Wasserstein metric space.

## Concepts Introduced or Discussed

- [[concepts/flow-matching]] -- the central framework
- [[concepts/rectified-flow]] -- straight-line transport optimization
- [[concepts/diffusion-models]] -- contrasted with flow matching
- [[concepts/optimal-transport]] -- theoretical foundation

## Metadata

- **Author**: ICLR Blogposts 2025
- **Date Published**: 2025-04-28
- **Format**: article (blog post)
- **URL**: https://iclr-blogposts.github.io/2025/blog/flow-with-what-you-know/
