---
title: "Temporal Knowledge Graphs"
type: concept
sources: ["[[sources/temporal-knowledge-graphs-survey]]", "[[sources/graphiti-temporal-knowledge-graphs]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge]]", "[[concepts/knowledge-graph-embeddings]]", "[[concepts/knowledge-graph-completion]]"]
last_compiled: 2026-04-05
summary: "Knowledge graphs that associate facts with explicit temporal information (timestamps or intervals), enabling reasoning about what was true when — with 10+ method categories from translation-based to LLM-integrated approaches."
---

## Overview

Temporal knowledge graphs (TKGs) extend standard [[concepts/knowledge-graph]] structures by associating each fact with explicit temporal information. While traditional KGs represent facts as triples (head, relation, tail), TKGs use quadruples: **(h, r, t, τ)** where τ denotes the timestamp or time interval.

Example: (Barack Obama, make_statement, Iran, 2014-06-19)

Formal definition: G=(E, R, T, F) where E = entities, R = relations, T = timestamps, F ⊂ E x R x E x T = facts.

This temporal dimension is critical for representing evolving knowledge — facts that change over time, such as a person's employment, a country's leader, or a company's market position.

## Core Tasks

### Interpolation

Filling missing facts within known time ranges. Given a TKG with some facts missing at certain timestamps, predict what was true but unrecorded.

### Extrapolation

Predicting future facts based on historical patterns. Given the history of a TKG up to time t, predict what will happen at time t+1. This is the more challenging task, requiring temporal pattern recognition.

### Entity Alignment

Mapping corresponding entities across different temporal knowledge graphs using shared semantic and temporal properties.

### Temporal Question Answering

Answering time-dependent queries like "Who was the President of France in 2018?" or "When did Company X acquire Company Y?"

## Representation Learning Methods

The [[sources/temporal-knowledge-graphs-survey]] identifies ten distinct categories:

### Translation-Based Methods

Extensions of [[concepts/knowledge-graph-embeddings]] with temporal information:
- **TTransE**: Concatenates temporal info to relations: score = ||h + r + τ - t||
- **TA-TransE**: Uses LSTM to encode temporal sequences into relation embeddings
- **HyTE**: Projects onto temporal hyperplanes specific to each timestamp

### Rotation-Based Methods

- **RotatE extensions**: Treating timestamps as entity rotations in complex space
- **ChronoR**: k-dimensional rotation transformations combining relations and timestamps
- **RotateQVS**: Quaternion vector space for enhanced expressiveness

### Decomposition-Based Methods

Order-4 tensor decomposition:
- **DE-SimplE**: Diachronic entity embeddings with time-dependent components
- **TComplEx**: Complex-valued temporal decomposition
- **TuckERT**: Order-4 Tucker decomposition for temporal completion

### Graph Neural Network Methods

- **TEA-GNN**: Time-aware attention with orthogonal transformations
- **TREA**: Integrated relational and temporal graph attention
- **T²TKG**: Structural encoders for intra-time and inter-time patterns

### Autoregressive Methods

Model TKGs as temporal snapshots {G₁, G₂, ..., Gₜ}:
- **RE-NET**: R-GCN for structure + GRU for temporal dynamics
- **RE-GCN**: Captures structural dependencies, sequential patterns, and static properties

### Temporal Point Process Methods

Continuous-time event modeling:
- **Know-Evolve**: Rayleigh process intensity functions
- **EvoKG**: Joint modeling of evolving structure and event timing
- **TANGO**: Neural ODEs for continuous-time evolution

### LLM-Integrated Methods

The frontier of temporal KG reasoning:
- **ICLTKG**: Few-shot prompting without fine-tuning
- **ECOLA**: Joint knowledge-text prediction with temporal embeddings
- **GenTKG**: RAG with fine-tuned language models for temporal prediction
- **zrLLM**: Enriched relation descriptions for zero-shot temporal reasoning

## Key Datasets

| Dataset | Entities | Relations | Timestamps | Facts |
|---------|----------|-----------|-----------|-------|
| ICEWS14 | 7,128 | 230 | 365 | 90,730 |
| ICEWS18 | 23,033 | 256 | 304 | 468,558 |
| Wikidata | 12,554 | 24 | 232 | 669,934 |
| GDELT | 7,691 | 240 | 2,751 | 2,278,405 |

## Practical Implementation: Graphiti

[[sources/graphiti-temporal-knowledge-graphs]] provides a practical open-source implementation of temporal knowledge graphs via the Graphiti framework (by Zep AI). Rather than academic benchmarks, Graphiti focuses on AI agent memory with time-windowed facts, hybrid retrieval (semantic + BM25 + graph traversal), and full provenance tracking. See [[concepts/temporal-knowledge]] for details.

## Sources

- [[sources/temporal-knowledge-graphs-survey]] — comprehensive academic survey with 10 method categories
- [[sources/graphiti-temporal-knowledge-graphs]] — practical open-source implementation

## Related Concepts

- [[concepts/knowledge-graph]] — the static foundation that TKGs extend
- [[concepts/temporal-knowledge]] — broader concept of temporal reasoning
- [[concepts/knowledge-graph-embeddings]] — foundation methods extended temporally
- [[concepts/knowledge-graph-completion]] — temporal completion as a key task
