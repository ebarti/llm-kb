---
title: "Source: Inference-Time Scaling -- The Paradigm Shift from Training to Inference"
type: source-summary
source: "[[raw/introl-inference-time-scaling-paradigm-shift]]"
related: ["[[concepts/training-vs-inference-compute]]", "[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]", "[[entities/deepseek-r1]]"]
tags: [paradigm-shift, inference-scaling, infrastructure, economics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "December 2025 analysis of the training-to-inference paradigm shift: 7B + 100x inference compute matches 70B; inference projected to exceed training demand by 118x by 2026; covers DeepSeek-R1, P1, ThreadWeaver breakthroughs."
---

## Key Points

- 7B parameters + 100x inference compute can match 70B parameter models with standard inference.
- Inference projected to exceed training compute demand by 118x by 2026.
- OpenAI 2024 inference spending: $2.3B -- 15x the training cost for GPT-4.
- DeepSeek-R1: pure RL achieved o1-level reasoning; explicitly found PRMs and MCTS unsuccessful.
- P1 Physics: first open-source gold at International Physics Olympiad via test-time agent collaboration.
- ThreadWeaver: parallel reasoning paths with 1.53x latency speedup.
- EU AI Act's training compute thresholds create regulatory gap for inference-scaled models.

## Detailed Summary

Blake Crosley's analysis (Introl, December 2025) provides the most data-rich account of the [[concepts/training-vs-inference-compute]] paradigm shift. The core thesis: AI development has fundamentally inverted from "train bigger" to "reason harder."

Three breakthroughs illustrate the shift:
1. **DeepSeek-R1** achieved o1-level reasoning through pure RL with GRPO, at 70% lower cost. Notably, R1's team explicitly found that [[concepts/process-reward-models]] and [[concepts/mcts-llm-reasoning]] were less effective than pure RL with extended generation.
2. **P1 Physics Model** won International Physics Olympiad gold using "PhysicsMinions" -- specialized agents collaborating at test time.
3. **ThreadWeaver** introduced parallel reasoning paths (vs. sequential CoT), achieving 1.53x speedup.

The infrastructure implications are staggering: inference market growing from $106B (2025) to $255B (2030). NVIDIA states next-gen reasoning models demand 100x more compute. This creates a regulatory gap: the EU AI Act uses training compute thresholds, but inference-scaled models can exceed capability thresholds through test-time reasoning alone.

## Metadata

- **Author**: Blake Crosley (Introl)
- **Date Published**: 2025-12-15
- **Format**: article
- **URL**: https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025
