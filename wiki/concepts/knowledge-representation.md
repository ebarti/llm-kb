---
title: "Knowledge Representation"
type: concept
sources: ["[[sources/wikipedia-knowledge-representation-reasoning]]", "[[sources/wikipedia-symbolic-ai]]", "[[sources/wikipedia-expert-systems]]", "[[sources/wikipedia-cyc]]", "[[sources/wikipedia-semantic-web]]", "[[sources/llm-enhanced-knowledge-representation-survey]]", "[[sources/llms-as-reliable-knowledge-bases]]", "[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/symbolic-ai]]", "[[concepts/expert-systems]]", "[[concepts/ontology]]", "[[concepts/semantic-web]]", "[[concepts/knowledge-graph]]", "[[concepts/neural-symbolic-integration]]", "[[concepts/llms-as-knowledge-bases]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "The AI discipline of encoding information so machines can reason over it — spanning 65+ years from logic and frames through expert systems, ontologies, and knowledge graphs to modern LLM-based implicit representations."
---

## Overview

Knowledge representation (KR) is one of AI's foundational subfields, concerned with how to encode information about the world so that computer systems can use it for reasoning, problem-solving, and decision-making. The field's 65-year history is a story of recurring tensions: expressiveness vs. tractability, breadth vs. depth, manual encoding vs. automated learning, and symbolic precision vs. statistical approximation.

The history of KR provides the essential context for understanding modern [[concepts/llm-knowledge-base]] systems. Every approach tried in this history — from frames to production rules to ontologies to knowledge graphs — represents a different answer to the same question Karpathy's system answers with "markdown files + LLM intelligence."

## Historical Timeline

### 1945-1959: Precursors
- [[entities/vannevar-bush]]'s [[concepts/memex]] (1945): Associative indexing as an alternative to hierarchical classification
- [[entities/douglas-engelbart]]'s "Augmenting Human Intellect" (1962): Computing as knowledge amplification
- Newell & Simon's General Problem Solver (1959): First AI data structures for knowledge
- [[entities/john-mccarthy]]'s Advice Taker (1959): Predicate calculus for common-sense reasoning

### 1960s-1970s: Foundations
- Semantic networks (Quillian, 1966): Graph-based concept relationships
- [[entities/ted-nelson]] coins "hypertext" (1965): Nonsequential knowledge linking
- Resolution theorem proving (Robinson): Automated logical inference
- Situation calculus (McCarthy & Hayes): Representing change and causation
- Logic programming / Prolog: Unifying logic and computation
- [[entities/marvin-minsky]]'s frames (mid-1970s): Stereotypical situations with slots and inheritance
- Roger Schank's scripts: Capturing common routines (e.g., dining out)

### 1980s: Expert Systems Era
- Production rules (if-then): [[concepts/expert-systems]] like MYCIN, XCON, DENDRAL
- [[entities/edward-feigenbaum]]'s insight: "In the knowledge lies the power"
- KL-ONE and description logics: Rigorous frame semantics
- KEE (Intellicorp, 1983): Integrated frames + rules + inference
- [[entities/cyc-project]] begins (1984): Most ambitious KR effort ever attempted

### 1990s-2000s: Formal Ontologies and the Web
- [[concepts/ontology]] engineering: Modular, reusable knowledge bases
- [[concepts/semantic-web]]: RDF (1999), OWL (2004), SPARQL — KR exported to the web
- Tom Gruber: "Every ontology is a treaty"
- DBpedia, Freebase, Wikidata: Large-scale knowledge extraction from Wikipedia

### 2010s-2020s: Neural and Hybrid Era
- Knowledge graph embeddings: TransE (2013) projects entities and relations into vector spaces
- [[concepts/neural-symbolic-integration]]: Six architectures combining symbolic and neural KR
- LLMs as implicit knowledge bases: Parametric knowledge stored probabilistically in weights
- LLM-enhanced KRL: BERT/GPT models enriching knowledge graph representations
- [[concepts/llm-knowledge-base]]: Markdown + LLM as a new KR paradigm

## Key Approaches

| Approach | Era | Strengths | Weaknesses |
|----------|-----|-----------|------------|
| Logic (FOL, Prolog) | 1960s-present | Precise, provable | Brittle, hard to scale |
| Semantic networks | 1960s-present | Intuitive graph structure | Vague semantics |
| Frames | 1970s-1990s | Rich structure, inheritance | Limited reasoning |
| Production rules | 1970s-1990s | Explainable, modular | Knowledge acquisition bottleneck |
| Ontologies (OWL) | 1990s-present | Formal, shareable | High cognitive overhead |
| Knowledge graphs | 2010s-present | Flexible, queryable | Expensive to build and maintain |
| Neural embeddings | 2010s-present | Learnable, scalable | Opaque, hallucination-prone |
| LLM parametric knowledge | 2020s-present | Vast coverage, natural language | Inconsistent, stale, unauditable |
| LLM + structured KB | 2020s-present | Combines strengths | Complexity, still maturing |

## The Central Tension

Every KR system navigates the same fundamental trade-off articulated by Ron Brachman (1985): **expressiveness vs. tractability**. First-order logic is maximally expressive but computationally intractable at scale. Production rules are efficient but limited. Ontologies try to find a sweet spot. Neural representations sidestep the trade-off by learning representations that are efficient but opaque.

Randall Davis's insight (1993) that KR serves five roles — surrogate, ontological commitment, reasoning theory, computational medium, and human expression — remains the best framework for evaluating any KR system, including modern LLM-based approaches.

## Connection to Modern LLM Knowledge Bases

The [[concepts/llm-knowledge-base]] approach (Karpathy's markdown wiki system) represents a novel position in the KR design space:
- **Representation**: Natural language in markdown files (human-readable, LLM-processable)
- **Reasoning**: LLM inference over index files and full articles
- **Ontological commitment**: Emergent from compilation rather than pre-specified
- **Tractability**: Bounded by context window rather than logical complexity
- **Knowledge acquisition**: Automated via web search + LLM extraction (solving the bottleneck that killed [[concepts/expert-systems]])

This approach echoes [[concepts/cheap-ontology]] — achieving 80% of formal ontology's value at 1% of the cost.

## Sources
- [[sources/wikipedia-knowledge-representation-reasoning]] — comprehensive KR&R overview
- [[sources/wikipedia-symbolic-ai]] — the paradigm KR belongs to
- [[sources/wikipedia-expert-systems]] — the commercial application of KR
- [[sources/llm-enhanced-knowledge-representation-survey]] — how LLMs enhance KG embeddings
- [[sources/llms-as-reliable-knowledge-bases]] — evaluation of LLMs as KBs
- [[sources/pebblous-cheap-ontology]] — placing KR in the context of LLM-era ontology

## Related Concepts
- [[concepts/symbolic-ai]] — the paradigm KR belongs to
- [[concepts/expert-systems]] — 1980s commercial application
- [[concepts/ontology]] — formal KR for the web era
- [[concepts/semantic-web]] — KR exported to the web
- [[concepts/knowledge-graph]] — modern graph-based KR
- [[concepts/neural-symbolic-integration]] — bridging symbolic KR and neural approaches
- [[concepts/llms-as-knowledge-bases]] — LLMs as implicit KR systems
- [[concepts/llm-knowledge-base]] — the hybrid approach this KB implements
- [[concepts/cheap-ontology]] — LLM-era democratization of KR
