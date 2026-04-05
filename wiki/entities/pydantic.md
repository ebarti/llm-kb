---
title: "Pydantic"
type: entity
entity_type: tool
sources: ["[[sources/instructor-library-structured-extraction]]", "[[sources/willison-llm-schemas-structured-extraction]]"]
related: ["[[concepts/structured-output-extraction]]", "[[entities/instructor]]"]
last_compiled: 2026-04-05
summary: "Python data validation library using type hints — the de facto standard for defining LLM extraction schemas, powering Instructor, Pydantic AI, LangChain structured output, and Simon Willison's LLM."
---

## Overview

Pydantic is a Python library for data validation using Python type hints. In the LLM extraction ecosystem, it has become the standard way to define output schemas. Nearly every [[concepts/structured-output-extraction]] library uses Pydantic models to specify what data to extract from LLM responses.

## Role in LLM Extraction

- **Schema definition**: Pydantic BaseModel classes define fields, types, and constraints
- **Validation**: Automatically validates LLM output against the schema
- **JSON Schema generation**: Pydantic models can be converted to JSON Schema for provider APIs
- **Error messages**: Validation errors provide structured feedback for retry loops

## Key Integrations

- [[entities/instructor]] — Pydantic as the core schema mechanism
- **Pydantic AI** — Pydantic's own LLM framework with Tool/Native/Prompted output modes
- **LangChain** — `.with_structured_output()` accepts Pydantic models
- **Simon Willison's LLM** — Python API accepts Pydantic BaseModel classes

## Mentioned In

- [[sources/instructor-library-structured-extraction]] — Pydantic as validation backbone
- [[sources/willison-llm-schemas-structured-extraction]] — Pydantic model support in LLM CLI
