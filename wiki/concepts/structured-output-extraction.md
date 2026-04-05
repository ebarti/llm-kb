---
title: "Structured Output Extraction"
type: concept
sources: ["[[sources/willison-llm-schemas-structured-extraction]]", "[[sources/instructor-library-structured-extraction]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/schema-guided-extraction]]", "[[entities/instructor]]", "[[entities/pydantic]]"]
last_compiled: 2026-04-05
summary: "Forcing LLM outputs into schema-conformant JSON/objects via constrained decoding (FSM) or validation-retry loops — the production backbone of all extraction pipelines."
---

## Overview

Structured output extraction is the technique of forcing LLM responses to conform to a predefined schema — typically JSON, Pydantic models, or database records. Rather than parsing free-text responses, the extraction pipeline defines exactly what fields, types, and constraints the output must satisfy.

As Simon Willison states in [[sources/willison-llm-schemas-structured-extraction]]: "The single most commercially valuable application of LLMs is turning unstructured content into structured data."

## Two Implementation Approaches

### 1. Constrained Decoding (FSM-Based)

As of early 2026, all major providers support native structured output via constrained decoding:

- The JSON Schema is compiled into a finite state machine (FSM)
- At each token generation step, only tokens keeping output on a valid FSM path are allowed
- Invalid tokens get their logits set to negative infinity
- This provides a **mathematical guarantee** of valid output, not a statistical one

Supported by: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, xAI (Grok), vLLM (local).

### 2. Validation-Retry (Instructor Pattern)

[[entities/instructor]] uses Pydantic validation as a feedback loop:

1. Define a Pydantic model for desired output
2. LLM generates a response
3. Instructor validates against the Pydantic model
4. If validation fails, re-prompts the LLM with failure context
5. Repeat until valid or max retries exceeded

This approach works with any LLM, even those without native structured output, and can enforce complex business logic validators beyond what JSON Schema supports.

### 3. Prompted Output (Fallback)

Include the schema in the prompt and instruct the model to output JSON. Least reliable but works universally. Often combined with post-hoc JSON parsing and error handling.

## Key Libraries and Tools

| Library | Approach | Language |
|---------|----------|----------|
| [[entities/instructor]] | Pydantic validation + retry | Python, TS, Go, Ruby, Elixir, Rust |
| Pydantic AI | Tool/Native/Prompted output | Python |
| LangChain | `.with_structured_output()` | Python, JS |
| Simon Willison's LLM | Schema CLI + Datasette integration | Python CLI |
| vLLM | FSM-based constrained decoding | Python (serving) |

## Schema Definition Patterns

```python
from pydantic import BaseModel
from typing import List, Optional

class Entity(BaseModel):
    name: str
    entity_type: str  # person, org, tool, paper
    description: Optional[str] = None

class Relationship(BaseModel):
    subject: str
    predicate: str
    object: str

class ExtractionResult(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]
    key_claims: List[str]
```

## Relevance to Wiki Compilation

In the [[concepts/wiki-compilation]] pipeline, structured output extraction is used for:

- **Frontmatter generation**: Extracting title, author, date, tags from raw sources
- **Entity extraction**: Returning typed entity objects for wiki/entities/ pages
- **Relationship extraction**: Returning subject-predicate-object triples for wikilinks
- **Claim extraction**: Returning atomic statements for concept articles
- **Classification**: Categorizing sources by type (article, paper, repo, tweet, video)

The validation-retry pattern is essential for production reliability — a single malformed extraction can break the compilation pipeline.

## Sources

- [[sources/willison-llm-schemas-structured-extraction]] — FSM-guaranteed extraction, datasette integration
- [[sources/instructor-library-structured-extraction]] — Pydantic-based validation and retry

## Related Concepts

- [[concepts/information-extraction]] — structured output is the delivery mechanism for all IE
- [[concepts/schema-guided-extraction]] — defines what schema to extract against
- [[concepts/named-entity-recognition]] — NER output as structured entity objects
- [[concepts/relation-extraction]] — relationship triples as structured output
