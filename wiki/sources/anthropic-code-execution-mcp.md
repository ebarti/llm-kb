---
title: "Source: Code Execution with MCP (Anthropic Engineering)"
type: source-summary
source: "[[raw/anthropic-code-execution-mcp]]"
related: ["[[concepts/model-context-protocol]]", "[[concepts/mcp-code-execution-pattern]]", "[[concepts/augmented-llm]]"]
last_compiled: 2026-04-05
summary: "Anthropic engineering pattern: agents write code to interact with MCP servers instead of loading all tool definitions — achieving 98.7% token savings, better security via PII filtering, and persistent state management."
---

## Key Points
- Problem: loading all MCP tool definitions into context consumes 100K+ tokens before any work begins
- Solution: agents write code that interacts with MCP tools via a filesystem-like structure, loading only needed definitions
- Token savings: 150,000 → 2,000 tokens (98.7% reduction) by filtering data locally before model processing
- Security benefit: PII can be tokenized/replaced before flowing through the model
- Data filtering: 10,000-row spreadsheet filtered to 5 relevant rows before model sees it
- Enables persistent state: agents save intermediate results and develop reusable "skills"

## Detailed Summary

This Anthropic engineering article addresses a critical scaling problem with [[concepts/model-context-protocol]]: as agents connect to more MCP servers, the upfront cost of loading all tool definitions into context becomes prohibitive. With thousands of tools, the context overhead alone can consume hundreds of thousands of tokens.

The proposed [[concepts/mcp-code-execution-pattern]] organizes MCP tools as a filesystem. Instead of loading all definitions, agents explore the directory structure, identify relevant tools, and write code that calls them directly. This achieves dramatic token savings — the article's example shows a 98.7% reduction from 150,000 to 2,000 tokens.

Beyond efficiency, the pattern improves security. Large datasets are filtered in the execution environment before reaching the model, and PII can be tokenized to prevent sensitive data from flowing through LLM context. Agents can also persist state across operations, building up reusable code functions as persistent skills.

## Related Concepts
- [[concepts/model-context-protocol]] — the underlying protocol
- [[concepts/mcp-code-execution-pattern]] — the pattern described
- [[concepts/augmented-llm]] — the broader agent architecture this optimizes
