---
title: "From System 1 to System 2: A Survey of Reasoning Large Language Models"
source: "https://arxiv.org/abs/2502.17419"
author: "Zhong-Zhi Li et al."
date_published: 2025-02-24
date_ingested: 2026-04-05
tags: [system-1, system-2, dual-process, reasoning-models, survey]
type: paper
status: raw
discovered_via: search
---

# From System 1 to System 2: A Survey of Reasoning Large Language Models

## Dual-Process Theory Applied to LLMs

Based on Kahneman's framework:

- **System 1 (Fast/Intuitive)**: Standard LLMs directly output a response by forwarding input through model layers. Quick, low-cost, but prone to biases and errors on complex tasks.
- **System 2 (Slow/Deliberate)**: Reasoning LLMs employ intermediate reasoning steps. Higher computational cost but superior results on structured, multi-step tasks.

## Key Models Examined

- **OpenAI o1/o3**: Trained with scaled reinforcement learning, hidden chain-of-thought, test-time search.
- **DeepSeek R1**: 4-phase training (cold start, GRPO RL, rejection sampling, diverse RL). Uses Mixture-of-Experts architecture.
- **Claude 3.7 Sonnet**: Extended thinking mode with configurable thinking budget.

## Training Methodologies for System 2

1. **Pure Reinforcement Learning**: DeepSeek-R1-Zero showed RL alone can produce emergent reasoning without supervised fine-tuning.
2. **RL + Supervised Fine-Tuning**: More stable training combining RL with curated reasoning examples.
3. **SFT + Distillation**: Training smaller models on reasoning traces from larger models.
4. **Inference-time scaling**: Chain-of-thought, tree search, process reward model selection.

## Performance Differences

- System 2 models excel at: arithmetic, symbolic reasoning, mathematical proofs, competitive programming.
- System 1 models are effective for: intuitive judgments, commonsense reasoning, simple factual questions.
- Hybrid approach (toggle on/off as in Claude 3.7) seen as promising direction.

## The Transition

The survey traces the evolution:
1. Pre-trained LLMs (System 1 only)
2. CoT prompting (System 2 via prompting)
3. Fine-tuned reasoning models (System 2 via training)
4. RL-trained reasoning models (System 2 via reinforcement learning)

Each stage represents deeper internalization of deliberate reasoning capabilities.
