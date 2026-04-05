---
title: "Source: Instructor — Structured Data Extraction Library for LLMs"
type: source-summary
source: "[[raw/instructor-library-structured-extraction]]"
related: ["[[concepts/structured-output-extraction]]", "[[concepts/information-extraction]]", "[[entities/instructor]]", "[[entities/pydantic]]"]
last_compiled: 2026-04-05
summary: "Instructor is the most popular Python library for structured LLM extraction (3M+ monthly downloads), using Pydantic models with automatic validation and retry across 15+ providers."
reading_time: "1 min"
---

## Key Points

- Most popular Python library for structured LLM extraction: 3M+ monthly downloads, 11k GitHub stars
- Uses Pydantic models to define output schemas with automatic validation and retry
- Supports 15+ providers: OpenAI, Anthropic, Gemini, Mistral, Cohere, Ollama, DeepSeek, etc.
- Multi-language: Python, TypeScript, Go, Ruby, Elixir, Rust
- Focused scope: "does one thing very well" vs. broader frameworks like LangChain

## Detailed Summary

[[entities/instructor]] represents the "thin library" approach to [[concepts/structured-output-extraction]]. Rather than building a full agent framework, it focuses exclusively on getting validated, typed data from LLMs. The pattern is: define a Pydantic model, call the LLM, get back a typed Python object.

The validation-retry loop is critical for production [[concepts/information-extraction]]: when the LLM's output fails Pydantic validation, Instructor automatically re-asks with failure context, enabling self-correction. This is essential for [[concepts/wiki-compilation]] pipelines where schema compliance is mandatory.

Compared to alternatives like LangChain's structured output or raw provider APIs, Instructor's advantage is simplicity and reliability. It is used by teams at OpenAI, Google, Microsoft, and AWS.

## Related Concepts

- [[concepts/structured-output-extraction]] — the core technique
- [[concepts/information-extraction]] — parent discipline
- [[entities/pydantic]] — the validation backbone
- [[concepts/wiki-compilation]] — extraction feeds into compilation pipelines
