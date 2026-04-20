---
title: "Understanding and Coding Self-Attention, Multi-Head Attention, Causal-Attention, and Cross-Attention in LLMs"
source: "https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention"
author: "Sebastian Raschka"
date_published: 2024-01-14
date_ingested: 2026-04-05
tags: [self-attention, multi-head-attention, causal-attention, cross-attention, implementation, LLM]
type: article
status: raw
discovered_via: search
---

# Understanding and Coding Self-Attention Variants in LLMs

## Self-Attention Mechanism

Self-attention enhances input embeddings by incorporating contextual information. The mechanism enables models to weigh the importance of different elements in an input sequence and dynamically adjust their influence on the output.

### Mathematical Foundation

Three weight matrices project inputs into query, key, and value components:
- Query: q(i) = x(i) W_q
- Key: k(i) = x(i) W_k
- Value: v(i) = x(i) W_v

Unnormalized attention weights are computed via dot product: omega_i,j = q(i) dot k(j)

### Scaled Dot-Product Attention

Normalized weights apply scaling and softmax:
- alpha = softmax(omega / sqrt(d_k))

The scaling by sqrt(d_k) ensures that the Euclidean length of weight vectors remains in similar magnitude, preventing numerical instability during training.

Context vectors result from: z(i) = alpha @ values

## Multi-Head Attention

Multiple attention heads operate independently, each with separate Q, K, V matrices. Outputs concatenate along the final dimension.

Each attention head can potentially learn to focus on different parts of the input sequence, capturing various aspects or relationships within the data. This diversity in representation distinguishes it from simply increasing a single head's output dimension.

Practical example: Llama 2 (7B) uses 32 attention heads.

## Causal Self-Attention

Restricts attention to preceding tokens, essential for decoder-style LLMs (GPT, Llama) during generation. Prevents models from accessing future tokens during training.

### Implementation via Pre-Softmax Masking

Replace above-diagonal values with -inf before softmax. The softmax function converts these to zero probability since e^(-inf) approaches 0.

```python
mask = torch.triu(torch.ones(block_size, block_size), diagonal=1)
masked = attn_scores.masked_fill(mask.bool(), -torch.inf)
attn_weights = torch.softmax(masked / d_k**0.5, dim=1)
```

## Cross-Attention

Unlike self-attention using identical sequences for queries and keys, cross-attention applies queries from one sequence against keys/values from another — useful for encoder-decoder architectures.

Cross-attention permits arbitrary dimension selection for value matrices, unlike self-attention where Q, K, V dimensions must be compatible.

## Key Implementation Insights

- Production systems (e.g., Llama 2) employ 4,096-dimensional embeddings
- Normalized attention weights resembling probability distributions improve interpretability and control gradient scales during backpropagation
- Optimized variants like FlashAttention v2 are used for production systems where computational optimization becomes critical
