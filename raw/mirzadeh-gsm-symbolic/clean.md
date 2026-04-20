---
title: "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"
source: "https://arxiv.org/abs/2410.05229"
author: "Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar"
date_published: 2024-10-07
date_ingested: 2026-04-05
tags: [mathematical-reasoning, GSM8K, benchmarks, limitations, pattern-matching]
type: paper
status: raw
discovered_via: search
---

# GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

ICLR 2025

## Key Findings

1. **Numerical sensitivity**: Models show noticeable variance when responding to different instantiations of the same question. Simply changing numerical values in GSM8K-style problems causes measurable performance degradation across all tested models.

2. **Fragility with complexity**: Performance deteriorates significantly as the number of clauses in a question increases, suggesting models cannot execute authentic logical reasoning.

3. **Susceptibility to irrelevant information**: Adding a single contextually relevant but mathematically unnecessary clause triggers significant performance drops (up to 65%) across state-of-the-art models.

4. **Pattern matching, not reasoning**: The paper's central hypothesis is that current LLMs "replicate reasoning steps from their training data" rather than performing genuine logical reasoning.

## Methodology: GSM-Symbolic Benchmark

- Created a symbolic template-based benchmark enabling more controllable evaluations.
- Templates allow generating diverse question instantiations from the same underlying problem structure.
- GSM-NoOp variant: adds irrelevant information to test distractor susceptibility.
- Enables systematic testing of whether models truly understand the reasoning vs. pattern-matching from training data.

## Specific Results

- High performance variance across different numerical instantiations of the same problem.
- Significant drop in performance with slight difficulty increases.
- Models incorporate irrelevant numerical information into calculations (GSM-NoOp finding).
- Performance correlates with answer probability -- models are more accurate when the correct answer is a high-probability sequence.

## Implications

This paper is a key piece of evidence in the debate about whether LLMs truly reason. The findings suggest that even impressive GSM8K scores may reflect sophisticated pattern matching rather than genuine mathematical understanding. The fragility to minor variations is particularly damning -- a true reasoner would not be derailed by changing numbers or adding irrelevant context.
