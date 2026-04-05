---
title: "Source: GPT-NER — Named Entity Recognition via Large Language Models"
type: source-summary
source: "[[raw/gpt-ner-named-entity-recognition]]"
related: ["[[concepts/named-entity-recognition]]", "[[concepts/information-extraction]]", "[[concepts/zero-shot-information-extraction]]"]
last_compiled: 2026-04-05
summary: "GPT-NER transforms NER from sequence labeling to text generation using special marker tokens, achieving supervised-comparable performance and excelling in few-shot settings."
reading_time: "2 min"
---

## Key Points

- LLMs underperform on NER because it is a sequence labeling task while LLMs are generation models — GPT-NER bridges this gap
- The method marks entities with special tokens (@@entity##) in generated text, transforming labeling into generation
- Self-verification strategy combats hallucinated entities by prompting the LLM to confirm extractions
- Achieves performance comparable to fully supervised baselines — a first for LLM-based NER
- Excels in low-resource and few-shot scenarios where labeled data is scarce

## Detailed Summary

GPT-NER (NAACL 2025 Findings) addresses a fundamental mismatch: [[concepts/named-entity-recognition]] is inherently a sequence labeling task, but LLMs are text-generation models. The paper's key insight is reformulating NER as generation — given "Columbus is a city," the model generates "@@Columbus## is a city" where @@/## delimit entities.

A critical innovation is the self-verification strategy to combat hallucination. LLMs tend to over-confidently label tokens as entities even when no entities are present. The self-verification prompt asks the model to confirm whether each extracted entity genuinely belongs to the target category.

This pattern — reformulating structured prediction as constrained generation — is generalizable beyond NER to other [[concepts/information-extraction]] tasks like [[concepts/relation-extraction]] and event extraction.

## Notable Quotes

> "The gap between NER and LLMs: the former is a sequence labeling task in nature while the latter is a text-generation model."

## Related Concepts

- [[concepts/named-entity-recognition]] — the task addressed
- [[concepts/zero-shot-information-extraction]] — GPT-NER's few-shot variant
- [[concepts/information-extraction]] — parent discipline
- [[concepts/hallucination-contamination]] — self-verification addresses extraction hallucinations
