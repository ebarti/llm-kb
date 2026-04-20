---
title: "RLHF and Alternatives: KTO (Kahneman-Tversky Optimization)"
source: "https://argilla.io/blog/mantisnlp-rlhf-part-7/"
author: "MantisNLP / Argilla"
date_published: 2024-05-01
date_ingested: 2026-04-05
tags: [kto, alignment, prospect-theory, kahneman, preference-optimization]
type: article
status: raw
discovered_via: search
---

# KTO: Kahneman-Tversky Optimization

## Theoretical Foundation
Based on Prospect Theory (Kahneman and Tversky): humans assess gains and losses asymmetrically. Loss aversion means emotional impact of losses exceeds equivalent gains.

## HALO Framework
Researchers framed alignment methods as HALOs (Human-Aware Loss functions) or non-HALOs. HALOs, which model human biases, matched or outperformed non-HALOs at 13B+ parameter scales.

## Data Requirements
Major advantage: requires only binary signals (desirable/undesirable), not preference pairs.
- Uses more abundant, cheaper-to-collect data
- Avoids noisy preference annotation issues
- Performs well with imbalanced desirable/undesirable examples
- KTO-aligned Llama-7B outperformed DPO even when 90% of desirable examples discarded

## Loss Function
- Directly maximizes generation utility using Kahneman-Tversky value functions
- Adds KL penalty that rises when model increases reward for desirable examples generically
- Forces model to learn what makes outputs desirable while maintaining flat KL divergence

## Experimental Results
- Superior or comparable to DPO across 1B-30B parameter scales
- Without prior SFT: DPO-aligned models rambled and hallucinated; KTO avoided this
- KTO alone matched SFT + DPO combined on Llama models
- Better performance on noisy, real-world datasets

## When to Use Each

**KTO**: Binary feedback available, imbalanced data, no prior SFT, noisy datasets
**DPO**: Clean preference pair data with low noise and high transitivity
**RLHF**: When explicit reward modeling is beneficial; increasingly superseded

## Key Insight
DPO works better with clean, transitive data, but KTO's worst-case guarantees excel when noise is present -- matching most real-world scenarios.
