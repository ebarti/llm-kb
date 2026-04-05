---
title: "Knowledge Graph Embeddings"
type: concept
sources: ["[[sources/knowledge-graph-embeddings-overview]]", "[[sources/kg-llm-link-prediction]]", "[[sources/temporal-knowledge-graphs-survey]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/knowledge-graph-completion]]", "[[concepts/temporal-knowledge-graphs]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Machine learning methods that map knowledge graph entities and relations to continuous vector spaces for link prediction, with three model families (translational, tensor decomposition, deep learning) increasingly complemented by LLM approaches."
---

## Overview

Knowledge graph embeddings (KGE) learn low-dimensional vector representations of a [[concepts/knowledge-graph]]'s entities and relations while preserving their semantic meaning. Given a knowledge graph with entities E, relations R, and facts (triples of the form (head, relation, tail)), KGE methods define a scoring function f_r(h,t) that measures how plausible a given triple is.

These methods are fundamental to [[concepts/knowledge-graph-completion]] — predicting missing facts in incomplete knowledge graphs.

## Major Model Families

### Translational / Geometric Models

Represent relations as geometric transformations between entity embeddings:

| Model | Approach | Limitation |
|-------|----------|------------|
| **TransE** | h + r = t (translation) | Fails on 1-to-N, symmetric relations |
| **TransH** | Projects onto relation-specific hyperplanes | More parameters |
| **TransR** | Separate entity/relation embedding spaces | Expensive projection matrices |
| **TransD** | Dynamic mappings (lighter than TransR) | Still limited expressiveness |
| **RotatE** | Relations as rotations in complex space | Superior to TransE family |

TransE (2013) is the foundational model, enforcing the simple constraint that h + r should approximate t. Despite its elegance, it cannot model one-to-many, many-to-one, or symmetric relations, motivating the extensions above.

### Tensor Decomposition Models

Decompose the knowledge graph as a 3-way tensor:

- **DistMult**: Diagonal matrices for relations; struggles with asymmetric facts
- **ComplEx**: Complex vector spaces enabling asymmetric relation handling
- **TuckER**: Tucker decomposition with learned core tensor
- **SimplE**: Separate head/tail embeddings via canonical polyadic decomposition

### Deep Learning Models

Learn non-linear interaction patterns:

- **ConvE**: 2D convolutions with 8x fewer parameters than DistMult
- **ConvKB**: 1D convolutions over concatenated triple elements
- **CapsE**: Capsule networks preserving spatial information
- **RSN**: Recurrent networks learning relational paths via random walks

## Training Methodology

1. Initialize entity and relation embeddings randomly
2. Sample batches of true triples from the training set
3. Generate corrupted triples by substituting head or tail with random entities
4. Minimize a loss function that makes true triples score higher than corrupted ones
5. Iterate until convergence or overfitting

## Evaluation Metrics

- **Hits@K**: Proportion of correct predictions in top K results
- **Mean Rank (MR)**: Average rank of correct predictions (lower = better)
- **Mean Reciprocal Rank (MRR)**: Average of 1/rank for correct predictions (higher = better)

Standard benchmarks: FB15k-237, WN18RR, YAGO3-10.

## KGE vs. LLM Approaches

The [[sources/kg-llm-link-prediction]] paper demonstrates that LLMs fine-tuned on knowledge graph data dramatically outperform traditional KGE methods on multi-hop link prediction:

| Method | F1 (WN18RR) | F1 (NELL-995) |
|--------|-------------|---------------|
| TransE, ComplEx, DistMult | 0.25-0.61 | 0.25-0.61 |
| KG-LLM (Gemma-7B) | 0.84 | 0.82 |
| KG-LLM + ICL | 0.98 | 0.95 |

This suggests that for complex multi-hop reasoning, LLM language understanding offers fundamental advantages over geometric/algebraic embeddings. However, KGE methods remain valuable for:
- Efficient single-hop link prediction at scale
- Interpretable, structured representations
- Integration with downstream ML pipelines
- Lower computational cost than LLM inference

## Temporal Extensions

[[concepts/temporal-knowledge-graphs]] extend KGE to handle time-varying facts, with methods like TTransE, DE-SimplE, and TComplEx adding temporal dimensions to standard embedding approaches.

## Sources

- [[sources/knowledge-graph-embeddings-overview]] — comprehensive overview of models and training
- [[sources/kg-llm-link-prediction]] — LLM approaches outperforming KGE on multi-hop tasks
- [[sources/temporal-knowledge-graphs-survey]] — temporal extensions of KGE methods

## Related Concepts

- [[concepts/knowledge-graph]] — the structure being embedded
- [[concepts/knowledge-graph-completion]] — primary application
- [[concepts/temporal-knowledge-graphs]] — temporal extensions
- [[concepts/vector-databases]] — related embedding-based technology
