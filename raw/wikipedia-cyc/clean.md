---
title: "Cyc Knowledge Base Project"
source: "https://en.wikipedia.org/wiki/Cyc"
author: "Wikipedia contributors"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [cyc, knowledge-base, common-sense, ontology, Doug-Lenat, symbolic-AI]
type: article
status: raw
discovered_via: search
---

# Cyc Knowledge Base Project

Cyc (from "encyclopedia") is a long-term AI project aiming to assemble a comprehensive ontology and knowledge base capturing fundamental concepts and rules about how the world works, with emphasis on implicit common sense knowledge.

## History

### Origins
Started July 1984 by Douglas Lenat at MCC (Microelectronics and Computer Technology Corporation), formed to counter the Japanese "fifth-generation" computing project. Cycorp, Inc. took over in January 1995 with Lenat as CEO.

### Technical Evolution
CycL evolved from RLL (Representation Language Language), developed by Lenat and Russell Greiner at Stanford (1979-1980). By 1989, CycL expanded to encompass higher-order logic.

### Scale
- 1994: ~100,000 terms, ~1 million assertions
- 2002: $60 million invested, 600 person-years of effort
- 2017: ~1.5 million terms, 24.5 million assertions, 2,000 person-years total
- 2008: Resources mapped to Wikipedia articles
- Over 1,000 specialized inference engines

## Technical Architecture

### Knowledge Representation
- Microtheories: each internally consistent, can hold contradictions across theories
- CycL terminology: individual constants (#$BillClinton), collections, functions, truth functions
- Frames (units) with slots containing property values
- Global ontology with "ontological engineers" manually extracting tacit knowledge

### Inference Engine
Performs logical deduction, inductive reasoning, statistical machine learning, symbolic learning, and abductive reasoning. Community-of-agents architecture where specialized modules gain priority based on problem-solving progress.

## Software Releases
- OpenCyc (2002): 6,000 concepts, 60,000 facts; Apache License
- OpenCyc 4.0 (2012): 239,000 concepts, 2.09 million assertions
- OpenCyc shutdown (2017): "fragmenting confusion" concerns
- ResearchCyc (2006): Free for researchers, includes lexicons, parsing tools

## Applications
- GlaxoSmithKline (2001): Biomedical research
- Cleveland Clinic (2007): Query interface reducing research time from months to hours
- Terrorism Knowledge Base (2004-2008): Logic-based intelligence analysis
- CycSecure (2002): Network vulnerability assessment at U.S. STRATCOM
- MathCraft: Sixth-grade mathematics education

## Critical Reception
Pedro Domingos: "catastrophic failure" — unending data requirements.
Gary Marcus: Different approach from deep learning; aligned with Lenat's principle "Sometimes the veneer of intelligence is not enough."
Described as "one of the most controversial endeavors of artificial intelligence history."

## Legacy
Doug Lenat (1950-2023) continued as Cycorp CEO until death from bile duct cancer.
His final paper proposed complementary synergies: LLMs possess fluency and breadth but lack consistency; Cyc offers auditable reasoning chains without LLMs' natural language facility. Integrated system might combine strengths.

In 1989, Lenat and R.V. Guha predicted "by 1999 no one would even think about having a computer that doesn't have Cyc running on it." This prediction proved spectacularly wrong.
