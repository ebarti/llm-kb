---
title: "PyMuPDF"
type: entity
entity_type: tool
sources: ["[[sources/pdf-parser-comparison-2026]]"]
related: ["[[concepts/pdf-parsing-tools]]", "[[concepts/document-processing-pipeline]]"]
last_compiled: 2026-04-05
summary: "Fastest Python PDF parser (0.12s markdown output): PyMuPDF4LLM variant optimized for LLM ingestion with layout analysis and semantic understanding; most consistent recall among rule-based tools; AGPL/commercial license."
---

## Overview

PyMuPDF (also known as `fitz`) is a high-performance Python library for PDF processing. Its LLM-optimized variant, PyMuPDF4LLM, is the fastest PDF-to-markdown converter available, achieving markdown output in 0.12 seconds — making it the top choice for high-volume digital PDF processing in [[concepts/document-processing-pipeline]] systems.

## Key Features

- **Speed**: Fastest among all PDF parsers tested (0.12s for markdown)
- **Consistency**: Most consistent recall across document categories among rule-based tools
- **PyMuPDF4LLM**: Specialized for LLM applications with layout analysis and semantic understanding
- **OCR support**: Integrated OCR for scanned documents
- **Table detection**: Built-in table extraction capabilities

## Limitations

- Struggles with complex scanned documents compared to AI-powered tools
- AGPL license may be restrictive for commercial use (commercial license available)
- Rule-based approach means less adaptability to novel document formats

## Mentioned In
- [[sources/pdf-parser-comparison-2026]] — benchmarked as fastest tool with consistent accuracy
