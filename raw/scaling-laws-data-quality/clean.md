---
title: "Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining"
source: "https://arxiv.org/abs/2510.03313"
author: "Various"
date_published: 2025-10-06
date_ingested: 2026-04-05
tags: [scaling-laws, data-quality, chinchilla, training-data, compute-optimal]
type: paper
status: raw
discovered_via: search
---

# Scaling Laws Revisited: Data Quality

## Core Framework

Introduces a quality-aware scaling law extending the Chinchilla framework:

L(N,D,Q) = A/N^α + B/(D^β · Q^γ) + E

Where N = model parameters, D = dataset size, Q = data quality (0,1], γ = empirically measured quality sensitivity exponent.

## Key Innovation

Traditional scaling laws are agnostic to data quality. This work formalizes how imperfect corpora (noise, redundancy, domain imbalance) affect performance through a dimensionless quality parameter. Q=1 is fully clean data; smaller values reflect corruption/redundancy.

## Theoretical Grounding

Two derivation perspectives:
1. Effective Sample Size: D_eff = D·g(Q), where g(Q) ≈ Q^γ
2. Information-Theoretic: Corruption reduces mutual information multiplicatively: I(X̃;Z) = ρ(Q)·I(X;Z)

## Quality Measures

Two practical estimators:
1. Corruption Rate: Q(ω) = 1 - CR
2. Data Deficiency: Q(ω) = exp(-Δ), aggregating noise, coverage gaps, redundancy, synthetic data issues

## Experimental Results

- Sublinear Quality Decay: γ ≈ 0.17 (NMT) and γ ≈ 0.40 (CLM) — models are more robust to moderate corruption than simple effective sample-size theories predict
- Loss predictability: test loss scales predictably across quality levels (Q from 0.5 to 1.0)

## Practical Implications

- Higher data quality → increased compute budget should be allocated to model scaling
- High-quality data reduces required model size and compute
- A billion high-quality tokens may be far more valuable than a billion noisy ones
- Particularly impactful for resource-constrained specialized applications

## Practitioner Recipe

1. Establish high-quality baseline reference (Q ≈ 1)
2. Select domain-relevant quality proxies
3. Compute deficiency scores
4. Map to Q via exponential transformation
5. Validate correlation with downstream performance
6. Fit scaling law parameters using robust Huber loss
