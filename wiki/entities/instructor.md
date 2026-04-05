---
title: "Instructor"
type: entity
entity_type: tool
sources: ["[[sources/instructor-library-structured-extraction]]"]
related: ["[[concepts/structured-output-extraction]]", "[[concepts/information-extraction]]", "[[entities/pydantic]]"]
last_compiled: 2026-04-05
summary: "The most popular Python library for structured LLM extraction (3M+ monthly downloads) — uses Pydantic models with automatic validation and retry across 15+ providers."
---

## Overview

Instructor is an open-source Python library (MIT license) created by Jason Liu / 567 Labs for extracting structured, validated data from Large Language Models. It is the most popular library in this category with over 3 million monthly downloads, 11,000+ GitHub stars, and 100+ contributors.

## Key Features

- **Pydantic-based schemas**: Define extraction targets as Pydantic models
- **Automatic validation + retry**: When LLM output fails validation, automatically re-prompts with failure context
- **15+ provider support**: OpenAI, Anthropic, Gemini, Mistral, Cohere, Ollama, DeepSeek, vLLM, etc.
- **Multi-language**: Python, TypeScript, Go, Ruby, Elixir, Rust
- **Streaming**: Real-time partial responses and list streaming
- **Type safety**: Full IDE autocomplete support

## Design Philosophy

Unlike broader AI frameworks (LangChain, LlamaIndex), Instructor focuses on doing one thing well: "getting reliable, validated data from LLMs." The library is a thin wrapper that adds [[concepts/structured-output-extraction]] capability to existing LLM clients.

## Usage

```python
import instructor
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

client = instructor.from_provider("openai/gpt-4o")
person = client.create(
    response_model=Person,
    messages=[{"role": "user", "content": "Extract: John is 30 years old"}]
)
```

## Adoption

Used by teams at OpenAI, Google, Microsoft, and AWS.

## Mentioned In

- [[sources/instructor-library-structured-extraction]] — primary source, full feature overview
