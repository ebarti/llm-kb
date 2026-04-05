---
title: "Qwen"
type: entity
entity_type: tool
sources: ["[[sources/bentoml-open-source-llms-2026]]", "[[sources/coding-models-comparison-2026]]", "[[sources/freecodecamp-local-rag-ollama]]"]
related: ["[[concepts/open-source-llms]]", "[[concepts/mixture-of-experts]]", "[[entities/deepseek]]", "[[concepts/small-language-models]]"]
last_compiled: 2026-04-05
summary: "Alibaba's open-source LLM family — Qwen 3.5 (397B MoE) leads reasoning benchmarks; Qwen 2.5 Coder (88.4% HumanEval) beats GPT-4; small variants (4B) rival 72B models."
---

## Overview

Qwen is Alibaba's family of open-source large language models and one of the most active contributors to the open-source LLM ecosystem. The Qwen series spans from tiny models (0.6B) suitable for mobile devices to massive MoE models (397B) competing at the frontier.

## Key Models

### Qwen 3.5-397B-A17B (February 2026)
- 397B total / 17B active, [[concepts/mixture-of-experts]]
- 262K native context, extendable to 1M+
- Strongest open model on several reasoning benchmarks
- 88.4 GPQA Diamond (surpasses every other open model)

### Qwen 2.5 Coder 32B
- 88.4% HumanEval — surpasses GPT-4's 87.1%
- 128K context, 92 programming languages
- Apache 2.0 license (unrestricted commercial use)
- Leading [[concepts/open-source-coding-models]]

### Qwen 3 4B
- ~70% MMLU, ~3GB VRAM with [[concepts/quantization]]
- Rivals Qwen 2.5-72B on specific tasks (18x size reduction)
- Dual-mode: /think (deep reasoning) + /no_think (fast)
- 119 languages
- Excellent [[concepts/small-language-models]] option

### Qwen3-Coder-Next (80B, 3B active)
- Released February 2026
- Outperforms much larger models like DeepSeek V3.2 (37B active)

## Mentioned In
- [[sources/bentoml-open-source-llms-2026]] — 3.5-397B ranked S-tier
- [[sources/coding-models-comparison-2026]] — 2.5 Coder leads HumanEval
- [[sources/freecodecamp-local-rag-ollama]] — Qwen 3 used in local RAG tutorial
