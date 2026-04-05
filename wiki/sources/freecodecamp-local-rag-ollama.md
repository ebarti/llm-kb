---
title: "Source: Build Local AI with RAG using Qwen 3 and Ollama"
type: source-summary
source: "[[raw/freecodecamp-local-rag-ollama]]"
related: ["[[concepts/local-knowledge-base]]", "[[entities/ollama]]", "[[entities/chromadb]]", "[[concepts/local-llm-inference]]"]
last_compiled: 2026-04-05
summary: "Step-by-step tutorial for building a fully local RAG system: Ollama + Qwen 3 + ChromaDB + LangChain — zero cloud dependency, handles PDFs with embeddings via nomic-embed-text."
---

## Key Points
- Three-component architecture: Ollama (LLM), ChromaDB (vectors), LangChain (orchestration)
- Embedding: nomic-embed-text via Ollama or sentence-transformers via HuggingFace
- RAG pipeline: load PDFs → split chunks (1000 chars, 200 overlap) → embed → store → retrieve → generate
- Critical config: num_ctx must be 8192+ (Ollama default is insufficient for RAG)
- Hardware: 8GB+ RAM for 4B models, 16GB+ for 8B models
- Extends to AI agents via ReAct framework with tool calling
- Qwen 3 /think and /no_think modes for adjusting reasoning depth
- Caveat: local models may struggle with complex agentic reasoning vs cloud models

## Detailed Summary

This freeCodeCamp tutorial provides a complete blueprint for building a [[concepts/local-knowledge-base]] without any cloud API. The architecture mirrors the existing [[concepts/llm-knowledge-base]] approach in this KB but replaces the Claude API with [[entities/ollama]] serving Qwen 3, and adds vector-based retrieval via [[entities/chromadb]].

The most relevant finding for this KB system: the same Ollama + LangChain + ChromaDB stack could theoretically replace the Claude API for wiki compilation and Q&A, though with reduced quality for complex reasoning tasks.

## Related Concepts
- [[concepts/local-knowledge-base]] — primary subject; practical how-to
- [[concepts/llm-knowledge-base]] — comparison with existing cloud-based approach
- [[concepts/rag-vs-index-based-retrieval]] — this tutorial uses RAG; our KB uses index-based
