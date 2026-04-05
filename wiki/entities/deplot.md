---
title: "DePlot"
type: entity
entity_type: tool
sources: ["[[sources/nvidia-multimodal-rag-intro]]"]
related: ["[[concepts/multimodal-rag]]", "[[concepts/image-understanding]]", "[[concepts/document-ai-ocr]]"]
last_compiled: 2026-04-05
summary: "Google's specialized tool for converting charts and plots into structured text (linearized tables), used in multimodal RAG preprocessing to make visual data accessible to text-based LLMs."
---

## Overview

DePlot is a specialized AI tool developed by Google that converts charts and plots into structured text representations. It reads visual data from bar charts, line graphs, scatter plots, and other common chart types, outputting linearized tabular text that can be processed by standard text-based LLMs.

## Role in Multimodal RAG

Per [[sources/nvidia-multimodal-rag-intro]], DePlot serves a critical role in [[concepts/multimodal-rag]] preprocessing pipelines:

1. Images are first classified as charts/graphs vs. general images
2. Chart-type images are processed by DePlot to extract the underlying data
3. The linearized table output is stored as metadata alongside the image
4. During inference, this structured data is included in LLM context for accurate responses

## Significance

DePlot represents the "specialized tool" approach to [[concepts/image-understanding]] — rather than relying on a general-purpose VLM to interpret charts, it provides a purpose-built solution optimized for accuracy on this specific task. This is particularly important for charts where precise numerical values matter (financial data, scientific measurements).

## Mentioned In

- [[sources/nvidia-multimodal-rag-intro]] — used in multimodal RAG chart processing pipeline
