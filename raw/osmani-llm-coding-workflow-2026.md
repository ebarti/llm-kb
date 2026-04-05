---
title: "My LLM Coding Workflow Going into 2026"
source: "https://addyosmani.com/blog/ai-coding-workflow/"
author: "Addy Osmani"
date_published: 2026-03-01
date_ingested: 2026-04-05
tags: [ai-coding-workflow, developer-tools, claude-code, cursor, copilot, best-practices]
type: article
status: raw
discovered_via: search
---

# My LLM Coding Workflow Going into 2026

By Addy Osmani (Google Chrome engineering lead)

## Core Philosophy

Osmani advocates for "AI-augmented software engineering" rather than fully autonomous AI development. The approach treats LLMs as powerful pair programmers requiring clear direction, context, and human oversight rather than independent agents.

## Key Workflow Steps

### 1. Specification and Planning First
Before writing code, create a detailed spec.md containing requirements, architecture decisions, data models, and testing strategy. Described as achieving a "waterfall in 15 minutes" — rapid structured planning that prevents wasted cycles. The AI should help iteratively flesh out requirements and edge cases through questioning.

### 2. Break Work into Small Iterations
Rather than requesting large monolithic outputs, divide projects into focused tasks. LLMs perform best with "focused prompts: implement one function, fix one bug, add one feature at a time." This prevents the "jumbled mess" from overwhelming the model with too much context.

### 3. Provide Extensive Context
Feed the AI all relevant information: existing codebase, project constraints, preferred approaches, and known pitfalls. Tools like Anthropic's Claude Projects can import entire repositories. Osmani uses gitingest or repo2txt to bundle relevant source files.

### 4. Choose the Right Model
Practice "model musical chairs" — trying multiple LLMs on the same prompt to see which handles it better. Use the newest pro-tier models when possible, as quality matters significantly.

### 5. Customize AI Behavior
Create files like CLAUDE.md or GEMINI.md containing process rules, style preferences, and conventions. This reduces the AI's tendency to go off-script. Use system prompts to guide the AI toward your team's idioms.

### 6. Integrate Testing and Automation
Ensure repositories have robust CI/CD setups with automated tests, linters (ESLint, Prettier), and staging deployments. Let the AI trigger these and evaluate results. "Those who get the most out of coding agents tend to be those with strong testing practices."

### 7. Keep Humans in the Loop
Never blindly trust LLM output. Treat AI-generated code like it came from a junior developer — reviewing it thoroughly, running tests, validating functionality. Use a "second AI session" to critique code from the first, or spawn different models for review.

### 8. Commit Often and Use Version Control
Make frequent, granular commits after each small task. This creates "save points" allowing easy rollback if the AI missteps. Use branches or worktrees to isolate experiments, enabling parallel AI work on different features.

### 9. Leverage Coding Agents Wisely
Tools like Claude Code, Jules, and GitHub Copilot Agent can execute multi-step tasks, write tests, and open PRs. However, these are power tools requiring supervision. Supply them with the spec or plan to keep them on track.

### 10. Learn Continuously
Using AI is a learning opportunity. Strong software engineering fundamentals amplify AI productivity. By reviewing AI code and debugging mistakes, developers deepen their understanding.

## Tools and Approaches

- **MCP (Model Context Protocol):** Claude Skills as durable, reusable capabilities packaged into modular units
- **Code Review Automation:** Use linters, type checkers, and CI feedback loops
- **Planning Documents:** Generate structured "prompt plan" files for sequential execution
- **Chrome DevTools MCP:** Provides agents direct access to browser execution for automated UI testing

## Key Insights

- Critical thinking remains essential — LLMs produce plausible-looking code confidently, including bugs
- Planning amplifies AI effectiveness — specs and architecture make code generation smoother
- Testing is a force multiplier — solid test suites enable AIs to "fly through projects"
- AI rewards existing best practices — design docs, code reviews, tests, version control become even more powerful
- The developer stays in charge — AI accelerates mechanical tasks while humans focus on design and architecture

Bottom line: "AI coding assistants are incredible force multipliers, but the human engineer remains the director of the show."
