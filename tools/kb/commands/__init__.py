"""Per-command implementations for the kb CLI.

Each module exports a ``run`` function returning a pydantic model from
``tools.kb.models``. ``cli.py`` wires these into typer-managed subcommands.
"""
