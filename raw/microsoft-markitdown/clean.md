---
title: "Microsoft MarkItDown: Universal Document-to-Markdown Converter"
source: "https://github.com/microsoft/markitdown"
author: "Microsoft"
date_published: 2024-12-01
date_ingested: 2026-04-05
tags: [markdown, conversion, llm, microsoft, document-processing, open-source]
type: article
status: raw
discovered_via: search
---

# Microsoft MarkItDown

## Purpose

MarkItDown is "a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines." It prioritizes preserving document structure — headings, lists, tables, links — in a format optimized for language models rather than human presentation.

## Supported File Formats

- **Documents**: PDF, PowerPoint, Word, Excel
- **Media**: Images (with EXIF/OCR), Audio (with transcription)
- **Web**: HTML, YouTube URLs
- **Data**: CSV, JSON, XML, ZIP archives, EPubs

## Why Markdown?

LLMs like GPT-4o natively understand Markdown due to extensive training on it. The format offers "minimal markup or formatting" while remaining "highly token-efficient," making it ideal for AI consumption.

## Architecture

Three-tier design:
1. User interfaces (CLI, Python API, MCP server)
2. Core orchestration layer
3. Extensible converter ecosystem with plugin support

Stream-based processing (binary file-like objects), no temporary file creation in v0.1.0+.

## Usage

**Command-line**: `markitdown document.pdf -o output.md`
**Python API**:
```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("test.xlsx")
print(result.text_content)
```

**With LLM vision** (image descriptions):
```python
from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")
result = md.convert("image.jpg")
```

## Advanced Features

- Azure Document Intelligence for enterprise-grade processing
- markitdown-ocr plugin for embedded image text extraction
- Docker support for containerized deployment
- MCP server for network-accessible conversion API

## Role in LLM Pipelines

Functions as a preprocessing layer, converting diverse document types into Markdown for RAG systems, document analysis workflows, and AI-powered applications requiring structured text extraction.
