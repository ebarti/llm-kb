---
title: "Knowledge Graph Completion"
type: concept
sources: ["[[sources/kg-llm-link-prediction]]", "[[sources/knowledge-graph-embeddings-overview]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/knowledge-graph-embeddings]]", "[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge-graphs]]"]
last_compiled: 2026-04-05
summary: "Predicting missing facts in incomplete knowledge graphs via link prediction, relation prediction, and triple classification — now dramatically improved by LLM-based approaches outperforming traditional embedding methods."
---

## Overview

Knowledge graph completion (KGC) addresses the fundamental incompleteness of real-world knowledge graphs. Even the largest KGs (Wikidata, Freebase) contain significant gaps. KGC methods predict missing triples — given (h, ?, t) predict the relation, given (h, r, ?) predict the tail entity, or given (?, r, t) predict the head entity.

## Core Tasks

### Link Prediction

The primary KGC task: predicting missing entities in incomplete triples. Given a query like (Barack Obama, born_in, ?), the system ranks all candidate entities by plausibility.

### Relation Prediction

Predicting the relationship between two known entities: given (Entity_A, ?, Entity_B), determine the most likely relation.

### Triple Classification

Binary classification: is a given triple (h, r, t) true or false? Used for knowledge graph validation and quality assurance.

## Traditional Approaches: Knowledge Graph Embeddings

[[concepts/knowledge-graph-embeddings]] are the classical approach to KGC:

- **Translational models** (TransE, RotatE): Model relations as geometric transformations
- **Tensor decomposition** (DistMult, ComplEx): Decompose the KG tensor
- **Deep learning** (ConvE, CapsE): Learn non-linear interaction patterns

These methods excel at efficient single-hop prediction but struggle with multi-hop reasoning requiring intermediate entity consideration.

## LLM-Based Approaches

LLMs have transformed KGC by bringing language understanding to graph reasoning:

### KG-LLM Framework

The [[sources/kg-llm-link-prediction]] paper converts knowledge graph paths to natural language chain-of-thought prompts and fine-tunes LLMs for multi-hop link prediction. Results are dramatic:

- **Traditional KGE** (TransE, ComplEx, DistMult): F1 = 0.25-0.61
- **KG-LLM** (Gemma-7B, fine-tuned): F1 = 0.84
- **KG-LLM + In-Context Learning**: F1 = 0.98

### Other LLM Approaches

- **KGaP (Knowledge Graph as Prompt)**: Enhances LLM reasoning with graph structure information
- **SAT**: Structure-aware alignment-tuning aligning graph embeddings with natural language space
- **LPNL**: Leverages LLMs for scalable link prediction on heterogeneous graphs

### Why LLMs Outperform KGE

Traditional KGE methods model direct pairwise relationships but struggle with multi-hop reasoning that requires considering intermediate entities. LLMs, through chain-of-thought prompting, can reason step-by-step through multi-hop paths, leveraging their language understanding to interpret relation semantics rather than treating them as abstract vectors.

## Temporal Knowledge Graph Completion

[[concepts/temporal-knowledge-graphs]] add a temporal dimension to KGC, predicting missing facts conditioned on time:
- **Interpolation**: Filling missing facts within known time ranges
- **Extrapolation**: Predicting future facts based on historical patterns

## Sources

- [[sources/kg-llm-link-prediction]] — LLM fine-tuning for multi-hop link prediction
- [[sources/knowledge-graph-embeddings-overview]] — traditional KGE methods
- [[sources/llm-kg-construction-survey]] — survey including KGC approaches

## Related Concepts

- [[concepts/knowledge-graph-embeddings]] — the traditional approach
- [[concepts/knowledge-graph]] — the structure being completed
- [[concepts/temporal-knowledge-graphs]] — time-aware completion
