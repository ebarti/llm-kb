---
title: "Docling"
type: entity
entity_type: tool
sources: ["[[sources/pdf-parser-comparison-2026]]"]
related: ["[[concepts/pdf-parsing-tools]]", "[[concepts/document-processing-pipeline]]", "[[concepts/ocr-document-extraction]]", "[[entities/surya-ocr]]"]
last_compiled: 2026-04-05
summary: "IBM open-source document parsing toolkit (MIT): DocLayNet layout analysis + TableFormer table recognition, outputs AI-ready JSON/Markdown, 9/10 performance, ideal for enterprise RAG in air-gapped environments."
---

## Overview

Docling is an open-source document parsing toolkit from IBM that converts diverse document formats into structured, AI-ready JSON and Markdown. It uses specialized AI models — DocLayNet for layout analysis and TableFormer for table structure recognition — to achieve 9/10 performance scores in benchmarks.

## Key Features

- **AI-powered layout analysis**: DocLayNet model for document structure detection
- **Table recognition**: TableFormer for complex table structure extraction
- **OCR support**: Integrates with [[entities/surya-ocr]] for scanned document processing
- **Multi-format**: Handles PDFs, images, office documents
- **Air-gapped deployment**: Self-hosted, no external API dependencies
- **License**: MIT (permissive)

## Integration with Surya OCR

By combining Docling's document structure understanding with Surya's multilingual OCR, users get accurate reconstruction of complex elements: nested tables, hierarchical headers, mathematical formulas, and correct reading order — particularly valuable for RAG applications.

## Mentioned In
- [[sources/pdf-parser-comparison-2026]] — rated 9/10 performance, recommended for enterprise RAG
