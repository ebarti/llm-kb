---
title: "Source: RAG vs Large Context Window — Redis"
type: source-summary
source: "[[raw/redis-rag-vs-long-context]]"
related: ["[[concepts/context-windows]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/context-engineering]]", "[[concepts/prompt-caching]]"]
last_compiled: 2026-04-05
summary: "Comprehensive analysis of RAG vs long-context tradeoffs: RAG wins on cost/latency (1s vs 30-60s), long context wins on full-document reasoning, hybrid approaches are the pragmatic path."
reading_time: "2 min"
---

## Key Points

- Accuracy drops **10-20+ percentage points** when relevant information sits in the middle of long contexts (the [[concepts/lost-in-the-middle]] problem)
- RAG latency ~1 second vs long-context 30-60 seconds on the same workload
- Identical answers produced ~60% of the time across 12 QA datasets
- Semantic caching can reduce RAG costs by **73%** in high-repetition workloads
- At 10,000 requests/month with 100K-token contexts, costs exceed **$2,000/month** before output tokens

## Detailed Summary

Redis's analysis challenges the popular narrative that million-token context windows make RAG obsolete. The article systematically compares the two approaches across speed, cost, and quality dimensions, finding that each excels in different scenarios.

The hidden costs of large context windows are substantial: O(n^2) attention complexity drives latency to 30-60 seconds, KV cache memory can exceed model weight sizes, and position bias degrades accuracy for middle-positioned information. RAG, by contrast, achieves ~1 second end-to-end with 50-200ms retrieval overhead.

The article proposes a "smart layering" pattern with four stages: writing context (capture), selecting context (retrieval), compressing context (summarization), and isolating context (separation of concerns). This maps directly to [[concepts/context-engineering]] principles.

## Notable Quotes

> "The best architecture isn't necessarily the one with the largest context window or most complex retrieval system. It's the one that matches your specific requirements for speed, cost, accuracy, and operational complexity."

## Related Concepts

- [[concepts/context-windows]] — core subject of the analysis
- [[concepts/rag-vs-index-based-retrieval]] — deepens the existing wiki coverage with production-scale cost/latency data
- [[concepts/lost-in-the-middle]] — position bias documented as key limitation of long-context
- [[concepts/context-engineering]] — the "smart layering" pattern is a context engineering framework
- [[concepts/prompt-caching]] — semantic caching as cost mitigation strategy
