---
title: "Lessons from Running an LLM Document Processing Pipeline in Production"
source: "https://medium.com/alan/lessons-from-running-an-llm-document-processing-pipeline-in-production-33d87f99cdb1"
author: "Othman Moumni Abdou"
date_published: 2026-03-01
date_ingested: 2026-04-05
tags: [document-processing, llm-pipeline, production, ocr, extraction]
type: article
status: raw
discovered_via: search
---

# Lessons from Running an LLM Document Processing Pipeline in Production

From the Alan Product and Technical Blog. Production pipeline at Alan (health insurance company) processing healthcare documents with LLMs.

## Pipeline Architecture

Multi-stage approach:
1. **OCR Transcription** — Markdown conversion from scanned/digital documents
2. **Document Classification** — Category/sub-category prediction
3. **Extraction** — Structured data generation via LLM
4. **Validation** — Pydantic schema verification
5. **Human Review** — Fallback for failures

## Multimodal Input Strategy

Team evolved from text-only to combining OCR transcription with document images. "The transcription provides reliable text content... The image provides visual layout context." This hybrid approach outperforms either input alone.

## Few-Shot Learning with HNSW

For high-volume categories, they implement approximate nearest neighbor search using Hierarchical Navigable Small World indexes to balance accuracy and speed across millions of examples.

## Validation Framework

Output validated against Pydantic schemas. Failures trigger human review with structured error explanations, preserving best-effort extractions as starting points.

## Evaluation & Monitoring

Before deployment, changes undergo backtesting against reference documents with verified extractions. Measures:
- Classification accuracy (category correctness)
- Extraction field-by-field comparisons with weighted criticality levels

## Critical Lessons

1. **Separate parsing from enrichment** — Mixing external knowledge in few-shot examples causes LLM hallucination
2. **Curated datasets bootstrap new categories** — Small hand-picked reference sets achieve surprising effectiveness
3. **Measure before shipping** — Every modification requires backtest validation

## Remaining Challenges

- **Document Quality**: Handwriting and poor scans degrade OCR reliability
- **Few-Shot Contamination**: Human-enriched examples mislead models into inferring unlisted information
- **Classification Bottleneck**: Misclassification cascades to extraction failure; edge cases like concatenated PDFs remain problematic

Human review remains essential for high-stakes healthcare documents despite achieving 70% automation.
