#!/usr/bin/env python3
"""Knowledge Graph Generator — interactive D3.js + static SVG.

Now reads from the typed graph store (`.graph.db`). Each edge carries a
predicate, and the output color-codes edges accordingly. If the graph DB
is absent or empty, we fall back to building it on the fly from the wiki/
directory.

Edge color scheme (kept in sync with PREDICATE_COLORS below and the legend
rendered in both the HTML and SVG outputs):

    cites        -> #4a90d9 (blue)     strong, directional (source citation)
    mentions     -> #7f8c8d (grey)     default/generic link
    compares     -> #9b59b6 (purple)
    implements   -> #1abc9c (teal)
    extends      -> #16a085 (dark teal)
    contradicts  -> #e74c3c (red)
    refutes      -> #c0392b (dark red)
    part_of      -> #f39c12 (orange)
    instance_of  -> #d35400 (dark orange)
"""

import html
import json
import math
import os
import sys
import sqlite3

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")
OUTPUT = os.path.join(BASE, "output", "images")
GRAPH_DB = os.path.join(BASE, ".graph.db")

# Node-type colors (nodes are colored by type).
NODE_COLORS = {
    "source-summary": "#4a90d9",
    "source": "#4a90d9",
    "concept": "#2ecc71",
    "entity": "#e67e22",
    "comparison": "#9b59b6",
    "raw": "#34495e",
    "meta": "#95a5a6",
}

# Edge colors by predicate.
PREDICATE_COLORS = {
    "cites":        "#4a90d9",
    "mentions":     "#7f8c8d",
    "compares":     "#9b59b6",
    "implements":   "#1abc9c",
    "extends":      "#16a085",
    "contradicts":  "#e74c3c",
    "refutes":      "#c0392b",
    "part_of":      "#f39c12",
    "instance_of":  "#d35400",
}


# ---------------------------------------------------------------------- #
#  Data loading — prefer the typed store, fall back to ad-hoc extraction.
# ---------------------------------------------------------------------- #
def load_from_graph_db(db_path):
    """Return (nodes dict, typed edges list) from a built .graph.db.

    Returns None if the DB is missing, empty, or unreadable for any reason
    (schema missing, corruption, locked, etc.) so the caller can fall back
    to live extraction rather than render a silently broken graph.
    """
    if not os.path.exists(db_path):
        return None
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        try:
            edge_count = conn.execute("SELECT COUNT(*) AS n FROM edges").fetchone()["n"]
        except sqlite3.Error:
            return None
        if not edge_count:
            return None

        nodes = {}
        for row in conn.execute("SELECT * FROM nodes"):
            nodes[row["id"]] = {
                "title": row["title"] or row["id"].split("/")[-1],
                "type": row["type"] or "concept",
                "summary": row["summary"] or "",
            }

        edges = []
        for row in conn.execute("SELECT src, dst, predicate FROM edges"):
            edges.append((row["src"], row["dst"], row["predicate"]))
        return nodes, edges
    except sqlite3.Error:
        return None
    finally:
        conn.close()


def load_from_wiki():
    """Build nodes + edges directly from wiki/ when the DB isn't available.

    We shell out to the `graph.extract` module so the viz has exactly the
    same view of predicates as `gq`.
    """
    sys.path.insert(0, os.path.join(BASE, "tools"))
    from graph.extract import extract_nodes_and_edges  # noqa: E402

    nodes_list, edges_list = extract_nodes_and_edges(WIKI)
    nodes = {
        n.id: {
            "title": n.title or n.id.split("/")[-1],
            "type": n.type or "concept",
            "summary": n.summary or "",
        }
        for n in nodes_list
    }
    edges = [(e.src, e.dst, e.predicate) for e in edges_list]
    return nodes, edges


def _wiki_is_newer_than_db(db_path: str, wiki_dir: str) -> bool:
    """Return True when any ``.md`` file under ``wiki_dir`` has a more
    recent mtime than the graph DB. Used to detect when ``kb compile``
    has updated articles but the graph rebuild was skipped or failed,
    so the viz falls back to live extraction instead of rendering
    silently stale nodes/edges.
    """
    if not os.path.exists(db_path):
        return True
    try:
        db_mtime = os.path.getmtime(db_path)
    except OSError:
        return True
    if not os.path.isdir(wiki_dir):
        return False
    for root, _dirs, files in os.walk(wiki_dir):
        for name in files:
            if not name.endswith(".md"):
                continue
            full = os.path.join(root, name)
            try:
                if os.path.getmtime(full) > db_mtime:
                    return True
            except OSError:
                continue
    return False


def load_graph():
    # Prefer the prebuilt DB, but fall back to live extraction when the
    # wiki has been edited since the DB was written. Without this the
    # viz renders a silently stale graph whenever the DB rebuild was
    # skipped or failed (kb compile treats that as non-fatal).
    if not _wiki_is_newer_than_db(GRAPH_DB, WIKI):
        data = load_from_graph_db(GRAPH_DB)
        if data is not None:
            return data
    return load_from_wiki()


# ---------------------------------------------------------------------- #
#  D3 / SVG rendering
# ---------------------------------------------------------------------- #
def build_graph_data(nodes, edges):
    # The store/extractor deliberately emits edges whose endpoints aren't
    # resolvable (e.g. dangling [[concepts/nonexistent]] links). We add
    # lightweight placeholder nodes for any missing endpoint so that those
    # edges still show up in the viz — otherwise the graph would silently
    # hide exactly the broken links the reader might be hunting for.
    nodes_out = dict(nodes)
    for src, tgt, _pred in edges:
        for endpoint in (src, tgt):
            if endpoint not in nodes_out:
                # Inherit type from a `raw/` prefix so raw-only targets
                # keep their colour; everything else is "meta" (grey).
                etype = "raw" if endpoint.startswith("raw/") else "meta"
                nodes_out[endpoint] = {
                    "title": endpoint.split("/")[-1],
                    "type": etype,
                    "summary": "(placeholder: referenced but no article)",
                }
    node_ids = set(nodes_out.keys())
    conn = {nid: 0 for nid in node_ids}
    valid_edges = []
    for src, tgt, pred in edges:
        if src in node_ids and tgt in node_ids:
            conn[src] += 1
            conn[tgt] += 1
            valid_edges.append({"source": src, "target": tgt, "predicate": pred})

    d3_nodes = [
        {
            "id": nid,
            "title": info["title"],
            "type": info["type"],
            "summary": info["summary"],
            "connections": conn.get(nid, 0),
        }
        for nid, info in nodes_out.items()
    ]
    return {"nodes": d3_nodes, "links": valid_edges}


def _json_for_html_script(value):
    """JSON-encode data for safe embedding in an inline <script> block."""
    return (
        json.dumps(value)
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def generate_html(graph_data):
    node_colors_js = _json_for_html_script(NODE_COLORS)
    edge_colors_js = _json_for_html_script(PREDICATE_COLORS)
    data_js = _json_for_html_script(graph_data)

    # Build legend rows — nodes by type, then edges by predicate.
    node_legend = "".join(
        f'<div class="legend-item"><div class="legend-dot" style="background:{c}"></div> {t}</div>'
        for t, c in NODE_COLORS.items()
        if t not in ("source", "meta")
    )
    edge_legend = "".join(
        f'<div class="legend-item"><div class="legend-bar" style="background:{c}"></div> {p}</div>'
        for p, c in PREDICATE_COLORS.items()
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Knowledge Graph</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #1a1a2e; color: #eee; overflow: hidden; }}
#controls {{ position: fixed; top: 12px; left: 12px; z-index: 10; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }}
#controls input {{ padding: 6px 10px; border-radius: 6px; border: 1px solid #444; background: #16213e; color: #eee; font-size: 14px; width: 200px; }}
#controls button {{ padding: 6px 12px; border-radius: 6px; border: 1px solid #444; background: #16213e; color: #eee; cursor: pointer; font-size: 13px; }}
#controls button.active {{ background: #0f3460; border-color: #e94560; }}
#controls button:hover {{ background: #0f3460; }}
#tooltip {{ position: fixed; display: none; background: #16213e; border: 1px solid #555; border-radius: 8px; padding: 12px 16px; max-width: 360px; font-size: 13px; line-height: 1.5; z-index: 20; pointer-events: none; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
#tooltip h3 {{ margin-bottom: 4px; font-size: 15px; }}
#tooltip .type-badge {{ display: inline-block; padding: 1px 8px; border-radius: 4px; font-size: 11px; margin-bottom: 6px; color: #fff; }}
svg {{ width: 100vw; height: 100vh; }}
.link {{ stroke-opacity: 0.5; }}
.node circle {{ stroke: #fff; stroke-width: 1.5; cursor: pointer; }}
.node text {{ font-size: 10px; fill: #ccc; pointer-events: none; }}
.legend {{ position: fixed; bottom: 12px; left: 12px; background: #16213e; border: 1px solid #444; border-radius: 8px; padding: 10px 14px; z-index: 10; font-size: 12px; max-width: 220px; }}
.legend h4 {{ font-size: 11px; margin: 4px 0 2px 0; text-transform: uppercase; letter-spacing: 0.5px; color: #888; }}
.legend-item {{ display: flex; align-items: center; gap: 6px; margin: 3px 0; }}
.legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
.legend-bar {{ width: 16px; height: 3px; border-radius: 2px; }}
</style>
</head>
<body>
<div id="controls">
  <input type="text" id="search" placeholder="Search nodes...">
  <button class="filter-btn active" data-type="all">All</button>
  <button class="filter-btn" data-type="source-summary">Sources</button>
  <button class="filter-btn" data-type="concept">Concepts</button>
  <button class="filter-btn" data-type="entity">Entities</button>
  <button class="filter-btn" data-type="comparison">Comparisons</button>
</div>
<div id="tooltip"></div>
<div class="legend">
  <h4>Nodes</h4>
  {node_legend}
  <h4>Edges (predicates)</h4>
  {edge_legend}
</div>
<svg></svg>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const NODE_COLORS = {node_colors_js};
const EDGE_COLORS = {edge_colors_js};
const graph = {data_js};
const width = window.innerWidth, height = window.innerHeight;

const svg = d3.select("svg").attr("viewBox", [0, 0, width, height]);
svg.append("defs").selectAll("marker")
  .data(Object.keys(EDGE_COLORS)).join("marker")
  .attr("id", d => "arrow-" + d)
  .attr("viewBox", "0 -5 10 10").attr("refX", 18).attr("refY", 0)
  .attr("markerWidth", 6).attr("markerHeight", 6).attr("orient", "auto")
  .append("path").attr("d", "M0,-5L10,0L0,5").attr("fill", d => EDGE_COLORS[d]);

const g = svg.append("g");

const zoom = d3.zoom().scaleExtent([0.1, 8]).on("zoom", (e) => g.attr("transform", e.transform));
svg.call(zoom);

const sim = d3.forceSimulation(graph.nodes)
  .force("link", d3.forceLink(graph.links).id(d => d.id).distance(100))
  .force("charge", d3.forceManyBody().strength(-300))
  .force("center", d3.forceCenter(width / 2, height / 2))
  .force("collision", d3.forceCollide().radius(d => nodeRadius(d) + 4));

function nodeRadius(d) {{ return Math.max(6, Math.min(24, 4 + d.connections * 1.5)); }}

const link = g.append("g").selectAll("line")
  .data(graph.links).join("line")
  .attr("class", "link")
  .attr("stroke", d => EDGE_COLORS[d.predicate] || "#555")
  .attr("stroke-width", d => d.predicate === "mentions" ? 0.8 : 1.5)
  .attr("marker-end", d => EDGE_COLORS[d.predicate] ? "url(#arrow-" + d.predicate + ")" : null);

const node = g.append("g").selectAll("g")
  .data(graph.nodes).join("g").attr("class", "node");

node.append("circle")
  .attr("r", d => nodeRadius(d))
  .attr("fill", d => NODE_COLORS[d.type] || "#999")
  .on("mouseover", showTooltip).on("mouseout", hideTooltip)
  .call(d3.drag().on("start", dragStart).on("drag", dragging).on("end", dragEnd));

node.append("text").attr("dx", d => nodeRadius(d) + 4).attr("dy", 4)
  .text(d => d.title.length > 30 ? d.title.slice(0, 28) + "..." : d.title);

sim.on("tick", () => {{
  link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
  node.attr("transform", d => `translate(${{d.x}},${{d.y}})`);
}});

function showTooltip(e, d) {{
  const tt = document.getElementById("tooltip");
  const color = NODE_COLORS[d.type] || "#999";
  const title = document.createElement("h3");
  title.textContent = d.title;

  const badge = document.createElement("span");
  badge.className = "type-badge";
  badge.style.background = color;
  badge.textContent = d.type;

  const summary = document.createTextNode(d.summary || "No summary.");

  const connections = document.createElement("small");
  connections.textContent = `${{d.connections}} connections`;

  tt.replaceChildren(
    title,
    badge,
    document.createElement("br"),
    document.createElement("br"),
    summary,
    document.createElement("br"),
    document.createElement("br"),
    connections,
  );
  tt.style.display = "block";
  tt.style.left = (e.pageX + 16) + "px";
  tt.style.top = (e.pageY - 10) + "px";
}}
function hideTooltip() {{ document.getElementById("tooltip").style.display = "none"; }}

function dragStart(e, d) {{ if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }}
function dragging(e, d) {{ d.fx = e.x; d.fy = e.y; }}
function dragEnd(e, d) {{ if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }}

document.getElementById("search").addEventListener("input", function() {{
  const q = this.value.toLowerCase();
  node.style("opacity", d => (!q || d.title.toLowerCase().includes(q) || d.id.toLowerCase().includes(q)) ? 1 : 0.1);
  link.style("opacity", d => {{
    if (!q) return 0.5;
    const sMatch = d.source.title.toLowerCase().includes(q) || d.source.id.toLowerCase().includes(q);
    const tMatch = d.target.title.toLowerCase().includes(q) || d.target.id.toLowerCase().includes(q);
    return (sMatch || tMatch) ? 0.6 : 0.05;
  }});
}});

let activeType = "all";
document.querySelectorAll(".filter-btn").forEach(btn => {{
  btn.addEventListener("click", function() {{
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    this.classList.add("active");
    activeType = this.dataset.type;
    node.style("opacity", d => (activeType === "all" || d.type === activeType) ? 1 : 0.08);
    link.style("opacity", d => {{
      if (activeType === "all") return 0.5;
      return (d.source.type === activeType || d.target.type === activeType) ? 0.5 : 0.03;
    }});
  }});
}});
</script>
</body>
</html>"""


def generate_svg(graph_data):
    nodes = graph_data["nodes"]
    links = graph_data["links"]
    W, H = 1200, 900

    # Circular layout with type grouping.
    type_groups = {}
    for n in nodes:
        type_groups.setdefault(n["type"], []).append(n)

    cx, cy = W / 2, H / 2
    angle = 0
    for typ, group in type_groups.items():
        r = 200 + len(group) * 15
        step = 2 * math.pi / max(len(group), 1)
        for i, n in enumerate(group):
            a = angle + i * step
            n["x"] = cx + r * math.cos(a)
            n["y"] = cy + r * math.sin(a)
        angle += 2 * math.pi / max(len(type_groups), 1)

    pos = {n["id"]: [n["x"], n["y"]] for n in nodes}
    for _ in range(80):
        ids = list(pos.keys())
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                dx = pos[ids[i]][0] - pos[ids[j]][0]
                dy = pos[ids[i]][1] - pos[ids[j]][1]
                dist = max(math.sqrt(dx * dx + dy * dy), 1)
                force = 5000 / (dist * dist)
                fx, fy = force * dx / dist, force * dy / dist
                pos[ids[i]][0] += fx
                pos[ids[i]][1] += fy
                pos[ids[j]][0] -= fx
                pos[ids[j]][1] -= fy

        for lnk in links:
            sid = lnk["source"] if isinstance(lnk["source"], str) else lnk["source"]["id"]
            tid = lnk["target"] if isinstance(lnk["target"], str) else lnk["target"]["id"]
            if sid not in pos or tid not in pos:
                continue
            dx = pos[tid][0] - pos[sid][0]
            dy = pos[tid][1] - pos[sid][1]
            dist = max(math.sqrt(dx * dx + dy * dy), 1)
            force = (dist - 120) * 0.005
            fx, fy = force * dx / dist, force * dy / dist
            pos[sid][0] += fx
            pos[sid][1] += fy
            pos[tid][0] -= fx
            pos[tid][1] -= fy

        for nid in pos:
            pos[nid][0] += (cx - pos[nid][0]) * 0.01
            pos[nid][1] += (cy - pos[nid][1]) * 0.01

    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append(f'<rect width="{W}" height="{H}" fill="#1a1a2e"/>')

    for lnk in links:
        sid = lnk["source"] if isinstance(lnk["source"], str) else lnk["source"]["id"]
        tid = lnk["target"] if isinstance(lnk["target"], str) else lnk["target"]["id"]
        pred = lnk.get("predicate", "mentions")
        if sid in pos and tid in pos:
            color = PREDICATE_COLORS.get(pred, "#555")
            opacity = 0.2 if pred == "mentions" else 0.55
            width = 0.8 if pred == "mentions" else 1.4
            lines.append(
                f'<line x1="{pos[sid][0]:.1f}" y1="{pos[sid][1]:.1f}" '
                f'x2="{pos[tid][0]:.1f}" y2="{pos[tid][1]:.1f}" '
                f'stroke="{color}" stroke-opacity="{opacity}" stroke-width="{width}"/>'
            )

    for n in nodes:
        if n["id"] not in pos:
            continue
        x, y = pos[n["id"]]
        r = max(6, min(24, 4 + n["connections"] * 1.5))
        color = NODE_COLORS.get(n["type"], "#999")
        title = n["title"][:28] + "..." if len(n["title"]) > 30 else n["title"]
        safe_title = html.escape(title, quote=True)
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" stroke="#fff" stroke-width="1"/>')
        lines.append(f'<text x="{x + r + 3:.1f}" y="{y + 3:.1f}" font-size="9" fill="#ccc" font-family="sans-serif">{safe_title}</text>')

    # Legend: node types + edge predicates.
    ly = 30
    lines.append(f'<text x="20" y="{ly}" font-size="12" fill="#fff" font-family="sans-serif" font-weight="bold">Nodes</text>')
    ly += 18
    for typ, color in NODE_COLORS.items():
        if typ in ("source", "meta"):
            continue
        lines.append(f'<circle cx="30" cy="{ly}" r="5" fill="{color}"/>')
        lines.append(f'<text x="42" y="{ly + 4}" font-size="11" fill="#ccc" font-family="sans-serif">{typ}</text>')
        ly += 18

    ly += 8
    lines.append(f'<text x="20" y="{ly}" font-size="12" fill="#fff" font-family="sans-serif" font-weight="bold">Edges (predicate)</text>')
    ly += 18
    for pred, color in PREDICATE_COLORS.items():
        lines.append(f'<line x1="22" y1="{ly}" x2="40" y2="{ly}" stroke="{color}" stroke-width="2"/>')
        lines.append(f'<text x="46" y="{ly + 4}" font-size="11" fill="#ccc" font-family="sans-serif">{pred}</text>')
        ly += 16

    lines.append("</svg>")
    return "\n".join(lines)


# ---------------------------------------------------------------------- #
#  Main
# ---------------------------------------------------------------------- #
def main():
    os.makedirs(OUTPUT, exist_ok=True)
    nodes, edges = load_graph()
    graph_data = build_graph_data(nodes, edges)

    html_path = os.path.join(OUTPUT, "knowledge-graph.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(generate_html(graph_data))
    print(f"Generated: {html_path}")

    svg_path = os.path.join(OUTPUT, "knowledge-graph.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(generate_svg(graph_data))
    print(f"Generated: {svg_path}")

    by_pred = {}
    for e in graph_data["links"]:
        by_pred[e["predicate"]] = by_pred.get(e["predicate"], 0) + 1
    print(f"  {len(graph_data['nodes'])} nodes, {len(graph_data['links'])} links")
    for pred, n in sorted(by_pred.items(), key=lambda x: -x[1]):
        print(f"    {pred}: {n}")


if __name__ == "__main__":
    main()
