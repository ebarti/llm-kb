#!/usr/bin/env python3
"""Obsidian Canvas Generator - Generate .canvas JSON files for wiki topics."""

import json
import math
import os
import re
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")

COLORS = {
    "source-summary": "1",  # Obsidian color codes: 1=red, 2=orange, 3=yellow, 4=green, 5=cyan, 6=purple
    "source": "1",
    "concept": "4",
    "entity": "2",
    "comparison": "6",
}

EDGE_COLORS = {
    "source-to-concept": "1",  # red
    "concept-to-concept": "4",  # green
    "default": "5",  # cyan
}


def parse_frontmatter(text):
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return fm
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def extract_wikilinks(text):
    body = re.sub(r"^---.*?---", "", text, count=1, flags=re.DOTALL)
    return list(set(re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", body)))


def normalise(link):
    link = link.strip()
    if link.startswith("wiki/"):
        link = link[5:]
    if link.startswith("raw/"):
        return None
    return link


def scan_wiki():
    nodes = {}
    edges = []
    for dirpath, _, filenames in os.walk(WIKI):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, WIKI).replace(".md", "")
            parent = rel.split("/")[0]
            if parent.startswith("_") or rel in ("log",):
                continue
            text = open(fpath, encoding="utf-8").read()
            fm = parse_frontmatter(text)
            node_type = fm.get("type", parent)
            nodes[rel] = {
                "title": fm.get("title", fn.replace(".md", "")),
                "type": node_type,
                "summary": fm.get("summary", ""),
            }
            for link in extract_wikilinks(text):
                target = normalise(link)
                if target and target != rel:
                    edges.append((rel, target))
    return nodes, edges


def make_id(s):
    return s.replace("/", "-").replace(" ", "-")


def generate_topic_canvas(topic, nodes, edges):
    """Generate a canvas centered on a specific topic/concept."""
    # Find the node
    center_id = None
    for nid in nodes:
        if nid.endswith("/" + topic) or nid == topic or nid.split("/")[-1] == topic:
            center_id = nid
            break
    if not center_id:
        print(f"Topic '{topic}' not found in wiki. Available topics:")
        for nid in sorted(nodes):
            print(f"  {nid}")
        sys.exit(1)

    # Find connected nodes (1 hop)
    connected = set()
    relevant_edges = []
    for src, tgt in edges:
        if src == center_id and tgt in nodes:
            connected.add(tgt)
            relevant_edges.append((src, tgt))
        elif tgt == center_id and src in nodes:
            connected.add(src)
            relevant_edges.append((src, tgt))

    # Layout: center node in middle, connected nodes in a circle
    cx, cy = 0, 0
    node_w, node_h = 320, 120
    center_w, center_h = 400, 160

    canvas_nodes = []
    canvas_edges = []

    # Center node
    canvas_nodes.append({
        "id": make_id(center_id),
        "type": "file",
        "file": f"wiki/{center_id}.md",
        "x": int(cx - center_w / 2),
        "y": int(cy - center_h / 2),
        "width": center_w,
        "height": center_h,
        "color": COLORS.get(nodes[center_id]["type"], "5"),
    })

    # Separate into sources and concepts
    source_nodes = [n for n in connected if n.startswith("sources/")]
    concept_nodes = [n for n in connected if n.startswith("concepts/")]
    other_nodes = [n for n in connected if not n.startswith("sources/") and not n.startswith("concepts/")]

    # Layout sources on the left arc, concepts on the right arc
    radius = 500
    groups = [
        (source_nodes, -math.pi * 0.75, -math.pi * 0.25),
        (concept_nodes, math.pi * 0.25, math.pi * 0.75),
        (other_nodes, math.pi * 0.85, math.pi * 1.15),
    ]

    for group, start_angle, end_angle in groups:
        if not group:
            continue
        step = (end_angle - start_angle) / max(len(group), 1)
        for i, nid in enumerate(sorted(group)):
            angle = start_angle + i * step
            nx = cx + radius * math.cos(angle) - node_w / 2
            ny = cy + radius * math.sin(angle) - node_h / 2
            canvas_nodes.append({
                "id": make_id(nid),
                "type": "file",
                "file": f"wiki/{nid}.md",
                "x": int(nx),
                "y": int(ny),
                "width": node_w,
                "height": node_h,
                "color": COLORS.get(nodes[nid]["type"], "5"),
            })

    # Edges
    for src, tgt in relevant_edges:
        src_type = nodes.get(src, {}).get("type", "")
        tgt_type = nodes.get(tgt, {}).get("type", "")
        if "source" in src_type and "concept" in tgt_type:
            edge_color = EDGE_COLORS["source-to-concept"]
        elif "concept" in src_type and "concept" in tgt_type:
            edge_color = EDGE_COLORS["concept-to-concept"]
        else:
            edge_color = EDGE_COLORS["default"]

        # Determine sides
        from_side = "right" if src == center_id else "left"
        to_side = "left" if tgt == center_id else "right"
        if src != center_id and tgt != center_id:
            from_side = "right"
            to_side = "left"

        canvas_edges.append({
            "id": f"edge-{make_id(src)}-{make_id(tgt)}",
            "fromNode": make_id(src),
            "toNode": make_id(tgt),
            "fromSide": from_side,
            "toSide": to_side,
            "color": edge_color,
        })

    return {"nodes": canvas_nodes, "edges": canvas_edges}


def generate_master_canvas(nodes, edges):
    """Generate a canvas of the entire wiki."""
    canvas_nodes = []
    canvas_edges = []

    # Group by type and lay out in a grid
    type_groups = {}
    for nid, info in nodes.items():
        type_groups.setdefault(info["type"], []).append(nid)

    node_w, node_h = 280, 100
    gap_x, gap_y = 60, 40
    group_gap = 200
    current_y = 0

    for typ, group in sorted(type_groups.items()):
        cols = max(1, min(4, len(group)))
        for i, nid in enumerate(sorted(group)):
            col = i % cols
            row = i // cols
            x = col * (node_w + gap_x)
            y = current_y + row * (node_h + gap_y)
            canvas_nodes.append({
                "id": make_id(nid),
                "type": "file",
                "file": f"wiki/{nid}.md",
                "x": x,
                "y": y,
                "width": node_w,
                "height": node_h,
                "color": COLORS.get(typ, "5"),
            })
        rows_used = (len(group) - 1) // cols + 1
        current_y += rows_used * (node_h + gap_y) + group_gap

    # Edges
    node_set = set(nodes.keys())
    for src, tgt in edges:
        if src in node_set and tgt in node_set:
            src_type = nodes[src]["type"]
            tgt_type = nodes[tgt]["type"]
            if "source" in src_type and "concept" in tgt_type:
                edge_color = EDGE_COLORS["source-to-concept"]
            elif "concept" in src_type and "concept" in tgt_type:
                edge_color = EDGE_COLORS["concept-to-concept"]
            else:
                edge_color = EDGE_COLORS["default"]

            canvas_edges.append({
                "id": f"edge-{make_id(src)}-{make_id(tgt)}",
                "fromNode": make_id(src),
                "toNode": make_id(tgt),
                "fromSide": "right",
                "toSide": "left",
                "color": edge_color,
            })

    return {"nodes": canvas_nodes, "edges": canvas_edges}


def main():
    nodes, edges = scan_wiki()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python canvas.py <topic>     Generate canvas for a specific topic")
        print("  python canvas.py --all       Generate master canvas of entire wiki")
        print()
        print("Available topics:")
        for nid in sorted(nodes):
            print(f"  {nid.split('/')[-1]}")
        sys.exit(0)

    if sys.argv[1] == "--all":
        canvas = generate_master_canvas(nodes, edges)
        out_path = os.path.join(WIKI, "master-canvas.canvas")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(canvas, f, indent=2)
        print(f"Generated: {out_path}")
        print(f"  {len(canvas['nodes'])} nodes, {len(canvas['edges'])} edges")
    else:
        topic = sys.argv[1]
        canvas = generate_topic_canvas(topic, nodes, edges)
        # Determine output path based on topic type
        center_id = None
        for nid in nodes:
            if nid.endswith("/" + topic) or nid == topic or nid.split("/")[-1] == topic:
                center_id = nid
                break
        if center_id:
            out_path = os.path.join(WIKI, center_id + ".canvas")
        else:
            out_path = os.path.join(WIKI, "concepts", topic + ".canvas")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(canvas, f, indent=2)
        print(f"Generated: {out_path}")
        print(f"  {len(canvas['nodes'])} nodes, {len(canvas['edges'])} edges")


if __name__ == "__main__":
    main()
