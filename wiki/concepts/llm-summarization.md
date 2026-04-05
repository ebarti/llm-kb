---
title: "LLM Summarization Techniques"
type: concept
sources: ["[[sources/wolfe-llm-summarization-evolution]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/wiki-compilation]]", "[[concepts/claim-extraction]]", "[[concepts/data-quality-bottleneck]]"]
last_compiled: 2026-04-05
summary: "Extractive vs. abstractive summarization with LLMs — in practice LLMs are more extractive than expected; hybrid extract-then-abstract approaches produce the most reliable wiki summaries."
---

## Overview

Summarization condenses source documents into shorter representations. It is a core operation in [[concepts/wiki-compilation]]: every source summary in `wiki/sources/` is a summarization product, and concept articles synthesize summaries from multiple sources.

## Two Paradigms

### Extractive Summarization
Selects and copies important sentences or passages verbatim from the source text. The summary is a subset of original sentences.

**Strengths**: No hallucination risk (all text is from the source), preserves exact phrasing
**Weaknesses**: May lack coherence, cannot combine information across passages

### Abstractive Summarization
Generates new text that rephrases and condenses the source material. The summary may contain words and phrasings not in the original.

**Strengths**: More coherent, can synthesize across passages, more concise
**Weaknesses**: Risk of hallucination, may distort meaning

### The Surprising Reality

From [[sources/wolfe-llm-summarization-evolution]]: despite theoretically being abstractive generators, LLMs tend to be "relatively extractive in practice." Models naturally learn to copy and synthesize from source text rather than generate entirely novel phrasings. This is actually desirable for knowledge base compilation where fidelity to sources matters.

## Hybrid Extract-Then-Abstract

The most reliable approach for [[concepts/wiki-compilation]]:

1. **Extract**: Identify key sentences and passages from the source
2. **Abstract**: Use an LLM to rephrase and condense the extractions into a coherent summary

This hybrid approach reduces hallucination risk (grounded in extracted passages) while producing readable output.

## Evaluation

### Traditional Metrics
ROUGE measures n-gram overlap between generated and reference summaries. However, ROUGE correlates poorly with human preferences — an LLM can produce a genuinely better summary that scores low on ROUGE.

### LLM-as-a-Judge
Emerging approach: use another LLM to evaluate summaries on four criteria:
- **Fluency**: Readability and grammatical correctness
- **Coherence**: Overall structural cohesiveness
- **Relevance**: Inclusion of important source material
- **Consistency**: Factual accuracy without hallucinations

### Advanced Reasoning Strategies (2025)

Recent research categorizes reasoning strategies for summarization:
- **Augmentation**: Expand input context with auxiliary information
- **Organization**: Structure generation via planning (outline first, then write)
- **Reflection**: Refine output through self-evaluation and selection

## Historical Significance

Summarization research at OpenAI directly led to the RLHF pipeline that became foundational for modern LLM training:
1. Supervised finetuning on human-written summaries
2. Reward model training from human preference pairs
3. RL optimization against the reward model

This three-stage pipeline became InstructGPT's training approach and all subsequent alignment work.

## Relevance to Wiki Compilation

In the [[concepts/llm-knowledge-base]] system:
- **Source summaries** (`wiki/sources/*.md`): Extractive-then-abstractive summaries of raw sources
- **Concept articles** (`wiki/concepts/*.md`): Cross-source synthesis (abstractive over multiple extractive summaries)
- **Q&A responses**: Summarize relevant articles to answer user questions
- **Index entries**: One-line summaries in `wiki/_meta/summaries.md`

## Sources

- [[sources/wolfe-llm-summarization-evolution]] — extractive vs. abstractive, RLHF origins, evaluation

## Related Concepts

- [[concepts/information-extraction]] — summarization is a form of extraction
- [[concepts/wiki-compilation]] — summarization drives wiki article creation
- [[concepts/claim-extraction]] — summaries contain claims that need verification
- [[concepts/data-quality-bottleneck]] — summary quality depends on source quality
- [[concepts/hallucination-contamination]] — abstractive summarization risks hallucination
