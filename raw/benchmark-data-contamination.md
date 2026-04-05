---
title: "When Benchmarks Lie: Why Contamination Breaks LLM Evaluation"
source: "https://thegrigorian.medium.com/when-benchmarks-lie-why-contamination-breaks-llm-evaluation-1fa335706f32"
author: "Anna Alexandra Grigoryan"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [data-contamination, benchmark-leakage, evaluation, training-data, decontamination]
type: article
status: raw
discovered_via: search
---

# Benchmark Data Contamination

## What Is Data Contamination?

Occurs when benchmark datasets leak into an LLM's training corpus. When a model has seen benchmark questions during training, its performance reflects memorization, not generalization.

## How It Happens

Web-scale training datasets include scraped content, books, papers, forums, and code. Public benchmarks (MMLU, ARC-Challenge, TruthfulQA, GSM8K) are freely available online and likely appear in training corpora verbatim or in near-identical forms.

## Consequences

1. Loss of diagnostic power: benchmarks no longer reveal genuine reasoning or generalization
2. Biased comparisons: different models have varying contamination levels, making fair comparison impossible

## Mitigation Strategies

### Semantic-Preserving (Single)
Typo insertion, synonym substitution, syntactic reordering, back-translation, choice shuffling, distractor injection. High fidelity (~0.90) but zero resistance.

### Semantic-Preserving (Combined)
Stacking multiple transformations (CleanEval, ITD, MPA). Improved resistance (~0.89) but lower fidelity (0.686).

### Semantic-Altering
LLM-generated questions via mimicking, application extension, comparative analysis. High resistance (>0.95) but low fidelity (0.66-0.75).

## The Fidelity-Resistance Tradeoff

Fundamental tension: no strategy achieves both high resistance AND high fidelity.
- Surface edits maintain validity but fail to prevent memorization
- Deep transformations block contamination but distort the original task

## Key Findings

- Previous evaluations relying on accuracy drop metrics were "over-optimistic"
- Question-level metrics reveal inconsistencies masked by aggregate statistics
- LessLeak-Bench: cleaned benchmark removing identified leaks across Java, C/C++, Python
- Inference-Time Decontamination (ITD): detects and rewrites leaked samples without altering difficulty

## Recommendations

- Develop high-fidelity paraphrasing constrained by semantic similarity
- Release benchmark variants with documented fidelity/resistance scores
- Build contamination-aware training and evaluation pipelines
- Interpret public benchmark results cautiously
