---
title: "Consistency Models: Fast, One-Step Alternatives to Diffusion Models"
source: "https://arxiv.org/abs/2303.01469"
author: "Yang Song, Prafulla Dhariwal, Mark Chen, Ilya Sutskever (OpenAI)"
date_published: 2023-03-02
date_ingested: 2026-04-05
tags: [consistency-models, fast-generation, diffusion, one-step]
type: paper
status: raw
discovered_via: search
---

# Consistency Models

## Core Concept
New family of generative models that learn direct mappings from noisy inputs to clean outputs in a single forward pass. Based on self-consistency property: all points along the same diffusion trajectory deterministically relate to one another.

## Self-Consistency Property
Consistency function f(xt, t) maps any noisy sample at time t back to original clean data x0. All points along the same trajectory yield the same output.

## Mathematical Framework
f_theta(x, t) = x + sigma(t) * F_theta(x, t), where F_theta is a U-Net backbone learning residual corrections. Consistency loss enforces stability between adjacent time steps using perceptual metrics (LPIPS) rather than pixel-level distances.

## Training Methods

### Consistency Distillation (CD)
Trains against pre-existing diffusion model. Enforces agreement between nearby trajectory points. Uses Heun's method ODE solver and EMA parameter updates.

### Consistency Training (CT)
Learns from scratch without teacher model. Adaptive scheduling for timestep counts and EMA decay rates. Proven to converge equivalently to CD in limiting cases.

## Performance Benchmarks
CIFAR-10 (32x32): CD achieves FID 2.82 (1-step), 2.20 (2-step). Progressive Distillation: FID 3.12, 2.40. Full diffusion: FID 2.04.
ImageNet 64x64: CD obtains FID 4.17 (1-step), 3.55 (2-step). CT: FID 3.90 (2-step).
Scalable to LSUN 256x256 with improved fidelity through few-step refinement.

## Recent Developments (2025)
SANA-Sprint: one-step diffusion with continuous-time consistency distillation, 10x faster (0.1s vs 1.1s on H100), 0.1s latency for 1024x1024 text-to-image.
Consistency Models Made Easy (ICLR 2025): simplified training procedures.

## Capabilities
Zero-shot data editing: inpainting, colorization, super-resolution without explicit task training.
