---
title: "Source: Addy Osmani's LLM Coding Workflow for 2026"
type: source-summary
source: "[[raw/osmani-llm-coding-workflow-2026]]"
related: ["[[concepts/ai-pair-programming]]", "[[concepts/spec-driven-development]]", "[[concepts/ai-coding-assistants]]", "[[entities/addy-osmani]]", "[[entities/claude-code]]", "[[entities/cursor]]"]
last_compiled: 2026-04-05
summary: "Google Chrome lead's 10-step workflow for AI-augmented engineering: spec-first planning, small iterations, extensive context, model rotation, testing as force multiplier, and humans as directors."
---

## Key Points

- Advocates "AI-augmented software engineering" over fully autonomous AI development
- 10-step workflow: spec first, small iterations, extensive context, model selection, customization, testing, human review, frequent commits, agent supervision, continuous learning
- Describes achieving "waterfall in 15 minutes" through rapid structured spec creation
- Emphasizes CLAUDE.md/GEMINI.md files for customizing AI behavior per project
- Testing described as the single greatest force multiplier for AI-assisted coding

## Detailed Summary

Addy Osmani, engineering lead at Google Chrome, presents a practitioner's framework for integrating LLMs into daily development work. The workflow is built around treating AI as a powerful but fallible pair programmer that requires clear direction and constant oversight.

The spec-first approach is central: creating a detailed spec.md before any code generation prevents the common failure mode where AI "gets confused halfway through." Osmani estimates this single step eliminates 80% of wasted AI cycles. He uses tools like gitingest and repo2txt to provide the AI with comprehensive codebase context.

The "model musical chairs" practice — trying the same prompt across multiple LLMs — acknowledges that different models have different strengths. He gravitates toward Gemini for natural interactions but switches models when needed.

Key tooling includes [[entities/claude-code]], Jules, GitHub Copilot Agent, and Chrome DevTools MCP for browser-based testing. The MCP ([[concepts/model-context-protocol]]) ecosystem features prominently as the integration layer connecting AI agents to external tools.

His most counterintuitive insight: AI rewards and amplifies existing engineering best practices. Teams with strong test suites, design documentation, code review culture, and version control discipline see the greatest productivity gains from AI tools.

## Notable Quotes

> "AI coding assistants are incredible force multipliers, but the human engineer remains the director of the show."

> "Those who get the most out of coding agents tend to be those with strong testing practices."

## Related Concepts

- [[concepts/spec-driven-development]] — Central to Osmani's workflow
- [[concepts/ai-pair-programming]] — The mental model he applies to AI interaction
- [[concepts/ai-coding-assistants]] — Tools he evaluates and recommends
- [[concepts/developer-experience-ai]] — How workflow design affects AI effectiveness
