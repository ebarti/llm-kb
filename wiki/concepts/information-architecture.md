---
title: "Information Architecture"
type: concept
sources: ["[[sources/ek-taxonomy-ia-semantic-layer]]", "[[sources/earley-ontology-ia-role-in-ai]]"]
related: ["[[concepts/semantic-layer]]", "[[concepts/ontology-and-taxonomy]]", "[[concepts/enterprise-knowledge-management]]", "[[concepts/enterprise-search]]"]
last_compiled: 2026-04-05
summary: "The structural design of shared information environments -- organization, labeling, search, and navigation systems. IA operates across all information management levels (not just presentation), determining how taxonomies and ontologies are applied to user experience. Critical for enterprise knowledge scaling: determines what knowledge is visible, findable, and navigable."
---

## Overview

Information Architecture (IA) is "the structural design of shared information environments" encompassing organization, labeling, search, and navigation systems. It determines how information is organized, labeled, searched, and navigated throughout an enterprise.

IA is not merely a presentation-layer concern. Per [[sources/ek-taxonomy-ia-semantic-layer]], it operates across all information management levels, providing structural context for the entire [[concepts/semantic-layer]] implementation. It determines which [[concepts/ontology-and-taxonomy]] concepts appear in hierarchies, filters, search suggestions, or remain as hidden matching criteria.

## Multi-Layered Function

IA operates at multiple levels within enterprise knowledge systems:

1. **Structural Context**: Illustrates the overarching design of the [[concepts/semantic-layer]] -- how different knowledge organization systems relate to each other
2. **Linking Function**: Connects content and data through shared metadata and knowledge organization systems
3. **Application Layer**: Implements systems in front-end applications serving user information needs (navigation, search, browse)

## Relationship to Adjacent Disciplines

Per [[sources/ek-taxonomy-ia-semantic-layer]]:
- IA has closer relationships with design, user experience, sociology, and psychology
- Taxonomy has closer relationships with indexing/tagging, NLP, ontologies, Semantic Web, and knowledge management
- Both are essential and complementary: taxonomy provides the vocabulary; IA provides the structure

## Enterprise Application

In [[concepts/enterprise-knowledge-management]], IA determines:
- How knowledge bases are organized (flat vs. hierarchical vs. network)
- How navigation systems expose content (breadcrumbs, faceted search, related items)
- How search results are ranked and presented
- How different user roles experience the same knowledge repository
- How new content is categorized and surfaced

Good IA is invisible when working and painfully obvious when missing. It is the primary determinant of whether users can actually find what they need in an [[concepts/enterprise-search]] system, regardless of how sophisticated the underlying AI is.

## Sources

- [[sources/ek-taxonomy-ia-semantic-layer]] -- IA's role in semantic layer architecture
- [[sources/earley-ontology-ia-role-in-ai]] -- IA powered by ontologies for AI systems

## Related Concepts

- [[concepts/semantic-layer]] -- IA provides the structural context for semantic layers
- [[concepts/ontology-and-taxonomy]] -- the knowledge structures IA organizes and applies
- [[concepts/enterprise-knowledge-management]] -- the organizational discipline IA serves
- [[concepts/enterprise-search]] -- IA determines search experience quality
