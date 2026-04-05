---
title: "OCR and Document Extraction"
type: concept
sources: ["[[sources/alan-llm-document-pipeline-production]]", "[[sources/pdf-parser-comparison-2026]]", "[[sources/huggingface-vlms-2025]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/pdf-parsing-tools]]", "[[concepts/vision-language-models]]", "[[entities/surya-ocr]]", "[[entities/doctr]]", "[[entities/tesseract]]"]
last_compiled: 2026-04-05
summary: "Modern OCR has evolved from character recognition to document understanding: traditional engines (Tesseract, PaddleOCR) deliver 99%+ on printed text, while LLM-powered models (RolmOCR, Qwen2.5-VL) handle complex layouts, tables, and handwriting."
---

## Overview

Optical Character Recognition (OCR) and document extraction convert visual document content — scanned pages, photographs, PDF renders — into machine-readable text and structure. In the context of [[concepts/document-processing-pipeline]] systems, OCR is the critical first transformation that determines the quality ceiling for all downstream processing.

Modern OCR in 2025-2026 has bifurcated into two paradigms: traditional OCR engines optimized for speed and accuracy on clean text, and LLM-powered vision models that understand document structure, context, and semantics.

## Traditional OCR Engines

### Tesseract
The most established open-source OCR engine. Known for stability and broad language support. Best for clean, structured text. Used as the default OCR backend in [[entities/unstructured-io]] and many pipeline frameworks.

### PaddleOCR
Strong performance with complex layouts and multilingual documents. Developed by Baidu. Good balance of speed and accuracy for production use.

### EasyOCR
Accessible Python library supporting 80+ languages. Good for quick prototyping but less accurate than PaddleOCR on complex layouts.

## Modern Deep Learning OCR

### Surya OCR
High-performance multilingual OCR toolkit by Vik Paruchuri. Key innovations:
- YOLOv5-based text detection across 90+ languages
- Transformer-based character recognition
- Graph neural network layout analysis for multi-column documents
- Dynamic segmentation for complex table structures
- 15-20% improvement over commercial alternatives on complicated tables

Integrates with [[entities/docling]] for enhanced document reconstruction.

### docTR (Document Text Recognition)
Deep-learning OCR library from Mindee. Two-stage approach: text detection (localizing words) then text recognition. Built on TensorFlow and PyTorch. Handles scanned documents, multi-column layouts, and mixed formatting.

## LLM-Powered Document Understanding

### RolmOCR (7B)
Specialized vision model optimized for OCR tasks. Identified by Hugging Face as the leading open-source OCR-specific VLM.

### Qwen2.5-VL
General-purpose VLM with strong document understanding. Reads text in low-light, blurred, or tilted images. Accurately parses complex documents, forms, and layouts. Available from 3B to 72B parameter sizes.

### GLM-4.5V
Can read text in challenging conditions and parse complex documents including forms and multi-column layouts.

## The Hybrid Approach (2026 Best Practice)

The emerging best practice combines OCR transcription with VLM visual understanding:

1. Run OCR to produce markdown transcription (reliable text extraction)
2. Feed BOTH the transcription AND the original document image to a VLM
3. The VLM uses the text for content accuracy and the image for layout context

Alan's production pipeline validates this: "The transcription provides reliable text content... The image provides visual layout context." This hybrid outperforms either approach alone.

## Accuracy Benchmarks (2026)

- Printed text: 99%+ accuracy with modern OCR
- Handwritten content: ~95% accuracy (improving rapidly)
- Complex tables: Surya achieves 15-20% improvement over commercial alternatives
- Scientific documents: Nougat (Meta) outperforms all rule-based tools

## Sources
- [[sources/alan-llm-document-pipeline-production]] — production hybrid OCR + VLM approach
- [[sources/pdf-parser-comparison-2026]] — OCR as part of PDF parsing pipeline
- [[sources/huggingface-vlms-2025]] — VLM-based document understanding models

## Related Concepts
- [[concepts/document-processing-pipeline]] — OCR is the foundational extraction stage
- [[concepts/pdf-parsing-tools]] — OCR integrated into PDF parsing workflows
- [[concepts/vision-language-models]] — VLMs as next-generation OCR
- [[concepts/data-quality-bottleneck]] — OCR quality sets the ceiling for downstream processing
