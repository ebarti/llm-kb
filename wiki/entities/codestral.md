---
title: "Codestral"
type: entity
entity_type: tool
url: "https://mistral.ai/news/codestral"
sources: ["[[sources/morphllm-coding-models-comparison-2026]]"]
related: ["[[concepts/ai-code-generation]]", "[[entities/claude-code]]", "[[entities/openai-codex]]"]
tags: [codestral, mistral, open-source, coding-model]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Mistral AI's open-weight coding model (22B parameters) -- fast local inference at 1.4s per response vs Claude's 2.1s, scoring within 85-90% of frontier models on straightforward tasks."
---

## Overview

Codestral is Mistral AI's dedicated coding language model, released with 22 billion parameters and designed for fast local inference. It represents the open-weight coding model category alongside DeepSeek-Coder and Qwen-Coder, competing with proprietary models by offering local deployment, data sovereignty, and lower latency on consumer hardware.

## Key Facts

- **Type**: Open-weight coding LLM
- **Developer**: Mistral AI
- **Parameters**: 22B
- **Inference speed**: ~1.4 seconds per response on consumer GPU
- **Notable for**: Fast local inference for code generation tasks

## Performance Context

Per [[sources/morphllm-coding-models-comparison-2026]], open-source coding models like Codestral, DeepSeek-Coder-V2, and Qwen2.5-Coder-32B have closed the gap with proprietary models "in ways that would have been unthinkable in 2024." On consumer hardware (RTX 4070 Ti Super), the best local models score within 85-90% of Claude Sonnet on straightforward function generation.

Codestral's primary advantage is speed: 1.4s per response vs Claude's 2.1s for standard queries, though cloud APIs pull ahead significantly for long outputs (200+ lines) due to infrastructure advantages (60-80 tok/s vs 15-25 on consumer GPU).

## Role in the Ecosystem

Codestral occupies the "fast local alternative" niche in [[concepts/ai-code-generation]], serving developers who need data sovereignty, minimal latency for autocomplete, or cost-free inference. It trades frontier-level reasoning for speed and accessibility.

## Mentions

- [[sources/morphllm-coding-models-comparison-2026]] -- benchmark and speed comparisons
