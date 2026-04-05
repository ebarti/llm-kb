---
title: "Unstructured.io"
type: entity
entity_type: tool
sources: ["[[sources/unstructured-io-document-etl]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/document-chunking-strategies]]", "[[concepts/ocr-document-extraction]]", "[[entities/langchain]]", "[[entities/llamaindex]]"]
last_compiled: 2026-04-05
summary: "Open-source Python library (Apache 2.0) for document ETL: partition() auto-detects 30+ formats, outputs typed semantic elements, four processing strategies, 14.4k GitHub stars, enterprise platform processes 15M pages/hour."
---

## Overview

Unstructured.io is the leading open-source library for converting unstructured documents into structured, AI-ready data. It serves as the preprocessing layer in [[concepts/document-processing-pipeline]] systems, handling the critical Extract and Transform stages of document ETL.

## Key Features

- **Auto-detection**: `partition()` function detects file type and routes to appropriate handler
- **30+ formats**: PDF, DOCX, PPTX, XLSX, HTML, images, email, XML, JSON, MS Office
- **Typed elements**: Outputs semantic elements (Title, NarrativeText, Table, Image) with metadata
- **Four strategies**: Fast (rule-based), HiRes (AI layout analysis), Auto (smart selection), OCR-only
- **Structure-aware chunking**: Chunks based on document semantics, not just text features

## Technical Details

- **Language**: Python
- **License**: Apache 2.0
- **GitHub**: 14.4k stars, 1.2k forks, 1,880 commits
- **Dependencies**: libmagic-dev, poppler-utils, tesseract-ocr, libreoffice
- **Install**: `pip install "unstructured[all-docs]"`

## Enterprise Platform

The commercial SaaS platform offers:
- 15 million pages/hour processing capacity
- Petabyte-level scalability
- 71 pre-built connectors (cloud storage, LLMs, vector DBs)
- Low-code UI and API access
- Enhanced enrichments and embeddings

## Integrations

Works alongside [[entities/langchain]] (orchestration) and [[entities/llamaindex]] (RAG framework). Typically handles document ingestion while those frameworks handle downstream processing.

## Mentioned In
- [[sources/unstructured-io-document-etl]] — core library documentation and capabilities
- [[sources/pdf-parser-comparison-2026]] — compared with PyMuPDF, Docling, Nougat
