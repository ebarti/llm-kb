---
title: "LlamaIndex"
type: entity
entity_type: tool
sources: ["[[sources/llamaindex-ingestion-pipeline]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/document-chunking-strategies]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[entities/llamaparse]]"]
last_compiled: 2026-04-05
summary: "Leading RAG framework with composable ingestion pipeline: SimpleDirectoryReader + LlamaParse + LlamaHub loaders, node parsers for chunking, cache-optimized transformations, docstore deduplication, and automatic vector store integration."
---

## Overview

LlamaIndex (formerly GPT-Index) is the leading open-source framework for building RAG (Retrieval-Augmented Generation) applications. Its ingestion pipeline provides the most fully-featured framework-level implementation of a [[concepts/document-processing-pipeline]], with composable, cache-optimized document loading, transformation, and indexing.

## Key Components

### Data Loading
- **SimpleDirectoryReader**: Local files in common formats (PDF, DOCX, images, audio, video)
- **[[entities/llamaparse]]**: Managed API for complex PDF parsing
- **LlamaHub**: Registry of hundreds of community data connectors

### Ingestion Pipeline
- **Node Parsers**: Sentence, token, HTML, JSON splitting
- **Metadata Extractors**: LLM-powered metadata enrichment
- **Transformations**: Composable chain of processing steps
- **Cache optimization**: Skip already-processed documents
- **Docstore deduplication**: Track document IDs to avoid reprocessing

### Indexing & Retrieval
- **Vector Store Index**: Standard embedding-based retrieval
- **Summary Index**: Full-document access
- **Tree Index**: Hierarchical summarization
- **Knowledge Graph Index**: Graph-based retrieval

## Mentioned In
- [[sources/llamaindex-ingestion-pipeline]] — ingestion pipeline documentation
- [[sources/firecrawl-web-data-api]] — Firecrawl integration
