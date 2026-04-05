---
title: "Anthropic Responsible Scaling Policy v3.0"
source: "https://www.anthropic.com/news/responsible-scaling-policy-v3"
author: "Anthropic"
date_published: 2026-02-24
date_ingested: 2026-04-05
tags: [anthropic, safety, responsible-scaling, rsp, asl]
type: article
status: raw
discovered_via: search
---

# Anthropic Responsible Scaling Policy v3.0

## Overview

The Responsible Scaling Policy (RSP) is Anthropic's risk governance framework for mitigating catastrophic risks from frontier AI systems. Version 3.0 was released February 24, 2026.

## Policy Evolution

- Version 1.0 (September 19, 2023): Original framework
- Version 2.0 (October 15, 2024): Added ASL-3 safeguard details
- Version 2.1 (March 31, 2025): Clarified capability thresholds and CBRN development standards
- Version 2.2 (May 14, 2025): Refined insider threat definitions
- Version 3.0 (February 24, 2026): Comprehensive rewrite
- Version 3.1 (April 2, 2026): Minor clarifications on AI R&D capability definitions

## AI Safety Levels (ASL)

Modeled loosely after biosafety levels (BSL):

### ASL-2 & ASL-3
Well-defined with implementation proven feasible. ASL-3 safeguards activated in May 2025 for models with biological science risks.

### ASL-3 Deployment Standard
Defense-in-depth with four layers:
1. Access controls (tiered partner trustworthiness evaluation)
2. Real-time classifiers (ML models analyzing inputs/outputs)
3. Asynchronous monitoring (simpler models with escalation)
4. Post-hoc jailbreak detection (rapid response patching)

### ASL-3 Security Standard
Seventeen key controls including:
- Multi-level access management
- Software supply chain scanning
- Binary authorization for endpoints
- Executive Risk Council oversight
- Multi-party authorization for model weight access
- Red teaming and penetration testing
- Honeypot deception technology
- Physical security surveillance

### ASL-4 & ASL-5
Intentionally left largely undefined due to uncertainty about future capabilities.

## Key Changes in v3.0

### Separation of Commitments
Distinguishes between unilateral Anthropic commitments and industry-wide recommendations. Reflects that "robust mitigations might prove impossible to implement without collective action."

### Frontier Safety Roadmap
New requirement for public documentation across four domains: Security, Alignment, Safeguards, Policy.

### Risk Reports
Published quarterly to semi-annually with third-party review.

### Capability Thresholds
- AI R&D Capability: ability to "compress two years of 2018-2024 AI progress into a single year"
- CBRN Development: "substantially uplift development capabilities of moderately resourced state programs"
- Evaluation interval extended from 3 months (v2) to 6 months (v3)

## Industry Impact
Within months of Anthropic's RSP, both OpenAI and Google DeepMind adopted similar frameworks. The RSP influenced California's SB 53, New York's RAISE Act, and EU AI Act.

## What Failed in Previous Versions
- Pre-set capability thresholds proved "far more ambiguous than anticipated"
- Government action lagged despite AI advancement
- Higher ASL safeguards appear unilaterally unachievable (RAND report: SL5 security "currently not possible")

## Competitive Dynamics (v3.0 stance)
"Having one developer pause while others continued without strong mitigations could result in a less safe world." Anthropic advocates a "race to the top" model.
