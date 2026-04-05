---
title: "Creating a Dynamic UX: Guidance for Generative AI Applications"
source: "https://learn.microsoft.com/en-us/microsoft-cloud/dev/copilot/isv/ux-guidance"
author: "Microsoft"
date_published: 2024-09-16
date_ingested: 2026-04-05
tags: [copilot, ux-design, microsoft, generative-ai, product-design, collaborative-ux]
type: article
status: raw
discovered_via: search
---

# Creating a Dynamic UX: Guidance for Generative AI Applications (Microsoft)

Official Microsoft guidance for ISVs building generative AI / copilot-style applications.

## Three UX Framework Variations

### 1. Immersive Focus (Whole Knowledge Base)
Full-screen experience utilizing the entire canvas for AI interaction. Best for: important tasks requiring deep focus, AI-generated dashboards, comprehensive security analysis. "The more important the task, the more real estate required."

### 2. Assistive Focus (In-App Experience)
Side panel within existing applications. AI integrated into user's workflow without context switching. Provides continuous access to tools and assistance without obstructing the main content area.

### 3. Embedded Focus (Single Entity)
Pop-up or inline AI for specific items or actions. Context-aware assistance without permanent screen space. Ideal for occasional guidance — e.g., highlighting code to invoke copilot, or diving deeper into a chart.

**Hybrid approach**: Combine embedded with immersive or assistive for richer experiences.

## Three Foundational Principles

### Principle 1: Human in Control
"A copilot is simply a tool to support the user. The human is the pilot." Position user in driver's seat. Language matters: say "Summarize with copilot" not "Copilot, summarize."

### Principle 2: Avoid Anthropomorphizing
Avoid words like "understand," "think," or "feel." Use "processing" and "analyzing." First-person singular (I, me) is fine for conversational tone. Go light on personality — the more character, the more humanized.

### Principle 3: Consider Direct and Indirect Stakeholders
Design for primary users AND everyone the output might impact. Consider unintended consequences, vulnerable stakeholders, content sharing chains.

## Input Design Tips

1. **Provide suggestions** — Large input boxes, character counters, promptbooks for predictable queries
2. **Encourage details** — Split one general prompt into multiple input fields (title, details, images, tone)
3. **Allow customization** — Predefined tone options, changeable anytime within a conversation
4. **Multimodal design** — Voice and text options, multi-lingual inputs

## Output Design Tips

1. **Show inputs and outputs together** — Tight feedback loop so users associate output quality with input choice
2. **Keep history** — Timeline of outputs for comparison; reuse previous prompts
3. **Add appropriate friction** — Slow users at save/share/copy to encourage review. "Add AI notices and disclaimers with each output"
4. **Encourage fact-checking** — Citations, direct quotes, links to source locations
5. **Allow editing** — Let users modify outputs; demonstrates copilot is helper, not authority
6. **Withhold outputs when necessary** — Better no answer than potentially harmful content
7. **Allow feedback** — Accuracy ratings, thumbs up/down, correction options

## Lifecycle Guidelines (from HAX Toolkit)

### First Run
- Make clear what the system can do
- Make clear how well the system can do it (error rates)

### During Interaction
- Match relevant social norms
- Mitigate social biases

### When Wrong
- Support efficient correction
- Make clear why the system did what it did

### Over Time
- Encourage granular feedback
- Provide global controls
