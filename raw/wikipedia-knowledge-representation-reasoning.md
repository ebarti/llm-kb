---
title: "Knowledge Representation and Reasoning"
source: "https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning"
author: "Wikipedia contributors"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [knowledge-representation, AI-history, symbolic-AI, ontology, reasoning]
type: article
status: raw
discovered_via: search
---

# Knowledge Representation and Reasoning

Knowledge representation (KR) aims to model information in a structured manner to formally represent it as knowledge in knowledge-based systems. Knowledge representation and reasoning (KRR) extends this by seeking to understand, reason, and interpret knowledge.

## Historical Evolution

### Early Foundations (1959)
Allen Newell and Herbert A. Simon developed the General Problem Solver (GPS) in 1959, featuring data structures for planning and decomposition. John McCarthy proposed the Advice Taker, suggesting use of predicate calculus for common sense reasoning.

### Graph-Based and Logic Approaches (1960s-1970s)
Early AI systems employed graph representations and semantic networks. John Alan Robinson developed the resolution method. McCarthy and Pat Hayes introduced the situation calculus for causal knowledge. Cordell Green demonstrated how resolution could support robot planning, question-answering, and automatic programming.

### The Logic vs. Procedural Divide (1970s)
MIT researchers rejected uniform proof procedures, advocating procedural knowledge embedding. This was resolved through logic programming and Prolog (Horn clauses as goal-reduction procedures using SLD resolution).

### Expert Systems Era (1970s-1980s)
The cognitive revolution in psychology sparked a knowledge-representation focused phase. This produced expert systems, production systems, and frame languages. AI shifted from general problem-solvers toward domain-specific expertise.

### Frame Theory (Mid-1970s)
Marvin Minsky developed frames — abstract descriptions of categories. Frames proved superior for representing real-world entities with classes, subclasses, slots (data values), and constraints.

### Integration Period (1980s)
Frame communities and rule-based researchers recognized synergies. The 1983 Knowledge Engineering Environment (KEE) from Intellicorp combined rule engines with frame-based knowledge bases. KL-ONE emerged as an influential frame language with rigorous semantics. Loom employed classifiers based on formal logic rather than IF-THEN rules.

### Common-Sense Reasoning Challenge
Doug Lenat's Cyc project tackled common-sense knowledge representation, establishing its own frame language with models of time, causality, physics, and intentions.

### Knowledge Representation Hypothesis (1985)
Brian C. Smith formalized: "Any mechanically embodied intelligent process will be comprised of structural ingredients that we as external observers naturally take to represent a propositional account of the knowledge that the overall process exhibits."

### Semantic Web Era (2000s)
RDF provides basic capability for classes, subclasses, and properties. OWL adds semantics and integrates with classification engines.

## Key Technical Approaches

- Vocabularies and thesaurus structures
- Semantic networks
- Axiom systems
- Frames
- Rules and rule-based systems
- Logic programs
- Ontologies

## Core Characteristics (Brachman, 1985)
1. Primitives (Lisp, semantic networks, frames, rules, FOL)
2. Meta-representation (reflection capabilities)
3. Incompleteness (confidence factors, fuzzy logic)
4. Definitions vs. Facts
5. Non-monotonic Reasoning (truth maintenance systems)
6. Expressive Adequacy
7. Reasoning Efficiency

## Five Roles of KR (Davis, 1993)
1. A surrogate enabling reasoning about the world
2. A set of ontological commitments
3. A fragmentary theory of intelligent reasoning
4. A medium for pragmatically efficient computation
5. A medium of human expression

## Ontology Engineering
Tom Gruber: "Every ontology is a treaty — a social agreement among people with common motive in sharing." Ontologies developed for liquids, electronic circuits, time, belief, and programming. Different ontologies offer distinct worldviews (e.g., MYCIN's rule-based vs. INTERNIST's frame-based approaches).

## Knowledge Extraction
Creates machine-readable knowledge from structured (relational databases, XML) and unstructured (text, documents, images) sources. Projects: DBpedia and Freebase (transforming Wikipedia into structured data).

## Contemporary
Modern machine learning (CNNs, transformers) can be regarded as knowledge representation formalisms. The choice between symbolic, connectionist, and hybrid systems remains debated.
