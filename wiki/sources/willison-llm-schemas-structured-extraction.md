---
title: "Source: Structured Data Extraction from Unstructured Content Using LLM Schemas"
type: source-summary
source: "[[raw/willison-llm-schemas-structured-extraction]]"
related: ["[[concepts/structured-output-extraction]]", "[[concepts/information-extraction]]", "[[entities/instructor]]", "[[entities/simon-willison]]"]
last_compiled: 2026-04-05
summary: "Simon Willison's LLM 0.23 introduces schema-based structured extraction — the 'single most commercially valuable LLM application' — with FSM-guaranteed JSON output across all major providers."
reading_time: "2 min"
---

## Key Points

- LLM 0.23 adds schema support for extracting structured data from unstructured content via JSON Schema
- All major providers (OpenAI, Anthropic, Gemini, Mistral, Cohere, xAI) now support native structured output as of early 2026
- JSON Schema is compiled into a finite state machine (FSM) providing mathematical guarantees of valid output — not statistical
- The datasette-extract plugin enables web-based extraction directly into SQLite databases
- Python API accepts Pydantic BaseModel classes for type-safe extraction

## Detailed Summary

Simon Willison describes structured data extraction as "the single most commercially valuable application of LLMs." His LLM CLI tool (version 0.23) allows users to specify output schemas via shorthand notation, JSON Schema files, or Pydantic models, and get back validated JSON from any supported provider.

The technical implementation relies on constrained decoding: the JSON Schema is compiled into a finite state machine (FSM), and at each token generation step, only tokens that keep the output on a valid path through the FSM are allowed. Invalid tokens get their logits set to negative infinity. This provides a mathematical guarantee of schema-conformant output.

The practical workflow chains extraction into SQLite via `sqlite-utils`, enabling SQL analysis through Datasette. This is particularly relevant to [[concepts/wiki-compilation]] pipelines where raw unstructured sources need to be converted into structured wiki entries.

## Notable Quotes

> "The single most commercially valuable application of LLMs is turning unstructured content into structured data."

## Related Concepts

- [[concepts/structured-output-extraction]] — core technique demonstrated here
- [[concepts/information-extraction]] — parent discipline
- [[concepts/llm-knowledge-base]] — extraction is the first step in the KB pipeline
- [[entities/instructor]] — alternative Python library for the same task
