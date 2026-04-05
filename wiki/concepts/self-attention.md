---
title: "Self-Attention"
type: concept
sources: ["[[sources/illustrated-transformer-jalammar]]", "[[sources/raschka-self-attention-coding]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/multi-head-attention]]", "[[concepts/causal-attention]]", "[[concepts/cross-attention]]", "[[concepts/flash-attention]]", "[[concepts/sparse-attention]]"]
last_compiled: 2026-04-05
summary: "The mechanism allowing each position in a sequence to attend to all others by computing scaled dot products between learned Query, Key, and Value projections — the core innovation of the Transformer."
---

## Overview

Self-attention (also called intra-attention) is the fundamental mechanism of the [[concepts/transformer-architecture]]. It allows each element in a sequence to dynamically weight and aggregate information from all other elements, enabling the model to capture contextual relationships regardless of distance. Unlike recurrence (which processes sequentially) or convolution (which uses fixed windows), self-attention computes pairwise interactions between all positions in parallel.

## How It Works

### Step 1: Projection

For each input vector x(i), three vectors are computed via learned weight matrices:
- **Query** q(i) = x(i) W_q — "what am I looking for?"
- **Key** k(i) = x(i) W_k — "what do I contain?"
- **Value** v(i) = x(i) W_v — "what information do I provide?"

### Step 2: Scoring

The attention score between positions i and j is the dot product of their query and key vectors:

omega(i,j) = q(i) * k(j)

### Step 3: Scaling and Normalization

Scores are scaled by sqrt(d_k) to prevent large values in high dimensions from causing vanishing gradients through softmax:

alpha(i,j) = softmax(omega(i,:) / sqrt(d_k))

### Step 4: Weighted Aggregation

The output for position i is a weighted sum of all value vectors:

z(i) = sum_j(alpha(i,j) * v(j))

### Matrix Form

For the full sequence: **Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V**

## Why Scale by sqrt(d_k)?

As Raschka explains: scaling ensures the Euclidean length of weight vectors remains in similar magnitude regardless of embedding dimension. Without scaling, large d_k values cause dot products to grow large, pushing softmax into saturated regions with near-zero gradients.

## Complexity

- **Time**: O(N^2 * d) where N is sequence length, d is dimension
- **Memory**: O(N^2) for the attention matrix (addressed by [[concepts/flash-attention]])

This quadratic scaling is the primary limitation, driving research into [[concepts/sparse-attention]], [[concepts/flash-attention]], and [[concepts/state-space-models]].

## Variants

- **[[concepts/multi-head-attention]]**: Multiple independent attention heads for diverse representations
- **[[concepts/causal-attention]]**: Masked self-attention preventing attention to future tokens
- **[[concepts/cross-attention]]**: Queries from one sequence, keys/values from another
- **[[concepts/grouped-query-attention]]**: Shared KV heads for memory efficiency
- **[[concepts/sparse-attention]]**: Attend to subsets of positions for linear complexity

## Sources

- [[sources/illustrated-transformer-jalammar]] — visual walkthrough of Q/K/V computation
- [[sources/raschka-self-attention-coding]] — PyTorch implementation from scratch

## Related Concepts

- [[concepts/transformer-architecture]] — the architecture built on self-attention
- [[concepts/multi-head-attention]] — parallel self-attention heads
- [[concepts/flash-attention]] — IO-aware optimization of the attention computation
- [[concepts/positional-encoding]] — injecting position information that attention lacks
