---
title: "Chinchilla Data-Optimal Scaling Laws: In Plain English"
source: "https://lifearchitect.ai/chinchilla/"
author: "Life Architect"
date_published: 2023-06-01
date_ingested: 2026-04-05
tags: [scaling-laws, chinchilla, compute-optimal, training-tokens, parameters]
type: article
status: raw
discovered_via: search
---

# Chinchilla Data-Optimal Scaling Laws

## Core Findings

The Chinchilla scaling laws, published by DeepMind in September 2022, fundamentally challenged prior assumptions about training large language models. Unlike the earlier Kaplan/GPT-3 approach, Chinchilla established that achieving optimal performance requires substantially more training data relative to model parameters.

## Key Metrics Comparison

GPT-3/Kaplan Scaling (May 2020):
- Ratio: 1.7 tokens per parameter
- Example: 300B tokens trained a 175B parameter model

Chinchilla/Hoffman Scaling (Sep 2022):
- Ratio: 20 tokens per parameter
- Example: 1.4T tokens optimally trained a 70B parameter model

This represents an 11x increase in data requirements for equivalent model performance.

## Practical Implications

A 175B parameter model using Kaplan's approach should have been trained with 3,500B (3.5T) tokens under Chinchilla standards — roughly 4-6TB of textual data depending on tokenization methods.

Training a 1T-parameter model requires approximately 20 trillion tokens, equivalent to consuming "all materials in the US Library of Congress," containing around 66.6 million books worth of text.

## Evolution of Understanding (2023-2024)

Subsequent research revealed variations:
- Mosaic (Dec 2023): 190:1 ratio, emphasizing inference costs
- DeepSeek (Jan 2024): 30:1 ratio, highlighting data quality importance
- Tsinghua (Apr 2024): 192:1 ratio for small models
- Llama 3 (Apr 2024): Extreme 1,875:1 ratio, suggesting massive overtrain for inference efficiency

## 2025 Update

Qwen3-0.6B achieved a record 60,000:1 tokens-to-parameters ratio, representing unprecedented training data intensity for compact models.

## Core Principle

For compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. Both parameters and training tokens scale with the cube root of the training compute.
