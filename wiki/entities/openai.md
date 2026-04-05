---
title: "OpenAI"
type: entity
entity_type: org
sources: ["[[sources/lightman-lets-verify-step-by-step]]", "[[sources/adaline-inside-reasoning-models]]"]
related: ["[[concepts/reasoning-models]]", "[[concepts/process-reward-models]]", "[[concepts/test-time-compute]]", "[[entities/deepseek]]"]
last_compiled: 2026-04-05
summary: "AI research company behind GPT-4, o1, and o3 reasoning models -- pioneers of process reward models (PRM800K), scaled reinforcement learning for reasoning, and test-time search with deliberative alignment."
---

## Overview

OpenAI is the AI research organization that has been at the forefront of both large language model development (GPT series) and reasoning model development (o1, o3 series). Their contributions to LLM reasoning include:

## Key Contributions to Reasoning

### Process Reward Models
- Published "Let's Verify Step by Step" (Lightman et al., 2023), establishing that process supervision outperforms outcome supervision.
- Released PRM800K: 800,000 step-level human feedback labels.
- PRMs became a key building block of the reasoning model paradigm.

### Reasoning Models (o1, o3)
- **o1** (2024): First major reasoning model. Hidden chain-of-thought, RL-trained.
- **o3** (2025): Second generation. Dense transformer with scaled RL, deliberative alignment, test-time search via beam search / MCTS.
- **o3-mini**: 15x cheaper and 5x faster than o1 with comparable performance.
- Training cost: 1.2M A100 GPU hours.
- Benchmark results: AIME 96.7%, SWE-bench 71.7%, GPQA Diamond ~87.7%.

### Architectural Approach
- Dense transformer architecture (all parameters active).
- Hidden chain-of-thought (reasoning not visible to users).
- Test-time search: multiple candidate CoTs evaluated at inference.
- Deliberative alignment: safety checking within the reasoning chain.

## Mentioned In

- [[sources/lightman-lets-verify-step-by-step]] -- authored by OpenAI researchers
- [[sources/adaline-inside-reasoning-models]] -- technical analysis of o3
