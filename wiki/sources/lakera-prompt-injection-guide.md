---
title: "Source: Comprehensive Guide to Prompt Injection (Lakera)"
type: source-summary
source: "[[raw/lakera-prompt-injection-guide]]"
related: ["[[concepts/prompt-injection]]", "[[concepts/prompt-engineering]]", "[[entities/owasp]]"]
last_compiled: 2026-04-05
summary: "Lakera's deep dive on prompt injection: direct vs indirect types, 5 attack techniques, 5 real-world incidents (2023-2024), defense limitations, and multi-layered prevention including Anthropic/OpenAI/Microsoft approaches."
---

## Key Points
- Two types: direct (override system instructions) and indirect (malicious content in external data)
- Attack techniques: multi-turn manipulation, role-playing, context hijacking, obfuscation, multi-language
- Real-world incidents: ChatGPT system prompt leak, copy-paste injection, GPT-Store vulnerabilities, memory exploit, Auto-GPT RCE
- OWASP ranked prompt injection as #1 AI security risk in 2025
- Static defenses fundamentally limited — rule-based filtering cannot capture infinite attack variations
- Industry defenses: Anthropic (RL training, ~1% attack success), OpenAI (Instruction Hierarchy), Microsoft (defense-in-depth), Task Shield (2.07% attack success)

## Detailed Summary
This is the most comprehensive treatment of [[concepts/prompt-injection]] in the KB. The key insight is that prompt injection exploits a fundamental architectural weakness: LLM instruction-following logic cannot fully separate trusted instructions from untrusted user input. No single defense is foolproof — the probabilistic nature of LLMs means deterministic security guarantees are impossible. The recommended approach is multi-layered defense combining model-level security, real-time detection, external data management, and continuous red teaming.

## Related Concepts
- [[concepts/prompt-injection]] — the core vulnerability
- [[concepts/prompt-engineering]] — defensive prompting practices
- [[concepts/system-prompt-design]] — clear system prompts as defense layer
