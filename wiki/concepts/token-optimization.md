---
title: "Token Optimization"
type: concept
sources: ["[[sources/redis-token-optimization]]", "[[sources/premai-llm-cost-optimization-guide]]"]
related: ["[[concepts/llm-cost-optimization]]", "[[concepts/prompt-caching]]", "[[concepts/semantic-caching]]"]
last_compiled: 2026-04-05
summary: "Systematic reduction of token consumption through prompt compression, output constraints, conversation history management, and context assembly optimization — cutting 20-40% of token waste without infrastructure changes."
---

## Overview

Token optimization is the practice of minimizing the number of tokens consumed per LLM interaction without degrading output quality. Since LLM costs scale linearly with token usage, and output tokens cost 3-5x more than input tokens, token optimization is the simplest (and often first) lever for [[concepts/llm-cost-optimization|cost reduction]].

## Where Token Waste Occurs

1. **Verbose system prompts** repeated across every query — the same 500-token instructions sent thousands of times daily
2. **Bloated conversation history** — 20-turn conversations consuming 5,000-10,000 tokens when 500-1,000 would suffice
3. **Unoptimized few-shot examples** — more examples don't always improve results
4. **Missing output limits** — no max_tokens constraint allows unnecessarily verbose responses
5. **Oversized RAG context** — retrieving more documents than necessary fills context with low-relevance information

## Optimization Techniques

### Input Optimization
- **Tighter prompts**: "Summarize:" often works as well as verbose instruction paragraphs. "What's on my calendar today?" (8 tokens) vs "Could you please provide me with a comprehensive overview of my scheduled appointments for today?" (18 tokens)
- **Prompt compression**: Tools like LLMLingua achieve 5-20x compression while preserving semantic meaning. One study showed compression from 800 to 40 tokens (95% reduction) with minimal quality loss.
- **Conversation summarization**: Compress older turns into summaries rather than carrying full history
- **Selective RAG retrieval**: Limit to a fixed token budget, prioritizing relevance over volume

### Output Optimization
- **Set max_tokens**: Always specify in API calls
- **Length constraints in instructions**: "Answer in 50 words" or "Reply with JSON only"
- **Format optimization**: Switching from verbose prose to JSON can reduce output by 15%
- **Output tokens are the priority**: they cost 3-5x more AND add sequential latency

### Context Assembly
- **Semantic chunking**: Split text based on meaning, not arbitrary character counts
- **Relevance scoring**: Only include context above a similarity threshold
- **Token budgeting**: Allocate fixed budgets per context section

## Sources
- [[sources/redis-token-optimization]] — token waste identification and optimization playbook
- [[sources/premai-llm-cost-optimization-guide]] — prompt optimization as the quickest win

## Related Concepts
- [[concepts/llm-cost-optimization]] — token optimization as a foundational strategy
- [[concepts/prompt-caching]] — reduces cost of remaining tokens
- [[concepts/semantic-caching]] — eliminates inference calls for similar queries
