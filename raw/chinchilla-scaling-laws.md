---
title: "Training Compute-Optimal Large Language Models (Chinchilla)"
source: "https://arxiv.org/abs/2203.15556"
author: "Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, et al. (DeepMind)"
date_published: 2022-03-29
date_ingested: 2026-04-05
tags: [scaling-laws, chinchilla, compute-optimal, training, LLM]
type: paper
status: raw
discovered_via: search
---

# Training Compute-Optimal Large Language Models (Chinchilla)

## Core Discovery

By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, researchers found that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size, the number of training tokens should also be doubled.

## Optimal Token-to-Parameter Ratio

The research showed the optimal balance was approximately 20 tokens per parameter for large-scale transformer models. A model with 70 billion parameters should be trained on roughly 1.4 trillion tokens to be compute-optimal.

## Previous Undertraining Problem

Current large language models were found to be significantly undertrained — a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. Models like GPT-3 had been trained on far less data than they could effectively utilize.

## Three Approaches to Estimation

The paper used three independent methods to estimate the optimal allocation:
1. Fix model sizes and vary number of training tokens
2. Fix FLOPs budgets and vary model size vs. tokens
3. Fit a parametric loss function to all experiments

All three approaches consistently showed models should be trained on substantially more data than was common practice.

## Practical Validation: Chinchilla Model

The hypothesis was tested by training Chinchilla: same compute budget as Gopher but with 70B parameters and 4x more data. Chinchilla uniformly and significantly outperforms:
- Gopher (280B)
- GPT-3 (175B)
- Jurassic-1 (178B)
- Megatron-Turing NLG (530B)

A 4x smaller model with 4x more data beat all larger alternatives on a large range of downstream evaluations.

## Scaling Law Formula

Loss(N, D) = E + A/N^alpha + B/D^beta

Where N = model parameters, D = training tokens, and E, A, B, alpha, beta are fitted constants.

## Impact and Post-Chinchilla Developments

The Chinchilla paper fundamentally changed how the industry trains LLMs. Post-Chinchilla models (Llama, Mistral) often overtrain relative to Chinchilla-optimal because inference cost savings from smaller models justify higher training compute. The "inference-optimal" perspective extends Chinchilla to account for deployment costs.
