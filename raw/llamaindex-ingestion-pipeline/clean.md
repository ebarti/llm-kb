---
title: "LlamaIndex Ingestion Pipeline and Document Loading"
source: "https://developers.llamaindex.ai/python/framework/module_guides/loading/"
author: "LlamaIndex"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [llamaindex, ingestion, document-loading, rag, transformations, chunking]
type: article
status: raw
discovered_via: search
---

# LlamaIndex Ingestion Pipeline and Document Loading

## Core Components

### Data Loaders (Readers)
Data connectors ingest data from different sources into Document objects.

1. **SimpleDirectoryReader**: Built-in loader for all file types from a local directory. Reads Markdown, PDFs, Word, PowerPoint, images, audio, video.
2. **LlamaParse**: Official tool for PDF parsing, available as managed API. Best-in-class for complex PDFs with tables and figures.
3. **LlamaHub**: Registry of hundreds of data loading libraries for any source.

### Transformation Pipeline

Three main stages after loading:
1. **Chunking**: Split documents into manageable pieces
2. **Metadata Extraction**: Enrich chunks with contextual metadata
3. **Embedding**: Convert each chunk into vector representation

### Node Parsers
- Sentence-based splitting
- Token-based splitting
- HTML parsing
- JSON parsing
- Specialized parsers per format

### Text Splitters
Range from paragraph/sentence/token splitters to file-based splitters (HTML, JSON).

## Ingestion Pipeline

Composable, cache-optimized process for loading data. Transformations are building blocks — each takes a list of Nodes and returns another list after modifications.

### Document Management
Attaching a docstore enables deduplication: actively looks for duplicate documents using `document.doc_id` or `node.ref_doc_id`.

### Vector Store Integration
Passing a vectorstore to the pipeline automatically adds final output nodes from the transformation sequence.

### Advanced Features
- Cache-optimized: skips already-processed documents
- Repeatable: deterministic transformation chains
- Composable: mix and match transformations

## Workflow Pattern

Documents → Node Parsers → Transformations → Nodes → Indexing/Storage

Modular design separates data acquisition from processing, enabling flexible, chainable operations.
