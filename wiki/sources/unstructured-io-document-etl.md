---
title: "Source: Unstructured.io — Open-Source Document ETL for AI"
type: source-summary
source: "[[raw/unstructured-io-document-etl]]"
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/document-chunking-strategies]]", "[[entities/unstructured-io]]", "[[entities/langchain]]"]
last_compiled: 2026-04-05
summary: "Unstructured.io open-source library: partition() auto-detects 30+ formats, outputs typed semantic elements, offers Fast/HiRes/Auto/OCR strategies, and enterprise platform processes 15M pages/hour."
---

## Key Points

- Open-source Python library (Apache 2.0, 14.4k GitHub stars) for document-to-structured-data conversion
- `partition()` function auto-detects file type and routes to appropriate handler
- Outputs typed Element objects: Title, NarrativeText, Table, Image with metadata
- Four partitioning strategies: Fast (rule-based), HiRes (AI layout analysis), Auto, OCR-only
- Supports 30+ file formats: PDF, DOCX, PPTX, XLSX, HTML, images, email, XML, JSON
- Enterprise platform: 15 million pages/hour, 71 pre-built connectors

## Detailed Summary

[[entities/unstructured-io]] is the most widely-used open-source library specifically designed for the ingestion stage of [[concepts/document-processing-pipeline]] systems. Its core insight is that document preprocessing should produce semantic elements (titles, paragraphs, tables) rather than raw text blobs.

The partitioning strategy system is particularly well-designed: Fast mode uses rules for quick processing, HiRes mode uses AI-powered layout analysis for complex documents, Auto mode selects the best strategy per document, and OCR-only mode handles scanned content. This tiered approach lets pipeline operators balance speed against accuracy.

For [[concepts/document-chunking-strategies]], Unstructured's approach is distinctive: it chunks based on document structure (semantic elements) rather than purely on text features. This produces more coherent chunks because the library understands the difference between a title, a paragraph, and a table row.

The comparison with [[entities/langchain]] is instructive: Unstructured specializes in document ETL (the "E" and "T"), while LangChain handles orchestration (the "L" and beyond). Production systems typically use both — Unstructured for ingestion, LangChain or [[entities/llamaindex]] for RAG orchestration.

## Related Concepts
- [[concepts/document-processing-pipeline]] — Unstructured is the canonical ingestion library
- [[concepts/document-chunking-strategies]] — structure-aware chunking approach
- [[concepts/ocr-document-extraction]] — built-in OCR support via Tesseract
