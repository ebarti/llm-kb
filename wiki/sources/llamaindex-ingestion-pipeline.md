---
title: "Source: LlamaIndex Ingestion Pipeline and Document Loading"
type: source-summary
source: "[[raw/llamaindex-ingestion-pipeline]]"
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/document-chunking-strategies]]", "[[entities/llamaindex]]", "[[entities/llamaparse]]"]
last_compiled: 2026-04-05
summary: "LlamaIndex's composable ingestion pipeline: SimpleDirectoryReader + LlamaParse loaders, node parsers (sentence/token/HTML/JSON), cache-optimized transformations, docstore deduplication, and automatic vector store integration."
---

## Key Points

- Three-tier loading: SimpleDirectoryReader (local files), LlamaParse (complex PDFs), LlamaHub (hundreds of connectors)
- Ingestion pipeline is composable: Documents → Node Parsers → Transformations → Nodes → Index
- Node parsers: sentence-based, token-based, HTML, JSON, specialized per format
- Cache-optimized: skips already-processed documents automatically
- Docstore attachment enables deduplication via doc_id/ref_doc_id
- Vector store integration: final nodes automatically added to attached store

## Detailed Summary

[[entities/llamaindex]]'s ingestion pipeline is the most fully-featured framework-level implementation of a [[concepts/document-processing-pipeline]]. Its design embodies the principle that data loading should be modular, composable, and cache-aware.

The three-tier loading architecture is pragmatic: SimpleDirectoryReader handles the 80% case (local files in common formats), [[entities/llamaparse]] tackles the hard 15% (complex PDFs with tables and figures), and LlamaHub covers the long tail of exotic sources.

For [[concepts/document-chunking-strategies]], LlamaIndex provides node parsers that split documents into typed nodes. The framework's insight is that different document types need different parsers: HTML documents should be split at tag boundaries, JSON at structural keys, and plain text at sentence or token boundaries.

The deduplication feature is particularly relevant for knowledge base pipelines: by tracking document IDs through a docstore, the pipeline can detect when a source has already been ingested and skip redundant processing. This is the framework equivalent of [[concepts/incremental-etl]] — processing only what's new.

The cache-optimization means that re-running the pipeline after adding new documents only processes the new ones, making incremental updates efficient.

## Related Concepts
- [[concepts/document-processing-pipeline]] — LlamaIndex's framework-level implementation
- [[concepts/document-chunking-strategies]] — node parsers as chunking mechanism
- [[concepts/incremental-etl]] — docstore deduplication enables incremental processing
