---
title: "A Survey on Temporal Knowledge Graph: Representation Learning and Applications"
source: "https://arxiv.org/abs/2403.04782"
author: "Various (arXiv)"
date_published: 2024-03-07
date_ingested: 2026-04-05
tags: [temporal-knowledge-graph, knowledge-graph-embedding, representation-learning, link-prediction]
type: paper
status: raw
discovered_via: search
---

# A Survey on Temporal Knowledge Graph: Representation Learning and Applications

## Definition and Representation

A temporal knowledge graph (TKG) extends standard knowledge graphs by associating each fact with explicit temporal information. While traditional KGs represent facts as triples (head entity, relation, tail entity), TKGs represent them as quadruples: (h, r, t, τ) where τ denotes the timestamp.

Example: (Barack Obama, make statement, Iran, 2014-6-19)

Formal definition: G=(E,R,T,F) where E represents entities, R represents relations, T represents timestamps, and F⊂E×R×E×T represents the set of all facts.

## Core Representation Learning Categories

The survey identifies ten distinct methodological approaches:

### 1. Transformation-Based Methods

**Translation-Based:**
- **TTransE**: Concatenates temporal information directly to relations, score function ||h+r+τ-t||
- **TA-TransE**: Uses LSTM to learn relation embeddings encoding temporal sequences
- **HyTE**: Projects entities and relations onto temporal hyperplanes specific to each timestamp

**Rotation-Based:**
- **RotatE**: Extends to complex vector space, treating relations as rotations where t = h∘r
- **Tero**: Regards timestamps as entity rotations in complex space
- **ChronoR**: Applies k-dimensional rotation transformations combining relations and timestamps
- **RotateQVS**: Utilizes quaternion vector space for enhanced expressiveness

### 2. Decomposition-Based Methods

Represent TKGs as order-4 tensors decomposed into factor matrices:

**CP Decomposition:**
- **DE-SimplE**: Applies diachronic entity embeddings with time-dependent components
- **TComplEx**: Extends to complex vector space with formula: re(⟨h, r, t̄, τ⟩)

**Tucker Decomposition:**
- **TuckER**: Uses 3-tensor decomposition ⟨W; h, r, t⟩
- **TuckERT**: Extends to order-4 tensors for temporal completion

### 3. Graph Neural Network-Based Methods

- **TEA-GNN**: Employs time-aware attention mechanisms with orthogonal transformations
- **TREA**: Integrates relational and temporal features through graph attention
- **T²TKG**: Uses structural encoders and latent relation learning for intra-time and inter-time patterns

### 4. Autoregression-Based Methods

Model TKGs as temporal snapshots {G₁, G₂, ..., Gₜ}:

- **RE-NET**: Uses R-GCN for structural learning and GRU for temporal dynamics
- **RE-GCN**: Captures structural dependencies, sequential patterns, and static properties
- **TiRGN**: Implements local-global historical pattern modeling

### 5. Temporal Point Process-Based Methods

Treat TKGs as continuous-time event sequences:

- **Know-Evolve**: Characterizes temporal point processes via Rayleigh processes
- **GHNN**: Uses Hawkes processes with continuous-time LSTM
- **EvoKG**: Jointly models evolving network structure and event time

### 6. Interpretability-Based Methods

- **xERTE**: Iteratively constructs explainable subgraphs through temporal relation attention
- **CluSTeR**: Two-stage strategy combining RL-based clue search with evolution modeling
- **TITer**: Uses temporal path-based RL with Dirichlet distribution rewards

### 7. Language Model Integration

**In-Context Learning:**
- **ICLTKG**: Leverages LLMs through few-shot prompting without fine-tuning
- **zrLLM**: Generates enriched relation descriptions for zero-shot learning

**Supervised Fine-Tuning:**
- **ECOLA**: Jointly optimizes knowledge-text prediction and temporal embedding
- **GenTKG** and **Chain of History**: Apply RAG with fine-tuned models

### 8. Few-Shot Learning Methods

- **MetaTKG**: Temporal meta-learning framework for emerging entities
- **TR-Match**: Multi-scale time-relation attention with relation-agnostic matching

## Key Datasets

| Dataset | Entities | Relations | Timestamps | Facts |
|---------|----------|-----------|-----------|-------|
| ICEWS14 | 7,128 | 230 | 365 | 90,730 |
| ICEWS18 | 23,033 | 256 | 304 | 468,558 |
| Wikidata | 12,554 | 24 | 232 | 669,934 |
| GDELT | 7,691 | 240 | 2,751 | 2,278,405 |

## Evaluation Metrics

- **Mean Reciprocal Rank (MRR)**: MRR = (1/|S|) Σ (1/rankᵢ), measures average ranking quality
- **Hits@k**: Percentage of correct answers appearing in top-k predictions

## Applications

- **Interpolation**: Filling missing facts within known time range
- **Extrapolation**: Predicting future unseen facts
- **Entity Alignment**: Mapping corresponding entities across TKGs
- **Temporal Question Answering**: Answering time-dependent queries

## LLM Integration Insights

Current approaches leverage LLMs through:
1. Prompt-based few-shot learning without parameter updates
2. Semantic enrichment via natural language descriptions of relations
3. Supervised fine-tuning jointly optimizing textual and embedding objectives
4. Retrieval-augmented generation combining historical fact retrieval with language model decoding
