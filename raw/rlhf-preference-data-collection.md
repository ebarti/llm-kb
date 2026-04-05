---
title: "Preference Data — RLHF Book by Nathan Lambert"
source: "https://rlhfbook.com/c/06-preference-data"
author: "Nathan Lambert"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [rlhf, preference-data, human-feedback, alignment, reward-model]
type: article
status: raw
discovered_via: search
---

# Preference Data for RLHF

## What Is Preference Data?

The foundational signal for RLHF systems. Rather than defining explicit reward functions for human values — effectively impossible — preference data captures relative judgments between model outputs. It is far easier to differentiate between a good and bad answer than to generate a good answer from scratch.

Critical nuance: the chosen response isn't necessarily globally correct, but better relative to alternatives shown.

## Collection Methods

### Interface Types
- Pairwise comparison: select between two completions (most common)
- Likert scales: A>>B, A>B, Tie, B>A, B>>A
- Unary feedback: thumbs up/down from production systems
- Arena-style: head-to-head with tie options

### Rankings vs Ratings
Rankings: relative orderings between completions (dominant approach).
Ratings: absolute scores (1-5) to individual responses. Can be converted to pairwise preferences.

## Data Format

Standard chosen/rejected pairs: prompt + chosen completion + rejected completion + optional metadata.

Multi-turn: preferences on final responses; conversations unrolled into many training prompts with prior turns masked.

## Major Public Datasets

- Anthropic HH-RLHF: 170K human preference comparisons (helpful + harmless + red teaming)
- HelpSteer2 (NVIDIA): largest recent human preference dataset
- UltraFeedback: ratings-to-pairs conversion methodology

Note: "there are no open models with fully open human preference data released with the methods used to collect it."

## On-Policy vs Off-Policy

On-policy data (from current model checkpoint) is crucial — different models have different generation patterns, making closely-related model data more robust. Significantly outperforms aggregated off-the-shelf datasets. Requires live endpoints during training phases.

## Quality and Bias

Common biases: prefix bias, sycophancy, verbosity bias, formatting bias. All readily transfer to final models.

Quality metrics: inter-annotator agreement, consistency checks, iterative refinement (early batches expect higher rejection rates).

## Operational Complexity

Collection involves: vendor selection (supply-constrained market), contract negotiation, phased delivery (weekly batches over 6+ weeks), quality iteration.

"Millions of dollars spent on these datasets are 'wasted' and not used in the final models" — reflecting iterative nature.

## Unresolved Questions

- Whether pairwise preferences adequately capture human preferences
- Minimum annotator population sizes for demographic representation
- How workplace context influences professional annotators
- Optimal balance between human and AI feedback signals
