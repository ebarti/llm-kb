---
title: "PagedAttention"
type: concept
sources: ["[[sources/kv-cache-optimization-techniques]]", "[[sources/kv-caching-huggingface-explained]]"]
related: ["[[concepts/kv-cache]]", "[[concepts/transformer-architecture]]", "[[concepts/grouped-query-attention]]", "[[concepts/attention-sinks]]", "[[concepts/virtual-context-management]]"]
last_compiled: 2026-04-05
summary: "Virtual-memory-inspired KV cache management (vLLM) that allocates non-contiguous memory blocks with mapping tables — reducing waste from 60-80% to 4% and enabling prompt sharing."
---

## Overview

PagedAttention, introduced in the vLLM project, applies operating system virtual memory concepts to [[concepts/kv-cache]] management. Instead of allocating a single contiguous memory block per request (which must accommodate the maximum possible sequence length), it allocates small non-contiguous blocks dynamically and maintains virtual-to-physical address mapping tables.

## Key Benefits

- **Memory wastage**: Reduced from 60-80% to 4%
- **Dynamic allocation**: Memory matches actual usage, not worst-case
- **Prompt sharing**: Requests with common prefixes share cached KV blocks
- **Batch capacity**: Equivalent to 2-4x more GPU memory for concurrent requests

## Sources

- [[sources/kv-cache-optimization-techniques]] — PagedAttention in KV cache optimization context

## Related Concepts

- [[concepts/kv-cache]] — the cache being managed
- [[concepts/grouped-query-attention]] — complementary optimization reducing cache size
