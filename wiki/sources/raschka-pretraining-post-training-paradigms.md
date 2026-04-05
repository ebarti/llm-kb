---
title: "Source: New LLM Pre-training and Post-training Paradigms"
type: source-summary
source: "[[raw/raschka-pretraining-post-training-paradigms]]"
related: ["[[concepts/llm-pretraining]]", "[[concepts/multi-stage-pretraining]]", "[[concepts/knowledge-distillation]]", "[[entities/llama]]"]
last_compiled: 2026-04-05
summary: "Sebastian Raschka's analysis of 2024 training pipelines across Qwen 2, Apple AFM, Gemma 2, and Llama 3.1 — identifying trends: multi-stage pretraining, knowledge distillation, DPO over PPO, synthetic data, and model averaging."
---

## Key Points

- Llama 3.1: 15.6T tokens (up from 2T in Llama 2), three-stage pretraining to 128k context
- Apple AFM: three stages — 6.3T core + 1T continued (math/code up-weighted) + 100B context extension
- Gemma 2 27B: 13T tokens, reward model 10x larger than policy model
- Qwen 2: 7T tokens, 30 languages, 151K vocabulary
- All four models use multi-stage pretraining with context extension phases
- DPO and rejection sampling replacing pure RLHF/PPO for post-training

## Detailed Summary

Raschka compares four state-of-the-art 2024 model training pipelines, revealing convergent strategies:

**[[concepts/multi-stage-pretraining]]** is universal:
1. Core pretraining on diverse web data
2. Continued pretraining with up-weighted quality data (math, code)
3. Context length extension using synthetic long-context data

**[[concepts/knowledge-distillation]]** is pervasive: Apple used a 6.4B teacher for its 3B device model; Gemma used distillation for smaller variants. This enables efficient deployment on constrained hardware.

**Data quality over quantity**: All four teams emphasize curation and filtering over raw scale. Qwen and Llama both used previous-generation models to synthesize additional training data.

**Post-training convergence**: Direct preference optimization and rejection sampling have largely replaced pure RLHF/PPO, cited as more stable and scalable.

**Model averaging**: Both Gemma and Llama merge checkpoints to stabilize and improve performance across training iterations.

## Related Concepts

- [[concepts/llm-pretraining]] — the core training process
- [[concepts/multi-stage-pretraining]] — the phased approach
- [[concepts/knowledge-distillation]] — teacher-student training
- [[entities/llama]] — Meta's model family
