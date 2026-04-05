---
title: "Source: The Shape of AI — UX Patterns for AI Design"
type: source-summary
source: "[[raw/shapeof-ai-ux-patterns]]"
related: ["[[concepts/ai-ux-design-patterns]]", "[[concepts/progressive-disclosure-ai]]", "[[concepts/human-in-the-loop]]", "[[concepts/trust-in-ai]]"]
last_compiled: 2026-04-05
summary: "Comprehensive catalog of 57 AI UX design patterns in six categories: Wayfinders, Prompt Actions, Tuners, Governors, Trust Builders, and Identifiers."
---

## Key Points
- The most complete open taxonomy of interaction patterns for AI products, with 57 named patterns
- Organized into six functional categories addressing the full lifecycle of AI interaction
- Patterns range from onboarding (Gallery, Suggestions) through execution (Chained Action, Synthesis) to oversight (Verification, Stream of Thought)
- Trust is treated as a first-class design concern with dedicated patterns for Consent, Disclosure, Footprints, and Data Ownership
- The "Governors" category specifically addresses [[concepts/human-in-the-loop]] control: Action Plans, Branches, Citations, Controls, Cost Estimates, Draft Mode, Memory, Verification

## Detailed Summary

The Shape of AI is a community-maintained catalog that provides the most granular taxonomy of AI UX patterns available. Its six categories map to distinct phases of the human-AI interaction loop:

**Wayfinders** solve the [[concepts/blank-page-problem]] — the challenge of getting users started when facing an empty prompt. Patterns include Gallery (example outputs), Suggestions (prompt starters), Templates (structured starting points), and Randomize (low-barrier exploration).

**Prompt Actions** define what AI can do: Expand, Summarize, Synthesize, Transform, Restructure, Restyle, and Regenerate. These map directly to the atomic operations a [[concepts/copilot-pattern]] product would expose.

**Tuners** give users control over context and parameters: Attachments, Connectors (external data), Filters, Modes, Voice and Tone, and Saved Styles. This is where [[concepts/personalization-in-ai]] lives architecturally.

**Governors** are the critical [[concepts/human-in-the-loop]] layer: Action Plan (preview before execution), Verification (confirm before proceeding), Stream of Thought (transparent reasoning), Citations, Cost Estimates, and Draft Mode.

**Trust Builders** address [[concepts/trust-in-ai]] through Disclosure (marking AI content), Footprints (tracing steps), Consent, Data Ownership, Watermarks, and Incognito Mode.

**Identifiers** handle AI branding: Avatar, Color, Iconography, Name, and Personality.

## Notable Quotes
> "Progressive Disclosure is an AI design pattern that reveals complexity gradually."
> "Allow users to confirm AI decisions and actions before proceeding." (Verification pattern)
> "Reveals the AI's logic thought process, tool use, and decisions for oversight and auditability." (Stream of Thought)

## Related Concepts
- [[concepts/ai-ux-design-patterns]] — this source is the primary taxonomy
- [[concepts/progressive-disclosure-ai]] — one of the named patterns, applied throughout
- [[concepts/human-in-the-loop]] — the Governors category directly implements this
- [[concepts/trust-in-ai]] — the Trust Builders category
- [[concepts/blank-page-problem]] — solved by Wayfinders patterns
- [[concepts/copilot-pattern]] — Prompt Actions map to copilot capabilities
