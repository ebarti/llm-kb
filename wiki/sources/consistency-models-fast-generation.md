---
title: "Source: Consistency Models (OpenAI)"
type: source-summary
source: "[[raw/consistency-models-fast-generation]]"
related: ["[[concepts/consistency-models]]", "[[concepts/diffusion-models]]", "[[concepts/fast-generation]]"]
tags: [consistency-models, fast-generation, one-step, diffusion]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "OpenAI's consistency models map noise to data in a single step via self-consistency property -- achieving FID 2.82 on CIFAR-10 (one-step) and enabling zero-shot inpainting, colorization, and super-resolution; SANA-Sprint (2025) achieves 0.1s latency for 1024x1024 images."
---

## Key Points

- [[concepts/consistency-models]] directly map noise to data in one forward pass, eliminating iterative sampling
- Self-consistency property: all points along a diffusion trajectory map to the same clean output x0
- Two training methods: Consistency Distillation (from pretrained diffusion model) and Consistency Training (from scratch)
- CIFAR-10: FID 2.82 (1-step), 2.20 (2-step); outperforms Progressive Distillation (3.12, 2.40)
- ImageNet 64x64: FID 4.17 (1-step), 3.55 (2-step)
- Supports zero-shot editing (inpainting, colorization, super-resolution) without task-specific training
- SANA-Sprint (2025): continuous-time consistency distillation achieves 0.1s latency for 1024x1024 text-to-image on H100
- Consistency Models Made Easy (ICLR 2025) simplified training procedures

## Detailed Summary

Yang Song, Prafulla Dhariwal, Mark Chen, and Ilya Sutskever at OpenAI introduced [[concepts/consistency-models]] as a fundamental alternative to iterative diffusion sampling. The key insight is that all points along a diffusion ODE trajectory share the same origin -- so a model can learn to directly predict this origin from any point on the trajectory.

The model uses skip-connection parameterization: f_theta(x,t) = x + sigma(t) * F_theta(x,t), where F_theta is a U-Net learning residual corrections. The consistency loss enforces stability between adjacent timesteps using perceptual metrics (LPIPS) rather than pixel-level MSE.

Two training paradigms exist. Consistency Distillation uses a pretrained diffusion model as a teacher, enforcing that nearby trajectory points produce identical outputs. Consistency Training learns the same property from scratch using adaptive scheduling. Both converge equivalently in the limit.

The practical impact is dramatic: traditional [[concepts/diffusion-models]] require 10-2000x more compute than single-step models. By 2025, SANA-Sprint achieved 0.1s latency for 1024x1024 generation on H100, making real-time image generation practical.

## Concepts Introduced or Discussed

- [[concepts/consistency-models]] -- the core contribution
- [[concepts/fast-generation]] -- practical speed improvements
- [[concepts/diffusion-models]] -- the baseline being improved upon
- [[concepts/knowledge-distillation]] -- CD uses teacher-student distillation

## Metadata

- **Author**: Yang Song, Prafulla Dhariwal, Mark Chen, Ilya Sutskever
- **Date Published**: 2023-03-02
- **Format**: paper
- **URL**: https://arxiv.org/abs/2303.01469
