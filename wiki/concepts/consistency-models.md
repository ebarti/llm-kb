---
title: "Consistency Models"
type: concept
sources: ["[[sources/consistency-models-fast-generation]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/fast-generation]]", "[[concepts/flow-matching]]", "[[concepts/knowledge-distillation]]"]
tags: [consistency-models, fast-generation, one-step, diffusion]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Generative models that map noise to data in 1-2 steps by enforcing self-consistency along diffusion trajectories -- achieving FID 2.82 on CIFAR-10 in one step, with SANA-Sprint (2025) reaching 0.1s latency for 1024x1024 generation on H100."
---

## Overview

Consistency models, introduced by Yang Song, Prafulla Dhariwal, Mark Chen, and Ilya Sutskever at OpenAI (2023), address the fundamental speed limitation of [[concepts/diffusion-models]]: the requirement for dozens or hundreds of iterative denoising steps. By learning a direct mapping from any point on a diffusion trajectory to its origin, consistency models enable high-quality generation in a single forward pass.

The self-consistency property is the key insight: all points along the same ODE trajectory of a diffusion process share the same starting point (clean data sample). A consistency model learns this mapping directly, bypassing iterative denoising entirely.

## Key Ideas

### Self-Consistency Property

Given a diffusion ODE trajectory from clean data x0 through progressively noisier versions x1, x2, ..., xT, a consistency function f(xt, t) maps any point back to x0. The model is trained so that f(xa, a) = f(xb, b) for any two points a, b on the same trajectory. This constraint is enforced during training via a consistency loss measured by perceptual similarity (LPIPS) rather than pixel-level MSE.

### Mathematical Formulation

The model uses skip-connection parameterization:
f_theta(x, t) = x + sigma(t) * F_theta(x, t)

where F_theta is a U-Net backbone learning residual corrections. This ensures differentiability at boundaries and stable training across all timesteps.

### Two Training Paradigms

**Consistency Distillation (CD)**: Uses a pretrained [[concepts/diffusion-models]] as a teacher. Numerical ODE solvers (Heun's method) trace trajectory points, and the student model is trained to produce identical outputs for nearby trajectory points. Uses EMA (exponential moving average) parameter updates for stability.

**Consistency Training (CT)**: Learns self-consistency from scratch without a teacher model. Employs adaptive scheduling for timestep counts and EMA decay rates. Proven to converge equivalently to CD in limiting cases -- no pretrained diffusion model needed.

### Performance

| Dataset | Method | 1-Step FID | 2-Step FID |
|---------|--------|-----------|-----------|
| CIFAR-10 | Consistency Distillation | 2.82 | 2.20 |
| CIFAR-10 | Progressive Distillation | 3.12 | 2.40 |
| CIFAR-10 | Full diffusion (1000 steps) | - | 2.04 |
| ImageNet 64x64 | Consistency Distillation | 4.17 | 3.55 |
| ImageNet 64x64 | Consistency Training | - | 3.90 |

### Recent Developments (2025)

- **SANA-Sprint**: Continuous-time consistency distillation achieving 0.1s latency for 1024x1024 text-to-image on H100 (10x faster than standard diffusion)
- **Consistency Models Made Easy** (ICLR 2025): Simplified training procedures reducing implementation complexity
- **Integration with DiT**: Consistency training applied to [[concepts/diffusion-transformer]] architectures

### Zero-Shot Editing

A significant advantage: consistency models support zero-shot data editing -- inpainting, colorization, super-resolution, stroke-guided generation -- without any task-specific training. This is possible because the self-consistency property preserves the structure of the diffusion trajectory.

## How It Connects

Consistency models represent one path toward [[concepts/fast-generation]], complementing [[concepts/flow-matching]] / [[concepts/rectified-flow]] (which achieves speed via straighter trajectories) and progressive distillation (which trains smaller models on fewer steps). Together, these approaches are making real-time [[concepts/image-generation]] practical, enabling interactive creative workflows.

## Open Questions

- Can consistency training match distillation quality without any teacher model?
- How well do consistency models scale to video and 3D generation?
- Is there a fundamental quality ceiling for one-step generation?

## Sources

- [[sources/consistency-models-fast-generation]] -- original paper analysis
