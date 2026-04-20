"""Typed subject-predicate-object graph store for the LLM knowledge base.

Stdlib-only SQLite backend that indexes wiki articles as nodes and
wikilinks as typed edges. Predicates are extracted heuristically from
the text surrounding each link, with optional frontmatter overrides.

Modules:
    store      — SQLite schema + insert/query functions.
    extract    — Wiki scanning + heuristic predicate detection.
    gq         — Command-line interface (also installed as an executable).
"""

from .store import (
    GraphStore,
    PREDICATES,
    DEFAULT_PREDICATE,
    DEFAULT_DB_PATH,
)
from .extract import (
    extract_nodes_and_edges,
    detect_predicate,
    PREDICATE_PATTERNS,
)

__all__ = [
    "GraphStore",
    "PREDICATES",
    "DEFAULT_PREDICATE",
    "DEFAULT_DB_PATH",
    "extract_nodes_and_edges",
    "detect_predicate",
    "PREDICATE_PATTERNS",
]
