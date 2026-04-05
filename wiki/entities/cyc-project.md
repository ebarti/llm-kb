---
title: "Cyc Project"
type: entity
entity_type: tool
sources: ["[[sources/wikipedia-cyc]]", "[[sources/outsiderart-cyc-forgotten-ai]]"]
related: ["[[entities/doug-lenat]]", "[[concepts/knowledge-representation]]", "[[concepts/symbolic-ai]]", "[[concepts/ontology]]", "[[concepts/neural-symbolic-integration]]", "[[concepts/cheap-ontology]]"]
last_compiled: 2026-04-05
summary: "AI's most ambitious knowledge engineering project (1984-present): 40 years encoding common-sense knowledge into 1.5M terms and 24.5M assertions in CycL — a cautionary tale and proof of concept for explicit knowledge representation."
---

## Overview

Cyc (from "encyclopedia") is the longest-running and most ambitious knowledge engineering project in AI history. Started in 1984 by [[entities/doug-lenat]] at MCC and continued by Cycorp, Inc., Cyc aims to encode the common-sense knowledge humans take for granted — facts about time, causality, physics, social interactions, and intentions that are obvious to humans but invisible to machines.

## Scale

| Metric | Value |
|--------|-------|
| Start date | July 1984 |
| Investment | $60M+ by 2002 |
| Person-years | ~2,000 by 2017 |
| Terms/concepts | ~1.5 million |
| Assertions/rules | ~24.5 million |
| Inference engines | 1,000+ specialized |
| Staff (current) | ~50 |

## Technical Architecture

### CycL
The knowledge representation language, evolved from RLL (1979). Supports higher-order logic (since 1989). Uses:
- Individual constants (#$BillClinton, #$Dog)
- Collections with membership
- Functions producing derived terms
- Truth functions expressing relationships

### Microtheories
Each microtheory is internally consistent but may contradict others. Example: "the Earth is flat" can be true in a Flat-Earth microtheory and false in a Modern-Physics microtheory. This enables context-dependent reasoning.

### Ontological Engineering
"Ontological engineers" (nicknamed "Cyclists") manually analyze English text to extract tacit knowledge — resolving ambiguous pronouns, inferring implied relationships, and encoding physical causality that humans never state explicitly.

## Applications

- **Cleveland Clinic** (2007): Reduced biomedical research query time from months to under an hour
- **U.S. intelligence**: Terrorism Knowledge Base (2004-2008) stored knowledge as mathematical logic
- **CycSecure** (2002): Network vulnerability assessment at U.S. STRATCOM
- **GlaxoSmithKline** (2001): Pharmaceutical research
- **MathCraft**: Sixth-grade mathematics tutoring

## Software Releases

- **OpenCyc** (2002-2017): Free version, grew from 6K to 239K concepts, shut down 2017
- **ResearchCyc** (2006): Research-grade version with NLP tools

## Why Cyc Matters for This Knowledge Base

Cyc is the most instructive precedent for [[concepts/llm-knowledge-base]] systems:

1. **What Cyc proved**: Explicit, structured knowledge is necessary for reliable reasoning
2. **What Cyc failed**: Manual encoding doesn't scale, even with $60M and 2,000 person-years
3. **The modern resolution**: Use LLMs to automate the encoding that Cyc required humans to do manually, while keeping knowledge in explicit, auditable form (markdown, not neural weights)

This is precisely the [[concepts/cheap-ontology]] thesis: achieve 80% of Cyc's value at 1% of the cost through LLM-maintained natural-language knowledge bases.

## Mentioned In
- [[sources/wikipedia-cyc]] — comprehensive technical and historical overview
- [[sources/outsiderart-cyc-forgotten-ai]] — narrative arc from AM/EURISKO through Cyc's decline
- [[sources/wikipedia-knowledge-representation-reasoning]] — Cyc as KR's most ambitious project
