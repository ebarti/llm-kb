---
title: "AI Governance"
type: concept
sources: ["[[sources/ai-governance-frameworks-comparison]]", "[[sources/fli-ai-safety-index-2025]]", "[[sources/international-ai-safety-report-2026]]", "[[sources/hitl-ai-agent-oversight]]"]
related: ["[[concepts/ai-safety]]", "[[concepts/human-in-the-loop]]", "[[concepts/red-teaming]]", "[[concepts/ai-safety-benchmarks]]", "[[entities/eu-ai-act]]", "[[entities/nist-ai-rmf]]"]
last_compiled: 2026-04-05
summary: "Regulatory and organizational frameworks for responsible AI development and deployment — centered on the EU AI Act (binding), NIST AI RMF (voluntary), and ISO/IEC 42001 (certifiable), with enforcement beginning August 2026."
---

## Overview

AI governance encompasses the laws, standards, organizational structures, and accountability mechanisms that ensure AI systems are developed and deployed responsibly. In 2025-2026, governance has shifted from aspirational principles to enforceable requirements, with the [[entities/eu-ai-act]] setting the global standard.

## Three Major Frameworks

### EU AI Act
The world's first comprehensive AI regulation. Binding law with extraterritorial reach — applies to any organization serving EU customers.

**Risk tiers:**
1. **Unacceptable Risk**: Prohibited (social scoring, manipulative AI)
2. **High Risk**: Heavily regulated (medical devices, employment, credit scoring)
3. **Limited Risk**: Transparency obligations required
4. **Minimal/No Risk**: Unrestricted use

**Key requirements for high-risk systems:**
- Technical documentation
- Data governance and quality standards
- [[concepts/human-in-the-loop|Human oversight]] mechanisms
- Conformity assessment before deployment
- Post-market monitoring
- Documented [[concepts/red-teaming]]

**Penalties**: Up to EUR 35 million or 7% of global annual turnover.

**Timeline**: GPAI provider compliance August 2025; full enforcement August 2, 2026; existing high-risk products August 2027.

### NIST AI Risk Management Framework (AI RMF)
Voluntary U.S. framework organized around four functions:
- **Govern**: Establish organizational environment for AI risk management
- **Map**: Understand context, stakeholders, and system limitations
- **Measure**: Analyze risks including bias, uncertainty, and performance
- **Manage**: Respond to identified risks with controls and documentation

Referenced as a baseline by regulators and standards bodies worldwide.

### ISO/IEC 42001
Certifiable international management system standard. Emphasizes lifecycle risk assessment without prescriptive categorization. Auditor qualification standards (BS ISO/IEC 42006:2025) are now published.

## Comparison

| Dimension | EU AI Act | NIST AI RMF | ISO/IEC 42001 |
|-----------|-----------|-------------|---------------|
| **Legal status** | Binding law | Voluntary guidance | Certifiable standard |
| **Geographic scope** | EU + extraterritorial | U.S.-focused, globally referenced | International |
| **Penalties** | Up to EUR 35M / 7% revenue | None | N/A |
| **Approach** | Prescriptive risk tiers | Flexible, sector-agnostic | Structured management |
| **Timeline** | Aug 2026 full enforcement | No deadlines | Ongoing certification |

([[sources/ai-governance-frameworks-comparison]])

## Governance for AI-Generated Content

For knowledge generation systems — including LLM-maintained wikis — governance implies:

1. **Transparency**: Users should know content is AI-generated
2. **Data lineage**: Tracking exactly what sources contributed to each output
3. **Human oversight checkpoints**: For content impacting safety, rights, or financial outcomes
4. **Risk classification**: Labeling each system with its risk level and compliance status
5. **Accountability**: Clear responsibility chains when AI-generated content causes harm

## Industry Safety Evaluation

The FLI AI Safety Index evaluates companies across six governance-relevant domains. In Summer 2025, even the highest-scoring company (Anthropic) achieved only C+ overall. Governance & Accountability and Information Sharing are explicit evaluation domains ([[sources/fli-ai-safety-index-2025]]).

## The Governance Speed Problem

A critical emerging challenge: AI governance mechanisms designed for human-speed review cannot keep pace with machine-speed AI operations. As AI systems become more agentic, governance must evolve from human-in-the-loop to AI-governing-AI architectures, with humans designing governance systems rather than performing oversight directly ([[sources/hitl-ai-agent-oversight]]).

## Sources
- [[sources/ai-governance-frameworks-comparison]] — detailed comparison of EU AI Act, NIST AI RMF, ISO/IEC 42001
- [[sources/fli-ai-safety-index-2025]] — company-level governance evaluation
- [[sources/international-ai-safety-report-2026]] — global policy context and expert recommendations
- [[sources/hitl-ai-agent-oversight]] — governance speed problem and AI-governing-AI evolution

## Related Concepts
- [[concepts/ai-safety]] — the goal governance frameworks serve
- [[concepts/human-in-the-loop]] — mandated for high-risk systems
- [[concepts/red-teaming]] — required testing methodology under EU AI Act
- [[concepts/ai-safety-benchmarks]] — evaluation methods referenced by governance frameworks
