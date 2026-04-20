---
title: "Model Context Protocol (MCP): Open Standard for AI Tool Integration"
source: "https://modelcontextprotocol.io/specification/2025-11-25"
author: "Anthropic"
date_published: 2024-11-25
date_ingested: 2026-04-05
tags: [mcp, model-context-protocol, tool-use, anthropic, open-standard]
type: article
status: raw
discovered_via: search
---

# Model Context Protocol (MCP)

## Overview

The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize the way AI systems integrate with external tools, data sources, and services. It uses JSON-RPC 2.0 messages for communication.

## Architecture

Three-tier architecture:
- **Hosts**: LLM applications that initiate connections
- **Clients**: Connectors within the host application
- **Servers**: Services that provide context and capabilities

Inspired by the Language Server Protocol (LSP) which standardized programming language support across development tools.

## Server Features (what servers expose to clients)

- **Resources**: Context and data for the user or the AI model to use
- **Prompts**: Templated messages and workflows for users
- **Tools**: Functions for the AI model to execute

## Client Features (what clients expose to servers)

- **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
- **Roots**: Server-initiated inquiries into URI or filesystem boundaries
- **Elicitation**: Server-initiated requests for additional information from users

## Additional Utilities
- Configuration, progress tracking, cancellation, error reporting, logging

## Security and Trust Principles

1. **User Consent and Control**: Explicit consent for data access and operations
2. **Data Privacy**: Hosts must obtain consent before exposing user data to servers
3. **Tool Safety**: Tools represent arbitrary code execution; hosts must obtain consent before invoking any tool
4. **LLM Sampling Controls**: Users must explicitly approve LLM sampling requests

## Industry Adoption

- March 2025: OpenAI adopted MCP across its products
- April 2025: Google DeepMind confirmed MCP support for Gemini
- November 2025: Major spec update (async operations, statelessness, server identity, community registry)
- December 2025: Anthropic donated MCP to Agentic AI Foundation (AAIF) under Linux Foundation, co-founded with Block and OpenAI
- By December 2025: 97 million monthly SDK downloads across all languages

## Pre-built Servers
Google Drive, Slack, GitHub, Git, Postgres, Puppeteer, and many community-built servers.

## When to Use MCP
Best for general-purpose agents, systems needing frequent API updates, LLM-based IDEs, evolving systems. Hardcoded tools may be simpler for focused, domain-specific agents.
