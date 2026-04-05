---
title: "LlamaParse"
type: entity
entity_type: tool
sources: ["[[sources/llamaindex-ingestion-pipeline]]", "[[sources/pdf-parser-comparison-2026]]"]
related: ["[[concepts/pdf-parsing-tools]]", "[[concepts/document-processing-pipeline]]", "[[entities/llamaindex]]"]
last_compiled: 2026-04-05
summary: "LlamaIndex's managed PDF parsing API: best-in-class for complex tables and figures, integrates natively with LlamaIndex ingestion pipeline, proprietary cloud service."
---

## Overview

LlamaParse is [[entities/llamaindex]]'s official managed API for PDF parsing, designed to handle the most challenging PDF documents — those with complex tables, nested figures, and mixed layouts that rule-based parsers struggle with.

## Key Features

- **Complex table extraction**: Best-in-class for documents with intricate table structures
- **Figure handling**: Strong extraction of charts, diagrams, and embedded images
- **Managed API**: Cloud-hosted service, no local model deployment needed
- **Native integration**: Direct integration with LlamaIndex's ingestion pipeline
- **Format output**: Produces structured markdown suitable for downstream LLM processing

## Trade-offs

- **Proprietary**: Requires API key and cloud access (not available air-gapped)
- **Cost**: API-based pricing per page processed
- **Speed**: Dependent on API latency and queue depth
- **Dependency**: Ties pipeline to LlamaIndex ecosystem

## Mentioned In
- [[sources/llamaindex-ingestion-pipeline]] — primary PDF parsing tool in LlamaIndex
- [[sources/pdf-parser-comparison-2026]] — best-in-class for tables and figures
