"""
kb — LLM Knowledge Base CLI (Python rewrite).

Typed command-line interface for a Claude-powered personal knowledge base.
All LLM-invoking subcommands support a token budget (--budget) that is
enforced against Anthropic SDK usage metadata, and every command supports
--json for machine-readable structured output.

See tools/kb/cli.py for the typer app, tools/kb/commands/ for per-command
implementations, and tools/kb/budget.py for budget enforcement.
"""

__version__ = "0.1.0"
