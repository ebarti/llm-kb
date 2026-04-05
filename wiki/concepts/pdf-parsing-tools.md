---
title: "PDF Parsing Tools"
type: concept
sources: ["[[sources/pdf-parser-comparison-2026]]", "[[sources/unstructured-io-document-etl]]", "[[sources/llamaindex-ingestion-pipeline]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/ocr-document-extraction]]", "[[entities/pymupdf]]", "[[entities/docling]]", "[[entities/llamaparse]]", "[[entities/unstructured-io]]"]
last_compiled: 2026-04-05
summary: "PDF parsing tool landscape: PyMuPDF4LLM (fastest, 0.12s), Docling (best enterprise, 9/10), Nougat (best scientific), LlamaParse (best tables), Unstructured (best multi-format) — with two paradigms: pipeline vs. end-to-end."
---

## Overview

PDF parsing is one of the most challenging stages in any [[concepts/document-processing-pipeline]] because PDFs are designed for visual rendering, not data extraction. Text can be in arbitrary positions, tables have no semantic markup, and scanned pages are just images. The choice of PDF parsing tool has an outsized impact on downstream quality.

## Two Fundamental Paradigms

### Pipeline Paradigm
Separate stages: OCR → layout analysis → table detection → text extraction. Modular, debuggable, each stage can be optimized independently. Used by Unstructured (Fast/HiRes modes), Docling (DocLayNet + TableFormer), and traditional OCR+extraction pipelines.

### End-to-End Paradigm
Single model handles full document understanding. Faster, less configuration, but less controllable. Used by Nougat, VLM-based approaches (Qwen2.5-VL, GLM-4.5V), and emerging multimodal models.

## Tool Comparison

### PyMuPDF / PyMuPDF4LLM
- **Speed**: Fastest — 0.12 seconds for markdown output
- **Accuracy**: High on digital PDFs, most consistent recall among rule-based tools
- **Best for**: High-volume digital PDF processing
- **Limitation**: Struggles with complex scanned documents
- **License**: AGPL/commercial

### Docling (IBM)
- **Speed**: Moderate
- **Accuracy**: 9/10 overall performance
- **Best for**: Enterprise RAG pipelines, air-gapped environments
- **Special**: DocLayNet layout analysis, TableFormer table recognition, OCR support
- **License**: MIT

### Unstructured
- **Speed**: Moderate (depends on strategy)
- **Accuracy**: High with HiRes mode
- **Best for**: Multi-format ETL pipelines (not PDF-only)
- **Special**: 30+ formats, Fast/HiRes/Auto/OCR strategies, typed elements
- **License**: Apache 2.0

### Nougat (Meta)
- **Speed**: Slow (learning-based)
- **Accuracy**: Superior on scientific and patent documents
- **Best for**: Academic papers with complex equations and figures
- **Special**: Outperforms all rule-based tools on scientific content
- **License**: Open source

### LlamaParse
- **Speed**: API-dependent
- **Accuracy**: Best-in-class for complex tables and figures
- **Best for**: Documents with intricate table structures
- **Special**: Managed API by LlamaIndex, integrates with ingestion pipeline
- **License**: Proprietary API

## Selection Guide

| Document Type | Recommended Tool | Reason |
|---------------|-----------------|--------|
| High-volume digital PDFs | PyMuPDF4LLM | Speed + accuracy |
| Enterprise / air-gapped | Docling | Self-hosted, strong layout |
| Mixed formats (not just PDF) | Unstructured | 30+ format support |
| Scientific papers | Nougat | Learning-based superiority |
| Complex tables/figures | LlamaParse | Table-optimized API |
| Scanned / OCR-heavy | Docling + Surya | Best OCR integration |

## Sources
- [[sources/pdf-parser-comparison-2026]] — comprehensive benchmark data
- [[sources/unstructured-io-document-etl]] — Unstructured's partitioning strategies
- [[sources/llamaindex-ingestion-pipeline]] — LlamaParse and integration patterns

## Related Concepts
- [[concepts/document-processing-pipeline]] — PDF parsing is the critical stage 1
- [[concepts/ocr-document-extraction]] — OCR as a component of PDF parsing
- [[concepts/vision-language-models]] — end-to-end alternative to pipeline parsing
