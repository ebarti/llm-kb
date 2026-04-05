---
marp: true
theme: default
paginate: true
---

# Knowledge Graphs and AI
## From Ontologies to LLM-Powered Graph Intelligence
### Structures, Systems, and Integration Patterns

---

## Agenda

1. Knowledge Graphs: Fundamentals
2. Property Graphs vs RDF
3. Knowledge Graph Embeddings
4. KG + LLM Integration
5. GraphRAG: Microsoft's Breakthrough
6. Temporal Knowledge Graphs
7. KARMA: Multi-Agent KG Enrichment
8. STORM: Automated Wiki Creation
9. Comparison with Wiki-Based Approaches
10. The Hybrid Future

---

## What is a Knowledge Graph?

A **knowledge graph** represents information as:
- **Nodes** (entities): people, concepts, tools, organizations
- **Edges** (relationships): connects, uses, created_by, part_of

**Key advantage**: structured querying and multi-hop reasoning that flat text cannot support.

**Example**: `(Karpathy) --[created]--> (LLM-KB)  --[uses]--> (Obsidian)`

---

## Why Knowledge Graphs Matter for AI

| Capability | Flat Text | Vector DB | Knowledge Graph |
|-----------|-----------|-----------|-----------------|
| Semantic search | No | Yes | Yes |
| Multi-hop reasoning | No | Limited | **Yes** |
| Explainability | No | No | **Yes** |
| Temporal tracking | Manual | No | **Yes** (Graphiti) |
| Aggregate queries | No | No | **Yes** (GraphRAG) |
| Provenance | File-level | Chunk-level | **Triple-level** |

---

## Two Data Models: Property Graphs vs RDF

| Dimension | Property Graph | RDF |
|-----------|---------------|-----|
| Model | Node-centric, rich properties | Edge-centric triples (S-P-O) |
| Identifiers | Database-assigned IDs | URIs (globally unique) |
| Query language | Cypher / Gremlin | SPARQL |
| Schema | Optional, flexible | OWL ontologies |
| Reasoning | Custom logic only | Automated inference (OWL) |
| Performance | Optimized for traversal | Optimized for interoperability |
| Standard | GQL (ISO, emerging) | W3C (mature) |

---

## Property Graphs: Strengths

- **Developer-friendly**: Cypher queries read like English
  ```
  MATCH (p:Person)-[:CREATED]->(t:Tool)
  WHERE t.name = "LLM-KB"
  RETURN p.name
  ```
- **Rich properties** on both nodes and edges
- **Neo4j** dominates: billions of nodes, ACID transactions
- **Best for**: traversal-heavy queries, developer teams, application backends

---

## RDF: Strengths

- **Formal reasoning**: OWL ontology enables automated inference
  - "A Person who likes Food is a FoodLover" -- derived automatically
- **Global interoperability**: URIs enable cross-organization linking
- **Schema validation**: SHACL constraints ensure data quality
- **Standardized**: W3C specs, mature ecosystem
- **Best for**: scientific data, regulatory compliance, cross-org integration

---

## LLM Integration: Bridging Both Models

- LLMs understand OWL well enough to generate SPARQL from ontology descriptions
- GraphRAG research predominantly uses **triple-based representations** (RDF-aligned)
- Property graphs align with **embedding-centric** AI workflows

**Practical hybrid**: OWL ontology defines concepts, property graph stores data, LLM bridges them.

---

## Knowledge Graph Embeddings (KGE)

Map entities and relations to continuous vector spaces:

| Model Family | Approach | Key Models |
|-------------|----------|------------|
| Translation-based | Entities as points, relations as translations | TransE, TransR, RotatE |
| Tensor decomposition | Factorize adjacency tensor | ComplEx, TuckER |
| GNN-based | Message passing on graph structure | R-GCN, CompGCN |

**Training**: corrupt triples (replace head/tail) as negative examples, contrastive loss.

**Use cases**: link prediction, entity classification, KG completion.

---

## KGE vs LLM for Knowledge Tasks

| Task | KGE (TransE, ComplEx) | LLM-Based |
|------|----------------------|-----------|
| Simple link prediction | Strong (F1 ~0.85) | Comparable |
| Multi-hop reasoning | Weak (F1 ~0.61) | **Strong (F1 ~0.98)** |
| Zero-shot new entities | Cannot handle | **Handles via text** |
| Training data needed | Large KG required | Few-shot capable |
| Explainability | Embedding distance | Natural language |

LLMs dominate multi-hop reasoning; KGEs remain efficient for simple structural patterns.

---

## GraphRAG: How It Works

**Microsoft Research (2024)**:

```
Raw Text
    |
    v
LLM Entity/Relation Extraction
    |
    v
Knowledge Graph Construction
    |
    v
Leiden Community Detection (clustering)
    |
    v
Hierarchical Community Summaries
    |
    v
Query -> Local (entity-focused) or Global (theme-level)
```

---

## GraphRAG: Results

**Outperforms baseline RAG on**:
- **Comprehensiveness**: captures cross-document themes
- **Evidence provision**: structured provenance
- **Viewpoint diversity**: community-level perspectives

**Maintains**: similar faithfulness (verified via SelfCheckGPT)

**Key insight**: similarity-based chunk retrieval fundamentally cannot answer "what are the main themes across these 1,000 documents?" -- you need graph structure.

---

## Temporal Knowledge Graphs (TKGs)

Standard KGs represent static facts. TKGs add time:

**Quadruple**: `(Barack Obama, make_statement, Iran, 2014-06-19)`

| Task | Description |
|------|-------------|
| Interpolation | Fill missing past facts |
| Extrapolation | Predict future facts |
| Temporal QA | Answer time-scoped questions |
| Entity alignment | Match entities across time |

---

## TKG Method Categories

| Category | Examples | Approach |
|----------|---------|----------|
| Translation-based | TTransE, HyTE | Temporal hyperplane projection |
| Decomposition | DE-SimplE, TComplEx | Temporal tensor factorization |
| GNN-based | TEA-GNN, TREA | Temporal message passing |
| Autoregressive | RE-NET, RE-GCN | Temporal snapshot sequences |
| Point processes | Know-Evolve, EvoKG | Continuous-time event modeling |
| LLM-based | ICLTKG, GenTKG | Few-shot + RAG for temporal reasoning |

Key datasets: ICEWS14 (90K facts), ICEWS18 (468K), GDELT (2.2M facts).

---

## Graphiti: Temporal Context Graphs

**Open-source framework by Zep AI** -- middle ground between markdown wikis and enterprise KGs:

- **Episodes**: raw provenance (like Karpathy's `raw/` directory)
- **Entities**: nodes with properties
- **Facts/Relationships**: edges with **temporal validity windows**
  - When the fact became true
  - When it was superseded
- **Incremental updates**: no batch recomputation; old facts invalidated, not deleted
- **Hybrid retrieval**: semantic + BM25 + graph traversal

---

## Graphiti: Why Temporal Matters

**Question**: "What was the product roadmap last quarter vs. today?"

| Approach | Can Answer? |
|----------|-----------|
| Static KG | No -- only current state |
| Vector DB | No -- no temporal model |
| Markdown wiki | Partially -- file dates only |
| **Graphiti** | **Yes** -- time-windowed facts |

Critical for AI agents operating in **dynamic, changing environments**.

---

## KARMA: 9-Agent KG Enrichment

**NeurIPS 2025 Spotlight** -- automated KG construction from unstructured text:

| Agent | Role |
|-------|------|
| Entity Discovery | Find new entities in text |
| Relation Extraction | Identify relationships |
| Schema Alignment | Map to existing ontology |
| Conflict Resolution | Resolve contradictions |
| + 5 more | Verification, integration, coordination |

**Results**: 83.1% accuracy, 38,230 new entities from 1,200 PubMed papers, 18.6% conflict reduction.

---

## KARMA Architecture

```
Unstructured Text (PubMed papers)
         |
         v
  +--- 9 Collaborative LLM Agents ---+
  |                                    |
  | Entity Discovery -> Schema Check   |
  | Relation Extraction -> Validation  |
  | Conflict Resolution -> Integration |
  |                                    |
  +------------------------------------+
         |
         v
  Formal Graph Triplets (with schema validation)
```

Formal triplets vs. Karpathy's natural-language markdown -- same pipeline pattern, different output representation.

---

## STORM: Automated Wiki Creation

**Multi-perspective article generation**:

1. **Perspective Discovery**: identify N expert viewpoints from related Wikipedia ToCs
2. **Multi-Turn Conversations**: LLMs simulate expert discussions from each perspective
3. **Outline Synthesis**: merge conversation insights into article structure
4. **Article Generation**: produce Wikipedia-style article with citations

**FreshWiki dataset**: articles after LLM training cutoff (prevents data leakage).

---

## STORM vs Karpathy's LLM-KB

| Dimension | STORM | Karpathy LLM-KB |
|-----------|-------|------------------|
| Mode | Single-shot generation | Persistent accumulation |
| Input | Web search | Curated raw sources |
| Output | One article per run | Growing wiki |
| Persistence | No KB between runs | Cumulative knowledge |
| Perspectives | Multi-perspective simulation | Single LLM compiler |
| Best for | Reference articles | Research compounding |

---

## KG vs Vector DB: When to Use What

| Criterion | Knowledge Graph | Vector Database |
|-----------|----------------|-----------------|
| Multi-hop queries | **Excellent** | Poor |
| Semantic similarity | Moderate | **Excellent** |
| Explainability | **Full provenance** | Opaque similarity |
| Setup complexity | Higher | Lower |
| Update speed | Incremental | Re-embed |
| Scale | Millions of triples | Billions of vectors |

**Recommendation** (Glean, Phyvant): **hybrid architecture** -- use both together.

---

## LLM-Driven KG Construction

The 2025 survey identifies three LLM roles in KG construction:

| Phase | LLM Role | Traditional Approach |
|-------|----------|---------------------|
| Ontology learning | Generate schema from text | Expert manual design |
| Entity/relation extraction | Zero-shot NER + RE | Supervised models |
| KG fusion | Resolve conflicts, merge | Rule-based systems |

LLMs reduce KG construction cost from **months of expert work** to **hours of compute**.

---

## The Cheap Ontology Thesis

**Pebblous** places LLM wikis in 50 years of ontology history:

- 1970s-2000s: enterprise ontologies cost **$10M-$20M**
- 2010s: knowledge graphs (Google, Wikidata) -- still expensive
- 2020s: vector databases -- semantics without structure
- **2026: LLM wikis as "Cheap Ontology"**
  - Markdown + LLM API + natural-language schema
  - Enabled by 1,000-fold context window expansion
  - Data quality (not model scale) is the bottleneck

---

## The Hybrid Future

```
                   Knowledge Graph
                   (structure, reasoning)
                        |
              +---------+---------+
              |                   |
        GraphRAG            Temporal KG
        (holistic queries)  (time tracking)
              |                   |
              +---------+---------+
                        |
                   Hybrid Layer
                        |
              +---------+---------+
              |                   |
        Vector Search       BM25 Search
        (semantic)          (keyword)
              |                   |
              +---------+---------+
                        |
                    LLM Generation
```

---

## Key Takeaways

1. **Knowledge graphs** enable multi-hop reasoning and explainability that vectors cannot
2. **GraphRAG** addresses fundamental limitations of similarity-based retrieval
3. **Temporal KGs** (Graphiti) track evolving knowledge -- critical for dynamic domains
4. **KARMA** shows multi-agent LLM systems can automate KG construction at scale
5. **Property graphs vs RDF**: performance vs reasoning -- choose based on use case
6. **Hybrid architectures** combining KG + vector search are the recommended path
7. **LLM wikis** offer a "cheap ontology" alternative for personal/team scale

---

## References

- Microsoft Research (2024). "GraphRAG: Unlocking LLM Discovery on Narrative Private Data."
- KARMA (NeurIPS 2025). "Multi-Agent LLM Framework for Knowledge Graph Enrichment."
- Graphiti/Zep (2025). "Temporal Context Graphs for AI Agents."
- STORM (2024). "Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking."
- Glean (2025). "Knowledge Graphs vs Vector Databases."
- arXiv (2024). "Survey on Temporal Knowledge Graph Representation Learning."
- arXiv (2025). "LLM-Empowered KG Construction Survey."
