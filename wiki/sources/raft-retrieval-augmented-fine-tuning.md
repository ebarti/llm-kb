---
title: "Source: RAFT — Adapting Language Model to Domain Specific RAG"
type: source-summary
source: "[[raw/raft-retrieval-augmented-fine-tuning]]"
related: ["[[concepts/raft]]", "[[concepts/fine-tuning]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "UC Berkeley paper combining RAG with fine-tuning: train models to ignore distractor documents and cite verbatim from oracle docs, achieving up to 76% improvement on domain-specific benchmarks."
reading_time: "2 min"
---

## Key Points

- RAFT trains models to ignore irrelevant retrieved documents (distractors) while citing verbatim from relevant ones
- Training mix: P% questions with oracle + distractor docs; (1-P)% with distractor-only docs (forces memorization)
- Chain-of-thought answers with explicit quotation markers prevent hallucination
- Results: +35.25% on HotpotQA, +76.35% on TorchHub, +31.41% on HuggingFace over baselines
- Base model: Llama2-7B on 4 A100-40G GPUs; deploys on single GPU
- Outperforms both RAG-only and fine-tuning-only approaches across all tested domains

## Detailed Summary

RAFT addresses a fundamental limitation in both RAG and fine-tuning: RAG alone doesn't train the model to handle domain-specific retrieval patterns, while fine-tuning alone ignores the reality that retrieved documents will be available at inference time. RAFT's analogy: traditional methods are like studying without the textbook you'll have during the exam.

The training recipe is elegantly simple: include distractor documents during training so the model learns to distinguish signal from noise, and require chain-of-thought explanations that quote source material verbatim. The dual-scenario design (sometimes with oracle docs, sometimes without) ensures the model both leverages retrieval and memorizes core domain knowledge.

## Notable Quotes

> "Standard approaches resemble studying without the textbook or practicing without access to reference materials you'll actually have during the test."

## Related Concepts

- [[concepts/raft]] — the hybrid RAG + fine-tuning methodology
- [[concepts/fine-tuning]] — one of the two approaches RAFT combines
- [[concepts/synthetic-data-generation]] — RAFT's training data preparation is a form of synthetic data curation
- [[concepts/catastrophic-forgetting]] — RAFT's distractor-only training mitigates by reinforcing domain memorization
