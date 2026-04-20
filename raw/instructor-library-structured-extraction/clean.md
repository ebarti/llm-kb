---
title: "Instructor: Structured Data Extraction Library for LLMs"
source: "https://python.useinstructor.com/"
author: "Jason Liu / 567 Labs"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [instructor, pydantic, structured-output, python, llm-tools, validation]
type: repo
status: raw
discovered_via: search
---

# Instructor: Structured Data Extraction Library for LLMs

## Overview

Instructor is the most popular Python library for extracting structured data from Large Language Models, with over 3 million monthly downloads, 11k GitHub stars, and 100+ contributors. It uses Pydantic models to define output schemas and automatically handles validation, retries, and error handling.

## Core Capabilities

- **Structured Outputs**: Define Pydantic models to specify exactly what data you want from your LLM
- **Automatic Retry Logic**: When validation fails, automatically re-asks with failure context
- **Data Validation**: Leverages Pydantic's full validation framework
- **Real-time Streaming**: Partial responses and list streaming
- **Full Type Safety**: IDE support with autocomplete

## Supported Providers (15+)

OpenAI (GPT models), Anthropic (Claude), Google Gemini, Mistral, Cohere, Ollama, llama-cpp-python, vLLM, DeepSeek, and more.

## How It Works

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
# person.name == "John", person.age == 30
```

## Validation & Retry Mechanism

When responses fail Pydantic validation, Instructor automatically re-asks the model with failure context, enabling self-correction without manual error handling. This is critical for production information extraction where schema compliance is mandatory.

## Multi-Language Support

Available in Python, TypeScript, Go, Ruby, Elixir, and Rust.

## Comparison to Alternatives

Instructor focuses specifically on extraction with validation and retries. Unlike broader AI frameworks (LangChain, LlamaIndex), it "does one thing very well: getting reliable, validated data from LLMs." The library emphasizes simplicity and transparency through Pydantic integration.

Widely adopted by teams at OpenAI, Google, Microsoft, and AWS. Open-source, MIT-licensed.
