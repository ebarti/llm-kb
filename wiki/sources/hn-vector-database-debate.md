---
title: "Source: Do You Need a Vector Database? (HN Discussion)"
type: source-summary
source: "[[raw/hn-vector-database-debate]]"
related: ["[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Hacker News practitioner debate: pgvector and Elasticsearch handle most cases; specialized vector DBs only justified at billion-vector scale; FAISS/Vespa.ai as middle ground; real question is 'do you need ANN search?'"
---

## Key Points
- pgvector sufficient for most projects; Elasticsearch handles vector ops without new infrastructure
- pgvector limitation: IVF algorithm, nprobes=3 default → ~50% recall; HNSW support being added
- FAISS: billion-scale disk-based indexing, open-source, good middle ground
- Vespa.ai: underrated hybrid engine (vector + metadata, multi-vector indexing)
- Single vector per document loses nuance: "like making a movie poster the average of all frames"
- Real question: "do you actually need approximate nearest-neighbor search?"

## Detailed Summary

This HN thread provides honest practitioner perspectives rarely found in vendor documentation. The consensus: for most teams, adding a specialized vector database is premature infrastructure. PostgreSQL with pgvector handles typical workloads; Elasticsearch already does vector search.

Dedicated vector databases only justify their operational complexity at billion-vector scale (Wikipedia-scale datasets, social media content). For personal-scale or team-scale knowledge bases (~100K to ~10M documents), existing tools suffice.

This aligns directly with Karpathy's observation: at ~100 articles / 400K words, an LLM with a 1M-token context window can simply load the entire index rather than doing approximate retrieval — eliminating both the need for vector search AND the accuracy loss from approximate nearest-neighbor algorithms.

## Related Concepts
- [[concepts/rag-vs-index-based-retrieval]] — the central debate
- [[concepts/vector-databases]] — what's being evaluated
