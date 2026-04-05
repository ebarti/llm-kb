---
title: "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls"
source: "https://arxiv.org/abs/2510.01631"
author: "Various"
date_published: 2025-10-02
date_ingested: 2026-04-05
tags: [synthetic-data, scaling-laws, model-collapse, pre-training, data-mixture]
type: paper
status: raw
discovered_via: search
---

# Demystifying Synthetic Data in LLM Pre-training

## Scope

Over 1,000 language model variants (up to 3B parameters) trained on datasets up to 200B tokens, consuming 100,000+ GPU hours.

## Data Types Examined

- Web rephrasing: high-quality (HQ) and question-answering (QA) formats
- Synthetic textbooks (TXBK) mimicking educational materials

## The Crucial 1/3 + 2/3 Discovery

Training on 1/3 rephrased synthetic data mixed with 2/3 natural web texts speeds up 5-10x in reaching target validation loss at larger data budgets. This mixture substantially outperformed both pure synthetic and pure natural baselines.

## Rephrased vs Textbook Data

Rephrased: Pure rephrased alone provided no speed advantage. Mixing ratios showed low sensitivity — both 33% and 67% similar results. HQ rephrasing optimal at ~30%.

Textbook: Pure textbook exhibited notably higher loss on many downstream domains at small data budgets. Required lower synthetic percentages (33% optimal over 67%). Required larger scales to show advantages.

## Scaling Laws

- Pure synthetic data is NOT superior to CommonCrawl
- Mixtures outperform both pure types
- 33% HQ rephrased + 67% CC shows lowest projected irreducible loss
- Synthetic data less favorable for model scaling than data scaling
- Larger models show reduced tolerance for high synthetic ratios

## Model Collapse Assessment

Rephrased data: No degradation at foreseeable scales.
Textbook data: Shows patterns predicted by model collapse, especially with limited data.

## Generator Model Size

Counterintuitive finding: 8B-parameter generators consistently outperform both smaller (3B) and larger (70B) models. Larger generators sometimes perform worse.

## Practical Recommendations

1. Target ~30% high-quality rephrased + 70% natural web text
2. Never rely entirely on synthetic data
3. Use ~8B parameter generators
4. Prioritize rephrased over textbook-style generation
5. Benefits conditional on deployment context
6. Empirical validation always required
