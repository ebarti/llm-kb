---
title: "Source: Why LLMs Love Markdown"
type: source-summary
source: "[[raw/llms-love-markdown]]"
related: ["[[concepts/markdown-for-ai-agents]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Quantifies markdown's advantages for LLMs: 25-75% token reduction vs HTML, 89% vs 62% RAG retrieval accuracy, and superior semantic parsing via AST tokenization."
reading_time: "2 min"
---

## Key Points

- Token efficiency: 75-80% reduction per heading vs HTML; 25-75% overall depending on source format
- "Introduction" heading: ~3 tokens in markdown, ~12 in HTML, ~15 in JSON
- 100-document KB converted from HTML to markdown saves 25-50% on API costs
- RAG retrieval accuracy: 89% with markdown vs 62% with raw PDF text
- LLMs process markdown via AST tokenization, grasping hierarchical relationships
- Training data heavily represents markdown (GitHub, Stack Overflow, technical docs)

## Detailed Summary

This source provides the quantitative evidence for what other sources argue qualitatively: markdown is the optimal format for LLM consumption. The token efficiency data is striking — a single heading costs 3 tokens in markdown versus 15 in JSON — and at scale, converting a knowledge base to markdown can halve API costs.

The RAG performance difference (89% vs 62%) is particularly relevant to the [[concepts/llm-knowledge-base]] architecture: by storing knowledge in markdown rather than raw PDF text, retrieval accuracy improves by 44% relatively. This validates the entire ingest-to-markdown pipeline.

The article also explains *why* LLMs handle markdown well: they tokenize its Abstract Syntax Tree, mapping headings, lists, and tables to semantic roles. This isn't just pattern matching — it's structural comprehension. The one caveat: for highly nested or interdependent structured data, XML's explicit demarcation may outperform markdown.

## Related Concepts

- [[concepts/markdown-for-ai-agents]] — quantitative backing for markdown as LLM input format
- [[concepts/markdown-as-universal-interface]] — evidence supporting the "LLM-friendly" property
- [[concepts/rag-vs-index-based-retrieval]] — markdown improves retrieval accuracy in RAG systems
- [[concepts/llm-knowledge-base]] — markdown KB outperforms raw-text alternatives
