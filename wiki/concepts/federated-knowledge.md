---
title: "Federated Knowledge"
type: concept
sources: ["[[sources/federated-wiki-cunningham]]", "[[sources/knowledge-commons-overview]]"]
related: ["[[concepts/wikipedia-knowledge-model]]", "[[concepts/collaborative-knowledge-building]]", "[[concepts/knowledge-graph]]", "[[concepts/knowledge-commons]]"]
last_compiled: 2026-04-05
summary: "Distributed knowledge architectures where independent nodes maintain their own knowledge while sharing across a network — from Cunningham's Federated Wiki ('chorus of voices') to Wikibase's federated knowledge graphs with underlays, overlays, and interlace."
---

## Overview

Federated knowledge systems distribute knowledge creation and authority across independent nodes that share information through a network, rather than centralizing it in a single canonical source. This contrasts with the [[concepts/wikipedia-knowledge-model]] (one article per topic, consensus-driven) and with [[concepts/llm-knowledge-base]] (one LLM compiles all sources).

Two major implementations exist: **Federated Wiki** (Ward Cunningham's forking-based system preserving multiple perspectives) and **Wikibase federation** (the Wikimedia Foundation's structured data sharing between independent instances).

## Key Ideas

### Federated Wiki: A Chorus of Voices

[[entities/ward-cunningham]], inventor of the original wiki, created Federated Wiki as a response to what he saw as a limitation of consensus-based wikis. Instead of converging on a single "truth," Federated Wiki allows users to **fork** any page, maintaining their own copies and modifications. Multiple versions of the same topic coexist — what Cunningham calls "a chorus of voices."

Key principles:
- **Forking over consensus**: Disagreement preserved rather than resolved
- **Individual authority**: Each wiki instance is self-governed
- **Cross-pollination**: Content flows across instances through forking
- **No central editorial control**: Distributed by design

### Wikibase Federation: Structured Data Sharing

The Wikimedia ecosystem's approach to federation focuses on structured data. Wikibase instances (including [[entities/wikidata]]) share information through:
- **Federated statements**: A local instance references data on a remote instance, treating it as authoritative
- **Entity matching**: Linking equivalent entities across instances
- **Federated SPARQL queries**: Queries spanning multiple instances simultaneously

### The Three-Layer Architecture

The Wikimedia federated knowledge vision defines three layers:
1. **Underlays**: Grounding layers of observations and primary source data — building blocks for other layers
2. **Overlays**: Experiential lenses for understanding subsets of information as contextual knowledge, with transparent provenance
3. **Interlace**: The connective matrix linking ideas, discoveries, and knowledge projects

This architecture offers a middle path between Wikipedia's enforced consensus and Federated Wiki's unconstrained plurality: structured sharing with distributed authority.

### Tradeoffs

| Dimension | Centralized (Wikipedia) | Federated (Cunningham) | Federated Structured (Wikibase) |
|-----------|------------------------|----------------------|-------------------------------|
| Authority | Consensus | Individual | Instance-level |
| Perspective | Neutral POV | Multi-POV | Schema-governed |
| Discoverability | High (single source) | Low (distributed) | Medium (SPARQL federation) |
| Consistency | Enforced | Emergent | Schema-constrained |
| Scalability | Bottleneck at consensus | Unlimited | Infrastructure-limited |

## Relevance to AI

Federated knowledge architectures are natural partners for AI systems:
- AI agents can traverse federated graphs more efficiently than humans
- Federation prevents the single-point-of-failure that AI content pollution creates in centralized systems
- Multi-perspective preservation aligns with emerging AI alignment approaches (diverse viewpoints as input to value learning)
- Wikibase federation provides structured training data with provenance — addressing the [[concepts/knowledge-commons]] crisis of unattributed AI training

## Sources

- [[sources/federated-wiki-cunningham]] — Cunningham's vision and implementation
- [[sources/knowledge-commons-overview]] — institutional governance context

## Related Concepts

- [[concepts/wikipedia-knowledge-model]] — the centralized model federation responds to
- [[concepts/collaborative-knowledge-building]] — the process federation implements
- [[concepts/knowledge-graph]] — structured knowledge representation federation enables
- [[concepts/knowledge-commons]] — governance framework for federated resources
