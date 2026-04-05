---
title: "Multi-Stage Pretraining"
type: concept
sources: ["[[sources/raschka-pretraining-post-training-paradigms]]", "[[sources/mlops-pretraining-pipeline]]"]
related: ["[[concepts/llm-pretraining]]", "[[concepts/pretraining-data-pipeline]]", "[[concepts/continual-pretraining]]"]
last_compiled: 2026-04-05
summary: "The universal 2024 practice of training LLMs in sequential phases with different data mixes: broad web data first, then high-quality math/code, then context extension. Used by Llama 3.1, Apple AFM, Gemma 2, and Qwen 2."
---

## Overview

Multi-stage pretraining divides the pretraining process into sequential phases, each with a different data distribution and sometimes different hyperparameters. This has become the de facto standard for frontier LLM training as of 2024, with all leading models adopting some variant.

## Common Pattern

### Stage 1: Core Pretraining
- **Data**: Dominated by massive web data for broad knowledge acquisition
- **Tokens**: The bulk of training (e.g., 6.3T for Apple AFM, ~15T for Llama 3.1)
- **Context**: Standard length (e.g., 8K tokens)
- **Goal**: Learn grammar, semantics, world knowledge, reasoning fundamentals

### Stage 2: Quality Upweighting / Annealing
- **Data**: Down-weight web data, up-weight math, code, curated sources
- **Tokens**: Typically 0.5-2T additional tokens
- **Goal**: Strengthen reasoning, coding, and factual accuracy
- **Example**: Apple's continued pretraining phase (1T tokens with math/code emphasis)

### Stage 3: Context Extension
- **Data**: Synthetic long-context documents, modified positional encodings
- **Tokens**: Relatively small (100B-1T)
- **Goal**: Extend context window (e.g., 8K -> 32K -> 128K)
- **Example**: Llama 3.1 extended through 6 sub-stages to reach 128K

## Model-Specific Implementations

| Model | Stage 1 | Stage 2 | Stage 3 |
|-------|---------|---------|---------|
| Llama 3.1 | Standard 8K (15T tokens) | Annealing on benchmarks | 6-stage context extension to 128K |
| Apple AFM | Core (6.3T tokens) | Math/code up-weighted (1T) | Synthetic long-context (100B) |
| Qwen 2 | Regular (7T tokens) | — | Long-context 4K->32K |
| Gemma 2 | Full training (13T) | — | — |

## Why Multi-Stage?

1. **Efficiency**: Not all data is equally valuable at all training stages
2. **Capability targeting**: Math/code benefit from focused later-stage training
3. **Context extension**: Long-context data is expensive to process; deferring it saves compute
4. **Stability**: Different phases can use different learning rates and batch sizes

## Sources

- [[sources/raschka-pretraining-post-training-paradigms]] — four-model comparison with specific configurations
- [[sources/mlops-pretraining-pipeline]] — multi-phase pretraining as modern innovation

## Related Concepts

- [[concepts/llm-pretraining]] — the process being staged
- [[concepts/pretraining-data-pipeline]] — the data fed into each stage
- [[concepts/learning-rate-schedules]] — interact with staging decisions
