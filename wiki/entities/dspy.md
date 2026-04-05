---
title: "DSPy"
type: entity
entity_type: tool
sources: ["[[sources/intuitionlabs-meta-prompting]]"]
related: ["[[concepts/meta-prompting]]", "[[concepts/prompt-engineering]]", "[[entities/textgrad]]"]
last_compiled: 2026-04-05
summary: "Declarative Self-improving Python framework that acts as a 'compiler' for LLM prompts, optimizing entire pipelines at compile-time — raised accuracy from 46.2% to 64.0% on prompt evaluation tasks."
---

## Overview

DSPy (Declarative Self-improving Python) is a framework for programming language models that treats prompt optimization as a compilation problem. Instead of manually crafting prompts, developers define their pipeline declaratively and DSPy automatically optimizes the prompts through bootstrapping few-shot examples from data.

## Key Features

- **Declarative pipeline definition**: Define what you want, not how to prompt
- **Compile-time optimization**: Automatically discovers effective prompts before deployment
- **Automatic few-shot learning**: Bootstraps examples from training data
- **Instruction optimization**: Refines prompt instructions automatically
- **Modular, reusable systems**: Optimized components can be composed

## Performance

A 2025 study found DSPy raised accuracy from 46.2% to 64.0% on prompt evaluation tasks — a significant improvement from automated optimization alone.

## Relationship to TextGrad

DSPy and [[entities/textgrad]] represent complementary approaches:
- **DSPy**: Best for pipeline-level optimization and reusable systems
- **TextGrad**: Best for instance-level refinement on hard tasks
- Combined, they suggest a hybrid approach for maximum performance

## Mentioned In
- [[sources/intuitionlabs-meta-prompting]] — DSPy as leading [[concepts/meta-prompting]] framework
