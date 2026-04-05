---
title: "From RAG to Context — A 2025 Year-End Review of RAG"
source: "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
author: "RAGFlow Team"
date_published: 2025-12-31
date_ingested: 2026-04-05
tags: [rag, context-engineering, treerag, graphrag, multimodal-rag, enterprise-ai]
type: article
status: raw
discovered_via: search
---

# From RAG to Context — A 2025 Year-End Review of RAG

## Overview

RAG has evolved significantly throughout 2025, contrary to predictions of its obsolescence. The technology has solidified its role as "a cornerstone of data infrastructure in the demanding arena of enterprise AI adoption," particularly among mid-to-large organizations genuinely investing in AI capabilities.

## Long Context vs. RAG Debate

The question of whether extended context windows could replace RAG proved inconclusive. Research demonstrated that simply feeding massive document batches into language models causes attention scatter and "information flooding" effects, degrading answer quality. Instead of replacement, the optimal approach combines both: "retrieval-first, long-context containment" creates synergistic benefits where models hold more complete, semantically coherent retrieved chunks.

Four approaches to knowledge provision with roughly two-order-of-magnitude cost differences:
- Relying solely on LLM's extended context capability
- Utilizing KV Cache systems
- Using simple search methods like Grep
- Employing full RAG architecture

## TreeRAG Architecture

A significant architectural advance involves decoupling RAG into distinct "Search" and "Retrieve" stages using different text granularities. RAGFlow's TreeRAG technology exemplifies this approach by:

- **Offline processing**: Using language models to analyze documents and construct hierarchical directory summaries (Chapter → Section → Subsection)
- **Online retrieval**: Performing similarity search on fine-grained fragments, then dynamically assembling larger, coherent context pieces using the pre-built directory structure

This methodology addresses the "Lost in the Middle" problem where fixed-size chunks either fragment context or introduce excessive noise.

## Graph-Based Approaches

GraphRAG extracts entities and relationships to build knowledge graphs for discovering indirectly related information. However, implementations revealed significant challenges: massive token consumption (several to dozens times original text), quality gaps between expected and actual extraction, and fragmented knowledge outputs requiring sophisticated LLM integration for coherent narratives.

Hybrid architectures combining TreeRAG's local semantic strengths with GraphRAG's relational discovery capabilities represent a promising direction.

## Evolution from Knowledge Bases to Data Foundations

RAG systems are transitioning beyond isolated Q&A applications toward foundational data platforms serving AI Agents. This requires robust Ingestion Pipelines (PTI: Parse-Transform-Index) analogous to traditional ETL/ELT systems but designed for unstructured data.

Key pipeline stages:
- **Parsing**: Converting multi-modal documents (PDFs, images, audio) into structured text using specialized models like DeepDoc
- **Transform**: Leveraging language models for semantic enhancement—tree generation, knowledge graphs, summaries, question generation, keyword extraction
- **Indexing**: Building efficient indexes supporting hybrid retrieval (vector, keyword, metadata filtering)

## The Shift to Context Engineering

Rather than being replaced by Agents, RAG's core retrieval capability has become central to a broader discipline: Context Engineering. The critical insight is that "no matter how intelligent an Agent is, the quality of its decisions and actions fundamentally depends on the quality and relevance of the Context it receives."

Modern Agents require intelligent assembly of three data categories:
1. **Domain Knowledge**: Traditional RAG retrieving enterprise documents and knowledge bases
2. **Tool Data**: Dynamically filtering relevant tool descriptions through Tool Retrieval
3. **Conversation State**: Managing historical interactions, user preferences, and internal Agent state through memory systems

## Multimodal RAG Progress

Multimodal RAG advancement stalled in 2025 due to engineering challenges. Two technical paths exist:
1. **Modality Conversion**: Converting images/tables to text descriptions via OCR or vision-language models
2. **Native Multimodal Path**: Direct visual tokenization creating fused multi-vector representations

The primary bottleneck is storage and computational costs from tensor data explosion. A single page image from models like ColPali generating 1024 tokens occupies ~512KB; scaling to million-page datasets produces terabyte-level indices.

## 2026 Outlook

RAG is "undergoing its own profound metamorphosis, evolving from the specific pattern of 'Retrieval-Augmented Generation' into a 'Context Engine' with 'intelligent retrieval' as its core capability."
