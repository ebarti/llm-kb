---
title: "Source: The Semantic Web (Wikipedia)"
type: source-summary
source: "[[raw/wikipedia-semantic-web]]"
related: ["[[concepts/semantic-web]]", "[[concepts/ontology]]", "[[concepts/knowledge-representation]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "History and architecture of the Semantic Web: Tim Berners-Lee's vision for machine-readable data on the web, implemented through RDF, OWL, SPARQL, and linked data — plus its challenges with vastness, vagueness, and adoption."
---

## Key Points
- Tim Berners-Lee's vision (1994-1998): extending the web to make data machine-readable
- Core stack: RDF (1999) -> RDFS -> OWL (2004/2009) -> SPARQL
- RDF uses subject-predicate-object triples; OWL adds class logic and inference
- Linked Data principles: URLs point to data, accessing them returns data, relationships link to more
- Five challenges: vastness, vagueness, uncertainty, inconsistency, deceit
- Greater adoption in specialized corporate settings than on the public web

## Detailed Summary

The [[concepts/semantic-web]] represents AI's [[concepts/knowledge-representation]] tradition exported to the World Wide Web. Berners-Lee's core idea was that computers should process not just documents but structured data with semantic meaning.

The technology stack forms a "layer cake": XML provides syntax, RDF provides data modeling through subject-predicate-object triples, RDFS adds vocabulary for properties and classes, OWL adds formal logic (disjointness, cardinality, equality), and SPARQL provides querying.

OWL's lineage traces through AI's KR history: from frame-based languages through SHOE (HTML), XOL/OIL (XML), to DAML+OIL (2001 EU/US collaboration), and finally OWL (W3C Recommendation 2004, OWL 2 in 2009).

Berners-Lee's "Giant Global Graph" concept envisioned linked data as a distributed database rather than a file system. By 2013, over 4 million web domains contained semantic markup.

But the vision faced fundamental challenges. Marshall and Shipman (2003) noted the cognitive overhead of formalization exceeds traditional authoring. Cory Doctorow's "metacrap" critique pointed out humans will game any metadata system. The brittleness of inference chains contrasted unfavorably with the robustness of statistical search engines.

Notable implementations include DBpedia, Wikidata, and OpenAlex for scholarly papers. Enterprise adoption (SAP, Oracle) proved more successful than general web adoption.

## Related Concepts
- [[concepts/semantic-web]] — the central topic
- [[concepts/ontology]] — the knowledge engineering discipline underlying the Semantic Web
- [[concepts/knowledge-graph]] — the successor/complement to Semantic Web approaches
- [[concepts/knowledge-representation]] — the AI tradition the Semantic Web draws from
- [[concepts/cheap-ontology]] — LLM-era approach that bypasses formal ontology engineering
