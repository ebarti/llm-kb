---
title: "MHA vs GQA vs MQA"
type: comparison
subjects: ["[[concepts/multi-head-attention]]", "[[concepts/grouped-query-attention]]"]
sources: ["[[sources/gqa-grouped-query-attention-overview]]", "[[sources/attention-mechanisms-comprehensive-survey]]"]
related: ["[[concepts/kv-cache]]", "[[concepts/attention-mechanisms]]", "[[concepts/transformer-architecture]]"]
tags: [MHA, GQA, MQA, attention-heads, KV-cache, inference]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Multi-Head Attention (max quality, max KV cache) vs Grouped Query Attention (near-MHA quality, 4-8x less KV cache) vs Multi-Query Attention (fastest, quality loss): GQA is the dominant choice for production LLMs since 2023."
---

## Overview

The choice of attention head structure directly determines the [[concepts/kv-cache]] size and therefore the inference cost of transformer models. MHA, GQA, and MQA represent three points on the quality-efficiency spectrum, with GQA having emerged as the clear winner for production deployment.

## Comparison Matrix

| Dimension | MHA (Multi-Head) | GQA (Grouped Query) | MQA (Multi-Query) |
|-----------|------------------|--------------------|--------------------|
| **KV heads** | Same as query heads (H) | G groups (1 < G < H) | 1 (single shared) |
| **KV cache size** | Full (baseline) | ~H/G reduction | H reduction |
| **Quality** | Baseline (best) | Near-MHA (<1% loss) | Measurable degradation |
| **Inference speed** | Baseline | 30-40% faster | Fastest |
| **Training** | Standard | Uptrain from MHA (5% compute) | Train from scratch |
| **Adoption (2024+)** | Legacy / small models | **Dominant** | Rare |

## Detailed Analysis

### Multi-Head Attention (MHA)

The original design from "Attention is All You Need": every query head has its own unique Key and Value projections.

**Strengths**: Maximum representational capacity; each head independently learns what to retrieve
**Weaknesses**: KV cache grows linearly with number of heads; becomes the inference bottleneck for large models

### Grouped Query Attention (GQA)

Groups of query heads share a single Key-Value head. For example, Llama 2 70B uses 64 query heads with 8 KV heads (8 groups of 8 query heads each).

**Strengths**:
- 4-8x KV cache reduction with minimal quality loss
- Can uptrain existing MHA checkpoints with only 5% of original pre-training compute
- Smooth interpolation between MHA and MQA

**Weaknesses**: Slightly less representational diversity than full MHA

### Multi-Query Attention (MQA)

All query heads share a single Key and Value head — the most aggressive efficiency option.

**Strengths**: Maximum KV cache reduction; fastest inference
**Weaknesses**: Measurable quality degradation; requires training from scratch

## Adoption Timeline

| Year | Trend |
|------|-------|
| 2017-2022 | MHA dominant (original Transformer, GPT-2/3, BERT) |
| 2022 | MQA explored (PaLM) but quality concerns noted |
| 2023 | **GQA introduced** (Ainslie et al., Google); Llama 2 adopts GQA |
| 2024 | GQA becomes standard: Llama 3, Mistral, Gemma, DeepSeek |
| 2025+ | GQA universal for production models; MHA only for small/research models |

## Concrete Model Examples

| Model | Query Heads | KV Heads | Type | KV Reduction |
|-------|-------------|----------|------|-------------|
| GPT-3 175B | 96 | 96 | MHA | 1x |
| BERT-base | 12 | 12 | MHA | 1x |
| PaLM 540B | 48 | 1 | MQA | 48x |
| Llama 2 7B | 32 | 32 | MHA | 1x |
| Llama 2 70B | 64 | 8 | GQA | 8x |
| Llama 3 8B | 32 | 8 | GQA | 4x |
| Mistral 7B | 32 | 8 | GQA | 4x |
| Gemma 2B | 16 | 2 | GQA | 8x |
| DeepSeek V3 | 128 | 1 | MQA* | 128x |

*DeepSeek V3 uses MLA (Multi-head Latent Attention), a further evolution.

## When to Use Each

| Scenario | Recommendation |
|----------|---------------|
| Research / small models (<1B params) | MHA (simplicity, maximum quality) |
| Production LLMs (7B-70B) | **GQA** (dominant standard) |
| Extreme inference optimization | MQA or MLA |
| Upgrading existing MHA model | Uptrain to GQA (5% compute) |
| Embedding models (not autoregressive) | MHA (no KV cache concern) |

## Sources

- [[sources/gqa-grouped-query-attention-overview]] — GQA as generalization of MHA and MQA
- [[sources/attention-mechanisms-comprehensive-survey]] — mathematical foundations
