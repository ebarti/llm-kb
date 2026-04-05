---
title: "World Models vs LLMs"
type: comparison
subjects: ["[[concepts/world-models]]", "[[concepts/llm-world-understanding]]"]
sources: ["[[sources/world-models-race-2026]]", "[[sources/llms-and-world-models-mitchell]]"]
related: ["[[concepts/jepa]]", "[[entities/yann-lecun]]", "[[concepts/embodied-ai]]"]
tags: [world-models, LLMs, AGI, paradigm-comparison]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The fundamental AI paradigm debate: LLMs predict text tokens from statistical patterns (Sutskever: 'enough for world understanding'), while world models predict physical dynamics from sensory data (LeCun: 'language alone will never suffice') — with $1.3B+ bet on world models in 2026."
---

## Overview

The most consequential debate in AI (2024-2026): can scaling large language models produce genuine understanding of reality, or does AI need a fundamentally different architecture — [[concepts/world-models]] — that learns from physical interaction and visual observation rather than text? This comparison has real stakes: [[entities/ami-labs]] raised $1.03B betting on world models, while Anthropic and OpenAI continue betting on language model scaling.

## Comparison Matrix

| Dimension | LLMs | World Models |
|-----------|------|-------------|
| **Training data** | Text (language corpora) | Video, interaction, sensor data |
| **Prediction target** | Next token (word/subword) | Next state (latent representation) |
| **Physical understanding** | Implicit (from text about physics) | Explicit (learned from observation) |
| **Causal reasoning** | Correlational (statistical patterns) | Causal (intervention and prediction) |
| **Temporal consistency** | Limited (no persistent state) | Core feature (maintained world state) |
| **Grounding** | Ungrounded (symbols only) | Grounded (in sensory experience) |
| **Interactivity** | None (generates text) | Core feature (action → state change) |
| **Inference cost** | 1-8 GPUs/request | 8-32 GPUs/request |
| **Training cost** | Hundreds-thousands GPUs | Thousands-tens of thousands GPUs |
| **Maturity** | Production-ready (2024+) | Research/early deployment (2026) |
| **Applications** | Text, code, analysis | Robotics, AV, simulation |
| **Leading labs** | OpenAI, Anthropic, Google | AMI Labs, DeepMind, NVIDIA |
| **Funding (2025-2026)** | $100B+ total | $1.3B+ dedicated |

## Analysis

### The Case for LLMs as World Models

Ilya Sutskever and the scaling camp argue that LLMs develop "compressed, abstract, usable representations" of the world through next-word prediction. Evidence includes:
- Othello-GPT develops internal board state representations
- Emergent reasoning improves with scale
- Language inherently encodes causal relationships
- LLMs handle some spatial/physical reasoning tasks

### The Case Against

LeCun and the dedicated world model camp argue:
- Text is a lossy, 1D projection of multidimensional reality
- No sensorimotor grounding or causal intervention
- LLMs have no notion of time or state persistence
- 2024 mathematical proof: LLMs cannot learn all computable functions
- Pre-LLM systems routinely learned superficial shortcuts (skin lesion/ruler, Atari pixel shift)

### The Orrery Framework

Mitchell's analysis suggests LLMs achieve at most "orrery-like" capability — tracking narrative dynamics without true causal simulation. For genuine [[concepts/world-models]], a system needs:
1. Internal representations of external phenomena
2. Preserved causal structure (not just correlations)
3. Algorithmic efficiency for prediction and counterfactuals

### The Convergence Path

Neither pure LLMs nor pure world models may be the answer. The emerging approach combines both:
- Language models for high-level reasoning and communication
- World models for physical understanding and planning
- Joint MLLM + WM architectures bridging semantic and physical intelligence

## When to Use Each

| Scenario | Recommendation |
|----------|---------------|
| Text generation, analysis, coding | LLMs (mature, production-ready) |
| Robotic planning and control | World models (V-JEPA 2, DreamerV3) |
| Autonomous driving simulation | World models (Cosmos, GAIA-2) |
| General question answering | LLMs (world models add no value here) |
| Interactive environment generation | World models (Genie 3) |
| Physical reasoning tasks | World models (LLMs fail on benchmarks) |
| Multimodal understanding | Hybrid (VLMs + world models) |

## Sources

- [[sources/world-models-race-2026]] — competitive landscape and funding
- [[sources/llms-and-world-models-mitchell]] — the philosophical framework
