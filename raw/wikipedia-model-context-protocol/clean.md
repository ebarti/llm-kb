---
title: "Model Context Protocol - Wikipedia"
source: "https://en.wikipedia.org/wiki/Model_Context_Protocol"
author: "Wikipedia Contributors"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [mcp, model-context-protocol, anthropic, open-standard, json-rpc, tool-use]
type: article
status: raw
discovered_via: search
---

# Model Context Protocol - Wikipedia

## Definition & Purpose
The Model Context Protocol (MCP) is an open standard and open-source framework introduced by Anthropic in November 2024. It standardizes how AI systems like large language models integrate and share data with external tools, systems, and data sources. The protocol provides "a universal interface for reading files, executing functions, and handling contextual prompts."

## Historical Background

**Initial Problem:** Before MCP, developers faced an "N×M data integration problem," requiring custom connectors for each combination of data source and tool. Earlier approaches like OpenAI's 2023 function-calling API and ChatGPT's plugin framework solved similar issues but demanded vendor-specific connectors.

**Launch Timeline:**
- **November 25, 2024:** Anthropic announced MCP as an open standard
- **March 2025:** OpenAI officially adopted the protocol across products including ChatGPT's desktop app
- **April 2025:** Google DeepMind announced adoption
- **December 2025:** Anthropic donated MCP to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI

## Technical Architecture

**Protocol Foundation:** MCP reuses message-flow concepts from the Language Server Protocol (LSP) and is transported over JSON-RPC 2.0.

**Component Structure:** The protocol defines relationships between MCP clients and servers, enabling standardized communication patterns.

**Key Features:**
- Specifications for data ingestion and transformation
- Contextual metadata tagging capabilities
- AI interoperability across different platforms
- Bidirectional connections between data sources and AI tools
- Support for natural language database queries

## SDK Support

Anthropic released software development kits in multiple programming languages:
- TypeScript
- Python
- Java
- Kotlin
- C#
- Go
- PHP
- Perl
- Ruby
- Rust
- Swift

Anthropic maintains an open-source repository of reference MCP server implementations and SDKs.

## Adoption & Integration

**Major Adopters:**
- OpenAI (March 2025)
- Google DeepMind (April 2025)
- Microsoft Semantic Kernel integration
- Azure OpenAI integration
- Cloudflare deployment capability
- IDEs and coding platforms (Replit, Sourcegraph)

**Use Cases:**
- AI-assisted software development
- Providing real-time project context to coding assistants
- Natural language data access from structured databases
- Querying diverse data sources with plain language

## Security & Reception

**Positive Reception:** The Verge reported that MCP addresses growing demand for contextually aware AI agents. The rapid adoption by major tech companies suggests "growing consensus around its utility."

**Security Concerns (April 2025):** Security researchers identified multiple outstanding issues:
- Prompt injection vulnerabilities
- Tool permission combinations enabling data exfiltration
- Lookalike tools that can silently replace trusted ones

## Comparison & Industry Position

MCP has been likened to OpenAPI, a similar specification for describing APIs. Industry observers have called MCP the "USB-C for AI," highlighting its role as a universal connector standard bringing competing companies together.

## Governance Evolution

The December 2025 transfer to the Agentic AI Foundation represents a shift toward neutral governance, with the protocol now stewarded by a Linux Foundation-backed organization rather than a single company.
