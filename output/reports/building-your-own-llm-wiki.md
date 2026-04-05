---
title: "Building Your Own LLM Wiki: A Practical Guide"
type: report
generated: 2026-04-05
sources_consulted: 28
---

# Building Your Own LLM Wiki: A Practical Guide

## Introduction

This guide walks through building an LLM-maintained personal knowledge base following the methodology pioneered by [[entities/andrej-karpathy]] ([[sources/karpathy-llm-knowledge-bases]]) and formalized by [[entities/elvis-saravia]] at [[entities/dairai]] ([[sources/dairai-llm-knowledge-bases-architecture]]). By the end, you will have a self-reinforcing knowledge system where an LLM authors, maintains, and queries a structured markdown wiki on your behalf.

The approach described here requires no vector databases, no cloud infrastructure beyond an LLM API, and no specialized tooling beyond a text editor and a markdown viewer. This is the "Cheap Ontology" ([[concepts/cheap-ontology]]) — a 1,000x cost reduction over traditional enterprise knowledge graphs.

---

## Step 1: Set Up the Directory Structure

The foundation is a simple file system layout ([[concepts/llm-knowledge-base]]):

```
my-knowledge-base/
  raw/              <- Source of truth: ingested documents
  wiki/             <- LLM-compiled and maintained (never edit manually)
    _index.md       <- Master article index
    _meta/          <- Summaries, link graph, manifest, stats
      summaries.md  <- One-line summary per article
      links.md      <- Backlink graph
      manifest.md   <- Compilation tracking
    sources/        <- Per-source summary articles
    concepts/       <- Cross-source concept articles
    entities/       <- Articles about people, tools, orgs
    comparisons/    <- Side-by-side comparison articles
  output/           <- Reports, slides, images (filed back)
```

**Key principle**: The `raw/` directory is the source of truth. The `wiki/` directory is entirely LLM-generated. You should never need to manually edit wiki files ([[sources/karpathy-llm-knowledge-bases]]).

**Vault separation** ([[concepts/vault-separation]]): If you have an existing personal knowledge base (e.g., in Obsidian), keep it in a completely separate vault. [[entities/steph-ango]], Obsidian's CEO, explicitly recommends this to prevent [[concepts/hallucination-contamination]] from corrupting your human-curated notes.

---

## Step 2: Choose Your Architecture

### Decision 1: LLM Provider

| Provider | Context Window | Strengths | Cost Consideration |
|----------|---------------|-----------|-------------------|
| Claude (Anthropic) | 1M tokens | Best for structured extraction, XML tags | [[sources/anthropic-claude-prompting-best-practices]] |
| GPT-4o (OpenAI) | 128K tokens | Widely available, tool ecosystem | Moderate |
| Gemini (Google) | 1-2M tokens | Largest context window | [[sources/prompt-caching-providers]]: 75% savings |
| Local (Ollama + Qwen/DeepSeek) | Varies | Privacy, zero per-token cost | [[concepts/local-knowledge-base]] |

**Recommendation**: Start with a frontier model (Claude or GPT-4o) for compilation quality. Consider local models ([[entities/ollama]]) for privacy-sensitive domains or cost reduction on routine queries ([[comparisons/local-vs-cloud-knowledge-base]]).

### Decision 2: Retrieval Strategy

| Corpus Size | Strategy | Infrastructure |
|-------------|----------|---------------|
| <100 articles | Index-based (summaries.md) | None |
| 100-1000 articles | Index-based + topic indexes | None |
| 1000+ articles | RAG with hybrid search | Vector DB needed |

At personal scale, Karpathy found index-based retrieval sufficient for ~400K words ([[concepts/rag-vs-index-based-retrieval]]). Do not over-engineer. Start simple and add infrastructure only when you hit actual limitations.

### Decision 3: Viewing Tool

[[entities/obsidian]] is the recommended viewing IDE ([[concepts/obsidian-as-ide]]):

- **Why Obsidian**: Local-first, markdown-native, graph view for visualizing connections, [[wikilinks]] for navigation, 2000+ community plugins
- **Key plugins**: [[entities/dataview]] for dynamic queries over frontmatter, [[entities/marp]] for viewing LLM-generated slide decks
- **Important**: Obsidian is a read-only viewer in this workflow. The LLM is the author.

**Alternatives**: VS Code with markdown preview, Logseq, or any markdown viewer. The wiki is plain markdown files ([[concepts/markdown-as-universal-interface]]), so it works with any tool ([[concepts/file-over-app]]).

---

## Step 3: Build the Ingestion Pipeline

### Source Acquisition

Raw sources should be high-quality documents relevant to your domain. Quality beats quantity ([[concepts/data-quality-bottleneck]]).

| Source Type | Ingestion Method | Tool |
|-------------|-----------------|------|
| Web articles | Browser clipper | [[entities/obsidian-web-clipper]] |
| PDFs | PDF-to-markdown conversion | [[entities/markitdown]], [[entities/docling]] |
| Academic papers | PDF parser + citation extraction | [[entities/pymupdf]], Nougat for scientific |
| YouTube videos | Transcript extraction | Various transcript APIs |
| Web scraping | API-based crawling | [[entities/firecrawl]] |
| Office documents | Document conversion | [[entities/markitdown]] |

**Best practice**: Convert everything to markdown before placing in `raw/`. Markdown is the universal interface for LLMs ([[concepts/markdown-as-universal-interface]]), achieving 25-75% token reduction vs HTML and 89% vs 62% RAG retrieval accuracy ([[sources/llms-love-markdown]]).

### Quality Gates

Before a document enters `raw/`, evaluate:

1. **Relevance**: Is this within the scope of your knowledge base?
2. **Quality**: Is the source credible and well-written?
3. **Novelty**: Does it add information not already covered?
4. **Recency**: Is the information current?

The "quality assurance layer" before pipeline entry is the highest-leverage investment you can make ([[sources/pebblous-cheap-ontology]]). Low-quality sources generate low-quality wiki content, which cascades into contaminated queries and flawed fine-tuning datasets.

### Frontmatter Template

Each raw file should have YAML frontmatter ([[concepts/yaml-frontmatter]]):

```yaml
---
title: "Descriptive Title of the Source"
source_url: "https://..."
author: "Author Name"
date_published: 2026-03-15
date_ingested: 2026-04-05
type: article  # article, paper, video, documentation
tags: [topic1, topic2]
---
```

---

## Step 4: Design the Compilation Pipeline

Wiki compilation ([[concepts/wiki-compilation]]) is the core of the system. The LLM transforms raw sources into structured wiki articles.

### The Four-Phase Cycle

Per [[sources/dairai-llm-knowledge-bases-architecture]]:

1. **Ingest**: New raw documents arrive in `raw/`
2. **Compile**: LLM processes new documents into wiki articles
3. **Query**: LLM answers questions by navigating the compiled wiki
4. **Maintain**: LLM lints, health-checks, and enriches the wiki

### Compilation Steps

For each new raw file:

1. **Check manifest**: Read `wiki/_meta/manifest.md` to identify unprocessed files
2. **Create source summary**: Generate `wiki/sources/<name>.md` with key points, notable quotes, and related concepts
3. **Identify concepts**: Determine which concepts appear in this source. For existing concepts, update the article. For new concepts, create new articles in `wiki/concepts/`
4. **Identify entities**: People, tools, organizations, papers mentioned. Create/update `wiki/entities/<name>.md`
5. **Create comparisons**: If the source compares approaches, create `wiki/comparisons/<name>.md`
6. **Update indexes**: Rebuild `wiki/_index.md`, update `wiki/_meta/summaries.md` with one-line summaries
7. **Update link graph**: Regenerate `wiki/_meta/links.md` with backlinks
8. **Update manifest**: Mark the raw file as compiled in `wiki/_meta/manifest.md`

### Compilation Prompt Template

```
You are a wiki compiler. Given the raw source document below, perform the following:

1. Create a source summary article following this template:
   - YAML frontmatter (title, type: source-summary, source, related concepts, summary)
   - Key Points (bullet list)
   - Detailed Summary (2-3 paragraphs)
   - Notable Quotes (if any)
   - Related Concepts (wikilinks)

2. Identify 3-7 key concepts. For each:
   - Check if wiki/concepts/<concept>.md already exists
   - If yes: suggest additions (new sources, new key ideas)
   - If no: create new concept article with overview, key ideas, sources, related concepts

3. Identify entities (people, tools, orgs). For each:
   - Create/update wiki/entities/<name>.md

4. Update wiki/_meta/summaries.md with a one-line summary of this source.

Use [[wikilinks]] extensively. Every concept, entity, and source reference should be a wikilink.
Cross-link aggressively — the graph density is a feature, not a bug.
```

### Information Extraction Subtasks

Each compilation step involves specific IE capabilities ([[concepts/wiki-compilation]]):

| Step | IE Subtask | Approach |
|------|-----------|----------|
| Extract metadata | [[concepts/structured-output-extraction]] | Pydantic schema / [[entities/instructor]] |
| Identify entities | [[concepts/named-entity-recognition]] | Zero-shot NER via LLM |
| Connect entities | [[concepts/relation-extraction]] | Triple extraction |
| Deduplicate mentions | [[concepts/entity-linking]] | LLM clustering |
| Create summaries | [[concepts/llm-summarization]] | Hybrid extract-then-abstract |
| Verify claims | [[concepts/claim-extraction]] | Atomic decomposition |

---

## Step 5: Implement Maintenance Workflows

### Linting and Health Checks

LLM-driven health checks ([[concepts/linting-and-health-checks]]) should run periodically:

1. **Broken link detection**: Scan for wikilinks that point to non-existent articles
2. **Orphan detection**: Find articles with no incoming links
3. **Contradiction detection**: Compare claims across articles for inconsistencies
4. **Staleness detection**: Flag articles based on source date vs. last compilation
5. **Coverage gaps**: Identify concepts mentioned but never given their own article
6. **Source verification**: Check that wiki claims trace back to raw sources (provenance)

### The Filing Loop

One of Karpathy's key insights ([[sources/glenrhodes-karpathy-workflow]]): outputs from queries should be filed back into the wiki.

```
Query: "Compare RAG approaches discussed in my sources"
  -> LLM generates a comparison report
  -> Report is saved to output/reports/rag-comparison.md
  -> Report is also filed into the wiki as a new article
  -> Future queries can reference this analysis
```

This creates a self-reinforcing cycle where the knowledge base compounds over time. Every exploration adds to the corpus.

### Scheduled Compilation

Set up automated processes:

- **On new raw file**: Trigger incremental compilation
- **Weekly**: Run full health check (broken links, orphans, contradictions)
- **Monthly**: Generate freshness report, coverage analysis, growth metrics
- **On demand**: Full recompilation when changing wiki structure or prompts

---

## Step 6: Handle Common Pitfalls

### Pitfall 1: Hallucination Contamination

**The risk** ([[concepts/hallucination-contamination]]): LLM-generated errors written into the wiki propagate through future queries and fine-tuning datasets. This is the primary systemic risk.

**Mitigations**:
- Always maintain provenance: every claim in the wiki should trace to a `raw/` source
- Run periodic contradiction scans
- Use [[concepts/vault-separation]]: never mix AI-generated content with human-curated notes
- Flag uncertain claims with explicit markers (e.g., "[unverified]")
- Consider [[concepts/calibrated-uncertainty]] — systems that signal doubt rather than confabulate

### Pitfall 2: Low-Quality Sources

**The risk** ([[concepts/data-quality-bottleneck]]): Garbage in, garbage out. A 1.3B-parameter model trained on "textbook quality" data matches models 10x larger ([[sources/textbooks-are-all-you-need-phi]]). The same principle applies to wiki quality.

**Mitigations**:
- Implement quality gates at ingestion
- Prefer primary sources over summaries-of-summaries
- Remove or quarantine low-quality raw files
- Score sources on credibility, recency, and depth

### Pitfall 3: Over-Engineering

**The risk**: Building RAG infrastructure, vector databases, and fine-tuning pipelines before you have enough content to need them.

**Mitigations**:
- Start with index-based retrieval. Add complexity only when you hit actual scaling limits.
- At <100 articles, all you need is markdown files and an LLM API
- The DAIR.AI analysis ([[sources/dairai-llm-knowledge-bases-architecture]]) emphasizes: no vector infrastructure needed at personal scale

### Pitfall 4: Inconsistent Schema

**The risk**: As the wiki grows, entity types, frontmatter fields, and wikilink conventions drift.

**Mitigations**:
- Define a `CLAUDE.md` or `AGENTS.md` file with explicit schema instructions ([[concepts/cheap-ontology]])
- Include frontmatter templates in your compilation prompts
- Use linting to enforce frontmatter consistency
- Standardize entity naming conventions early

### Pitfall 5: Context Window Overflow

**The risk**: As the wiki grows beyond ~400K words, the LLM can no longer load the entire summaries index.

**Mitigations**:
- Create hierarchical indexes: topic-level summaries that point to article-level summaries
- Consider adding RAG for specific query types while keeping index-based for navigation
- Use [[concepts/context-compression]] techniques to fit more into each query
- Explore [[concepts/prompt-caching]] to reduce cost of repeated index loading

### Pitfall 6: Ignoring Temporal Knowledge

**The risk**: Facts become outdated but the wiki doesn't reflect this ([[concepts/temporal-knowledge]]).

**Mitigations**:
- Include `date_published` and `last_compiled` in all frontmatter
- Run freshness reports that flag articles based on source age
- Consider [[entities/graphiti]]'s approach of explicit validity windows for facts
- When a new source contradicts an old one, update the wiki and note the supersession

---

## Step 7: Scale When Needed

### Scaling Path

| Stage | Articles | Words | Strategy |
|-------|----------|-------|----------|
| 1. Personal | 10-100 | 5K-50K | Index-based, single LLM, manual ingestion |
| 2. Growing | 100-500 | 50K-250K | Topic indexes, automated compilation, health checks |
| 3. Substantial | 500-2000 | 250K-1M | Hybrid index + RAG, [[entities/chromadb]] or [[entities/pgvector]] |
| 4. Enterprise | 2000+ | 1M+ | Full RAG + GraphRAG + fine-tuning |

### When to Add RAG

Add vector retrieval when:
- LLM can no longer process the full summaries index in one context window
- Query accuracy degrades because one-line summaries lack discriminating detail
- You need semantic search across the full corpus
- Cross-document questions require finding non-obvious connections

**Recommended starter RAG stack**: [[entities/chromadb]] (simple, local) or [[entities/pgvector]] (if you already use PostgreSQL). Use [[concepts/hybrid-search]] combining vector similarity with BM25 keyword search ([[sources/weaviate-hybrid-search-explained]]).

### When to Add Fine-Tuning

Add fine-tuning when:
- The wiki contains stable domain knowledge that changes infrequently
- You want to reduce per-query costs by eliminating retrieval
- You need a domain-specialized model for deployment (edge, offline)
- You have enough quality data (100s-10Ks of examples)

**Recommended approach**: Generate synthetic Q&A pairs from wiki content ([[concepts/synthetic-data-generation]]), then fine-tune with LoRA ([[concepts/parameter-efficient-fine-tuning]]). Consider RAFT ([[concepts/raft]]) for training the model to both know the domain and cite sources.

### When to Add Knowledge Graphs

Add a knowledge graph when:
- You need multi-hop reasoning across entities and relationships
- Temporal tracking of facts is important
- You have complex entity relationships (people, organizations, projects)
- You want structured querying beyond natural language

**Options**: [[entities/microsoft-graphrag]] for graph-enhanced RAG, [[entities/graphiti]] for temporal contexts, or [[sources/gallagher-second-brain-knowledge-graphs]]'s SQLite + ChromaDB approach for personal scale.

---

## Step 8: Measure and Iterate

### Key Metrics

| Metric | How to Measure | Target |
|--------|---------------|--------|
| Article count | `find wiki/ -name "*.md" \| wc -l` | Growing steadily |
| Word count | `find wiki/ -name "*.md" -exec cat {} + \| wc -w` | Growing steadily |
| Link density | Wikilinks per article | >5 average |
| Orphan rate | Articles with 0 incoming links | <10% |
| Freshness | Articles compiled in last 30 days | >80% |
| Query satisfaction | Manual assessment | Improving over time |
| Compilation errors | Health check results | Decreasing over time |

### Iteration Cycle

1. **Weekly**: Ingest new sources, compile, review health check output
2. **Monthly**: Generate coverage report, identify thin topics, plan ingestion
3. **Quarterly**: Review architecture decisions, assess if scaling is needed, refine compilation prompts

---

## Tool Recommendations Summary

| Need | Recommended Tool | Alternative |
|------|-----------------|-------------|
| Viewing | [[entities/obsidian]] | VS Code, Logseq |
| LLM API | Claude (Anthropic) | GPT-4o, Gemini, local via [[entities/ollama]] |
| Web clipping | [[entities/obsidian-web-clipper]] | Markdownload, manual copy |
| PDF conversion | [[entities/markitdown]] | [[entities/docling]], [[entities/pymupdf]] |
| Web scraping | [[entities/firecrawl]] | Playwright, Puppeteer |
| Vector DB (when needed) | [[entities/chromadb]] or [[entities/pgvector]] | [[entities/weaviate]], [[entities/qdrant]] |
| Graph DB (when needed) | [[entities/neo4j]] | SQLite (simple), [[entities/graphiti]] |
| Pipeline orchestration (when needed) | [[entities/apache-airflow]] | ZenML, simple cron |

---

## Quick Start Checklist

- [ ] Create directory structure: `raw/`, `wiki/`, `output/`
- [ ] Install Obsidian and point it at your knowledge base root
- [ ] Choose an LLM API and set up credentials
- [ ] Write your `CLAUDE.md` / `AGENTS.md` with compilation instructions
- [ ] Ingest your first 5-10 high-quality sources into `raw/`
- [ ] Run first compilation pass
- [ ] Review generated wiki articles in Obsidian
- [ ] Run first health check
- [ ] Set up a weekly ingestion and compilation rhythm
- [ ] Resist the urge to manually edit wiki files

---

## Further Reading

- [[sources/karpathy-llm-knowledge-bases]] — the original workflow description
- [[sources/dairai-llm-knowledge-bases-architecture]] — four-phase architecture
- [[sources/antigravity-post-code-ai-workflow]] — use cases and role transformation
- [[sources/pebblous-cheap-ontology]] — historical context and cost analysis
- [[concepts/llm-knowledge-base]] — the core concept article
- [[concepts/wiki-compilation]] — the compilation pipeline
- [[concepts/hallucination-contamination]] — the primary risk to manage
- [[concepts/rag-vs-index-based-retrieval]] — when to add retrieval infrastructure
- [[comparisons/rag-vs-fine-tuning]] — architecture decision framework
- [[comparisons/knowledge-graph-vs-wiki]] — when to add formal structure
- [[comparisons/local-vs-cloud-knowledge-base]] — privacy and cost tradeoffs
