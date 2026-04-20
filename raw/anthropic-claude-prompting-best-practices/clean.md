---
title: "Anthropic Claude Prompting Best Practices"
source: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
author: "Anthropic"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, claude, anthropic, best-practices, xml-tags, system-prompt]
type: article
status: raw
discovered_via: search
---

# Claude Prompting Best Practices (Official Anthropic Guide)

The single reference for prompt engineering with Claude's latest models (Opus 4.6, Sonnet 4.6, Haiku 4.5).

## General Principles

### Be Clear and Direct
Claude responds well to clear, explicit instructions. Think of Claude as a brilliant but new employee who lacks context.

Golden rule: Show your prompt to a colleague with minimal context and ask them to follow it. If they'd be confused, Claude will be too.

### Add Context to Improve Performance
Explain WHY behind instructions. E.g., instead of "NEVER use ellipses" → "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the TTS engine will not know how to pronounce them."

### Use Examples Effectively (Few-Shot)
- 3-5 examples for best results
- Make them relevant, diverse, and structured
- Wrap in <example> tags to distinguish from instructions
- Ask Claude to evaluate or generate additional examples

### Structure Prompts with XML Tags
XML tags help Claude parse complex prompts unambiguously. Use consistent, descriptive tag names. Nest tags when content has natural hierarchy.

### Give Claude a Role
Setting a role in system prompt focuses behavior and tone. Even a single sentence makes a difference.

### Long Context Prompting
- Put longform data at the TOP, above queries/instructions
- Queries at the end can improve quality by up to 30%
- Structure documents with XML tags (<document>, <document_content>, <source>)
- Ground responses in quotes: ask Claude to quote relevant parts before answering

## Output and Formatting

### Communication Style
Claude 4.6 is more direct, grounded, conversational, and less verbose.

### Control Format
1. Tell Claude what to do instead of what NOT to do
2. Use XML format indicators
3. Match prompt style to desired output style
4. Provide detailed formatting preferences

### Migrating Away from Prefilled Responses
Prefilled responses deprecated in Claude 4.6. Alternatives:
- Structured Outputs for format control
- Direct instructions to skip preamble
- Move continuations to user message

## Thinking and Reasoning

### Adaptive Thinking
Claude 4.6 uses adaptive thinking (thinking: {type: "adaptive"}) where Claude dynamically decides when/how much to think. Controlled by effort parameter.

Best practices:
- Prefer general instructions over prescriptive steps
- "Think thoroughly" often produces better reasoning than hand-written step-by-step plans
- Multishot examples work with thinking (use <thinking> tags)
- Ask Claude to self-check before finishing

### Manual CoT as Fallback
When thinking is off, encourage step-by-step reasoning with structured tags like <thinking> and <answer>.

## Agentic Systems

### Prompt Chaining
With adaptive thinking and subagent orchestration, Claude handles most multi-step reasoning internally. Explicit chaining still useful when you need to inspect intermediate outputs.

Most common pattern: self-correction (generate → review → refine).

### Subagent Orchestration
Claude 4.6 can recognize when tasks benefit from delegating to subagents and does so proactively.

### Balancing Autonomy and Safety
Add guidance for Claude to confirm before potentially destructive/irreversible actions.

### Research and Information Gathering
- Provide clear success criteria
- Encourage source verification
- Use structured approach with competing hypotheses and confidence levels

### Minimizing Hallucinations
"Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering."
