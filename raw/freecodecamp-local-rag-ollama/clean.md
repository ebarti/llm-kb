---
title: "How to Build Your Own Local AI: Create Free RAG and AI Agents with Qwen 3 and Ollama"
source: "https://www.freecodecamp.org/news/build-a-local-ai/"
author: "freeCodeCamp"
date_published: 2025-12-15
date_ingested: 2026-04-05
tags: [local-rag, ollama, qwen, chromadb, langchain, knowledge-base, tutorial]
type: article
status: raw
discovered_via: search
---

# Build Local AI with RAG: Qwen 3 + Ollama + ChromaDB

## Architecture
Three-component local AI system:
1. LLM Engine: Qwen 3 models via Ollama
2. Retrieval System: ChromaDB vector database
3. Integration Framework: LangChain orchestration

## Hardware Requirements
- 4B models: 8GB+ RAM
- 8B models: 16GB+ RAM
- 30B MoE models: 16GB+ VRAM
- VRAM dictates largest model that runs efficiently

## RAG Pipeline

### Phase 1: Data Preparation
- Load PDFs with PyPDFLoader or UnstructuredPDFLoader
- Split into chunks (1000 chars, 200 char overlap) using RecursiveCharacterTextSplitter

### Phase 2: Embedding Generation
- Option A (recommended): OllamaEmbeddings with nomic-embed-text
- Option B: HuggingFaceEmbeddings with sentence-transformers

### Phase 3: Vector Storage
ChromaDB with persistent directory for local vector search

### Phase 4: RAG Chain Assembly
- Retriever: similarity search, k=3 default
- Prompt template with context injection
- ChatOllama LLM with num_ctx=8192+
- Output parser

## Critical Configuration
- num_ctx must be 8192+ for effective RAG (default Ollama insufficient)
- chunk_size: 1000 chars, chunk_overlap: 200 chars
- search_type: "similarity" or "mmr"

## AI Agent Extension
- Custom tools via @tool decorator
- ReAct framework with AgentExecutor
- Qwen 3 supports /think and /no_think modes

## Installation
```bash
curl -fsSL https://ollama.com/install.sh | sh
pip install langchain langchain-community langchain-ollama chromadb sentence-transformers pypdf
```

## Key Design Principles
- Privacy: all data stays local
- Cost: zero per-token charges
- Offline: works without internet
- Caveat: local models may struggle with complex agentic reasoning vs cloud models
