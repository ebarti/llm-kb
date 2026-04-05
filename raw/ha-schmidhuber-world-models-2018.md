---
title: "World Models (Ha & Schmidhuber, 2018)"
source: "https://worldmodels.github.io/"
author: "David Ha, Jürgen Schmidhuber"
date_published: 2018-03-01
date_ingested: 2026-04-05
tags: [world-models, VAE, MDN-RNN, reinforcement-learning, foundational-paper]
type: paper
status: raw
discovered_via: search
---

# World Models (Ha & Schmidhuber, 2018)

## Architecture: V (Vision) + M (Memory) + C (Controller)

### VAE (Vision Model)
- Convolutional Variational Autoencoder
- Compresses 64x64 RGB frames into latent vectors: z ∈ ℝ³² (CarRacing), z ∈ ℝ⁶⁴ (VizDoom)
- 4 convolutional encoder layers, 4 deconvolutional decoder layers (stride-2)
- Latent space: factored Gaussian N(μ, σ²I)

### MDN-RNN (Memory Model)
- LSTM + Mixture Density Network output layer
- Models P(z_{t+1}|a_t, z_t, h_t) as mixture of Gaussians
- CarRacing: 256 hidden units, 5 Gaussian mixtures
- VizDoom: 512 hidden units
- Diagonal covariance matrix (no correlation between z elements)

### Controller (C)
- Single linear layer: a_t = W_c[z_t h_t] + b_c
- CarRacing: 867 parameters; VizDoom: 1,088 parameters
- Optimized with CMA-ES evolutionary algorithm

## Training Procedure
1. Collect 10,000 rollouts from random policy
2. Train VAE (1 epoch, L² reconstruction + KL loss)
3. Train MDN-RNN (20 epochs)
4. Evolve Controller using CMA-ES (population 64, 16 rollouts/agent)

## Results
- CarRacing-v0: Full model 906 ± 21 (previous best 838 ± 11; DQN/A3C: 343-652)
- VizDoom Take Cover: Trained in dream, transferred to real: 1092 ± 556 (target 750)

## Learning Inside a Dream
- MDN-RNN generates synthetic environments
- Temperature parameter τ controls stochasticity
- Agents discovered "adversarial policies" exploiting model imperfections
- Higher τ (~1.15) prevents exploitation, improves real-world transfer

## Parameter Counts
| Component | CarRacing | VizDoom |
|-----------|-----------|---------|
| VAE       | 4,348,547 | 4,446,915 |
| MDN-RNN   | 422,368   | 1,678,785 |
| Controller| 867       | 1,088 |

## Key Insight
Agents develop compact policies by learning rich world representations unsupervised, then train controllers through evolution — eliminating credit assignment bottleneck of traditional deep RL.
