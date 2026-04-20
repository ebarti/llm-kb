---
title: "What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models"
source: "https://arxiv.org/abs/2503.24235"
author: "Zhang et al."
date_published: 2025-03-31
date_ingested: 2026-04-05
tags: [test-time-compute, inference-scaling, reasoning, survey, scaling-laws]
type: paper
status: raw
discovered_via: search
---

# What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models

Comprehensive survey organizing TTS research along four dimensions.

## Core Framework: Four Dimensions

### 1. What to Scale
- **Parallel Scaling**: Generates multiple outputs in parallel and aggregates them into a final answer.
- **Sequential Scaling**: Directs later computations based on intermediate reasoning steps.
- **Hybrid Scaling**: Combines parallel and sequential approaches.
- **Internal Scaling**: Allows models to autonomously determine computational allocation during inference.

### 2. How to Scale

**Tuning Methods:**
- Supervised Fine-Tuning: Training on extended chain-of-thought examples.
- Reinforcement Learning: Guides models toward longer or more accurate solutions.

**Inference Methods:**
- **Stimulation**: Encourages generating more and longer samples.
- **Verification**: Selects outputs, guides exploration, or weights aggregation.
- **Search**: Systematically explores potential outputs (beam search, MCTS, tree search).
- **Aggregation**: Consolidates multiple solutions into final decisions.

### 3. Where to Scale
**Reasoning Tasks**: Mathematics, coding, science, game strategy, medical applications.
**General-Purpose Tasks**: Q&A, agents, knowledge tasks, multi-modal reasoning.

### 4. How Well to Scale
- **Performance**: Correctness and robustness metrics.
- **Efficiency**: Cost-benefit tradeoffs.
- **Controllability**: Adherence to compute budgets or output constraints.
- **Scalability**: Improvement rates with increased test-time compute.

## Key Techniques Catalogued (30+ major papers)

| Technique | Scale Type | Primary Methods | Applications |
|-----------|-----------|-----------------|--------------|
| DeepSeek-R1 | Internal | RL (GRPO) | Math, Code, Science |
| Tree of Thoughts | Hybrid | Tree search, self-evaluation | Games, open-ended reasoning |
| rStar-Math | Hybrid | MCTS, process reward models | Mathematics |
| Archon | Hybrid | Multi-agent, verification ensemble | Math, code, general tasks |

## Major Findings
- Test-time computation can outperform parameter scaling in specific reasoning domains.
- Verifier models serve multiple roles: selection, guidance, and weighting.
- Multi-agent approaches emerging as effective for both verification and generation.
- Token cost and latency tradeoffs vary significantly by method.

Website: https://testtimescaling.github.io/
GitHub: https://github.com/testtimescaling/testtimescaling.github.io
