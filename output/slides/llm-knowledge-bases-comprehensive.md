---
marp: true
theme: default
paginate: true
---

# LLM Knowledge Bases
## A Comprehensive Overview
### From Karpathy's Vision to Production Systems

---

## Agenda

1. What is an LLM Knowledge Base?
2. The Karpathy Vision
3. Three-Layer Architecture (Raw, Wiki, Schema)
4. The Ingest Pipeline
5. Wiki Compilation Process
6. Q&A and Query System
7. Linting and Health Checks
8. Output Formats (Reports, Slides, Viz)
9. Tools Ecosystem
10. Search Engine
11. Auto-Discovery and the Filing Loop
12. Scaling Considerations
13. Future Directions
14. Conclusion and References

---

## What is an LLM Knowledge Base?

- A **personal or team knowledge system** where an LLM authors and maintains all structured content
- Source documents are ingested raw; the LLM compiles them into a navigable wiki
- Humans interact via **natural language** -- the LLM writes, updates, and maintains everything
- Not a chatbot, not a RAG pipeline -- a **persistent, accumulating knowledge compiler**

> "You rarely ever write or edit the wiki manually, it's the domain of the LLM."
> -- Andrej Karpathy

---

## The Karpathy Vision (April 2026)

- LLMs are increasingly useful for **manipulating knowledge**, not just code
- A shift from "code generation" to "knowledge compilation"
- The next developer competitive advantage: curating knowledge, not writing code
- Potential for a **polished product** rather than a "hacky collection of scripts"
- Targets the **$62B enterprise knowledge management** sector

> "I think there is room here for an incredible new product instead of a hacky collection of scripts."

---

## Core Principle: LLM as Compiler

| Traditional KM | LLM Knowledge Base |
|---|---|
| Human writes articles | LLM writes articles |
| Manual cross-linking | Automated wikilinks |
| Search via keyword | LLM-mediated Q&A |
| Static once written | Incrementally updated |
| Expert-dependent | Source-dependent |

The LLM transforms unstructured inputs into structured, cross-referenced knowledge.

---

## Three-Layer Architecture

```
raw/          <-- Ingested source documents (source of truth)
wiki/         <-- LLM-compiled and maintained
  _index.md       Master article index
  _meta/          Summaries, link graph, manifest
  sources/        Per-source summary articles
  concepts/       Cross-source concept articles
  entities/       Named entity profiles
  comparisons/    Side-by-side analyses
output/       <-- Reports, slides, images (filed back)
```

---

## Layer 1: Raw Sources

- **Source of truth** -- never modified after ingestion
- Ingested via Obsidian Web Clipper, manual copy, API scraping
- Formats: articles, papers, repos, datasets, transcripts
- Each file preserves original content with metadata
- Provenance chain: every wiki claim traces back to a raw file

---

## Layer 2: The Wiki

- **LLM-authored** structured markdown with wikilinks
- **Source summaries** (`wiki/sources/`): key points, quotes, related concepts per raw file
- **Concept articles** (`wiki/concepts/`): cross-source synthesis on topics
- **Entity profiles** (`wiki/entities/`): named entities (people, tools, orgs)
- **Comparisons** (`wiki/comparisons/`): structured side-by-side analyses
- **Metadata** (`wiki/_meta/`): summaries index, link graph, manifest

---

## Layer 3: Schema and Metadata

- `_index.md` -- master listing of all articles with one-line descriptions
- `_meta/summaries.md` -- one-line summaries for Q&A context loading
- `_meta/links.md` -- backlink graph showing article connections
- `_meta/manifest.md` -- tracks which raw files have been compiled
- YAML frontmatter on every article: title, type, sources, related, last_compiled

---

## The Ingest Pipeline

```
Web Clipper / API / Manual Copy
         |
         v
    raw/<source-name>.md
         |
         v
  Manifest check: already compiled?
         |
    No --+-- Yes (skip)
         |
         v
  LLM compilation triggered
```

- Multiple ingestion channels: Obsidian Web Clipper, Firecrawl, manual
- Microsoft MarkItDown converts PDFs, Office docs, images to markdown
- Pandoc handles format conversion with markdown as hub format

---

## Wiki Compilation: Step by Step

1. Read `_meta/manifest.md` to identify unprocessed raw files
2. For each new raw file: create/update `wiki/sources/<name>.md`
3. Identify key concepts; create/update `wiki/concepts/<concept>.md`
4. Create/update entity profiles in `wiki/entities/`
5. Rebuild `wiki/_index.md`
6. Update `_meta/summaries.md`, `_meta/links.md`, `_meta/manifest.md`

> "The key innovation centers on the workflow pattern: having an LLM progressively construct and sustain a structured knowledge repository."
> -- DAIR.AI Academy

---

## Compilation: Information Extraction

| Step | IE Subtask | Approach |
|------|-----------|----------|
| Extract title, author, date | Structured output extraction | Pydantic schema |
| Identify people, tools, papers | Named entity recognition | Zero-shot LLM |
| Connect entities to concepts | Relation extraction | Triple extraction |
| Deduplicate mentions | Entity linking | LLM clustering |
| Create source summaries | Summarization | Extract-then-abstract |
| Verify extracted claims | Claim extraction | Atomic decomposition |

---

## The Four-Phase Operational Cycle

```
    Ingest          Compile          Query          Maintain
  +---------+    +-----------+    +--------+    +-----------+
  | raw/    | -> | wiki/     | -> | Q&A    | -> | Lint      |
  | sources |    | articles  |    | output |    | health    |
  +---------+    +-----------+    +--------+    +-----------+
       ^                               |              |
       |                               v              v
       +----------- Filing Loop -------+--------------+
```

Every query result and lint suggestion feeds back into the KB.

---

## Q&A Without Vector Databases

- At ~100 articles (~400K words), **no RAG pipeline needed**
- LLM reads `_meta/summaries.md` (one-line summaries of all articles)
- Selects relevant articles based on summaries
- Reads full articles and synthesizes answers
- Context window sufficient for navigation + answer generation

> "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries."
> -- Karpathy

---

## Q&A: Index-Based Retrieval Flow

```
User Question
     |
     v
Read _meta/summaries.md (~400 lines)
     |
     v
LLM selects 3-8 relevant articles
     |
     v
Read full article content
     |
     v
Synthesize answer with citations
     |
     v
File answer back into wiki (optional)
```

---

## Linting and Health Checks

- **Inconsistency detection**: compare claims across articles for contradictions
- **Missing data imputation**: fill gaps using web search during lint pass
- **Broken link detection**: find `[[wikilinks]]` to non-existent files
- **Orphan detection**: articles with no incoming links
- **New article suggestions**: concepts mentioned but lacking dedicated articles
- **Stale content detection**: raw files not yet compiled
- **Question generation**: suggest further research directions

Output saved to `output/lint-report.md`.

---

## Output Formats

| Format | Tool | Use Case |
|--------|------|----------|
| Markdown reports | LLM + templates | Deep-dive analyses |
| Slide decks | Marp | Presentations |
| Visualizations | matplotlib | Charts, graphs |
| Comparison tables | LLM | Side-by-side analyses |
| Glossaries | LLM | Term definitions |
| Reading lists | LLM | Curated references |

All outputs viewable in Obsidian and filed back into the wiki.

---

## Marp: Markdown to Slides

- Marp converts markdown files to HTML, PDF, or PPTX presentations
- Native Obsidian integration via Marp plugin
- `---` separators between slides
- Supports themes, pagination, tables, blockquotes, images
- LLM generates slide content directly from wiki articles

---

## Tools Ecosystem

- **Obsidian** -- read-only frontend IDE for viewing wiki, raw, and outputs
- **Obsidian Web Clipper** -- primary ingestion tool
- **Microsoft MarkItDown** -- convert any document to markdown
- **Pandoc** -- universal format converter
- **Marp** -- markdown presentations
- **matplotlib** -- visualization generation
- **Custom CLI search** -- semantic indexing for larger queries
- **MCP servers** -- tool integration via Model Context Protocol

---

## The Search Engine

- Custom CLI tool for semantic search over the knowledge base
- Handed off to the LLM as a tool for queries beyond index navigation
- Combines keyword matching with structural navigation
- At scale, may incorporate embeddings via ChromaDB or pgvector
- At personal scale, index-based navigation suffices

---

## Auto-Discovery: The Filing Loop

- Every query result **compounds** the knowledge base
- Exploration outputs get filed back as new wiki content
- Lint passes suggest new articles from observed gaps
- Research questions generated by the LLM drive future ingestion

> "My own explorations and queries always 'add up' in the knowledge base."
> -- Karpathy

This creates a **self-reinforcing flywheel** of knowledge accumulation.

---

## Hallucination Contamination Risk

- LLM errors written into the wiki can propagate through:
  - Future queries using contaminated articles as context
  - Fine-tuning on wiki content with embedded errors
  - Cross-linked articles amplifying incorrect claims
- **Mitigation**: vault separation (Steph Ango's recommendation)
  - Keep AI-generated wiki separate from human-curated notes
- **Mitigation**: source provenance chain back to raw files
- **Mitigation**: lint passes for contradiction detection

---

## The "Cheap Ontology" Framing

- Enterprise knowledge graphs cost $10M-$20M to build and maintain
- LLM wikis achieve similar results via markdown + LLM API + natural-language schema
- Enabled by **1,000-fold context window expansion** (2023-2026)
- Data quality (not model scale) is the decisive bottleneck

| Approach | Cost | Maintenance | Accessibility |
|----------|------|-------------|---------------|
| Enterprise KG | $10M+ | Expert teams | SPARQL queries |
| LLM Wiki | ~$0/month | LLM API calls | Natural language |

---

## Scaling Considerations

| Scale | Strategy | Infrastructure |
|-------|----------|---------------|
| ~100 articles | Index-based Q&A | Markdown + LLM API |
| ~1,000 articles | Hybrid index + embeddings | + ChromaDB/pgvector |
| ~10,000 articles | Full RAG pipeline | + Vector DB + reranking |
| Enterprise | Knowledge graph + RAG | + Neo4j/Graphiti |

- pgvector/FAISS handle most cases; dedicated vector DBs only at billion-vector scale
- Context windows growing ~30x/year; effective usage growing ~250x

---

## Comparison: LLM KB vs STORM vs KARMA

| Dimension | Karpathy LLM KB | STORM | KARMA |
|-----------|----------------|-------|-------|
| Approach | Persistent accumulating wiki | Single-shot article generation | Multi-agent KG enrichment |
| Scale | ~100 articles | One article per run | 1,200+ papers |
| Output | Markdown wiki | Wikipedia-style article | Graph triplets |
| Agents | Single LLM | Multi-perspective simulation | 9 specialized agents |
| Persistence | Yes | No | Yes |
| Best for | Personal research | Reference articles | Scientific literature |

---

## Comparison: LLM KB vs Traditional RAG

| Dimension | LLM Knowledge Base | Traditional RAG |
|-----------|-------------------|-----------------|
| Retrieval | Index + summaries | Vector similarity |
| Infrastructure | Markdown files | Vector DB + embeddings |
| Maintenance | LLM compilation + linting | Re-indexing pipeline |
| Auditability | Full source provenance | Chunk-level |
| Cost | Near-zero | Cloud vector DB fees |
| Scale ceiling | ~1,000 articles (unassisted) | Millions of documents |

---

## Related Systems in the Ecosystem

- **Graphiti** (Zep): temporal context graphs with time-windowed facts
- **Knowledge Graph Kit** (Gallagher): SQLite + ChromaDB personal graph
- **Decoding AI**: production FTI architecture (MongoDB + Llama fine-tuning)
- **MarkdownDB**: indexing markdown into SQLite for structured queries
- **Second Brain RAG**: Notion-based ETL pipeline with vector search

---

## Future Directions

1. **Synthetic data generation**: LLM generates training data from wiki content
2. **Fine-tuning**: the LLM "knows" the corpus in its weights (RAFT, LoRA, QLoRA)
3. **Multi-agent compilation**: specialized agents for different extraction tasks
4. **Temporal knowledge**: tracking what was true when (Graphiti-style)
5. **Multimodal ingestion**: images, charts, diagrams as first-class sources
6. **Product gap**: from scripts to polished product for non-technical users
7. **Context engineering**: RAG evolving into unified context management

---

## Synthetic Data and Fine-Tuning Pipeline

```
wiki/ articles
     |
     v
Generate Q&A pairs (synthetic data)
     |
     v
Quality filtering (Phi "textbook quality" approach)
     |
     v
Fine-tune with LoRA/QLoRA
     |
     v
LLM "knows" corpus in weights
     |
     v
Faster queries, lower latency, offline capability
```

RAFT (Retrieval-Augmented Fine-Tuning) achieves up to **76% improvement** on domain benchmarks.

---

## The Product Gap

> "I think there is room here for an incredible new product."
> -- Karpathy

**What exists**: hacky scripts, manual CLI workflows, developer-only tools

**What's needed**:
- One-click ingestion from any source
- Automatic compilation with visual feedback
- Natural language Q&A interface
- Collaborative multi-user wikis
- Enterprise-grade access controls

**Market**: $62B enterprise knowledge management sector

---

## Key Takeaways

1. **LLM as author**: the paradigm shift from human-written to LLM-compiled knowledge
2. **Markdown as substrate**: human-readable, LLM-friendly, version-controllable, future-proof
3. **Simplicity scales**: index-based Q&A works surprisingly well at personal scale
4. **Self-reinforcing**: every query compounds the knowledge base
5. **Data quality > model scale**: garbage in, hallucinations out
6. **The filing loop**: exploration and output feed back into the KB

---

## References

- Karpathy, A. (2026). "Thread on LLM Knowledge Bases." Twitter/X.
- Saravia, E. (2026). "LLM Knowledge Bases: Architecture Overview." DAIR.AI Academy.
- Rhodes, G. (2026). "Karpathy Workflow Technical Walkthrough."
- Antigravity Codes (2026). "6-Step AI Workflow Analysis."
- Pebblous (2026). "Cheap Ontology: 50 Years of Ontology History."
- Ango, S. "File Over App." Obsidian Blog.
- Sivers, D. "Plain Text Files." sivers.org.

---

## Thank You

### LLM Knowledge Bases: The Future of Personal and Team Knowledge Management

**Key insight**: Architecture matters more than model size. A well-designed knowledge compilation system with simple retrieval can outperform complex RAG pipelines at personal scale.

**Start here**: `raw/` directory + LLM API + Obsidian = your first LLM Knowledge Base.
