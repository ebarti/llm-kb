---
title: "Rectified Flow"
type: concept
sources: ["[[sources/flow-matching-iclr-2025]]", "[[sources/flux-architecture-demystified]]"]
related: ["[[concepts/flow-matching]]", "[[concepts/diffusion-models]]", "[[concepts/fast-generation]]", "[[concepts/consistency-models]]"]
tags: [rectified-flow, flow-matching, fast-generation, optimal-transport]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Optimization of flow matching that straightens transport trajectories from noise to data, enabling large integration steps and few-step generation -- the 'reflow' procedure uses teacher-student distillation to further reduce curvature, underpinning FLUX and SD3 training."
---

## Overview

Rectified flow is an optimization technique within the [[concepts/flow-matching]] framework that explicitly straightens the transport paths from noise to data. While flow matching learns velocity fields that transform distributions, the trajectories can still have curvature requiring many small integration steps. Rectified flow addresses this by optimizing for straight-line trajectories, enabling the model to take much larger steps without losing accuracy.

The term "rectified flow" is sometimes used interchangeably with "flow matching" because the straightening effect is inherent to the flow matching training process. However, the "reflow" procedure -- iteratively distilling the model to produce even straighter paths -- represents an additional optimization step.

Rectified flow training is the basis for [[entities/flux]] FLUX.1 and [[entities/stable-diffusion]] 3.

## Key Ideas

### Straight-Line Transport

Standard diffusion models follow curved, noisy paths requiring dozens or hundreds of denoising steps. Rectified flow learns straight-line ODE trajectories: the model predicts velocity vectors pointing directly from noise to data along a linear interpolation path. Fewer steps are needed because each step covers more ground without error accumulation.

### The Reflow Procedure

Reflow iteratively improves trajectory straightness:
1. Train an initial flow matching model on random noise-data pairs
2. Use this model to generate synthetic target endpoints from noise inputs
3. Train a new student model on these noise-to-synthetic-endpoint pairs, which are straighter
4. Repeat if needed

Each iteration reduces trajectory curvature. RE-Meanflow (2025) achieves 33.4% FID improvement over 2-rectified flow while reducing training cost by 90%.

### Connection to Optimal Transport

Rectified flows approximate the Benamou-Brenier formulation of optimal transport, where mass transport follows constant-velocity geodesics in Wasserstein metric space. This theoretical grounding explains why the straightened paths are efficient: they minimize the transport cost between distributions.

## How It Connects

Rectified flow is the bridge between [[concepts/flow-matching]] theory and practical [[concepts/fast-generation]]. It provides the training objective for [[entities/flux]] and [[entities/stable-diffusion]] 3, where the model predicts velocity vectors rather than noise. Combined with [[concepts/consistency-models]], rectified flow represents one of two main paths to one-step or few-step generation.

## Sources

- [[sources/flow-matching-iclr-2025]] -- mathematical foundations and reflow
- [[sources/flux-architecture-demystified]] -- rectified flow in FLUX.1
