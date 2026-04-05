---
marp: true
theme: kb-theme
paginate: true
header: "LLM Knowledge Base"
footer: "Generated 2026-04-05"
---

<!-- _class: title -->

# LLM Knowledge Bases
## How LLMs Author and Maintain Personal Wikis

Compiled from 11 sources | 20 concepts | April 2026

---

## What Is an LLM Knowledge Base?

A system where **source documents are ingested** into a raw directory and an **LLM incrementally compiles** them into a structured wiki of markdown files.

The human owner interacts only through natural language prompts -- the LLM writes, updates, and maintains all wiki content directly.

> Pioneered by **Andrej Karpathy** (April 2026) and analyzed by DAIR.AI, Glen Rhodes, Antigravity Codes, and Pebblous.

---

## The Core Architecture

```
raw/          <-- ingested source documents (source of truth)
wiki/         <-- LLM-compiled and maintained
  _index.md   <-- master article index
  _meta/      <-- summaries, link graph, manifest
  sources/    <-- per-source summary articles
  concepts/   <-- cross-source concept articles
  entities/   <-- tool/person/org profiles
output/       <-- reports, slides, images (filed back into wiki)
```

All content authored by the LLM. Humans curate inputs and ask questions.

---

## The Four-Phase Operational Cycle

<div class="columns">
<div>

### 1. Ingest
- Raw documents dropped into `raw/`
- URLs fetched and converted to markdown
- No preprocessing by humans

### 2. Compile
- LLM reads manifest for new files
- Creates source summaries
- Synthesizes cross-source concept articles
- Rebuilds index and metadata

</div>
<div>

### 3. Query
- LLM reads `summaries.md` to find relevant articles
- Navigates to full articles for detailed answers
- No vector database needed at small scale

### 4. Maintain
- Linting checks for contradictions
- Broken link detection
- Orphan article identification
- New content suggestions

</div>
</div>

---

<!-- _class: divider -->

# Key Concepts
## The ideas that make this work

---

## Cheap Ontology

Traditional enterprise knowledge graphs cost **$10M-$20M** with ontology engineers at $107K-$207K/year -- and only 27% reach production.

Karpathy's approach: **API costs only**, setup in days, no specialized expertise.

<div class="columns">
<div>

### What Gets Replaced
- RDF/OWL/SPARQL --> markdown + wikilinks
- Schema axioms --> CLAUDE.md instructions
- Ontology engineers --> system prompts
- Formal reasoners --> LLM health checks

</div>
<div>

### The Enabler
Context windows grew **1,000x** in 5 years:
- GPT-3: 2K tokens
- Gemini 2.0 Pro: 2M tokens

Entire wikis now fit in context.

</div>
</div>

---

## Self-Reinforcing Knowledge Loop

The knowledge base **compounds over time**:

1. New sources ingested --> new articles compiled
2. Questions asked --> answers generated --> filed back
3. Reports, slides, comparisons --> become queryable content
4. Each query can trigger new article creation

> Glen Rhodes calls this the **"filing loop"** -- query results compound the KB over time, making each subsequent query richer.

---

## Markdown as Universal Interface

Why markdown is the optimal knowledge substrate:

- **Human-readable**: No special tools needed to read or edit
- **LLM-friendly**: Native to every model's training data
- **Version-controllable**: Git tracks every change
- **Tool-agnostic**: Works in Obsidian, VS Code, any text editor
- **Future-proof**: Plain text outlasts every proprietary format
- **Cross-linkable**: Wikilinks create a navigable knowledge graph

---

## Obsidian as IDE

Obsidian serves as a **read-only viewing frontend** for the LLM-maintained wiki:

- Graph view visualizes the knowledge structure
- Canvas files create spatial layouts
- Search works across all articles
- Backlinks show concept relationships
- Marp plugin renders presentations (like this one)

The LLM is the author. Obsidian is the viewer.

---

<!-- _class: divider -->

# Retrieval Without RAG
## Why simple indexing works

---

## Index-Based Retrieval

At **~100 articles and ~400K words**, LLM-maintained index files and one-line summaries replace vector database RAG.

| Dimension | Index-Based | RAG | Finetuning |
|-----------|-------------|-----|------------|
| Infrastructure | Minimal | Vector DB required | Training pipeline |
| Scale | Small-medium | Large | Very large |
| Freshness | Immediate | Re-embed on update | Retrain to update |
| Accuracy | High (full articles) | Depends on chunk quality | Baked into weights |

The LLM reads `summaries.md`, identifies relevant articles, and reads them in full. Not approximate -- exact reasoning over a compact index.

---

<!-- _class: divider -->

# Risks & Mitigations
## What can go wrong

---

## Hallucination Contamination

The primary systemic risk: **LLM-generated errors propagate and compound**.

<div class="columns">
<div>

### The Cascade
1. LLM hallucinates a fact during compilation
2. Error written into a wiki article
3. Future queries reference the error
4. Fine-tuning bakes it into weights **permanently**

</div>
<div>

### Mitigations
- **Vault separation** (Steph Ango): separate AI-generated from human-curated
- **Provenance tracing**: all claims trace to `raw/` sources
- **LLM linting**: periodic scan for contradictions
- **Quality gates**: validate raw inputs before ingestion

</div>
</div>

---

## The Data Quality Bottleneck

**Data quality > model scale** in LLM-KB pipelines.

Low-quality raw inputs cascade:
- Bad source --> bad summary --> bad concept article --> bad fine-tuning data

The fix is upstream: curate inputs carefully, validate before ingestion, and maintain provenance chains.

---

<!-- _class: divider -->

# The Broader Landscape
## Alternative approaches

---

## Approaches Compared

| Approach | Example | Strength | Weakness |
|----------|---------|----------|----------|
| Markdown wiki | Karpathy | Simple, auditable, cheap | Scale ceiling ~400 articles |
| Knowledge graph | KARMA, Graphiti | Formal reasoning, temporal | Expensive, complex |
| Production RAG | Decoding AI | Scales to millions | Less auditable, infra-heavy |
| Auto-wiki | STORM | Single-shot articles | No accumulation over time |
| Second brain | Gallagher Kit | Task/relationship tracking | SQLite + ChromaDB overhead |

---

## Multi-Agent Systems in Knowledge Management

<div class="columns">
<div>

### KARMA (NeurIPS 2025)
- 9 collaborative LLM agents
- Automated knowledge graph enrichment
- 83.1% accuracy
- 38,230 new entities from 1,200 PubMed papers

</div>
<div>

### STORM
- Multi-perspective question-asking
- Retrieval-augmented article creation
- Wikipedia-style output
- Single-shot vs. Karpathy's accumulating model

</div>
</div>

---

## The Product Gap

Karpathy acknowledges this is **"hacky scripts"** -- not a product.

<div class="callout info">

**Market opportunity**: The gap between technical workflow and polished product sits in a **$62B enterprise knowledge management** sector. Non-technical users need accessible LLM-KB tooling.

</div>

The shift is from **code generation to knowledge compilation** -- "manipulating knowledge, not code" as the next developer competitive advantage.

---

## This Wiki: A Living Example

This knowledge base is itself an LLM-maintained wiki:

- **11 sources** ingested and compiled
- **20 concept articles** synthesized across sources
- **9 entity profiles** for tools, people, and frameworks
- **Full cross-linking** with backlink graph
- **Generated outputs**: status reports, comparisons, and these slides

All compiled by an LLM from raw source documents. All viewable in Obsidian.

---

<!-- _class: end -->

# LLM Knowledge Bases

The future of personal knowledge management is LLM-authored.

LLM Knowledge Base | April 2026
