---
title: "MMLU (Massive Multitask Language Understanding)"
type: entity
entity_type: dataset
sources: ["[[sources/responsible-ai-labs-benchmarks-2025]]", "[[sources/raschka-state-of-llms-2025]]"]
related: ["[[concepts/llm-benchmarks]]", "[[concepts/benchmark-saturation]]", "[[entities/helm]]"]
last_compiled: 2026-04-05
summary: "The most widely-cited LLM knowledge benchmark: 15,908 multiple-choice questions across 57 subjects from elementary math to professional law — now saturated above 90% for frontier models."
---

## Overview

MMLU (Massive Multitask Language Understanding) is a benchmark of 15,908 multiple-choice questions spanning 57 academic subjects, from elementary mathematics to professional law and medicine. It is the most widely-cited general knowledge benchmark for LLMs.

## Current Status (2026)

MMLU is **saturated**: frontier models routinely exceed 90% accuracy, with GPT-5.3 Codex scoring 93%. At these levels, score differences reflect noise and optimization rather than genuine capability differences. MMLU scores "no longer differentiate between leading models."

## Limitations

- Doesn't evaluate safety, bias, or alignment
- Multiple-choice format doesn't test generation quality
- Vulnerable to data contamination (published questions appear in training data)
- Saturated for frontier models

## Mentioned In

- [[sources/responsible-ai-labs-benchmarks-2025]] — benchmark taxonomy
- [[sources/raschka-state-of-llms-2025]] — saturation analysis
