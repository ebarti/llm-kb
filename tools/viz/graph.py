#!/usr/bin/env python3
"""Knowledge Graph Generator - Interactive D3.js force-directed graph + static SVG."""

import json
import os
import re
import sys
import math

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")
OUTPUT = os.path.join(BASE, "output", "images")

COLORS = {
    "source-summary": "#4a90d9",
    "source": "#4a90d9",
    "concept": "#2ecc71",
    "entity": "#e67e22",
    "comparison": "#9b59b6",
    "meta": "#95a5a6",
}

TYPE_DIRS = {
    "sources": "source-summary",
    "concepts": "concept",
    "entities": "entity",
    "comparisons": "comparison",
}


def parse_frontmatter(text):
    """Extract YAML frontmatter as a dict (simple parser, no pyyaml needed)."""
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return fm
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
    return fm


def extract_wikilinks(text):
    """Return set of wikilink targets from body text (after frontmatter)."""
    body = re.sub(r"^---.*?---", "", text, count=1, flags=re.DOTALL)
    return set(re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", body))


def normalise(link):
    """Normalise a wikilink target to a relative wiki path without .md."""
    link = link.strip()
    if link.startswith("wiki/"):
        link = link[5:]
    # Remove raw/ prefix links -- they point outside the wiki
    if link.startswith("raw/"):
        return None
    return link


def scan_wiki():
    """Scan all wiki markdown files, return nodes dict and edges list."""
    nodes = {}  # id -> {title, type, summary, links_out}
    edges = []  # (source_id, target_id)

    for dirpath, _, filenames in os.walk(WIKI):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, WIKI).replace(".md", "")
            # skip _meta, _index, log
            parent = rel.split("/")[0]
            if parent.startswith("_") or rel in ("log",):
                continue

            text = open(fpath, encoding="utf-8").read()
            fm = parse_frontmatter(text)
            wikilinks = extract_wikilinks(text)

            node_type = fm.get("type", TYPE_DIRS.get(parent, "concept"))
            nodes[rel] = {
                "title": fm.get("title", fn.replace(".md", "")),
                "type": node_type,
                "summary": fm.get("summary", ""),
            }

            for link in wikilinks:
                target = normalise(link)
                if target and target != rel:
                    edges.append((rel, target))

    return nodes, edges


def build_graph_data(nodes, edges):
    """Build D3-compatible graph JSON."""
    node_ids = set(nodes.keys())
    # Count connections per node
    conn = {nid: 0 for nid in node_ids}
    valid_edges = []
    for src, tgt in edges:
        if src in node_ids and tgt in node_ids:
            conn[src] = conn.get(src, 0) + 1
            conn[tgt] = conn.get(tgt, 0) + 1
            valid_edges.append({"source": src, "target": tgt})

    d3_nodes = []
    for nid, info in nodes.items():
        d3_nodes.append({
            "id": nid,
            "title": info["title"],
            "type": info["type"],
            "summary": info["summary"],
            "connections": conn.get(nid, 0),
        })

    return {"nodes": d3_nodes, "links": valid_edges}


def generate_html(graph_data):
    """Generate self-contained interactive HTML with D3.js."""
    colors_js = json.dumps(COLORS)
    data_js = json.dumps(graph_data)

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
.link {{ stroke-opacity: 0.3; }}
.node circle {{ stroke: #fff; stroke-width: 1.5; cursor: pointer; }}
.node text {{ font-size: 10px; fill: #ccc; pointer-events: none; }}
.legend {{ position: fixed; bottom: 12px; left: 12px; background: #16213e; border: 1px solid #444; border-radius: 8px; padding: 10px 14px; z-index: 10; font-size: 12px; }}
.legend-item {{ display: flex; align-items: center; gap: 6px; margin: 3px 0; }}
.legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
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
  <div class="legend-item"><div class="legend-dot" style="background:#4a90d9"></div> Sources</div>
  <div class="legend-item"><div class="legend-dot" style="background:#2ecc71"></div> Concepts</div>
  <div class="legend-item"><div class="legend-dot" style="background:#e67e22"></div> Entities</div>
  <div class="legend-item"><div class="legend-dot" style="background:#9b59b6"></div> Comparisons</div>
</div>
<svg></svg>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const COLORS = {colors_js};
const graph = {data_js};
const width = window.innerWidth, height = window.innerHeight;

const svg = d3.select("svg").attr("viewBox", [0, 0, width, height]);
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
  .attr("class", "link").attr("stroke", "#555").attr("stroke-width", 1);

const node = g.append("g").selectAll("g")
  .data(graph.nodes).join("g").attr("class", "node");

node.append("circle")
  .attr("r", d => nodeRadius(d))
  .attr("fill", d => COLORS[d.type] || "#999")
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
  const color = COLORS[d.type] || "#999";
  tt.innerHTML = `<h3>${{d.title}}</h3><span class="type-badge" style="background:${{color}}">${{d.type}}</span><br><br>${{d.summary || "No summary."}}<br><br><small>${{d.connections}} connections</small>`;
  tt.style.display = "block";
  tt.style.left = (e.pageX + 16) + "px";
  tt.style.top = (e.pageY - 10) + "px";
}}
function hideTooltip() {{ document.getElementById("tooltip").style.display = "none"; }}

function dragStart(e, d) {{ if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }}
function dragging(e, d) {{ d.fx = e.x; d.fy = e.y; }}
function dragEnd(e, d) {{ if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }}

// Search
document.getElementById("search").addEventListener("input", function() {{
  const q = this.value.toLowerCase();
  node.style("opacity", d => (!q || d.title.toLowerCase().includes(q) || d.id.toLowerCase().includes(q)) ? 1 : 0.1);
  link.style("opacity", d => {{
    if (!q) return 1;
    const sMatch = d.source.title.toLowerCase().includes(q) || d.source.id.toLowerCase().includes(q);
    const tMatch = d.target.title.toLowerCase().includes(q) || d.target.id.toLowerCase().includes(q);
    return (sMatch || tMatch) ? 0.6 : 0.05;
  }});
}});

// Filter
let activeType = "all";
document.querySelectorAll(".filter-btn").forEach(btn => {{
  btn.addEventListener("click", function() {{
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    this.classList.add("active");
    activeType = this.dataset.type;
    node.style("opacity", d => (activeType === "all" || d.type === activeType) ? 1 : 0.08);
    link.style("opacity", d => {{
      if (activeType === "all") return 1;
      return (d.source.type === activeType || d.target.type === activeType) ? 0.5 : 0.03;
    }});
  }});
}});
</script>
</body>
</html>"""


def generate_svg(graph_data):
    """Generate a static SVG of the knowledge graph using simple force simulation."""
    nodes = graph_data["nodes"]
    links = graph_data["links"]
    W, H = 1200, 900

    # Build index
    idx = {n["id"]: i for i, n in enumerate(nodes)}
    # Simple circular layout with type grouping
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

    # Simple force iterations
    pos = {n["id"]: [n["x"], n["y"]] for n in nodes}
    for _ in range(80):
        # Repulsion
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

        # Attraction along links
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

        # Center gravity
        for nid in pos:
            pos[nid][0] += (cx - pos[nid][0]) * 0.01
            pos[nid][1] += (cy - pos[nid][1]) * 0.01

    # Build SVG
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append(f'<rect width="{W}" height="{H}" fill="#1a1a2e"/>')

    # Edges
    for lnk in links:
        sid = lnk["source"] if isinstance(lnk["source"], str) else lnk["source"]["id"]
        tid = lnk["target"] if isinstance(lnk["target"], str) else lnk["target"]["id"]
        if sid in pos and tid in pos:
            lines.append(f'<line x1="{pos[sid][0]:.1f}" y1="{pos[sid][1]:.1f}" x2="{pos[tid][0]:.1f}" y2="{pos[tid][1]:.1f}" stroke="#555" stroke-opacity="0.3" stroke-width="1"/>')

    # Nodes
    for n in nodes:
        if n["id"] not in pos:
            continue
        x, y = pos[n["id"]]
        r = max(6, min(24, 4 + n["connections"] * 1.5))
        color = COLORS.get(n["type"], "#999")
        title = n["title"][:28] + "..." if len(n["title"]) > 30 else n["title"]
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" stroke="#fff" stroke-width="1"/>')
        lines.append(f'<text x="{x + r + 3:.1f}" y="{y + 3:.1f}" font-size="9" fill="#ccc" font-family="sans-serif">{title}</text>')

    # Legend
    ly = H - 100
    for i, (typ, color) in enumerate(COLORS.items()):
        if typ in ("meta",):
            continue
        lines.append(f'<circle cx="30" cy="{ly + i * 18}" r="5" fill="{color}"/>')
        lines.append(f'<text x="42" y="{ly + i * 18 + 4}" font-size="11" fill="#ccc" font-family="sans-serif">{typ}</text>')

    lines.append("</svg>")
    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT, exist_ok=True)
    nodes, edges = scan_wiki()
    graph_data = build_graph_data(nodes, edges)

    html_path = os.path.join(OUTPUT, "knowledge-graph.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(generate_html(graph_data))
    print(f"Generated: {html_path}")

    svg_path = os.path.join(OUTPUT, "knowledge-graph.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(generate_svg(graph_data))
    print(f"Generated: {svg_path}")

    print(f"  {len(graph_data['nodes'])} nodes, {len(graph_data['links'])} links")


if __name__ == "__main__":
    main()
