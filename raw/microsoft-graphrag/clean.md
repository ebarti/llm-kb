---
title: "GraphRAG: Unlocking LLM Discovery on Narrative Private Data"
source: "https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/"
author: "Microsoft Research"
date_published: 2024-02-13
date_ingested: 2026-04-05
tags: [graphrag, knowledge-graph, rag, microsoft, retrieval]
type: article
status: raw
discovered_via: search
---

# GraphRAG: Unlocking LLM Discovery on Narrative Private Data

## Overview

Microsoft Research introduced GraphRAG, a system that enhances LLMs' ability to analyze private datasets through knowledge graph construction and graph machine learning.

## Key Problems with Baseline RAG

Traditional RAG struggles in two main scenarios:
1. **Connection gaps**: Difficulty synthesizing insights across disparate information pieces that share attributes
2. **Holistic understanding**: Poor performance when summarizing semantic concepts across large documents or entire collections

"Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections."

## How GraphRAG Works

### Knowledge Graph Construction

1. LLMs process entire datasets, identifying entities (people, places, organizations) and relationships, creating a foundation knowledge graph
2. Graph machine learning performs bottom-up clustering to organize data hierarchically into semantic clusters
3. Pre-summarization enables understanding at multiple abstraction levels

### Architecture

"The graph is then used alongside graph machine learning to perform prompt augmentation at query time," enabling more relevant context retrieval than similarity-based vector searches.

## Performance Comparison

### Exploratory Query: "What is Novorossiya?"
Both systems performed adequately.

### Connecting Information: "What has Novorossiya done?"
Baseline RAG returned no results; GraphRAG identified destructive activities with specific supporting relationships.

### Whole-Dataset Analysis: Top themes in Ukraine-Russia conflict data
**Baseline RAG** returned irrelevant themes (urban development, economic growth).
**GraphRAG** correctly identified conflict/military activity, political entities, infrastructure concerns, community analysis, and health/humanitarian issues.

## Evaluation Results

GraphRAG consistently outperforms baseline RAG on comprehensiveness, human enfranchisement (supporting evidence), and diversity of viewpoints. Faithfulness measurement via SelfCheckGPT showed GraphRAG achieves similar faithfulness to baseline RAG.

## Provenance

GraphRAG links conclusions to original supporting documents, enabling human auditors to verify claims — critical for trustworthiness.

## Applications

Tested across social media, news articles, workplace productivity, and chemistry domains.
