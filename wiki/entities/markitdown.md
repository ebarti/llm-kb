---
title: "MarkItDown (Microsoft)"
type: entity
entity_type: tool
sources: ["[[sources/microsoft-markitdown]]"]
related: ["[[concepts/markdown-ecosystem]]", "[[concepts/markdown-for-ai-agents]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Microsoft's open-source Python tool for converting PDFs, Office docs, images, audio, and web content to markdown — designed for LLM ingestion pipelines."
---

## Overview

MarkItDown is a lightweight Python utility by Microsoft for converting various file formats to markdown. It is designed specifically for LLM and text analysis pipelines, prioritizing structure preservation (headings, lists, tables, links) over visual fidelity.

## Supported Formats

PDF, DOCX, PPTX, XLSX, HTML, images (EXIF/OCR), audio (transcription), CSV, JSON, XML, ZIP archives, EPubs, YouTube URLs.

## Architecture

- Three-tier: CLI / Python API / MCP server
- Stream-based processing (no temp files)
- Plugin ecosystem for extensibility
- Optional LLM vision integration (GPT-4o for image descriptions)
- Azure Document Intelligence for enterprise processing

## Installation

```bash
pip install 'markitdown[all]'  # or selective: 'markitdown[pdf, docx, pptx]'
```

## Significance

MarkItDown is a strong signal from Microsoft that markdown has become the de facto interchange format for AI pipelines. The tool's entire purpose — converting the world's documents into markdown for LLM consumption — validates the [[concepts/markdown-as-universal-interface]] thesis from the conversion/ingestion angle.

## Mentioned In

- [[sources/microsoft-markitdown]] — full feature and architecture overview
- [[concepts/markdown-ecosystem]] — MarkItDown as conversion infrastructure
- [[concepts/markdown-for-ai-agents]] — preprocessing for LLM consumption
