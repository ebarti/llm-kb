---
title: "Large Language Models as Reliable Knowledge Bases?"
source: "https://arxiv.org/abs/2407.13578"
author: "Multiple authors"
date_published: 2024-07-01
date_ingested: 2026-04-05
tags: [LLM, knowledge-base, factuality, consistency, hallucination, implicit-knowledge]
type: paper
status: raw
discovered_via: search
---

# Large Language Models as Reliable Knowledge Bases?

## Evaluation Framework
Two dimensions: factuality and consistency across both seen and unseen knowledge.

### Factuality Metrics
- Net Correct Rate (NCR): Measures how much more likely the model is to provide correct vs. wrong responses
- Uninformative Rate (UR): Tracks responses acknowledging knowledge gaps

### Consistency Metrics
Tests whether models maintain stable answers across multiple prompts using multiple-choice variants.

## How LLMs Store Knowledge
Unlike traditional databases with explicit storage locations, language models encode information probabilistically within parameters. Three response types: correct, uninformative, and wrong — fundamentally different from deterministic knowledge bases.

## Key Findings

### Reliability Assessment
- gpt-3.5-turbo ranked most reliable, yet achieved only 32% Net Consistently Correct Rate on seen knowledge
- Performance diverges: models excelling on known information fail on unfamiliar topics, and vice versa
- Larger models: better on seen knowledge, worse on unseen knowledge
- Models with high consistency in correct responses also show high consistency in wrong responses

### Major Limitations
1. **Hallucination & Inconsistency**: Confident false information, especially for numerical and temporal questions
2. **Staleness**: Knowledge cutoff dates create inherent obsolescence
3. **Inconsistent Responses**: In-context learning and instruction-tuning reduce consistency across equivalent questions
4. **Fine-tuning trade-offs**: Improves handling of unfamiliar knowledge but degrades seen-knowledge performance

## Conclusion
LLMs cannot reliably replace traditional knowledge bases. While capable of encoding parametric knowledge, current models lack the factuality and consistency guarantees essential for knowledge base functionality.

## Implications
This supports hybrid approaches where structured knowledge bases (whether symbolic, graph-based, or markdown-based) complement LLM capabilities — the same insight motivating Karpathy's LLM-maintained wiki approach and Lenat's final paper proposing Cyc+LLM integration.
