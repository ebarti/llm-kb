---
title: "Source: LLM Distillation Explained"
type: source-summary
source: "[[raw/llm-knowledge-distillation-survey]]"
related: ["[[concepts/knowledge-distillation]]", "[[concepts/fine-tuning]]", "[[concepts/synthetic-data-generation]]"]
last_compiled: 2026-04-05
summary: "Overview of LLM knowledge distillation: teacher-student paradigm, white-box vs. black-box methods, rationale-based distillation, and practical deployment benefits."
reading_time: "2 min"
---

## Key Points

- Knowledge distillation: smaller student model trained to mimic larger teacher model
- White-box distillation: student accesses teacher internals (hidden states, attention patterns)
- Black-box distillation: student only sees teacher's final outputs — practical for proprietary models
- Three approaches: logit-based, feature-based, rationale-based ("Distilling Step-by-Step")
- Rationale-based: extract reasoning steps as natural language, train small models more data-efficiently
- Key application: transferring capabilities from proprietary (GPT-4) to open-source (LLaMA, Mistral)
- MiniLLM (ICLR 2024): on-policy distillation outperforms standard KD approaches

## Detailed Summary

Knowledge distillation has become the primary mechanism for democratizing LLM capabilities. The teacher-student paradigm enables creating deployment-friendly models that approximate the performance of models 10-100x their size. The distinction between white-box (access to internals) and black-box (output-only) distillation is practically important: most commercial distillation from GPT-4 or Claude uses black-box methods since model internals are inaccessible.

The most promising direction is rationale-based distillation (Google's "Distilling Step-by-Step"), which extracts intermediate reasoning steps rather than just final outputs. This enables smaller models to learn not just what to predict but how to reason, achieving better data efficiency than traditional approaches.

## Related Concepts

- [[concepts/knowledge-distillation]] — the core methodology
- [[concepts/synthetic-data-generation]] — distillation output is synthetic training data
- [[concepts/fine-tuning]] — distillation is a specialized form of fine-tuning
- [[entities/microsoft-phi]] — phi models demonstrate distillation-and-beyond approach
