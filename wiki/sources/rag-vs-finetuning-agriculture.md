---
title: "Source: RAG vs Fine-tuning — Pipelines, Tradeoffs, and Agriculture Case Study"
type: source-summary
source: "[[raw/rag-vs-finetuning-agriculture]]"
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/fine-tuning]]", "[[comparisons/rag-vs-fine-tuning]]"]
last_compiled: 2026-04-05
summary: "ArXiv paper demonstrating RAG and fine-tuning are complementary: fine-tuning adds +6pp accuracy, RAG adds another +5pp, and combining both improved geographic knowledge transfer from 47% to 72% similarity."
reading_time: "1 min"
---

## Key Points

- RAG augments the prompt with external data at runtime; fine-tuning incorporates knowledge into model parameters
- Fine-tuning alone improved accuracy by 6+ percentage points on agricultural QA
- RAG added a further 5 percentage points on top of fine-tuning
- Geographic knowledge transfer improved from 47% to 72% answer similarity
- Tested on Llama2-13B, GPT-3.5, and GPT-4

## Detailed Summary

This research paper provides empirical evidence that [[concepts/retrieval-augmented-generation]] and [[concepts/fine-tuning]] are complementary rather than competing approaches. Using agriculture as a test domain — chosen for its limited AI adoption and need for location-specific knowledge — the authors implement a multi-stage pipeline covering PDF extraction, Q&A generation, fine-tuning, and GPT-4-based evaluation.

The key finding is cumulative benefit: each technique addresses different knowledge dimensions. Fine-tuning internalizes domain behavior, terminology, and reasoning patterns. RAG provides current factual grounding from external documents. The combination outperforms either alone.

## Notable Quotes

> "RAG augments the prompt with the external data, while fine-Tuning incorporates the additional knowledge into the model itself."

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — one of the two compared approaches
- [[concepts/fine-tuning]] — the other compared approach
- [[comparisons/rag-vs-fine-tuning]] — detailed comparison article
