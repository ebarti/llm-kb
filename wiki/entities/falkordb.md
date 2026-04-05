---
title: "FalkorDB"
type: entity
entity_type: tool
sources: ["[[sources/branzan-production-knowledge-graphs-2025]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/graphrag]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "Graph database with GraphRAG SDK for performance-critical knowledge graph deployments. Sub-50ms query latency, 90% hallucination reduction vs. traditional RAG, multi-model support (OpenAI, Gemini, Anthropic, Groq, Ollama). Self-hosted or cloud deployment."
---

## Overview

FalkorDB is a graph database with a purpose-built GraphRAG SDK designed for performance-critical knowledge graph deployments. It combines native graph operations with LLM-powered knowledge extraction and retrieval.

## Key Specifications

- **Query latency**: Sub-50ms
- **Hallucination reduction**: 90% vs. traditional RAG
- **Model support**: OpenAI, Gemini, Anthropic, Groq, Ollama, local models
- **Deployment**: Self-hosted or cloud
- **API**: Clean Python API with async support

## Best For

Performance-critical deployments requiring graph-native RAG operations, where query latency and hallucination reduction are primary concerns.

## Mentioned In

- [[sources/branzan-production-knowledge-graphs-2025]] -- detailed as first of five production-ready KG tools
