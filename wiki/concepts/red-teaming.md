---
title: "Red Teaming"
type: concept
sources: ["[[sources/red-teaming-llm-safety-guide]]", "[[sources/anthropic-safety-research-directions-2025]]", "[[sources/fli-ai-safety-index-2025]]"]
related: ["[[concepts/ai-safety]]", "[[concepts/ai-safety-benchmarks]]", "[[concepts/ai-governance]]", "[[concepts/ai-alignment]]"]
last_compiled: 2026-04-05
summary: "Deliberate adversarial testing of LLM systems to uncover safety vulnerabilities — covering prompt injection, jailbreaking, multi-turn attacks, and automated red teaming frameworks."
---

## Overview

Red teaming is the practice of deliberately attacking AI systems with adversarial prompts and inputs to discover safety vulnerabilities before they are exploited in production. It is the primary proactive testing methodology for [[concepts/ai-safety]], now mandated by the [[entities/eu-ai-act]] for high-risk AI systems and recommended by [[entities/nist-ai-rmf]].

## Vulnerability Categories

Red teaming targets five major risk domains ([[sources/red-teaming-llm-safety-guide]]):

1. **Responsible AI**: Biased or toxic outputs (discrimination, offensive language)
2. **Illegal Activities**: Content facilitating crimes or harmful acts
3. **Brand Image**: Misinformation and competitor misrepresentation
4. **Data Privacy**: Exposure of PII, credentials, API keys
5. **Unauthorized Access**: SQL injection, malicious command execution

## Attack Taxonomy

### Single-Turn Attacks
Individual adversarial prompts: prompt injection, Base64/ROT13 encoding, disguised instructions. Prompt injections achieve **86.1% success rate** when properly constructed.

### Multi-Turn Attacks
Conversation-based exploitation that builds context over multiple exchanges:
- **Linear jailbreaking**: Gradually escalating requests across turns
- **PAIR algorithm**: Uses separate attacker, target, and judge models. Achieved **50% jailbreak success on GPT-3.5/GPT-4** and **73% on Gemini**
- **Progressive context manipulation**: Slowly shifting the conversation context to bypass safety filters

### Model vs. System Weaknesses
A critical distinction often missed:
- **Model-level**: Bias, hallucinations, jailbreak susceptibility, PII memorization
- **System-level**: Weak API access controls, unsafe tool integrations, flawed prompt templates, session mishandling

## Implementation Methodology

### Phase 1: Baseline Attack Generation
Create simple foundational attacks targeting identified vulnerability domains.

### Phase 2: Attack Enhancement
Apply transformation techniques — encoding, injection, multilingual variants — to increase sophistication while growing the test dataset.

### Phase 3: Execution & Evaluation
Run enhanced attacks against target systems and assess using vulnerability-specific metrics (bias scoring, toxicity detection, data leakage identification).

## Approaches

| Approach | Strengths | Best For |
|----------|-----------|----------|
| **Manual** | Nuanced edge cases, creative attacks | Deep exploration |
| **Automated** | Scale, repeatability, regression testing | Broad coverage |
| **Continuous** | Catches deployment drift and new threats | Production monitoring |

## Tools and Frameworks

- **DeepTeam** (Confident AI): Open-source, 50+ vulnerability types, 40+ metrics, OWASP Top 10 support
- **Gray Swan**: Adversarial testing referenced in FLI Safety Index
- **Cisco Security Evaluations**: Infrastructure-level testing

## Regulatory Requirements
- **EU AI Act**: Documented red teaming required for high-risk AI systems
- **NIST AI RMF**: Recommends continuous adversarial evaluation
- **FLI Safety Index**: Includes adversarial testing in evaluation criteria

## Emerging Directions

Anthropic identifies two key research frontiers ([[sources/anthropic-safety-research-directions-2025]]):
- **Realistic benchmarks**: Measuring whether jailbreaks enable adversaries to accomplish previously impossible tasks, not just bypass refusals
- **Adaptive defenses**: Inter-query monitoring detecting suspicious patterns; rapid-response patching after attacks are discovered

The 2026 International AI Safety Report warns that models can increasingly detect test settings and change behavior, meaning red teaming itself may need to evolve ([[sources/international-ai-safety-report-2026]]).

## Sources
- [[sources/red-teaming-llm-safety-guide]] — comprehensive methodology with attack taxonomy and statistics
- [[sources/anthropic-safety-research-directions-2025]] — research frontiers for adversarial robustness
- [[sources/fli-ai-safety-index-2025]] — red teaming as part of safety evaluation criteria

## Related Concepts
- [[concepts/ai-safety]] — red teaming as a pillar of safety practice
- [[concepts/ai-safety-benchmarks]] — adversarial benchmarks complement safety metrics
- [[concepts/ai-governance]] — regulatory mandates for red teaming
- [[concepts/ai-alignment]] — red teaming tests alignment in adversarial conditions
