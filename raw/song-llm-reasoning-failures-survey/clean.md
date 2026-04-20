---
title: "Large Language Model Reasoning Failures: A Survey"
source: "https://arxiv.org/abs/2602.06176"
author: "Peiyang Song, Pengrui Han, Noah Goodman"
date_published: 2026-02-05
date_ingested: 2026-04-05
tags: [reasoning-failures, survey, limitations, taxonomy, robustness]
type: paper
status: raw
discovered_via: search
---

# Large Language Model Reasoning Failures: A Survey

TMLR 2026 (Survey Certification)

## Taxonomy of Reasoning

The survey distinguishes:
- **Embodied reasoning**: Physical/experiential reasoning about the world.
- **Non-embodied reasoning**: Split into:
  - **Informal (intuitive)**: Commonsense, analogical, abductive reasoning.
  - **Formal (logical)**: Deductive, inductive, mathematical reasoning.

## Three Types of Failures

1. **Fundamental failures**: Intrinsic to LLM architectures, broadly affecting downstream tasks.
   - Next-token optimization biases toward locally coherent, statistically plausible continuation rather than constraint satisfaction or stepwise deductive logic.
   - Self-attention and positional encoding induce surface-level pattern-matching over global compositional structure.

2. **Application-specific limitations**: Domain-particular weaknesses.
   - Compositional and disjunctive reasoning failures.
   - Multi-path tasks (disjunctive/intersection) systematically fail.
   - Graph coloring: models hallucinate non-existent problem features, causing cascading logical failures.

3. **Robustness issues**: Inconsistent performance across minor input variations.
   - Performance varies significantly with superficial changes to problem presentation.
   - Models treat paths independently or output plausible answers by frequency heuristics rather than performing algebraic closure.

## Architectural Root Causes

- Training biases toward local pattern completion over global logical planning.
- Limitations in working memory and sequential reasoning due to self-attention dispersion.
- Tokenization artifacts that destabilize token-level manipulations.
- Optimization for next-token likelihood, not constraint satisfaction.

## Mitigation Strategies

For each identified failure, the survey provides: clear definition, analysis of existing studies, exploration of root causes, and mitigation strategies.

## Resources

Accompanied by GitHub repository "Awesome-LLM-Reasoning-Failures" with curated research works.
