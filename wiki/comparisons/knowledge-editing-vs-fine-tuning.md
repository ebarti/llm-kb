---
title: "Knowledge Editing vs. Fine-Tuning"
type: comparison
subjects: ["[[concepts/knowledge-editing]]", "[[concepts/fine-tuning]]"]
sources: ["[[sources/rome-memit-knowledge-editing]]", "[[sources/lora-qlora-efficient-fine-tuning]]"]
last_compiled: 2026-04-05
summary: "Knowledge editing (ROME/MEMIT) is surgical and cheap for individual facts but degrades with sequential edits; fine-tuning is broader but expensive — use editing for corrections, fine-tuning for domain adaptation."
---

## Overview

[[concepts/knowledge-editing]] and [[concepts/fine-tuning]] are both methods for putting knowledge into model weights, but they operate at fundamentally different granularities. Knowledge editing modifies specific factual associations (e.g., changing where the Eiffel Tower is located), while fine-tuning adapts broad capabilities across an entire domain.

## Comparison Table

| Dimension | Knowledge Editing (ROME/MEMIT) | Fine-Tuning (LoRA) |
|-----------|-------------------------------|---------------------|
| **Granularity** | Single facts | Domain/task level |
| **Cost per update** | Very low (rank-one computation) | Medium (GPU hours) |
| **Data requirement** | One fact tuple | Hundreds to thousands of examples |
| **Scope of change** | Narrow (one association) | Broad (general behavior) |
| **Generalization** | Edits generalize to paraphrases | Generalizes across domain |
| **Specificity** | High (neighbors unaffected) | Lower (may affect unrelated tasks) |
| **Sequential updates** | Degrades progressively | Can be retrained |
| **Scalability** | Limited (catastrophic failure) | Good (retrain as needed) |
| **Traceability** | None | None |
| **New concepts** | Cannot add | Can learn new concepts |
| **Forgetting risk** | Progressive with edits | Managed with PEFT |

## When to Use Each

### Knowledge Editing
- Correcting a small number of known factual errors
- Emergency patches to deployed models
- Research into how models store knowledge
- NOT for ongoing knowledge maintenance

### Fine-Tuning
- Domain adaptation (vocabulary, tone, reasoning)
- Learning new tasks or output formats
- Broad knowledge injection from training data
- Ongoing model improvement cycles

### Neither (Use RAG Instead)
- Frequently changing facts
- Need for citation and traceability
- Large knowledge bases that exceed model capacity
- When knowledge provenance matters

## The Practical Verdict

For [[concepts/llm-knowledge-base]] systems, knowledge editing is a fascinating research direction but not yet practical for continuous knowledge updates due to sequential degradation. Fine-tuning (especially via [[concepts/parameter-efficient-fine-tuning|LoRA]]) combined with RAG is the practical choice.

## Sources

- [[sources/rome-memit-knowledge-editing]] — knowledge editing methodology and limitations
- [[sources/lora-qlora-efficient-fine-tuning]] — fine-tuning methodology and costs
