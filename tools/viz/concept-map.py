#!/usr/bin/env python3
"""Concept Map Generator - Hierarchical D3.js tree/cluster layout from wiki metadata."""

import json
import os
import re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")
OUTPUT = os.path.join(BASE, "output", "images")

COLORS = {
    "source-summary": "#4a90d9",
    "source": "#4a90d9",
    "concept": "#2ecc71",
    "entity": "#e67e22",
    "comparison": "#9b59b6",
}


def parse_links_md():
    """Parse wiki/_meta/links.md to extract the link graph."""
    links_path = os.path.join(WIKI, "_meta", "links.md")
    if not os.path.exists(links_path):
        return {}, {}
    text = open(links_path, encoding="utf-8").read()

    outgoing = {}  # node -> [targets]
    incoming = {}  # node -> [sources]
    current = None
    for line in text.split("\n"):
        m = re.match(r"^## (.+)$", line)
        if m:
            current = m.group(1).strip()
            continue
        if current and line.startswith("->") or line.startswith("→"):
            targets = re.findall(r"\[\[([^\]]+)\]\]", line)
            outgoing[current] = targets
        if current and (line.startswith("<-") or line.startswith("←")):
            sources = re.findall(r"\[\[([^\]]+)\]\]", line)
            incoming[current] = sources
    return outgoing, incoming


def parse_summaries_md():
    """Parse wiki/_meta/summaries.md for one-line summaries."""
    path = os.path.join(WIKI, "_meta", "summaries.md")
    if not os.path.exists(path):
        return {}
    text = open(path, encoding="utf-8").read()
    sums = {}
    for m in re.finditer(r"\[\[([^\]]+)\]\]\s*[-—]\s*(.+)", text):
        sums[m.group(1)] = m.group(2).strip()
    return sums


def build_tree(outgoing, incoming, summaries):
    """Build a hierarchical tree for D3 from the link data."""
    # Group: sources feed into concepts
    # Root -> type groups -> individual nodes
    concepts = sorted(set(k for k in outgoing if k.startswith("concepts/")))
    sources = sorted(set(k for k in outgoing if k.startswith("sources/")))

    # For each concept, find which sources point to it
    concept_sources = {}
    for src in sources:
        for tgt in outgoing.get(src, []):
            if tgt.startswith("concepts/"):
                concept_sources.setdefault(tgt, []).append(src)

    # For each concept, find related concepts
    concept_related = {}
    for c in concepts:
        related = [t for t in outgoing.get(c, []) if t.startswith("concepts/") and t != c]
        concept_related[c] = related

    # Build tree: root -> concept clusters
    # Hub concepts (most connections) become cluster centers
    conn_count = {}
    for c in concepts:
        conn_count[c] = len(incoming.get(c, [])) + len(outgoing.get(c, []))

    # Sort concepts by connectivity
    ranked = sorted(concepts, key=lambda c: conn_count.get(c, 0), reverse=True)

    # Build D3 tree data
    children = []

    # Sources group
    src_children = []
    for s in sources:
        label = s.split("/")[-1]
        src_children.append({
            "name": label,
            "id": s,
            "type": "source-summary",
            "summary": summaries.get(s, ""),
            "size": len(outgoing.get(s, [])),
        })
    if src_children:
        children.append({"name": "Sources", "id": "_sources", "type": "group", "children": src_children})

    # Concepts group - cluster by hub relationships
    assigned = set()
    for hub in ranked[:6]:  # top 6 hubs
        if hub in assigned:
            continue
        cluster_nodes = [hub]
        assigned.add(hub)
        for rel in concept_related.get(hub, []):
            if rel not in assigned and rel in concepts:
                cluster_nodes.append(rel)
                assigned.add(rel)

        cluster_children = []
        for c in cluster_nodes:
            label = c.split("/")[-1]
            node = {
                "name": label,
                "id": c,
                "type": "concept",
                "summary": summaries.get(c, ""),
                "size": conn_count.get(c, 1),
            }
            # Attach sources as children of concepts
            src_kids = []
            for src in concept_sources.get(c, []):
                src_kids.append({
                    "name": src.split("/")[-1],
                    "id": src,
                    "type": "source-summary",
                    "summary": summaries.get(src, ""),
                    "size": 1,
                })
            if src_kids:
                node["children"] = src_kids
            cluster_children.append(node)

        hub_label = hub.split("/")[-1]
        children.append({
            "name": hub_label,
            "id": hub + "_cluster",
            "type": "cluster",
            "children": cluster_children,
        })

    # Remaining concepts
    remaining = [c for c in concepts if c not in assigned]
    if remaining:
        rem_children = []
        for c in remaining:
            label = c.split("/")[-1]
            rem_children.append({
                "name": label,
                "id": c,
                "type": "concept",
                "summary": summaries.get(c, ""),
                "size": conn_count.get(c, 1),
            })
        children.append({"name": "Other Concepts", "id": "_other", "type": "group", "children": rem_children})

    return {"name": "Knowledge Base", "id": "_root", "type": "root", "children": children}


def generate_html(tree_data):
    data_js = json.dumps(tree_data)
    colors_js = json.dumps(COLORS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Concept Map</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #1a1a2e; color: #eee; overflow: hidden; }}
h1 {{ position: fixed; top: 10px; left: 50%; transform: translateX(-50%); font-size: 20px; color: #e94560; z-index: 10; }}
#tooltip {{ position: fixed; display: none; background: #16213e; border: 1px solid #555; border-radius: 8px; padding: 12px; max-width: 350px; font-size: 13px; z-index: 20; pointer-events: none; box-shadow: 0 4px 20px rgba(0,0,0,.5); line-height: 1.5; }}
svg {{ width: 100vw; height: 100vh; }}
.link {{ fill: none; stroke: #444; stroke-width: 1.5; }}
.node circle {{ stroke: #fff; stroke-width: 1.5; cursor: pointer; }}
.node text {{ font-size: 10px; fill: #ccc; }}
.legend {{ position: fixed; bottom: 12px; left: 12px; background: #16213e; border: 1px solid #444; border-radius: 8px; padding: 10px 14px; z-index: 10; font-size: 12px; }}
.legend-item {{ display: flex; align-items: center; gap: 6px; margin: 3px 0; }}
.legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
</style>
</head>
<body>
<h1>Concept Map</h1>
<div id="tooltip"></div>
<div class="legend">
  <div class="legend-item"><div class="legend-dot" style="background:#4a90d9"></div> Sources</div>
  <div class="legend-item"><div class="legend-dot" style="background:#2ecc71"></div> Concepts</div>
  <div class="legend-item"><div class="legend-dot" style="background:#e67e22"></div> Entities</div>
  <div class="legend-item"><div class="legend-dot" style="background:#9b59b6"></div> Comparisons</div>
  <div class="legend-item"><div class="legend-dot" style="background:#e94560"></div> Clusters</div>
</div>
<svg></svg>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const COLORS = {colors_js};
COLORS["cluster"] = "#e94560";
COLORS["group"] = "#555";
COLORS["root"] = "#e94560";
const data = {data_js};

const width = window.innerWidth, height = window.innerHeight;
const svg = d3.select("svg").attr("viewBox", [-width/2, -height/2, width, height]);
const g = svg.append("g");

const zoom = d3.zoom().scaleExtent([0.2, 5]).on("zoom", e => g.attr("transform", e.transform));
svg.call(zoom);

const root = d3.hierarchy(data);
const treeLayout = d3.cluster().size([2 * Math.PI, Math.min(width, height) / 2 - 120]);
treeLayout(root);

// Radial layout helper
function radialPoint(angle, radius) {{
  return [(radius) * Math.cos(angle - Math.PI / 2), (radius) * Math.sin(angle - Math.PI / 2)];
}}

// Links
g.selectAll(".link").data(root.links()).join("path")
  .attr("class", "link")
  .attr("d", d3.linkRadial().angle(d => d.x).radius(d => d.y));

// Nodes
const node = g.selectAll(".node").data(root.descendants()).join("g")
  .attr("class", "node")
  .attr("transform", d => `translate(${{radialPoint(d.x, d.y)}})`);

const tooltip = document.getElementById("tooltip");

node.append("circle")
  .attr("r", d => d.children ? 6 : Math.max(4, Math.min(12, (d.data.size || 1) * 1.5)))
  .attr("fill", d => COLORS[d.data.type] || "#999")
  .on("mouseover", (e, d) => {{
    tooltip.innerHTML = `<strong>${{d.data.name}}</strong><br><small style="color:${{COLORS[d.data.type] || '#999'}}">${{d.data.type}}</small><br><br>${{d.data.summary || ""}}`;
    tooltip.style.display = "block";
    tooltip.style.left = (e.pageX + 12) + "px";
    tooltip.style.top = (e.pageY - 10) + "px";
  }})
  .on("mouseout", () => {{ tooltip.style.display = "none"; }});

node.append("text")
  .attr("dy", "0.31em")
  .attr("x", d => d.x < Math.PI === !d.children ? 8 : -8)
  .attr("text-anchor", d => d.x < Math.PI === !d.children ? "start" : "end")
  .attr("transform", d => d.x >= Math.PI ? "rotate(180)" : null)
  .text(d => d.data.name.length > 25 ? d.data.name.slice(0, 23) + "..." : d.data.name)
  .style("font-size", d => d.children ? "11px" : "9px")
  .style("fill", d => d.children ? "#fff" : "#bbb");
</script>
</body>
</html>"""


def main():
    os.makedirs(OUTPUT, exist_ok=True)
    outgoing, incoming = parse_links_md()
    summaries = parse_summaries_md()
    tree_data = build_tree(outgoing, incoming, summaries)

    html_path = os.path.join(OUTPUT, "concept-map.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(generate_html(tree_data))
    print(f"Generated: {html_path}")


if __name__ == "__main__":
    main()
