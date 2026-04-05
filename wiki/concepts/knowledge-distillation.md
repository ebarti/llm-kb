---
title: "Knowledge Distillation"
type: concept
sources: ["[[sources/llm-knowledge-distillation-survey]]", "[[sources/textbooks-are-all-you-need-phi]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/synthetic-data-generation]]", "[[concepts/parameter-efficient-fine-tuning]]"]
last_compiled: 2026-04-05
summary: "Transferring capabilities from large teacher models to small student models via logit matching, feature mimicry, or rationale extraction — enabling deployment-friendly models at a fraction of the cost."
---

## Overview

Knowledge distillation is a model compression technique where a smaller "student" model is trained to replicate the behavior of a larger "teacher" model. In the LLM era, distillation has become the primary mechanism for democratizing AI capabilities — transferring knowledge from proprietary models (GPT-4, Claude) to open-source models (LLaMA, Mistral) that can be deployed locally.

Distillation is intimately connected to [[concepts/synthetic-data-generation]]: the teacher model's outputs on prompts constitute synthetic training data for the student. The distinction is mainly one of framing — distillation emphasizes the teacher-student relationship, while synthetic data generation emphasizes the data pipeline.

## Methods

### White-Box Distillation
The student has access to the teacher's internal representations:
- **Logit-based**: Student learns from teacher's probability distribution over the full vocabulary (soft targets), not just the argmax prediction
- **Feature-based**: Student mimics intermediate hidden states and attention patterns
- **Requires**: Access to model internals — only possible with open-source teachers

### Black-Box Distillation
The student only sees the teacher's final outputs:
- **Output mimicry**: Train student on (input, teacher_output) pairs
- **Rationale-based**: Extract chain-of-thought reasoning from teacher, train student on reasoning steps (Google's "Distilling Step-by-Step")
- **Most practical**: Works with proprietary API-only models (GPT-4, Claude)

### Beyond Distillation
[[entities/microsoft-phi]]'s phi-4 demonstrates that careful synthetic data generation combined with rigorous filtering can produce students that surpass their teachers on specific benchmarks. This suggests that distillation is not just knowledge transfer but can be a form of knowledge amplification when combined with quality curation.

## Key Results

- **Distilling Step-by-Step** (Google): 770M T5 model outperforms 540B PaLM on some tasks using rationale-based distillation with less training data
- **MiniLLM** (ICLR 2024): On-policy distillation improves over standard KD by training the student on its own output distribution
- **Phi-4**: Surpasses GPT-4 teacher on STEM benchmarks through strategic synthetic data incorporation

## Practical Applications

1. **Cost reduction**: Replace expensive API calls with small local models
2. **Latency**: Smaller models serve faster responses
3. **Privacy**: Run models on-premise without sending data to third-party APIs
4. **Edge deployment**: Models small enough for mobile and embedded devices
5. **Democratization**: Open-source alternatives to proprietary models

## Connection to LLM Knowledge Bases

In a [[concepts/llm-knowledge-base]] system, distillation enables:
- Creating small, fast models specialized for wiki compilation tasks
- Training domain-specific Q&A models from general-purpose teachers
- Building edge-deployable knowledge assistants from cloud-scale models
- Reducing the cost of running continuous linting and health checks

## Sources

- [[sources/llm-knowledge-distillation-survey]] — methods overview and practical benefits
- [[sources/textbooks-are-all-you-need-phi]] — distillation-and-beyond with phi models

## Related Concepts

- [[concepts/synthetic-data-generation]] — distillation outputs are synthetic training data
- [[concepts/fine-tuning]] — distillation is specialized supervised fine-tuning
- [[concepts/parameter-efficient-fine-tuning]] — complementary compression technique
- [[concepts/model-collapse]] — risk when distilling from models already trained on synthetic data
