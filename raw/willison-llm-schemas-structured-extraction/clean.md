---
title: "Structured Data Extraction from Unstructured Content Using LLM Schemas"
source: "https://simonwillison.net/2025/Feb/28/llm-schemas/"
author: "Simon Willison"
date_published: 2025-02-28
date_ingested: 2026-04-05
tags: [information-extraction, structured-output, llm-tools, json-schema, pydantic]
type: article
status: raw
discovered_via: search
---

# Structured Data Extraction from Unstructured Content Using LLM Schemas

Simon Willison announced LLM 0.23's signature feature: schema support for extracting structured data from unstructured content. This capability enables users to specify desired output formats and receive JSON-compliant results from LLM queries.

## Core Functionality

The feature allows straightforward commands like:

```
llm --schema 'name,age int,short_bio' 'invent a cool dog'
```

This returns validated JSON with fields matching the specified schema. Users can provide schemas through multiple methods: direct JSON schema syntax, concise shorthand notation (comma-separated fields with optional types), file references, previously logged schema IDs, and saved templates.

## Technical Implementation

Supported providers: OpenAI (Structured Outputs), Anthropic (tool use mechanism), Gemini (structured output API), Mistral (custom structured outputs).

The implementation uses JSON schema specifications to guide model outputs. Some providers employ techniques like Jsonformer to compile schemas into runtime constraints, while others rely on model capability to follow specifications accurately.

## Key Insight

"The single most commercially valuable application of LLMs is turning unstructured content into structured data." This approach excels at converting articles, PDFs, and screenshots into queryable formats.

## Workflow Integration

LLM automatically logs all prompts using a SQLite database. The `llm logs` command retrieves responses by schema. The `--data` flag outputs only schema-extracted JSON, enabling piping to sqlite-utils for database creation and SQL analysis via Datasette.

## Python Library Support

The library accepts Pydantic BaseModel classes or JSON schemas:

```python
model.prompt("Describe a dog", schema=Dog)
```

## Practical Applications

The workflow supports extracting structured data from multiple sources and aggregating results into searchable databases — particularly valuable for data journalism and research projects. The datasette-extract plugin provides a web UI for structured data extraction that writes the resulting records directly to a SQLite database table.

## Provider-Level Structured Output Support

As of early 2026, OpenAI, Anthropic, Google Gemini, Mistral, Cohere, and xAI (Grok) all support native structured output. The JSON Schema is compiled into a finite state machine (FSM). At each token generation step, only tokens that keep the output on a valid path through the FSM are allowed — invalid tokens get their logits set to negative infinity. This gives a mathematical guarantee of valid output, not a statistical one.
