---
title: "GraphRAG: Unlocking LLM Discovery on Narrative Private Data"
source: "https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/"
author: "Microsoft Research"
date_published: 2024-07-02
date_ingested: 2026-04-05
tags: [graphrag, knowledge-graph, rag, llm, community-detection, summarization]
type: article
status: raw
discovered_via: search
---

# GraphRAG: Unlocking LLM Discovery on Narrative Private Data

## Motivation

GraphRAG addresses fundamental limitations in baseline RAG systems. Microsoft researchers identified two critical failure modes: baseline RAG "struggles to connect the dots" when answers require traversing disparate information through shared attributes, and it "performs poorly when being asked to holistically understand summarized semantic concepts" across large datasets.

## Knowledge Graph Construction

The LLM processes the entire private dataset to create an entity-relationship graph by extracting all entities (persons, places, organizations) and their relationships. This process establishes connections throughout the source material without manual annotation.

## Indexing Pipeline

The indexing process follows four key stages:

1. **Text Segmentation**: Input corpus is divided into TextUnits serving as analyzable chunks with granular reference capabilities.
2. **Information Extraction**: The system extracts all entities, relationships, and key claims from the TextUnits.
3. **Hierarchical Clustering**: Uses the Leiden technique to organize the graph hierarchically. Each circle is an entity (e.g., a person, place, or organization), with the size representing the degree.
4. **Community Summarization**: Generates summaries of each community and its constituents from the bottom-up to enable holistic understanding.

## Community Detection and Clustering

The system employs bottom-up clustering on the graph structure to organize data hierarchically into semantic clusters. The visualization shows entities as circles where size represents relationship count, with color indicating cluster membership. This partitioning enables multi-level analysis.

## Hierarchical Summarization

Pre-summarized semantic concepts and themes are generated for each cluster, allowing the system to answer questions at varying levels of abstraction — from specific entity relationships to dataset-wide patterns.

## Query Modes

GraphRAG provides three specialized search approaches:

- **Global Search**: Reasons about corpus-wide questions using community summaries. Best for holistic/thematic queries.
- **Local Search**: Focuses on specific entities and their neighbors. Best for entity-specific questions.
- **DRIFT Search**: Similar to Local Search but incorporates additional community context.
- **Basic Search**: Falls back to conventional vector retrieval when appropriate.

## Performance Comparison

### Where GraphRAG Excels

The system dramatically outperforms baseline RAG on "connecting the dots" questions. When asked "What has Novorossiya done?" baseline RAG returned no results, while GraphRAG identified specific planned destructive activities with source provenance.

### Whole-Dataset Reasoning

For thematic queries like "What are the top 5 themes?" baseline RAG retrieved irrelevant results, while GraphRAG accurately identified conflict, political entities, infrastructure concerns, community analysis, and humanitarian issues present in the dataset.

## Evaluation Results

GraphRAG "consistently outperforms baseline RAG" on qualitative metrics including comprehensiveness, human enfranchisement (source provision), and diversity. The system maintains "similar level of faithfulness to baseline RAG" using SelfCheckGPT measurements, ensuring factual accuracy grounded in source material.

## Optimization

Using GraphRAG with your data out of the box may not yield the best possible results. The system recommends following their Prompt Tuning Guide for domain-specific optimization.
