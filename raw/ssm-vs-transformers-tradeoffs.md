---
title: "On the Tradeoffs of SSMs and Transformers"
source: "https://goombalab.github.io/blog/2025/tradeoffs/"
author: "Goomba Lab (Albert Gu)"
date_published: 2025-03-15
date_ingested: 2026-04-05
tags: [SSM, transformer, Mamba, architecture-comparison, hybrid-models]
type: article
status: raw
discovered_via: search
---

# On the Tradeoffs of SSMs and Transformers

## Core Architectural Differences

SSMs compress all historical context into a fixed-size hidden state, processing data in a streaming fashion. Transformers maintain an explicit token cache (KV cache) that grows linearly with sequence length, enabling fine-grained retrieval.

As Gu notes: "Transformers are like databases" storing every observation, while "SSMs are like brains" with finite-sized memories processing inputs continuously.

## Computational Characteristics

**SSMs:**
- Linear time complexity during inference (constant-time recurrence steps)
- Fixed memory footprint regardless of context length
- Three key ingredients: expanded state size, data-dependent selectivity, efficient parallel training

**Transformers:**
- Quadratic complexity from pairwise token interactions
- Memory scales linearly with context (problematic for extended sequences)
- Leverage matmul efficiency on accelerators despite algorithmic complexity

## Task-Specific Performance

**Where SSMs Excel:**
SSMs substantially outperform Transformers on "high-resolution" data lacking semantic meaning — byte-level and character-level language modeling. SSMs also dominate where meaningful tokenization is difficult: DNA sequences, audio, time series, raw visual data.

**Where Transformers Dominate:**
Transformers excel when data has been pre-processed to a semantically meaningful level. Tokenized language modeling is the canonical use case. The inductive bias toward individual token attention suits data where each token is semantically meaningful.

## Modeling Power Heuristic

Gu's principle: "The inductive bias of soft attention is hard attention."

| Data Type | Token Meaningfulness | Preferred Architecture |
|-----------|---------------------|----------------------|
| BPE tokens | High | Transformers |
| Characters | Low | SSMs |
| DNA bases | Low | SSMs |

## In-Context Learning & Memory

SSMs cannot memorize and retrieve arbitrary information from context (like reciting a phonebook). However, they maintain long-term fuzzy contextual understanding.

Transformers exhibit perfect recall and fine-grained manipulation of individual tokens but face hard context-length limits.

## Hybrid Approaches

Multiple independent studies (H3, Jamba, Zamba, Samba) found optimal performance using roughly 3:1 to 10:1 ratios of SSM layers to attention layers. State-of-the-art models from NVIDIA (Nemotron-H, 560B+) and Tencent validate this approach.

## Practical Recommendations

1. For tokenized language: Transformers remain appropriate
2. For raw sequential data: Prioritize SSMs or hybrids
3. For mixed modalities: Interleave SSM and attention layers
4. For new domains: Question whether tokenization serves semantic purposes
