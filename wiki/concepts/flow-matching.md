---
title: "Flow Matching"
type: concept
sources: ["[[sources/flow-matching-iclr-2025]]", "[[sources/flux-architecture-demystified]]", "[[sources/flux-vs-stable-diffusion-2026]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/rectified-flow]]", "[[concepts/diffusion-transformer]]", "[[concepts/consistency-models]]", "[[entities/flux]]", "[[entities/stable-diffusion]]"]
tags: [flow-matching, generative-models, velocity-field, optimal-transport]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Generative framework learning velocity fields that transport noise distributions to data distributions along straight-line ODE paths -- simpler, faster, and more flexible than traditional diffusion denoising, now the standard training objective for FLUX, SD3, and other leading models."
---

## Overview

Flow matching is a generative modeling framework that learns a velocity field v(x, t) describing how to transport samples from a noise distribution to a data distribution. Unlike traditional [[concepts/diffusion-models]] that simulate stochastic Brownian motion and predict noise at each step, flow matching solves an ordinary differential equation (ODE): dx = v(x, t) dt. The result is a deterministic, efficient mapping from noise to data along smooth trajectories.

Flow matching has rapidly become the standard training objective for leading image generation systems. [[entities/flux]] FLUX.1, [[entities/stable-diffusion]] 3, and many recent video and audio models all use flow matching instead of the original DDPM noise-prediction formulation.

## Key Ideas

### Mathematical Foundation

The core equation is simple: given a source distribution (Gaussian noise) and a target distribution (data), flow matching learns a neural network that predicts the velocity at each point in space and time. Training uses linear interpolation between random noise-data pairs:

- Sample noise x0 and data x1
- Create interpolated point xt = (1-t) * x0 + t * x1
- Train network to predict velocity v = x1 - x0 at point (xt, t)

The learned velocity field, despite being trained on individual paired trajectories that cross, averages to produce smooth, non-crossing flows.

### Rectified Flows

[[concepts/rectified-flow]] is the key optimization: the training process naturally straightens transport paths, reducing the curvature that requires small integration steps. The **reflow** procedure further improves this:

1. Use a pretrained flow model to generate synthetic target endpoints
2. Train a student model on these straighter noise-to-endpoint trajectories
3. The resulting model requires fewer steps for high-quality generation

This teacher-student approach connects to [[concepts/knowledge-distillation]] and enables dramatic speedup -- potentially one-step generation.

### Comparison with Traditional Diffusion

| Property | Flow Matching | Traditional Diffusion (DDPM) |
|----------|--------------|---------------------------|
| Process type | Deterministic ODE | Stochastic SDE |
| Prediction target | Velocity vector | Noise (epsilon) |
| Trajectory shape | Straight lines | Curved, noisy paths |
| Integration | Benefits from RK4 | Less benefit from higher-order methods |
| Steps needed | 4-20 typical | 20-50 typical |
| Priors | Flexible | Gaussian required |

### Connection to Optimal Transport

Reflowed streamlines approximate the solution to the Benamou-Brenier formulation of optimal transport: constant-velocity geodesics in Wasserstein metric space. This means flow matching naturally finds efficient transport paths between distributions, connecting to deep mathematical theory.

### Practical Integration Methods

The choice of numerical integrator matters significantly:
- **Forward Euler**: Fast per step but accumulates error
- **RK4 (4th-order Runge-Kutta)**: 4 function evaluations per step but dramatically better results
- **Time warping**: Non-uniform temporal sampling concentrating steps where trajectory curvature peaks

## Research Momentum

Flow matching research is exploding: 30+ papers accepted at NeurIPS 2025, 150+ submissions to ICLR 2026. Specialized variants include categorical flow matching, Riemannian flow matching, and Dirichlet flow matching for applications in structural biology, molecular modeling, and biomedical imaging.

## How It Connects

Flow matching sits at the intersection of [[concepts/diffusion-models]] theory and practical generation efficiency. It provides the training objective for [[concepts/diffusion-transformer]] architectures, enables [[concepts/fast-generation]] through straight trajectories, and connects theoretically to [[concepts/optimal-transport]]. The combination of flow matching training with DiT/MMDiT architectures defines the current state of the art in [[concepts/image-generation]], [[concepts/video-generation]], and increasingly [[concepts/audio-generation]].

## Open Questions

- Can flow matching be extended to discrete domains (text generation) as effectively as continuous domains?
- What is the theoretical minimum number of steps needed for given quality levels?
- How do flow matching models compose with other conditioning mechanisms (ControlNet, IP-Adapter)?

## Sources

- [[sources/flow-matching-iclr-2025]] -- comprehensive physics-based explanation
- [[sources/flux-architecture-demystified]] -- flow matching in FLUX.1
- [[sources/flux-vs-stable-diffusion-2026]] -- flow matching vs DDPM comparison
