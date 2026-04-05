---
title: "Responsible Scaling Policy (RSP)"
type: concept
sources: ["[[sources/anthropic-rsp-v3]]", "[[sources/anthropic-safety-research-directions-2025]]", "[[sources/fli-ai-safety-index-2025]]"]
related: ["[[entities/anthropic]]", "[[concepts/ai-safety]]", "[[concepts/constitutional-ai]]", "[[concepts/ai-safety-benchmarks]]", "[[concepts/ai-governance]]", "[[concepts/scalable-oversight]]"]
tags: [anthropic, safety, rsp, asl, governance, policy]
last_compiled: 2026-04-05
summary: "Anthropic's risk governance framework using AI Safety Levels (ASL-1 through ASL-5) modeled after biosafety levels, requiring escalating safeguards proportional to model capabilities -- evolved through 6 versions from September 2023 to April 2026."
---

## Overview

The Responsible Scaling Policy (RSP) is [[entities/anthropic]]'s framework for governing the development and deployment of increasingly capable AI models. It establishes the principle of **proportional protection**: safeguards that scale with potential risks. The framework uses AI Safety Levels (ASL), modeled after the U.S. government's biosafety level (BSL) standards.

The RSP was the first major voluntary safety governance framework from a frontier AI lab, released in September 2023. Within months, both OpenAI and Google DeepMind adopted broadly similar frameworks.

## AI Safety Levels

| Level | Risk Category | Status |
|-------|--------------|--------|
| ASL-1 | Negligible catastrophic risk | Baseline |
| ASL-2 | Models with some dangerous knowledge but below uplift threshold | Active (most models) |
| ASL-3 | Models that could meaningfully uplift CBRN capabilities | Active since May 2025 |
| ASL-4 | Models with autonomous AI R&D capabilities | Undefined (aspirational) |
| ASL-5 | Models posing catastrophic/existential risk | Undefined (theoretical) |

## ASL-3 Safeguards (Active)

### Deployment Standard (Four Layers)
1. **Access controls**: Tiered partner evaluation based on trustworthiness and use-case value
2. **Real-time classifiers**: ML models analyzing inputs/outputs with streaming implementation
3. **Asynchronous monitoring**: Simpler models (e.g., Claude 3 Haiku) with escalation to advanced models
4. **Post-hoc jailbreak detection**: Rapid response procedures including patching and prompt reinforcement

### Security Standard (17 Controls)
Multi-level access management, compartmentalization, software supply chain scanning, binary authorization, Executive Risk Council oversight, multi-party authorization for model weights, red teaming, penetration testing, honeypot deception, physical security, centralized logging with SIEM/SOAR.

## Policy Evolution

| Version | Date | Key Change |
|---------|------|------------|
| v1.0 | Sep 2023 | Original framework with ASL concept |
| v2.0 | Oct 2024 | Added ASL-3 safeguard details |
| v2.1 | Mar 2025 | Clarified capability thresholds, CBRN standards |
| v2.2 | May 2025 | Refined insider threat definitions |
| v3.0 | Feb 2026 | Separated unilateral/industry commitments; Frontier Safety Roadmaps |
| v3.1 | Apr 2026 | Clarified AI R&D capability definitions |

## Key Innovations in v3.0

### Separation of Commitments
Distinguishes between what Anthropic can implement alone versus what requires industry coordination. Acknowledges that "robust mitigations might prove impossible to implement without collective action."

### Frontier Safety Roadmaps
Mandatory public documentation of concrete plans across four domains: Security, Alignment, Safeguards, Policy. Includes moonshot security projects, automated red-teaming, and AI-monitored activity logs.

### Risk Reports
Published quarterly to semi-annually with minimal redactions and third-party review. Explain how capabilities, threat models, and mitigations interconnect.

### Capability Thresholds
- **AI R&D Capability**: Ability to "compress two years of 2018-2024 AI progress into a single year"
- **CBRN Development**: "Substantially uplift development capabilities of moderately resourced state programs"

## Lessons from Implementation

Anthropic has been transparent about what failed:
- Pre-set capability thresholds proved "far more ambiguous than anticipated"
- Government action lagged despite AI advancement
- Higher ASL safeguards appear unilaterally unachievable (RAND: SL5 "currently not possible")
- Evaluation intervals needed extension from 3 to 6 months for quality

## Competitive Dynamics

The RSP v3.0 explicitly addresses the tension between safety and competition: "Having one developer pause while others continued without strong mitigations could result in a less safe world." This frames the RSP as a "race to the top" mechanism rather than a unilateral constraint.

## Industry Influence

The RSP influenced:
- OpenAI's Preparedness Framework (adopted within months)
- Google DeepMind's Frontier Safety Framework
- California's SB 53
- New York's RAISE Act
- EU AI Act provisions

## Sources

- [[sources/anthropic-rsp-v3]] -- comprehensive v3.0 details
- [[sources/anthropic-safety-research-directions-2025]] -- research priorities building on RSP
- [[sources/fli-ai-safety-index-2025]] -- independent evaluation of Anthropic's safety practices

## Related Concepts

- [[concepts/ai-safety]] -- the broader safety landscape RSP addresses
- [[concepts/constitutional-ai]] -- complementary alignment technique
- [[concepts/ai-safety-benchmarks]] -- evaluation methods referenced by RSP
- [[concepts/ai-governance]] -- regulatory context
- [[concepts/scalable-oversight]] -- the scaling problem RSP manages
