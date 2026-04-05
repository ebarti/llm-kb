---
title: "RAFT (Retrieval Augmented Fine-Tuning)"
type: concept
sources: ["[[sources/raft-retrieval-augmented-fine-tuning]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/synthetic-data-generation]]"]
last_compiled: 2026-04-05
summary: "Hybrid approach training models on questions with oracle + distractor documents, teaching them to leverage retrieval while ignoring noise — up to 76% improvement over baselines."
---

## Overview

RAFT (Retrieval Augmented Fine-Tuning) is a training methodology from UC Berkeley that combines [[concepts/fine-tuning]] with retrieval-augmented generation to create models that excel in domain-specific "open-book" question answering. Rather than choosing between RAG or fine-tuning, RAFT trains models to intelligently use retrieved documents while filtering out irrelevant ones.

The core insight: traditional RAG doesn't train the model to handle domain-specific retrieval patterns, and traditional fine-tuning ignores the reality that retrieved documents will be available at inference time. RAFT prepares the model for the actual test conditions.

## The Study Analogy

- **Standard RAG**: Taking an open-book exam without studying — you have the book but don't know how to use it efficiently
- **Standard fine-tuning**: Studying without the book — memorization without retrieval skills
- **RAFT**: Studying with the book — learning both the material and how to find and cite relevant passages

## Training Recipe

### Data Composition
- **P% of examples**: Question + oracle document (contains answer) + distractor documents → model learns to find and cite relevant information
- **(1-P)% of examples**: Question + only distractor documents → model forced to memorize domain knowledge (no oracle available)

### Chain-of-Thought with Quotation
Models are trained to:
1. Reason step-by-step through the question
2. Explicitly quote relevant passages using markers (`##begin_quote##` / `##end_quote##`)
3. Synthesize an answer grounded in cited evidence

This quotation mechanism is a built-in hallucination prevention technique.

## Results

| Benchmark | Improvement over Baseline |
|-----------|--------------------------|
| HotpotQA | +35.25% |
| TorchHub | +76.35% |
| HuggingFace | +31.41% |

RAFT consistently outperforms both RAG-only and fine-tuning-only approaches. A RAFT-trained Llama2-7B outperforms GPT-3.5 on domain-specific tasks.

## Relevance to LLM Knowledge Bases

RAFT is directly applicable to [[concepts/llm-knowledge-base]] systems:
- Train the compilation LLM with RAFT on the KB's own raw sources
- Distractor documents mirror real retrieval noise (index misses, partial matches)
- Chain-of-thought quotation naturally produces the citation behavior needed for wiki compilation
- The model learns both domain knowledge (from memorization instances) and retrieval skills (from oracle+distractor instances)

## Sources

- [[sources/raft-retrieval-augmented-fine-tuning]] — methodology and results

## Related Concepts

- [[concepts/fine-tuning]] — RAFT is a specialized fine-tuning recipe
- [[concepts/rag-vs-index-based-retrieval]] — RAFT bridges RAG and fine-tuning
- [[concepts/synthetic-data-generation]] — RAFT's training data preparation is a form of synthetic curation
- [[concepts/hallucination-contamination]] — quotation markers prevent hallucination
