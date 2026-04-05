---
title: "Token Counting"
type: concept
sources: ["[[sources/winder-token-count-practical-guide]]", "[[sources/github-faster-bpe-tokenizer]]"]
related: ["[[concepts/tokenization]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[entities/tiktoken]]"]
last_compiled: 2026-04-05
summary: "Practical techniques for counting and estimating token usage in LLM applications — critical for cost management, context window budgeting, and prompt engineering."
---

## Overview

Token counting is the practical engineering discipline of measuring, estimating, and optimizing the number of tokens consumed by LLM applications. Since commercial LLMs charge per token and enforce context window limits, accurate token counting is essential for cost management and application design.

## Key Ideas

### Rules of Thumb

- 1 English token ≈ 4 characters ≈ 0.75 words
- 1,000 tokens ≈ 750 English words
- These ratios vary dramatically by language: German compound words generate 2x+ tokens; non-Latin scripts can be 5-15x worse

### Tools by Provider

| Provider | Tool | Notes |
|----------|------|-------|
| OpenAI | [[entities/tiktoken]] | cl100k_base (GPT-4), p50k_base (Codex), r50k_base (GPT-3) |
| HuggingFace | AutoTokenizer | Works with any model on the Hub |
| Open-source | SentenceTransformers | WordPiece-based for embedding models |
| GitHub | bpe crate | 4x faster than tiktoken, Rust-based |

### Critical Principle: Model-Specific Counting

Different models tokenize differently. A prompt that's 500 tokens on GPT-4 might be 600 on Claude or 400 on Llama 3. **Always count with the correct tokenizer for your target model.** The rule-of-thumb "4 chars per token" is only useful for rough estimation.

### Chat Message Overhead

For chat-based APIs (GPT-4, Claude), each message adds overhead beyond the text content — approximately 3 tokens per message for OpenAI, plus additional tokens for function/tool parameters.

### Incremental Token Counting

[[sources/github-faster-bpe-tokenizer]] introduced incremental encoders that enable **constant-time token counting** as text is appended — essential for dynamically building prompts within a token budget. Traditional tokenizers require re-encoding the entire text to count tokens after any change.

### Cost Optimization

- Remove redundant instructions and boilerplate
- Use concise language without sacrificing clarity
- Monitor usage via API response objects (prompt_tokens, completion_tokens, total_tokens)
- Consider language choice: equivalent content in a more efficiently-tokenized language costs less

### Language-Specific Variability

The German word "neunzehnhundertvierundachtzig" (1984) requires ~11 tokens vs. English "nineteen eighty four" at ~5 tokens. This variability means cost estimates based on English character counts are unreliable for multilingual applications.

## Sources

- [[sources/winder-token-count-practical-guide]] — comprehensive practical guide with code examples
- [[sources/github-faster-bpe-tokenizer]] — incremental token counting innovation

## Related Concepts

- [[concepts/tokenization]] — the process that produces tokens to count
- [[concepts/vocabulary-size-tradeoffs]] — vocabulary size directly affects token counts
- [[entities/tiktoken]] — the primary tool for OpenAI token counting
- [[concepts/multilingual-tokenization]] — language affects token counts dramatically
