---
title: "Summarization and the Evolution of LLMs"
source: "https://cameronrwolfe.substack.com/p/summarization-and-the-evolution-of"
author: "Cameron R. Wolfe"
date_published: 2024-12-01
date_ingested: 2026-04-05
tags: [summarization, extractive, abstractive, RLHF, LLM, evaluation]
type: article
status: raw
discovered_via: search
---

# Summarization and the Evolution of LLMs

## Two Primary Approaches

**Extractive summarization** constructs summaries by selectively copying entire sentences or text spans from source documents. **Abstractive summarization** rephrases information from the original material, creating shorter explanations of relevant content.

Key insight: while LLMs theoretically produce abstractive summaries, research reveals they operate more extractively in practice — "summaries generated with an LLM tend to be (relatively) extractive in practice," with models naturally learning to copy and synthesize information rather than generate entirely novel phrasings.

## Evaluation Criteria

- **Fluency**: readability and grammatical correctness
- **Coherence**: overall structural cohesiveness
- **Relevance**: inclusion of important source material
- **Consistency**: factual accuracy without hallucinations

Traditional metrics like ROUGE measure n-gram overlap with reference summaries but correlate poorly with human preferences. Recent studies suggest using LLMs as reference-free metrics through LLM-as-a-Judge evaluation approaches.

## Training Approaches

**Supervised finetuning** trains models on human-written reference summaries, though this treats all references equally regardless of quality.

**Preference tuning** leverages human feedback by collecting pairs of summaries where annotators identify the superior option, enabling reward model training. Preference-based approaches significantly outperform supervised baselines — smaller models trained on human preferences exceed larger supervised models in human evaluations.

## RLHF Origins in Summarization

Critical OpenAI research demonstrates how summarization work directly influenced modern LLM development. Work on learning from human feedback for summarization established the three-stage pipeline: supervised finetuning, reward model training, and reinforcement learning optimization. These techniques became foundational for InstructGPT and subsequent alignment approaches.

## LLMs as Summarization Tools

Modern LLMs demonstrate remarkable summarization capabilities through in-context learning, requiring only prompt-based instruction without parameter updates. Instruction-tuning emerges as the crucial factor distinguishing effective summarization models from their untuned counterparts.

## Hybrid Extract-Then-Abstract

Extractive-abstractive summarization first generates an extractive summary, then uses an abstractive system to refine it — making it more concise and informative. Recent 2025 research categorizes reasoning prompting strategies into three schemes: Augmentation (expanding input context), Organization (structuring generation via planning), and Reflection (refining output through self-evaluation).
