---
title: "The Semantic Web"
source: "https://en.wikipedia.org/wiki/Semantic_Web"
author: "Wikipedia contributors"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [semantic-web, RDF, OWL, knowledge-representation, Tim-Berners-Lee, ontology]
type: article
status: raw
discovered_via: search
---

# The Semantic Web

The Semantic Web (also called Web 3.0) extends the World Wide Web through W3C standards to make Internet data machine-readable. Tim Berners-Lee: "a web of data that can be processed directly and indirectly by machines."

## History
- Early 1960s: Semantic network concept emerged (Allan M. Collins, Ross Quillian, Elizabeth F. Loftus)
- 1994: Berners-Lee discussed semantic web needs at International WWW Conference
- 1998: Published "Semantic Web Road Map"
- 1999: Berners-Lee's vision of "intelligent agents" handling trade and bureaucracy
- 2001: First semantic web patent (Amit Sheth et al.)
- 2013: Over 4 million web domains contained semantic markup

## Core Technologies

### RDF (Resource Description Framework)
Subject-predicate-object triples for describing information. Represents arbitrary entities. W3C Recommendation 1999, revised 2004.

### OWL (Web Ontology Language)
Extends RDF vocabulary: disjointness, cardinality, equality, property characteristics. OWL 2 became W3C Recommendation October 2009. Evolution: SHOE (HTML) -> XOL/OIL (XML) -> DAML+OIL (2001 EU/US merger) -> OWL.

### SPARQL
Protocol and query language for semantic web data sources.

### Other Standards
- RDFS: Extends RDF for properties and classes
- Turtle/N3: Human-readable RDF serialization
- JSON-LD: JSON-based linked data
- RIF: Rule Interchange Format
- SKOS: Simple Knowledge Organization System

## Semantic Web Stack (Layer Cake)
XML/XML Schema -> RDF -> RDFS -> OWL -> SPARQL -> Unifying Logic -> Proof (still under development)

## Linked Data
Berners-Lee's "Giant Global Graph." Principles: URLs point to data; accessing URLs returns data; relationships point to additional URLs.

## Knowledge Representation
Formal descriptions of concepts, terms, and relationships within knowledge domains through ontologies. Embedded semantics enable reasoning over data and operating with heterogeneous sources.

## Challenges
1. Vastness: Billions of pages, massive ontologies (SNOMED CT: 370,000 class names)
2. Vagueness: Imprecise concepts need fuzzy logic
3. Uncertainty: Precise concepts with uncertain values need probabilistic reasoning
4. Inconsistency: Logical contradictions in large ontologies
5. Deceit: Intentional misinformation

## Criticisms
- Marshall and Shipman (2003): Cognitive overhead of formalizing knowledge
- Brittleness of inference chains vs. robustness of search engines
- Cory Doctorow's "metacrap" critique: humans include spurious metadata
- Privacy/censorship concerns: automated content blocking
- Double effort problem (both human-readable and machine-readable)

## Applications
- DBpedia, Wikidata, Scholia, OpenAlex
- Kialo (collaborative structured argument mapping)
- SAP, Oracle business intelligence integration

## Status
Tim O'Reilly: semantic web transforms web from distributed file system to distributed database. Specialized corporate implementations show greater adoption than general public web.
