---
title: "LangChain"
type: entity
entity_type: tool
sources: ["[[sources/unstructured-io-document-etl]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/document-chunking-strategies]]", "[[entities/unstructured-io]]", "[[entities/llamaindex]]"]
last_compiled: 2026-04-05
summary: "Open-source LLM application framework: document loaders, RecursiveCharacterTextSplitter for chunking, chains (Stuff/Refine/MapReduce) for document processing, and extensive LLM provider integrations."
---

## Overview

LangChain is the most widely-used open-source framework for building applications powered by large language models. For [[concepts/document-processing-pipeline]] systems, it provides document loaders, text splitters, and document chains that handle the Transform and Load stages of document ETL.

## Key Components for Document Processing

### Document Loaders
Specialized components that convert data from various sources into standardized Document objects with `page_content` and `metadata` attributes. Supports `.load()` (all at once) and `.lazy_load()` (incremental).

### Text Splitters
- **RecursiveCharacterTextSplitter**: Default — iterates separators ["\n\n", "\n", " ", ""] to preserve semantic units
- Configurable `chunk_size` and `chunk_overlap` parameters
- HTML, Markdown, and code-aware splitters available

### Document Chains
- **Stuff**: Simple — concatenate all documents into one prompt
- **Refine**: Sequential — maintain running context across documents
- **MapReduce**: Parallel — process documents independently, then combine

### LLM Integration
Extensive provider support: OpenAI, Anthropic, Google, local models via Ollama/vLLM.

## Relationship to Unstructured

LangChain and [[entities/unstructured-io]] complement each other: Unstructured handles document ETL (Extract + Transform), LangChain handles orchestration (Load + Query). Production systems often use both.

## Mentioned In
- [[sources/unstructured-io-document-etl]] — comparison with Unstructured
- [[sources/rag-chunking-strategies-dasroot]] — RecursiveCharacterTextSplitter benchmarks
