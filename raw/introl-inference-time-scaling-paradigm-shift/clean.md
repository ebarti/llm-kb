---
title: "Inference-Time Scaling: The Paradigm Shift from Training to Inference"
source: "https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025"
author: "Blake Crosley"
date_published: 2025-12-15
date_ingested: 2026-04-05
tags: [inference-scaling, paradigm-shift, training-vs-inference, infrastructure, economics]
type: article
status: raw
discovered_via: search
---

# Inference-Time Scaling: The Paradigm Shift

December 2025 analysis of the shift from training-focused to inference-focused AI scaling.

## The Paradigm Shift
Traditional model invested compute during training (larger models, more data). New paradigm allocates compute during inference: models with 7B parameters plus 100x inference compute can match 70B parameter models with standard inference.

## Key Breakthroughs

### DeepSeek-R1
- Achieved reasoning matching OpenAI o1 through pure RL and extended CoT.
- AIME accuracy: 15.6% -> 71%, reaching 86.7% with majority voting.
- 70% lower inference cost than comparable systems.
- Used GRPO (Group Relative Policy Optimization).
- Explicitly found PRMs and MCTS unsuccessful; pure RL with extended outputs serves as implicit scaling.

### P1 Physics Model
- First open-source system to win gold at International Physics Olympiad (2025).
- Score: 21.2/30 points.
- Combines train-time RL with test-time "PhysicsMinions" agents for visual analysis, logical reasoning, and solution verification.

### ThreadWeaver
- Parallel reasoning paths instead of sequential CoT.
- 1.53x average latency speedup on math benchmarks while maintaining accuracy.
- Trie-based co-design enabling concurrent reasoning without modifying position embeddings.
- P-GRPO algorithm for joint accuracy-latency optimization.

## Infrastructure Implications
- Inference projected to exceed training compute demand by 118x by 2026.
- Inference claiming 75% of total AI compute by 2030.
- AI inference market: $106B (2025) -> $255B (2030) at 19.2% CAGR.
- OpenAI 2024 inference spending: $2.3B -- 15x the training cost for GPT-4.
- NVIDIA: next-gen reasoning models demand up to 100x more computational resources.

## Regulatory Gap
Current EU AI Act uses training compute thresholds (10^25 FLOPs). Inference-time scaling creates a regulatory gap: smaller models can exceed capability thresholds through test-time reasoning alone.
