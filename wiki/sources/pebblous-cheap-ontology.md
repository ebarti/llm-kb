---
title: "Source: LLMs That Compile Knowledge: The Karpathy Methodology and the Democratization of Ontology"
type: source-summary
source: "[[raw/pebblous-cheap-ontology]]"
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/cheap-ontology]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/hallucination-contamination]]", "[[concepts/data-quality-bottleneck]]"]
last_compiled: 2026-04-05
summary: "Deep analysis placing Karpathy's markdown wiki within 50 years of ontology history, quantifying the RAG vs. fine-tuning vs. LLM-KB tradeoffs, and identifying data quality as the decisive bottleneck."
---

## Key Points
- Traditional enterprise knowledge graphs: $10M–$20M upfront, 27% reach production — Karpathy's approach is "Cheap Ontology"
- Three-layer architecture: **raw/** (immutable) → **wiki/** (LLM-maintained) → **schema** (CLAUDE.md/AGENTS.md)
- Context windows expanded 1,000-fold in 5 years (GPT-3 2K → Gemini 2.0 Pro 2M tokens) — enabling full-wiki loading
- RAG accuracy: 87.5%; fine-tuning accuracy on new facts: only 50.4%; Karpathy = wiki-quality dependent
- Data quality > model scale (Microsoft phi-1 study); low-quality raw → contaminated wiki → flawed fine-tuning
- Knowledge graph market: $1.07B (2024) → $6.94B (2030) at 36.6% CAGR
- McKinsey: employees spend 1.8 hours/day (25% of workday) searching for information

## Detailed Summary

Pebblous provides the most historically grounded analysis, tracing the lineage from 1970s formal ontologies through Semantic Web (RDF/OWL/SPARQL), to Google-scale knowledge graphs, to LLM wikis. The key insight: context windows expanding 1,000-fold in five years made it feasible to load an entire personal wiki into a single LLM prompt, eliminating the need for vector database retrieval at personal scale.

The "Cheap Ontology" framing is particularly useful: what required $10–20M, specialized ontology engineers, and years of schema design now costs only API fees and takes days to prototype. The CLAUDE.md or AGENTS.md file replaces formal ontology axioms with natural-language rules.

The comparative table (RAG vs. fine-tuning vs. Karpathy) is quantitative and valuable: fine-tuning achieves only 50.4% accuracy on new facts (vs. RAG's 87.5%), making it a poor choice for knowledge that changes. Karpathy's approach offers a unique advantage: compounding knowledge via the filing loop, which neither RAG nor fine-tuning supports.

The article identifies data quality — not model capability — as the decisive bottleneck. Low-quality raw inputs cascade into contaminated wiki, then into polluted fine-tuning datasets.

## Notable Quotes
> "The bottleneck shifts from technical capability to data quality."
> "Every organization maintains raw directories of meeting notes, emails, and documents in uncompiled state."

## Related Concepts
- [[concepts/cheap-ontology]] — the core framing
- [[concepts/data-quality-bottleneck]] — critical vulnerability
- [[concepts/rag-vs-index-based-retrieval]] — quantitative comparison
- [[concepts/hallucination-contamination]] — cascading risk
- [[concepts/llm-knowledge-base]] — the methodology
