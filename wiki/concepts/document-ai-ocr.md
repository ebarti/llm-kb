---
title: "Document AI and OCR"
type: concept
sources: ["[[sources/ocr-technology-evolution-2026]]", "[[sources/claude-vision-capabilities]]", "[[sources/bentoml-vision-language-models-2026]]"]
related: ["[[concepts/vision-language-models]]", "[[concepts/image-understanding]]", "[[concepts/multimodal-ai]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Evolution from character-level OCR (~85% accuracy) to AI-powered document intelligence (99%+) via VLMs; LLMs now rival or exceed specialized OCR engines on complex layouts."
---

## Overview

Document AI (also called Intelligent Document Processing or IDP) encompasses the technologies for automatically extracting, understanding, and processing information from documents. It has evolved dramatically from traditional Optical Character Recognition (OCR) — which simply recognized individual characters — to modern document intelligence systems that understand layout, structure, semantics, and context.

The transition can be summarized as: from "what characters are on the page?" to "what does this document mean?"

## Three Paradigms of Modern OCR

Per [[sources/ocr-technology-evolution-2026]], the field has settled into three paradigms:

### 1. Traditional OCR Engines
- **Examples**: Tesseract, EasyOCR, PaddleOCR
- **Approach**: Pattern matching on character shapes, trained on known fonts
- **Accuracy**: ~85% on complex layouts; 95%+ on clean printed text
- **Strengths**: Fast, lightweight (PaddleOCR PP-OCR at 3.5 MB), deployable on edge devices
- **Weaknesses**: Struggle with handwriting, complex layouts, degraded images

### 2. Layout-Aware Document Models
- **Examples**: Microsoft LayoutLM, DocFormer, PaddleOCR-VL
- **Approach**: Combine text recognition with spatial layout understanding
- **Innovation**: Text + layout embeddings enable understanding form fields, tables, document structure
- **Capability**: Understand that text at position (x,y) is a field label while text at position (x',y') is its value

### 3. Vision-Language Model OCR
- **Examples**: GPT-4V, Claude Vision, Gemini, DeepSeek-OCR
- **Approach**: End-to-end visual understanding — the model "reads" the document as an image and reasons about content
- **Performance**: LLMs "significantly outperformed state-of-the-art OCR models" on difficult handwriting; as low as 1% character error rate for post-correction
- **Tradeoff**: Higher cost and latency; risk of hallucination (fabricating text not present in document)

## Performance Comparison

| Solution | Accuracy | Strengths |
|----------|----------|-----------|
| Tesseract | ~85% (complex) | Free, mature |
| EasyOCR | Competitive | 80+ languages, easy API |
| PaddleOCR-VL-1.5 | 95% (benchmark) | Open-source, fast |
| Google Vision | ~98% | 100+ languages |
| AWS Textract | ~99.3% | Table/form extraction |
| Azure | ~99.8% (typed) | 160+ languages |
| Claude 3 | Highest median (industrial) | Context-aware, flexible |
| DeepSeek-OCR | 97% at 20x compression | Speed + compression |

## Document AI for Knowledge Bases

For an [[concepts/llm-knowledge-base]], Document AI is critical for:

1. **PDF ingestion**: Converting scanned or image-based PDFs to text during the ingest pipeline
2. **Screenshot processing**: Extracting text from captured web pages, presentations, and applications
3. **Table extraction**: Recovering structured data from tables in images
4. **Form processing**: Understanding field-value relationships in forms and documents
5. **Handwriting recognition**: Digitizing handwritten notes and annotations

### Practical Approach

The most pragmatic approach for a markdown-based KB:
- Use VLM-based OCR (Claude Vision, GPT-4V) for complex or high-value documents where accuracy matters
- Use lightweight OCR (PaddleOCR, Tesseract) for bulk processing where speed matters
- Store both the OCR output and original image for verification
- Use VLMs for post-correction when traditional OCR accuracy is insufficient

## Key Concepts

- **Agentic Document Processing**: AI systems that autonomously decide how to handle extracted data — validate, categorize, enrich, and route without human intervention
- **Document Foundation Models**: Specialized models (LayoutLM series) that combine layout understanding with language semantics
- **Hybrid Approaches**: Using specialized OCR for high-volume commodity tasks and LLMs for complex understanding requiring contextual reasoning

## Sources

- [[sources/ocr-technology-evolution-2026]] — comprehensive evolution and comparison
- [[sources/claude-vision-capabilities]] — Claude's specific OCR capabilities
- [[sources/bentoml-vision-language-models-2026]] — DeepSeek-OCR profiled

## Related Concepts

- [[concepts/vision-language-models]] — the models driving the OCR revolution
- [[concepts/image-understanding]] — Document AI as a specialized form of image understanding
- [[concepts/llm-knowledge-base]] — primary application context
- [[concepts/multimodal-ai]] — broader field
