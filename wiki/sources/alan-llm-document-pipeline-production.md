---
title: "Source: Lessons from Running an LLM Document Processing Pipeline in Production"
type: source-summary
source: "[[raw/alan-llm-document-pipeline-production]]"
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/ocr-document-extraction]]", "[[concepts/data-quality-bottleneck]]", "[[entities/pydantic]]"]
last_compiled: 2026-04-05
summary: "Production lessons from Alan's healthcare document pipeline: OCR+image multimodal input, Pydantic validation, HNSW few-shot retrieval, and 70% automation with human-in-the-loop fallback."
---

## Key Points

- Production LLM document processing at Alan (health insurance) combines OCR transcription with document images for best accuracy
- Pipeline follows five stages: OCR → Classification → Extraction → Validation → Human Review
- Pydantic schema validation catches extraction errors before they propagate
- HNSW-based few-shot example retrieval balances accuracy and speed at scale
- Achieved 70% automation rate; human review remains essential for high-stakes healthcare documents

## Detailed Summary

Alan runs one of the more transparent production [[concepts/document-processing-pipeline]] systems documented publicly. Their architecture illustrates the typical multi-stage approach: first converting documents via [[concepts/ocr-document-extraction]], then classifying them by type, extracting structured fields with an LLM, validating outputs against Pydantic schemas, and routing failures to human reviewers.

The most valuable insight is their evolution from text-only to multimodal input. Combining OCR markdown transcription with the original document image outperforms either alone — the text provides reliable content while the image supplies visual layout context. This aligns with the broader trend toward [[concepts/vision-language-models]] for document understanding.

Their few-shot learning system uses [[entities/hnsw]] approximate nearest neighbor search to find the most relevant examples from a large library, feeding them as context to the LLM. This is a practical application of [[concepts/rag-vs-index-based-retrieval]] at production scale.

Three critical lessons emerged:
1. **Separate parsing from enrichment** — mixing external knowledge in examples causes hallucination (echoing [[concepts/hallucination-contamination]])
2. **Curated datasets bootstrap new categories** — small hand-picked reference sets are surprisingly effective
3. **Measure before shipping** — every change requires backtesting against verified extractions

The remaining challenges — handwriting degradation, few-shot contamination, classification cascading failures — highlight that [[concepts/data-quality-bottleneck]] remains the dominant constraint in production document pipelines.

## Notable Quotes

> "The transcription provides reliable text content... The image provides visual layout context."

## Related Concepts
- [[concepts/document-processing-pipeline]] — this is a canonical production example
- [[concepts/ocr-document-extraction]] — OCR as the critical first pipeline stage
- [[concepts/data-quality-bottleneck]] — document quality degrades the entire chain
- [[concepts/hallucination-contamination]] — few-shot contamination as a specific vector
