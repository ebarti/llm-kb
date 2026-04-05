---
title: "DeepSeek V3"
type: entity
entity_type: tool
sources: ["[[sources/training-costs-2026-analysis]]"]
related: ["[[concepts/llm-training-costs]]", "[[concepts/llm-pretraining]]", "[[concepts/5d-parallelism]]"]
last_compiled: 2026-04-05
summary: "Chinese AI lab's 671B-parameter MoE model trained for a reported $5.6M — challenging the assumption that frontier LLMs require $100M+ budgets, though the figure excluded infrastructure, experimentation, and failed runs."
---

## Overview

DeepSeek V3 is a Mixture-of-Experts (MoE) language model with 671B total parameters (37B active per token) developed by Chinese AI lab DeepSeek. It achieved frontier-level performance at a reported training cost of just $5.5-5.6 million, making it one of the most cost-efficient large language models ever trained.

## Significance

The $5.6M figure was a watershed moment for the industry, demonstrating that algorithmic innovation (novel MoE architecture, multi-head latent attention, FP8 mixed-precision training) could dramatically reduce the cost of frontier model training. However, critics noted the figure excluded:
- Infrastructure costs (the GPUs were presumably already available)
- Research and experimentation costs leading to the final architecture
- Failed training runs and hyperparameter searches

## Architecture Innovations

- Mixture-of-Experts with fine-grained routing
- Multi-head latent attention for memory efficiency
- FP8 training for further compute savings
- Novel load-balancing without auxiliary loss

## Impact

DeepSeek V3 (and its reasoning variant DeepSeek-R1) pushed other labs to focus more on efficiency and less on raw scale. It demonstrated that the cost curve for frontier AI can be bent by architectural innovation, not just by building bigger clusters.

## Mentioned In

- [[sources/training-costs-2026-analysis]] — $5.6M training cost analysis
