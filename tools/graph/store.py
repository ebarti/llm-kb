"""SQLite-backed typed graph store.

Schema (idempotent — uses CREATE TABLE IF NOT EXISTS):

    CREATE TABLE nodes (
        id       TEXT PRIMARY KEY,   -- wiki-relative path, no .md (e.g. 'concepts/rag')
        type     TEXT,               -- concept | entity | source-summary | comparison | raw | meta
        title    TEXT,               -- human-readable title
        path     TEXT,               -- absolute or repo-relative path on disk
        summary  TEXT                -- one-line summary (may be empty)
    );

    CREATE TABLE edges (
        src         TEXT NOT NULL,   -- source node id
        dst         TEXT NOT NULL,   -- destination node id
        predicate   TEXT NOT NULL,   -- one of PREDICATES
        provenance  TEXT,            -- 'heuristic:<pattern>', 'frontmatter:<field>',
                                     -- e.g. 'frontmatter:manual', or 'default'
        PRIMARY KEY (src, dst, predicate)
    );

    CREATE INDEX IF NOT EXISTS idx_edges_src ON edges(src);
    CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst);
    CREATE INDEX IF NOT EXISTS idx_edges_predicate ON edges(predicate);
    CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(type);

Stdlib only — no sqlalchemy, no pip packages.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from typing import Iterable, Iterator, Optional, Sequence


# Canonical predicate vocabulary. Any other value is rejected to keep the
# graph queryable. `mentions` is the default/fallback for untyped links.
PREDICATES = (
    "cites",
    "mentions",
    "compares",
    "implements",
    "extends",
    "contradicts",
    "refutes",
    "part_of",
    "instance_of",
)

DEFAULT_PREDICATE = "mentions"

# Location of the SQLite file at the repo root.
DEFAULT_DB_PATH = str(
    Path(__file__).resolve().parents[2] / ".graph.db"
)


class GraphStore:
    """Thin wrapper around a sqlite3.Connection for the typed graph.

    Usage:
        store = GraphStore("/path/to/.graph.db")
        store.init_schema()
        store.upsert_node("concepts/rag", type="concept", title="RAG", path=..., summary=...)
        store.upsert_edge("concepts/rag", "concepts/retrieval", "part_of", "heuristic:part_of")
        rows = store.cites_of("sources/attention-is-all-you-need")
        store.close()

    Context-manager usage is also supported:
        with GraphStore(path) as store:
            store.init_schema()
            ...
    """

    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        self.db_path = db_path
        # Ensure the parent directory exists (repo root always does, but be safe).
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        # Respect foreign key discipline even though we don't declare FKs —
        # avoids surprises if schema evolves.
        self.conn.execute("PRAGMA foreign_keys = ON")

    # ------------------------------------------------------------------ #
    #  Context manager
    # ------------------------------------------------------------------ #
    def __enter__(self) -> "GraphStore":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close(commit=exc_type is None)

    def close(self, commit: bool = True) -> None:
        try:
            if commit:
                self.conn.commit()
            else:
                self.conn.rollback()
        finally:
            self.conn.close()

    # ------------------------------------------------------------------ #
    #  Schema
    # ------------------------------------------------------------------ #
    def init_schema(self) -> None:
        """Create tables and indexes if they don't already exist (idempotent)."""
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS nodes (
                id      TEXT PRIMARY KEY,
                type    TEXT,
                title   TEXT,
                path    TEXT,
                summary TEXT
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS edges (
                src        TEXT NOT NULL,
                dst        TEXT NOT NULL,
                predicate  TEXT NOT NULL,
                provenance TEXT,
                PRIMARY KEY (src, dst, predicate)
            )
            """
        )
        cur.execute("CREATE INDEX IF NOT EXISTS idx_edges_src ON edges(src)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst)")
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_edges_predicate ON edges(predicate)"
        )
        cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(type)")
        self.conn.commit()

    def reset(self) -> None:
        """Drop all rows from both tables. Used by `gq build` before rebuilding."""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM edges")
        cur.execute("DELETE FROM nodes")
        self.conn.commit()

    # ------------------------------------------------------------------ #
    #  Inserts / upserts
    # ------------------------------------------------------------------ #
    def upsert_node(
        self,
        node_id: str,
        type: str = "",
        title: str = "",
        path: str = "",
        summary: str = "",
    ) -> None:
        """Insert or replace a node. Last write wins on duplicate id."""
        self.conn.execute(
            """
            INSERT INTO nodes (id, type, title, path, summary)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                type    = excluded.type,
                title   = excluded.title,
                path    = excluded.path,
                summary = excluded.summary
            """,
            (node_id, type, title, path, summary),
        )

    def upsert_edge(
        self,
        src: str,
        dst: str,
        predicate: str,
        provenance: str = "",
    ) -> None:
        """Insert an edge if not already present with the same (src,dst,predicate).

        Provenance wins: if the same edge is inserted twice, the later
        provenance string replaces the earlier one. This means a frontmatter
        override re-runs the insert and overwrites a heuristic provenance.
        """
        if predicate not in PREDICATES:
            raise ValueError(
                f"invalid predicate {predicate!r}; expected one of {PREDICATES}; "
                f"src={src!r}, dst={dst!r}, provenance={provenance!r}"
            )
        if not src or not dst:
            raise ValueError("edge requires non-empty src and dst")
        self.conn.execute(
            """
            INSERT INTO edges (src, dst, predicate, provenance)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(src, dst, predicate) DO UPDATE SET
                provenance = excluded.provenance
            """,
            (src, dst, predicate, provenance),
        )

    def commit(self) -> None:
        self.conn.commit()

    # ------------------------------------------------------------------ #
    #  Bulk helpers
    # ------------------------------------------------------------------ #
    def upsert_nodes(self, rows: Iterable[dict]) -> None:
        for r in rows:
            self.upsert_node(
                r["id"],
                type=r.get("type", ""),
                title=r.get("title", ""),
                path=r.get("path", ""),
                summary=r.get("summary", ""),
            )

    def upsert_edges(self, rows: Iterable[dict]) -> None:
        for r in rows:
            self.upsert_edge(
                r["src"],
                r["dst"],
                r["predicate"],
                provenance=r.get("provenance", ""),
            )

    # ------------------------------------------------------------------ #
    #  Queries
    # ------------------------------------------------------------------ #
    def get_node(self, node_id: str) -> Optional[sqlite3.Row]:
        cur = self.conn.execute("SELECT * FROM nodes WHERE id = ?", (node_id,))
        return cur.fetchone()

    def all_nodes(self) -> list[sqlite3.Row]:
        return list(self.conn.execute("SELECT * FROM nodes ORDER BY id"))

    def all_edges(self) -> list[sqlite3.Row]:
        return list(
            self.conn.execute(
                "SELECT * FROM edges ORDER BY src, predicate, dst"
            )
        )

    def count(self, table: str) -> int:
        if table not in ("nodes", "edges"):
            raise ValueError(f"unknown table: {table!r}")
        row = self.conn.execute(f"SELECT COUNT(*) AS n FROM {table}").fetchone()
        return int(row["n"])

    def predicate_counts(self) -> list[tuple[str, int]]:
        rows = self.conn.execute(
            "SELECT predicate, COUNT(*) AS n FROM edges "
            "GROUP BY predicate ORDER BY n DESC, predicate ASC"
        )
        return [(r["predicate"], int(r["n"])) for r in rows]

    def outgoing(
        self, src: str, predicate: Optional[str] = None
    ) -> list[sqlite3.Row]:
        if predicate is None:
            cur = self.conn.execute(
                "SELECT * FROM edges WHERE src = ? ORDER BY predicate, dst",
                (src,),
            )
        else:
            cur = self.conn.execute(
                "SELECT * FROM edges WHERE src = ? AND predicate = ? ORDER BY dst",
                (src, predicate),
            )
        return list(cur)

    def incoming(
        self, dst: str, predicate: Optional[str] = None
    ) -> list[sqlite3.Row]:
        if predicate is None:
            cur = self.conn.execute(
                "SELECT * FROM edges WHERE dst = ? ORDER BY predicate, src",
                (dst,),
            )
        else:
            cur = self.conn.execute(
                "SELECT * FROM edges WHERE dst = ? AND predicate = ? ORDER BY src",
                (dst, predicate),
            )
        return list(cur)

    def cites_of(self, article: str) -> list[sqlite3.Row]:
        """Return edges from `article` with predicate = 'cites'."""
        return self.outgoing(article, predicate="cites")

    def mentioned_by(self, article: str) -> list[sqlite3.Row]:
        """Return edges ending at `article` with predicate = 'mentions'."""
        return self.incoming(article, predicate="mentions")

    def contradictions(self) -> list[sqlite3.Row]:
        """Return all 'contradicts' and 'refutes' edges."""
        cur = self.conn.execute(
            "SELECT * FROM edges WHERE predicate IN ('contradicts', 'refutes') "
            "ORDER BY predicate, src, dst"
        )
        return list(cur)

    # ------------------------------------------------------------------ #
    #  Free-form query (read-only)
    # ------------------------------------------------------------------ #
    def query(self, sql: str, params: Sequence = ()) -> Iterator[sqlite3.Row]:
        """Execute a read-only SQL query. Rejects anything that looks mutating.

        This is deliberately conservative — the CLI `gq query` exposes this.
        Writes happen only through `build`.

        The scanner strips SQL comments (``--`` line, ``/* */`` block),
        collapses all whitespace to single spaces, and tokenizes on
        non-word boundaries so that `` 'WITH x AS (SELECT 1)\\nDELETE FROM
        ...'`` cannot smuggle a DELETE past the guard.
        """
        if not sql or not sql.strip():
            raise ValueError("empty query")

        # Strip block comments ``/* ... */`` and line comments ``-- ...``.
        cleaned = re.sub(r"/\*.*?\*/", " ", sql, flags=re.DOTALL)
        cleaned = re.sub(r"--[^\n]*", " ", cleaned)
        # Collapse all whitespace (including newlines, tabs) to single spaces.
        cleaned = re.sub(r"\s+", " ", cleaned).strip().rstrip(";")
        lowered = cleaned.lower()

        if not lowered.startswith(("select ", "with ", "explain ",
                                    "select(", "with(", "explain(")) \
                and lowered not in ("select", "with", "explain"):
            raise ValueError(
                "only read-only queries allowed (SELECT/WITH/EXPLAIN)"
            )

        # Tokenize on non-word boundaries so keywords are matched even
        # when surrounded by newlines, commas, parens, etc.
        tokens = set(re.findall(r"[a-z_]+", lowered))
        forbidden = {
            "insert", "update", "delete", "drop", "alter",
            "create", "replace", "pragma", "attach", "detach",
            "reindex", "vacuum", "truncate",
        }
        bad = tokens & forbidden
        if bad:
            raise ValueError(f"forbidden keyword in query: {sorted(bad)[0]}")
        return iter(self.conn.execute(sql, params))


def ensure_db(db_path: str = DEFAULT_DB_PATH) -> GraphStore:
    """Open (or create) the graph DB and apply the schema."""
    store = GraphStore(db_path)
    store.init_schema()
    return store
