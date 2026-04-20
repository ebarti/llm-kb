---
title: "Flow With What You Know: Flow Matching Explained"
source: "https://iclr-blogposts.github.io/2025/blog/flow-with-what-you-know/"
author: "ICLR Blogposts 2025"
date_published: 2025-04-28
date_ingested: 2026-04-05
tags: [flow-matching, rectified-flow, generative-models, diffusion]
type: article
status: raw
discovered_via: search
---

# Flow Matching: Technical Overview

## Mathematical Foundations
Flow matching learns to estimate velocity fields that transform probability distributions. Core equation: dr = v(r,t) dt, where v is the velocity vector. Grounded in physics of fluid dynamics and particle motion.

## Training Mechanism
1. Random pairing: source and target points randomly matched (initially crossing trajectories)
2. Linear interpolation: points move along straight paths at constant velocity
3. Velocity prediction: neural network learns to estimate correct velocities at each position and time
4. Aggregation: individual trajectory crossings average out to smooth, non-crossing flows

"The learned velocity field might not exactly match any of our training trajectories, but it captures the statistical flow needed to transform one distribution into another."

## Rectified Flows and Reflow
Rectified flows are the natural outcome of flow matching -- trajectories become non-crossing through training. Reflow extension: use pretrained model to generate simulated endpoints, train student model with straighter trajectories, reducing curvature for faster integration. Teacher-student approach enables dramatic speedup.

## Comparison with Diffusion Models
- Determinism: Flow models are deterministic; standard diffusion injects noise (Brownian motion)
- Integration: Smooth flow trajectories benefit from higher-order methods (RK4); stochastic diffusion paths benefit less
- Flexibility: Flow matching permits more flexible trajectory choices
- Diffusion models also admit deterministic sampling (DDIM), making them directly comparable

## Optimal Transport Connection
Reflowed streamlines approximate time-independence (stationarity), connecting to Benamou-Brenier formulation: optimal mass transport follows constant-velocity geodesics in Wasserstein metric space.

## Practical Details
- Forward Euler: fast but accumulates error
- RK4: 4 evaluations per step but dramatically better results
- Time warping: non-uniform sampling concentrates steps where curvature peaks
- Velocity model dimensionality matches data structure (pixel-wise for images, component-wise for audio)

## Key Advantages
- Physics-based intuition over probability mathematics
- Straight trajectories enable few-step generation
- No requirement for Gaussian priors
- Simpler implementation than normalizing flows
