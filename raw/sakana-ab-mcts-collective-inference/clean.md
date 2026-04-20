---
title: "AB-MCTS: Inference-Time Scaling and Collective Intelligence for Frontier AI"
source: "https://sakana.ai/ab-mcts/"
author: "Sakana AI"
date_published: 2025-06-15
date_ingested: 2026-04-05
tags: [mcts, inference-scaling, test-time-compute, multi-model, collective-intelligence]
type: article
status: raw
discovered_via: search
---

# AB-MCTS: Adaptive Branching Monte Carlo Tree Search

## Core Method
AB-MCTS is an inference-time scaling algorithm enabling efficient trial-and-error across two search dimensions:
- **Depth**: Refines promising solutions.
- **Width**: Generates entirely new solutions.
Uses Thompson Sampling to probabilistically decide which direction to pursue at each step.

## Multi-LLM Cooperation
Multi-LLM AB-MCTS adds a third dimension: dynamically selecting which frontier model to employ. Maintains separate probability models for each LLM type, updated based on observed performance. Identifies which model excels at specific problem types and allocates computational resources accordingly.

Models with distinct training backgrounds build upon each other's work -- even when individual models fail, combining outputs can yield solutions.

## Performance Results (ARC-AGI-2)
- Single o4-mini with repeated sampling: 23% success rate.
- AB-MCTS with o4-mini: 27.5% success rate.
- Multi-LLM AB-MCTS (3 frontier models): 30%+ success rate.
- Tentative Pass@2 score: 19.2%.

## Significance
Demonstrates that inference performance can be enhanced through both systematic trial-and-error and deliberate model collaboration. Extends MCTS beyond single-model use to collective intelligence at inference time.
