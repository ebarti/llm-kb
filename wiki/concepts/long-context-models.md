---
title: "Long-Context Models"
type: concept
sources: ["[[sources/epoch-context-window-growth]]", "[[sources/magic-ltm-100m-context]]", "[[sources/infinite-context-approaches]]", "[[sources/redis-rag-vs-long-context]]"]
related: ["[[concepts/context-windows]]", "[[concepts/needle-in-a-haystack]]", "[[concepts/lost-in-the-middle]]", "[[concepts/infinite-context]]"]
last_compiled: 2026-04-05
summary: "Models designed for extended context: Gemini (1-2M), Claude (200K-1M), Llama 4 Scout (10M), Magic LTM-2-Mini (100M) — each with distinct architecture-efficiency tradeoffs."
---

## Overview

Long-context models are LLMs specifically designed or optimized to process input sequences far beyond the traditional 4K-8K token range. As of early 2026, the landscape spans from 200K tokens (production workhorses) to 100M tokens (research frontier), with most frontier models converging on the 1M token mark.

## Current Landscape (2026)

### Frontier Production Models (1-2M tokens)

| Model | Context Window | Architecture Notes |
|-------|---------------|-------------------|
| Gemini 2.5 Pro | 1M tokens | Multimodal; also processes 19hrs audio at 2M |
| Claude Opus 4.6 | 1M tokens | Available at GA/standard API |
| Claude Sonnet 4.6 | 1M tokens | Available at GA/standard API |
| GPT-5.4 | 1M tokens | Available at GA/standard API |
| Gemini 2.0 Pro | 2M tokens | Largest production-accessible window |

### Extended Context Models (10M+ tokens)

| Model | Context Window | Architecture Notes |
|-------|---------------|-------------------|
| Llama 4 Scout | 10M tokens | ~7,500 pages of text; open-source |
| DeepSeek-V3.2 | ~1M | Sparse attention for efficiency |
| Qwen3.5 | ~1M | MoE + multimodal + ultra-long context |
| MiMo-V2-Flash | 256K | Hybrid thinking mode |

### Research Frontier (100M+ tokens)

| Model | Context Window | Architecture Notes |
|-------|---------------|-------------------|
| [[entities/magic-ltm]] LTM-2-Mini | 100M tokens | Novel sequence-dimension algorithm; 1,000x cheaper than standard attention |

## Key Architectural Approaches

### Standard Attention Scaling
Most production models use optimized attention mechanisms (FlashAttention, GQA, sliding window) to push standard transformer architecture further. Still O(n^2) in theory but with significant constant-factor improvements.

### Sparse Attention
DeepSeek-V3.2 and similar models use sparse attention mechanisms where only a subset of tokens interact, reducing compute for long inputs while preserving quality.

### Mixture of Experts (MoE)
Qwen3.5 combines MoE architecture with long context support, activating only relevant expert subnetworks per token. Reduces compute per token while maintaining model capacity.

### Novel Architectures
[[entities/magic-ltm]]'s sequence-dimension algorithm represents a fundamental departure: 1,000x cheaper than Llama 3.1 405B attention at 100M tokens, requiring a fraction of one H100 vs 638 for standard transformers. Custom training and inference stack (no torch autograd, custom CUDA).

## Performance Reality

Despite massive context windows, effective utilization remains challenging:
- Even Gemini 2.5 Pro only scores >80% on 8K input length in the hardest MRCR variant ([[sources/epoch-context-window-growth]])
- All models show degradation as context grows ("context rot")
- The [[concepts/lost-in-the-middle]] problem persists across architectures
- Practical guidance: don't exceed 60% of window capacity

## Evaluation

Long-context models are evaluated through:
- [[concepts/needle-in-a-haystack]] and variants (single/multi-needle)
- **MRCR**: Multi-needle retrieval with distractors
- **Fiction.liveBench**: Narrative comprehension across documents
- **HashHop**: Incompressible hash pair retrieval (Magic's harder alternative to NIAH)
- **BABILong**: Distributed fact processing in long documents

## Sources

- [[sources/epoch-context-window-growth]] — growth trends and effective usage metrics
- [[sources/magic-ltm-100m-context]] — extreme context via novel architecture
- [[sources/infinite-context-approaches]] — architectural innovations for unbounded context
- [[sources/redis-rag-vs-long-context]] — practical limitations of long-context in production

## Related Concepts

- [[concepts/context-windows]] — the fundamental constraint these models address
- [[concepts/needle-in-a-haystack]] — primary evaluation paradigm
- [[concepts/lost-in-the-middle]] — persistent performance challenge
- [[concepts/infinite-context]] — theoretical limit of long-context scaling
- [[concepts/rag-vs-index-based-retrieval]] — alternative approach to the same problem
