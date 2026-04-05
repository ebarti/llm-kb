---
marp: true
theme: kb-theme
paginate: true
header: "LLM Knowledge Base"
footer: "Generated 2026-04-05"
---

<!-- _class: title -->

# RAG vs. Index-Based Retrieval
## When You Don't Need a Vector Database

LLM Knowledge Base | April 2026

---

## Why This Comparison Matters

The dominant assumption in LLM applications is that you need **Retrieval-Augmented Generation (RAG)** with a vector database for document Q&A.

Karpathy's LLM knowledge base workflow challenges this directly: at personal scale, **LLM-maintained index files beat vector search** in accuracy, simplicity, and cost.

---

<!-- _class: divider -->

# RAG
## The standard approach

---

## How RAG Works

```
Documents --> Chunk --> Embed --> Vector DB
                                    |
Query --> Embed --> Similarity Search --> Top-K Chunks --> LLM --> Answer
```

1. **Chunk** documents into passages (500-1000 tokens each)
2. **Embed** each chunk into a high-dimensional vector
3. **Store** vectors in a specialized database (Pinecone, Weaviate, Chroma)
4. At query time: embed the query, find nearest neighbors, feed to LLM

---

## RAG Strengths

- **Scales to millions** of documents without hitting context limits
- **Mature ecosystem**: dozens of vector DBs, embedding models, frameworks
- **Works with any document type** regardless of structure
- **Sub-millisecond retrieval** at scale with ANN indexes

---

## RAG Weaknesses

- **Approximate** -- ANN search may miss the true best matches
- **Chunk quality matters**: bad chunking = bad retrieval = bad answers
- **Infrastructure cost**: vector DB hosting, embedding compute, re-indexing
- **Stale on update**: documents change --> must re-chunk and re-embed
- **Loss of structure**: cross-references and context lost in chunking

---

<!-- _class: divider -->

# Index-Based Retrieval
## The simpler alternative

---

## How Index-Based Retrieval Works

```
Wiki Articles --> summaries.md (one line per article)
                       |
Query --> LLM reads summaries --> Identifies relevant articles --> 
LLM reads full articles --> Answer
```

1. LLM maintains a `summaries.md` with **one-line descriptions** of every article
2. At query time: LLM reads the index (~20K tokens for 100 articles)
3. LLM **reasons** about which articles are relevant
4. LLM reads those full articles and synthesizes an answer

---

## Index-Based Strengths

- **Exact** -- the LLM reasons over every article summary, missing nothing
- **Zero infrastructure** -- just markdown files
- **Instant freshness** -- recompile the wiki and the index is current
- **Structure preserved** -- cross-links, context, and relationships intact
- **Full article access** -- no lossy chunking, LLM reads the complete article

---

## Index-Based Weaknesses

- **Scale ceiling** at ~100-400 articles (~400K-1M words total)
- **Context window dependent** -- needs large-context LLMs (100K+ tokens)
- **Higher per-query token cost** -- reads more text per query
- **No multi-modal** -- text-only (no image/audio similarity search)

---

## Head-to-Head Comparison

| Dimension | RAG | Index-Based |
|-----------|-----|-------------|
| Scale | Millions of docs | ~100-400 articles |
| Accuracy | Approximate (ANN) | Exact (LLM reasoning) |
| Infrastructure | Vector DB + embeddings | Markdown files only |
| Update latency | Re-embed required | Instant (recompile) |
| Per-query cost | Low (small chunks) | Higher (full articles) |
| Setup complexity | Medium-High | Minimal |
| Structure preservation | Lost in chunking | Fully preserved |
| Multi-modal | Supported | Text only |

---

## The Scale Threshold

<div class="columns">
<div>

### Below the Threshold
**~100 articles / ~400K words**

Index-based retrieval wins:
- Simpler
- More accurate
- Zero infrastructure
- Karpathy's proven workflow

</div>
<div>

### Above the Threshold
**1,000+ articles / 1M+ words**

RAG becomes necessary:
- Exceeds context windows
- ANN tradeoff acceptable
- Or: consider finetuning

</div>
</div>

---

## The Third Option: Finetuning

At very large scale, synthetic data generation + finetuning could **encode the corpus into model weights**:

- Eliminates context window retrieval entirely
- Knowledge is "baked in" permanently
- Risk: hallucination contamination baked into weights is **irreversible**
- Tanwar et al. (2024): finetuning on hallucinated data causes "poor calibration"

---

## What Practitioners Say

The Hacker News vector database debate revealed practitioner consensus:

> **pgvector** and **Elasticsearch** handle most use cases. Dedicated vector DBs are only justified at **billion-vector scale**.

The real question is not "do you need a vector database?" but **"do you need approximate nearest-neighbor search?"**

---

## When Vector DBs Are Actually Justified

- **Billion-vector scale**: Wikipedia, social media, enterprise-wide search
- **Sub-millisecond latency**: real-time similarity in production
- **Multi-modal retrieval**: text + images + audio in the same index
- **Existing infrastructure**: if you already run Elasticsearch, add vectors there

**Alternatives that suffice at smaller scale**:
- pgvector (PostgreSQL extension) -- but watch out for IVF recall issues
- FAISS -- open-source, handles billions with disk-based indexing
- Vespa.ai -- underrated hybrid engine

---

## The Verdict

<div class="callout">

For personal or team-scale knowledge bases (~100-400 articles), **index-based retrieval is superior**: it is simpler, more accurate, preserves document structure, and requires zero infrastructure beyond markdown files and an LLM with a large context window.

RAG becomes necessary only when the corpus exceeds context window limits -- and even then, pgvector or FAISS may suffice without a dedicated vector database.

</div>

---

## Sources

- **Karpathy** -- RAG not needed at small scale; index navigation sufficient
- **DAIR.AI Academy** -- No vector infrastructure needed at ~100-article scale
- **Pebblous** -- Context window expansion makes vector DBs unnecessary at personal scale
- **Decoding AI** -- Production RAG with MongoDB vector search (justified at their scale)
- **HN Vector DB Debate** -- Practitioner consensus: pgvector handles most cases

---

<!-- _class: end -->

# RAG vs. Index-Based Retrieval

Start simple. Scale when you must.

LLM Knowledge Base | April 2026
