---
title: "Unstructured.io: Open-Source Document ETL for AI"
source: "https://github.com/Unstructured-IO/unstructured"
author: "Unstructured.io"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [unstructured, document-processing, etl, pdf, ocr, partitioning]
type: repo
status: raw
discovered_via: search
---

# Unstructured.io: Open-Source Document ETL for AI

Open-source Python library for transforming complex documents into structured data for LLMs. Apache 2.0 licensed. 14.4k GitHub stars.

## Core Architecture

**Partition Functions**: Primary interface uses automatic file detection routing. The `partition()` function detects file types and directs them to appropriate handlers.

**Processing Pipeline**:
1. Detection and ingestion
2. Layout analysis
3. Character recognition (OCR)
4. Content extraction
5. Structured output generation

## Supported Formats
30+ file formats: PDF, DOCX, PPTX, XLSX, HTML, images, email, plain text, XML, JSON, MS Office formats.

## Key Features

**Document Element System**: Processes documents into semantic elements (titles, text blocks, tables, images) with metadata preservation. Typed Element objects: Title, NarrativeText, Table, Image, etc.

**Partitioning Strategies**: Multiple strategies optimized for different needs:
- Fast: Rule-based, quickest processing
- HiRes: AI-powered layout analysis for complex documents
- Auto: Automatically selects optimal strategy
- OCR-only: For scanned documents

**Chunking**: Uses deep understanding of document formats to partition into semantic units rather than relying solely on text-based features.

## Installation

```
pip install "unstructured[all-docs]"  # All document types
pip install "unstructured[docx,pptx]"  # Specific formats
```

System dependencies: libmagic-dev, poppler-utils, tesseract-ocr, libreoffice.

## Enterprise Platform
SaaS platform processes over 15 million pages per hour with petabyte-level scalability. 71 pre-built connectors across storage, LLMs, and vector databases.

## Comparison with LangChain

Unstructured specializes in document preprocessing/ETL; LangChain is an LLM application framework. They complement each other: Unstructured for ingestion, LangChain for orchestration. Unstructured is better for production document pipelines; LangChain for exploratory LLM development.

## Batch Processing
Separate `unstructured-ingest` repository handles large-scale document processing with connectors for cloud storage and databases.
