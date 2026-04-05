---
title: "Surya OCR"
type: entity
entity_type: tool
sources: ["[[sources/pdf-parser-comparison-2026]]"]
related: ["[[concepts/ocr-document-extraction]]", "[[concepts/document-processing-pipeline]]", "[[entities/docling]]"]
last_compiled: 2026-04-05
summary: "High-performance multilingual OCR toolkit by Vik Paruchuri: YOLOv5 text detection, Transformer recognition across 90+ languages, graph neural network layout analysis, 15-20% improvement over commercial tools on complex tables."
---

## Overview

Surya is an open-source, high-performance OCR toolkit designed for complex document processing across 90+ languages. Developed by Vik Paruchuri, it combines modern deep learning architectures for text detection, recognition, and layout analysis.

## Technical Architecture

- **Text Detection**: Improved YOLOv5 detection algorithm for text localization
- **Character Recognition**: Transformer-based architecture supporting 90+ languages
- **Layout Analysis**: Graph neural networks for document formatting structure reconstruction (multi-column, headers, footnotes)
- **Table Processing**: Dynamic segmentation lines and context-aware techniques for complex table structures

## Performance

- 15-20% improvement over mainstream commercial alternatives on complicated table scenarios
- Strong multi-column layout reconstruction
- Accurate nested table and hierarchical header detection
- Mathematical formula recognition support

## Integration

Integrates with [[entities/docling]] framework for enhanced document reconstruction, combining Surya's OCR accuracy with Docling's structural understanding. Particularly valuable for RAG and LLM training data preparation.

## Mentioned In
- [[sources/pdf-parser-comparison-2026]] — highlighted for table recognition superiority
