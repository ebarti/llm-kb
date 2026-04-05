---
title: "Source: Taxonomy and Information Architecture for the Semantic Layer"
type: source-summary
source: "[[raw/ek-taxonomy-ia-semantic-layer]]"
related: ["[[concepts/semantic-layer]]", "[[concepts/ontology-and-taxonomy]]", "[[concepts/information-architecture]]", "[[concepts/enterprise-knowledge-management]]"]
last_compiled: 2026-04-05
summary: "Enterprise Knowledge deep-dive on how taxonomy, information architecture, and ontology compose the semantic layer. Semantic layer = standardized abstraction between data repositories and front-end applications. Taxonomy provides controlled vocabulary; IA provides structural design; ontology provides cross-taxonomy relationships. Best practice: govern on W3C SKOS standards."
---

## Key Points

- The semantic layer is the standardized framework that organizes and abstracts organizational data and serves as a connector between repositories and front-end applications
- Taxonomy, IA, and ontology are distinct but deeply interconnected: taxonomy provides controlled vocabulary, IA provides structural design, ontology provides cross-taxonomy relationships
- Not all taxonomy concepts should be visible to users -- IA determines what appears in hierarchies, filters, search suggestions, or hidden matching
- The semantic layer comprises business glossaries, controlled metadata, data catalogs, taxonomies/thesauri, and ontologies/knowledge graphs
- Taxonomies must be governed outside individual system implementations (CMS, DAM, CRM) on open W3C SKOS standards
- Disambiguation is a critical AI preparation: taxonomy provides the context AI needs to distinguish between ambiguous terms

## Detailed Summary

Enterprise Knowledge presents the semantic layer as the integration architecture for enterprise knowledge. The key insight is that a semantic layer is not a single technology but a composition of multiple knowledge organization systems, each playing a distinct role.

The article clarifies the relationship hierarchy: controlled vocabularies standardize terminology, thesauri identify related terms, taxonomies establish hierarchical relationships, ontologies encode cross-taxonomy relationships, and [[concepts/knowledge-graph]] instances capture specific relationship instances. This hierarchy maps directly to the knowledge model continuum described in [[sources/earley-ontology-ia-role-in-ai]].

Information architecture transcends the presentation layer -- it operates across all information management levels, determining not just how information is displayed but how it is organized, labeled, searched, and navigated throughout the enterprise.

## Related Concepts

- [[concepts/semantic-layer]] -- primary topic of the article
- [[concepts/ontology-and-taxonomy]] -- the building blocks of the semantic layer
- [[concepts/information-architecture]] -- the structural design discipline
- [[concepts/enterprise-search]] -- semantic layers enable unified search across disparate sources
- [[concepts/knowledge-graph]] -- the most specific level of knowledge organization
