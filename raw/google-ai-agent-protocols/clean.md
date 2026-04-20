---
title: "Developer's Guide to AI Agent Protocols"
source: "https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/"
author: "Google Developers Blog"
date_published: 2026-03-01
date_ingested: 2026-04-05
tags: [mcp, a2a, protocols, google, adk, agent-protocols, ucp, a2ui, ag-ui]
type: article
status: raw
discovered_via: search
---

# AI Agent Protocols: Comprehensive Overview

## The Six Core Protocols

Google Developers blog post introduces a suite of six standardized protocols designed to eliminate custom integration code in AI agent development.

### 1. Model Context Protocol (MCP)

**Purpose:** Standardizes how agents connect to external systems and data sources.

**Key Features:**
- Provides "a single standard connection pattern for hundreds of servers"
- Servers advertise their tools automatically, enabling agent discovery
- Eliminates need for custom API integration code

**Implementation:** ADK's McpToolset provides first-class support, connecting to resources like the MCP Toolbox for Databases and various vendor-specific MCPs.

### 2. Agent2Agent Protocol (A2A)

**Purpose:** Enables agents to discover and communicate with other remote agents.

**Key Architecture:**
- Agents publish "Agent Cards" at /.well-known/agent-card.json
- Cards describe capabilities, endpoints, and available skills
- Agents discover each other at runtime without code changes

**Differentiation:** Unlike MCP (data access), A2A addresses "expertise" — knowledge that lives with specialized remote agents.

### 3. Universal Commerce Protocol (UCP)

**Purpose:** Standardizes shopping and commerce workflows across diverse suppliers.
- Provides "strongly typed request and response schemas that remain consistent"
- Works across REST, MCP, A2A, and embedded protocols

### 4. Agent Payments Protocol (AP2)

**Purpose:** Adds cryptographic authorization and audit trails to financial transactions.
- IntentMandate: Configures guardrails (approved merchants, spending limits)
- PaymentMandate: Binds authorization to specific transactions
- PaymentReceipt: Closes the audit trail

### 5. Agent-to-User Interface Protocol (A2UI)

**Purpose:** Lets agents dynamically compose user interfaces from fixed component primitives.
- Declarative JSON format with 18 safe component types
- Flat component lists with ID references (non-nested structure)

### 6. Agent-User Interaction Protocol (AG-UI)

**Purpose:** Standardizes streaming event format between agents and frontends.
- Acts as middleware translating framework-specific events into standardized Server-Sent Events (SSE)
- Event types: TEXT_MESSAGE_CONTENT, TOOL_CALL_START, TOOL_CALL_RESULT, TOOL_CALL_END, RUN_STARTED, RUN_FINISHED

## Integrated Workflow Example

All six protocols working together in a restaurant supply chain scenario:
1. MCP queries inventory database for stock levels
2. A2A retrieves pricing and quality data from remote specialist agents
3. UCP places orders with wholesale distributors
4. AP2 secures transactions with payment mandates
5. A2UI composes interactive dashboards
6. AG-UI streams the entire interaction to the frontend

## Implementation Framework

Agent Development Kit (ADK): Google's framework providing integrated support for all six protocols. Key Principle: "Add protocols as you need them" — most agents begin with MCP for basic data access, expanding protocol adoption as requirements grow.
