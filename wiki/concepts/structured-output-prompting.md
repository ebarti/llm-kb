---
title: "Structured Output Prompting"
type: concept
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/few-shot-prompting]]", "[[concepts/system-prompt-design]]"]
last_compiled: 2026-04-05
summary: "Techniques for getting LLMs to produce predictable, parseable output formats (JSON, XML, Markdown tables) — essential for production systems that programmatically consume model outputs."
---

## Overview

Structured output prompting is the practice of getting LLMs to return data in a predictable, parseable format — typically JSON, XML, Markdown tables, or other machine-readable structures. This is essential for any production system that needs to programmatically process model outputs rather than display them to humans.

In 2025-2026, a major shift occurred: leading model providers now offer constrained generation capabilities where models are literally prevented from producing invalid JSON at the token level. This eliminates parsing errors entirely and represents a move from prompting-based format control to API-level guarantees.

## Techniques

### The Four-Layer Approach
1. **Define the schema**: Specify field names and types
2. **Show one perfect example**: Reinforce the structure concretely
3. **Add strict formatting rules**: Specify delimiters, escaping, etc.
4. **Include a validation instruction**: "Verify your output matches the schema before returning"

### XML Tags (Claude-specific)
Anthropic recommends wrapping content in XML tags for unambiguous structure:
```xml
<instructions>Your task description</instructions>
<context>Background information</context>
<output_format>
  <field name="title" type="string"/>
  <field name="summary" type="string"/>
</output_format>
```

### Positive Format Instructions
Tell the model what format TO produce rather than what to avoid:
- Instead of "Do not use markdown" → "Write in smoothly flowing prose paragraphs"
- Use XML format indicators: "Write the prose in `<prose>` tags"

### Constrained Generation APIs
OpenAI's structured outputs API (late 2025) and similar offerings enforce JSON schemas at the token level — the model cannot generate invalid output. This is the future of structured output: not prompting, but schema-level constraints.

## Model Preferences

Research shows format preference varies by model:
- **GPT-3.5-turbo**: Performance varies by up to 40% depending on format; prefers JSON
- **GPT-4**: More robust to format variations; favors Markdown
- **Claude**: Benefits from XML-style tags and explicit boundary definitions
- **Gemini**: Excels with hierarchical Markdown structure

## Application to This KB

This KB's entire operation depends on structured output:
- Frontmatter YAML in every wiki article
- Consistent heading structure (## Key Points, ## Detailed Summary, etc.)
- Wikilink format (bracketed category-and-slug references like concepts/example)
- Index and manifest as structured Markdown tables

## Sources
- [[sources/anthropic-claude-prompting-best-practices]] — XML tags, format control, structured outputs
- [[sources/lakera-prompt-engineering-guide]] — Format constraints as core technique

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/few-shot-prompting]] — examples as format demonstration
- [[concepts/system-prompt-design]] — format constraints in system prompts
