---
title: "Multi-Head Attention"
type: concept
sources: ["[[sources/illustrated-transformer-jalammar]]", "[[sources/raschka-self-attention-coding]]", "[[sources/attention-mechanisms-comprehensive-survey]]", "[[sources/gqa-grouped-query-attention-overview]]"]
related: ["[[concepts/self-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/grouped-query-attention]]", "[[concepts/attention-mechanisms]]", "[[comparisons/mha-vs-gqa-vs-mqa]]"]
last_compiled: 2026-04-05
summary: "Running multiple parallel self-attention heads with independent Q/K/V projections, then concatenating results — enabling the model to capture diverse relationship types simultaneously."
---

## Overview

Multi-head attention extends [[concepts/self-attention]] by running h independent attention computations in parallel, each with its own learned Q, K, V weight matrices. The outputs are concatenated and projected through a final weight matrix W_O. This allows the model to attend to information from different representation subspaces at different positions simultaneously.

## How It Works

Given h attention heads:

1. For each head i: Q_i = X W_q^i, K_i = X W_k^i, V_i = X W_v^i
2. Each head computes: head_i = Attention(Q_i, K_i, V_i)
3. Concatenate: Concat(head_1, ..., head_h)
4. Project: MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W_O

The original Transformer uses h=8 heads with d_k = d_v = d_model/h = 64.

## Why Multiple Heads?

A single attention head computes one weighted average over values. But a sequence element often needs to attend to multiple different aspects — syntactic structure, semantic similarity, coreference, etc. Multiple heads let the model capture these different relationship types independently.

As Raschka notes, each head can learn to focus on different parts of the input sequence, capturing various aspects or relationships within the data. This is fundamentally different from simply increasing a single head's dimension.

## Practical Dimensions

| Model | Heads | d_model | d_k per head |
|-------|-------|---------|-------------|
| Original Transformer | 8 | 512 | 64 |
| BERT-base | 12 | 768 | 64 |
| GPT-3 175B | 96 | 12288 | 128 |
| Llama 2 7B | 32 | 4096 | 128 |
| Llama 2 70B | 64 | 8192 | 128 |

## Evolution: Efficiency Variants

The memory cost of multi-head attention has driven three key optimizations:

- **Multi-Query Attention (MQA)**: Single KV head shared across all query heads (drastically reduces [[concepts/kv-cache]])
- **[[concepts/grouped-query-attention]] (GQA)**: Groups of query heads share KV heads (interpolates MHA and MQA)
- Both reduce KV cache memory proportionally while maintaining most of the quality of full multi-head attention

## Sources

- [[sources/illustrated-transformer-jalammar]] — visual explanation of 8-head attention with concatenation
- [[sources/raschka-self-attention-coding]] — implementation showing independent heads capture different patterns

## Related Concepts

- [[concepts/self-attention]] — the base mechanism each head computes
- [[concepts/grouped-query-attention]] — memory-efficient variant
- [[concepts/kv-cache]] — the memory bottleneck multi-head attention creates
- [[concepts/transformer-architecture]] — the architecture using multi-head attention
