"""Sprint 2 · WS7 — Interactive topology (pyvis + spring_layout).

Martin Sprint 1 feedback:
- #4 Cluster by Team (spatial clustering, not just color)
- #5 Interactive hover/click tooltip

Design:
- `nx.spring_layout` with augmented edge weights: `intra-team weight = 3.0`,
  `inter-team weight = 1.0`. This pulls same-Team nodes together in 2D space.
- pyvis renders the resulting positions; physics engine disabled so the
  spring-layout geometry is preserved.
- Node encoding:
    color = Team
    size  = in_degree
    border width = Isolation_Risk_Tier (High=4 / Medium=2 / Low=1)
    shape = Profile_Type (balanced=circle / hub=diamond / broker=triangle /
            island=square)
    tooltip (title) includes all relevant metrics.
- Edge encoding:
    width = Interaction_Frequency_Weight × 4
    color = Hard (dark gray) / Soft (blue-ish)
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import pandas as pd
from pyvis.network import Network

# Color-blind-friendly palette (ColorBrewer Set2).
TEAM_COLORS = {
    "Information Management": "#66c2a5",
    "Data Engineering": "#fc8d62",
    "Solution Architecture": "#8da0cb",
    "Client Services": "#e78ac3",
    "Platform Engineering": "#a6d854",
    "Analytics & BI": "#ffd92f",
}

PROFILE_SHAPES = {
    "balanced": "dot",
    "hub": "diamond",
    "broker": "triangle",
    "island": "square",
}

TIER_BORDER = {"High": 4, "Medium": 2, "Low": 1}
TIER_BORDER_COLOR = {"High": "#d7191c", "Medium": "#fdae61", "Low": "#9e9e9e"}

EDGE_COLOR = {"Hard": "#505050", "Soft": "#4575b4"}


def build_digraph(nodes: pd.DataFrame, edges: pd.DataFrame) -> nx.DiGraph:
    G = nx.DiGraph()
    for _, r in nodes.iterrows():
        G.add_node(r["EMP_ID"], Team=r["Team"])
    for _, e in edges.iterrows():
        G.add_edge(
            e["Source_EMP_ID"],
            e["Target_EMP_ID"],
            weight=float(e["Interaction_Frequency_Weight"]),
            interaction_type=e["Interaction_Type"],
            freq_label=e["Interaction_Frequency"],
        )
    return G


def compute_team_clustered_positions(
    G: nx.DiGraph,
    intra_team_weight: float = 2.5,
    inter_team_weight: float = 0.3,
    virtual_intra_team_weight: float = 5.0,
    seed: int = 5228,
    iterations: int = 300,
) -> dict[str, tuple[float, float]]:
    """Spring-layout with two reinforcements to create visible team clusters.

    Strategy:
    1. Weight real edges by membership: intra-team real edges get a mid-range
       pull; inter-team real edges get a weak pull.
    2. Inject *virtual* intra-team edges between every pair of same-Team members
       (with a strong `virtual_intra_team_weight`) so clusters cohere regardless
       of whether real nominations exist between them. This is a well-known
       trick for attribute-driven clustering in force-directed layouts.
    """
    team_of = nx.get_node_attributes(G, "Team")

    # Start from an undirected scaffold of the real graph.
    H = nx.Graph()
    for n, attrs in G.nodes(data=True):
        H.add_node(n, **attrs)
    for u, v, d in G.edges(data=True):
        w = intra_team_weight if team_of.get(u) == team_of.get(v) else inter_team_weight
        if H.has_edge(u, v):
            H[u][v]["layout_weight"] = max(H[u][v]["layout_weight"], w)
        else:
            H.add_edge(u, v, layout_weight=w)

    # Inject virtual edges between every pair of same-Team members.
    team_buckets: dict[str, list[str]] = {}
    for n, t in team_of.items():
        team_buckets.setdefault(t, []).append(n)
    for members in team_buckets.values():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                u, v = members[i], members[j]
                if H.has_edge(u, v):
                    # Combine: take max of existing weight and virtual weight.
                    H[u][v]["layout_weight"] = max(
                        H[u][v]["layout_weight"], virtual_intra_team_weight
                    )
                else:
                    H.add_edge(u, v, layout_weight=virtual_intra_team_weight)

    pos = nx.spring_layout(
        H,
        weight="layout_weight",
        seed=seed,
        iterations=iterations,
        k=None,
    )
    return pos


def _scale_positions(
    pos: dict[str, tuple[float, float]], scale: float = 1200.0
) -> dict[str, tuple[float, float]]:
    """Scale spring_layout's [-1, 1]-ish coords to pyvis canvas coords."""
    return {n: (xy[0] * scale, xy[1] * scale) for n, xy in pos.items()}


def render_interactive_topology(
    nodes_with_metrics: pd.DataFrame,
    edges: pd.DataFrame,
    output_html_path: Path,
    notebook_mode: bool = False,
) -> None:
    """Produce a self-contained interactive HTML."""
    G = build_digraph(nodes_with_metrics[["EMP_ID", "Team"]], edges)
    pos = _scale_positions(compute_team_clustered_positions(G))

    net = Network(
        height="820px",
        width="100%",
        directed=True,
        bgcolor="#fafbff",
        font_color="#111",
        notebook=notebook_mode,
        cdn_resources="in_line",  # self-contained HTML
    )
    net.toggle_physics(False)

    metrics_idx = nodes_with_metrics.set_index("EMP_ID")
    for emp_id in G.nodes():
        row = metrics_idx.loc[emp_id]
        team = row["Team"]
        tier = row["Isolation_Risk_Tier"]
        shape = PROFILE_SHAPES.get(row["Profile_Type"], "dot")
        color = TEAM_COLORS.get(team, "#bbbbbb")
        size = int(10 + min(40, 1.8 * int(row["in_degree"])))

        tooltip = (
            f"EMP_ID: {emp_id}\n"
            f"Team: {team}\n"
            f"Seniority: {row['Seniority']} (Years_Exp: {int(row['Years_Exp'])})\n"
            f"Profile_Type: {row['Profile_Type']}\n"
            f"In-degree: {int(row['in_degree'])} | Out-degree: {int(row['out_degree'])}\n"
            f"Betweenness: {float(row['betweenness_centrality']):.4f}\n"
            f"Cross-Team Tie Count: {int(row['Cross_Team_Tie_Count'])}\n"
            f"Weak outbound ties: {int(row['Weak_Tie_Outbound_Count'])} "
            f"(weak cross-team: {int(row['Weak_Cross_Team_Tie_Count'])})\n"
            f"Isolation Score: {float(row['Isolation_Score']):.4f} [Tier: {tier}]"
        )
        label = emp_id.split("_")[-1]  # e.g. '247'
        x, y = pos.get(emp_id, (0.0, 0.0))
        net.add_node(
            emp_id,
            label=label,
            title=tooltip,
            color={"background": color, "border": TIER_BORDER_COLOR[tier]},
            borderWidth=TIER_BORDER[tier],
            borderWidthSelected=TIER_BORDER[tier] + 2,
            shape=shape,
            size=size,
            x=x,
            y=y,
            fixed={"x": True, "y": True},
        )

    for u, v, d in G.edges(data=True):
        net.add_edge(
            u,
            v,
            width=max(1, float(d["weight"]) * 4),
            color=EDGE_COLOR.get(d["interaction_type"], "#909090"),
            title=(
                f"{u} → {v}\n"
                f"Type: {d['interaction_type']}\n"
                f"Frequency: {d['freq_label']} (weight={d['weight']:.2f})"
            ),
            arrows="to",
        )

    net.set_options(
        """
        {
          "nodes": {"font": {"size": 10, "color": "#222"}},
          "edges": {"smooth": {"enabled": true, "type": "dynamic"}, "arrowStrikethrough": false},
          "interaction": {"hover": true, "tooltipDelay": 60, "zoomView": true, "dragView": true},
          "physics": {"enabled": false}
        }
        """
    )

    output_html_path.parent.mkdir(parents=True, exist_ok=True)
    net.save_graph(str(output_html_path))


def _inject_focus_interactions(html: str) -> str:
    """Enhance pyvis HTML with click-to-focus interactions.

    Behavior:
    - Click node: keep node + its incident edges + adjacent nodes highlighted.
    - Click edge: keep edge + its two endpoint nodes highlighted.
    - Others are faded via low alpha.
    - Selection info is mirrored in a fixed panel (besides native hover tooltip).
    """
    marker = "network = new vis.Network(container, data, options);"
    if marker not in html:
        raise ValueError("Could not find vis.Network initialization marker in HTML.")

    focus_js = """
                  network = new vis.Network(container, data, options);

                  var __origNodes = nodes.get().map(function(n) { return JSON.parse(JSON.stringify(n)); });
                  var __origEdges = edges.get().map(function(e) { return JSON.parse(JSON.stringify(e)); });
                  var __nodeById = {};
                  var __edgeById = {};
                  __origNodes.forEach(function(n) { __nodeById[n.id] = n; });
                  __origEdges.forEach(function(e) { __edgeById[e.id] = e; });

                  var __infoPanel = document.createElement("div");
                  __infoPanel.id = "focus-info-panel";
                  __infoPanel.style.position = "fixed";
                  __infoPanel.style.right = "14px";
                  __infoPanel.style.top = "14px";
                  __infoPanel.style.zIndex = "9999";
                  __infoPanel.style.maxWidth = "360px";
                  __infoPanel.style.maxHeight = "70vh";
                  __infoPanel.style.overflow = "auto";
                  __infoPanel.style.whiteSpace = "pre-wrap";
                  __infoPanel.style.fontFamily = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace";
                  __infoPanel.style.fontSize = "12px";
                  __infoPanel.style.lineHeight = "1.4";
                  __infoPanel.style.padding = "10px 12px";
                  __infoPanel.style.background = "rgba(255,255,255,0.96)";
                  __infoPanel.style.border = "1px solid #d9d9d9";
                  __infoPanel.style.borderRadius = "8px";
                  __infoPanel.style.boxShadow = "0 4px 16px rgba(0,0,0,0.12)";
                  __infoPanel.textContent = "Click a node or edge to focus.";
                  document.body.appendChild(__infoPanel);

                  function __toRgba(color, alpha) {
                    if (!color) return "rgba(160,160,160," + alpha + ")";
                    if (typeof color !== "string") return "rgba(160,160,160," + alpha + ")";
                    if (color.indexOf("rgba(") === 0) {
                      return color.replace(/rgba\\((\\d+),\\s*(\\d+),\\s*(\\d+),\\s*[0-9.]+\\)/, "rgba($1,$2,$3," + alpha + ")");
                    }
                    if (color.indexOf("rgb(") === 0) {
                      var inner = color.slice(4, -1);
                      return "rgba(" + inner + "," + alpha + ")";
                    }
                    if (color.indexOf("#") === 0) {
                      var hex = color.slice(1);
                      if (hex.length === 3) {
                        hex = hex.split("").map(function(ch) { return ch + ch; }).join("");
                      }
                      if (hex.length !== 6) return "rgba(160,160,160," + alpha + ")";
                      var r = parseInt(hex.slice(0,2), 16);
                      var g = parseInt(hex.slice(2,4), 16);
                      var b = parseInt(hex.slice(4,6), 16);
                      return "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
                    }
                    return "rgba(160,160,160," + alpha + ")";
                  }

                  function __resetFocus() {
                    nodes.update(__origNodes.map(function(n) { return JSON.parse(JSON.stringify(n)); }));
                    edges.update(__origEdges.map(function(e) { return JSON.parse(JSON.stringify(e)); }));
                    __infoPanel.textContent = "Click a node or edge to focus.";
                  }

                  function __fadeNode(node) {
                    var bg = (node.color && node.color.background) ? node.color.background : "#bbbbbb";
                    var bd = (node.color && node.color.border) ? node.color.border : "#999999";
                    return {
                      id: node.id,
                      color: { background: __toRgba(bg, 0.08), border: __toRgba(bd, 0.12) },
                      font: { color: "rgba(34,34,34,0.20)" }
                    };
                  }

                  function __fadeEdge(edge) {
                    var base = (typeof edge.color === "string") ? edge.color : ((edge.color && edge.color.color) ? edge.color.color : "#909090");
                    return {
                      id: edge.id,
                      color: { color: __toRgba(base, 0.08), highlight: __toRgba(base, 0.25), hover: __toRgba(base, 0.25) },
                      width: 1
                    };
                  }

                  function __focusNode(nodeId) {
                    var connectedEdgeIds = network.getConnectedEdges(nodeId);
                    var keepEdges = {};
                    connectedEdgeIds.forEach(function(eid) { keepEdges[eid] = true; });
                    var connectedNodeIds = network.getConnectedNodes(nodeId);
                    var keepNodes = {};
                    keepNodes[nodeId] = true;
                    connectedNodeIds.forEach(function(nid) { keepNodes[nid] = true; });

                    nodes.update(__origNodes.map(function(n) {
                      return keepNodes[n.id] ? JSON.parse(JSON.stringify(n)) : __fadeNode(n);
                    }));
                    edges.update(__origEdges.map(function(e) {
                      if (keepEdges[e.id]) {
                        var copy = JSON.parse(JSON.stringify(e));
                        copy.width = Math.max((copy.width || 1) * 1.35, 2);
                        return copy;
                      }
                      return __fadeEdge(e);
                    }));

                    var n = __nodeById[nodeId];
                    __infoPanel.textContent = n && n.title ? n.title : String(nodeId);
                  }

                  function __focusEdge(edgeId) {
                    var e = __edgeById[edgeId];
                    if (!e) return;
                    var keepNodes = {};
                    keepNodes[e.from] = true;
                    keepNodes[e.to] = true;

                    nodes.update(__origNodes.map(function(n) {
                      return keepNodes[n.id] ? JSON.parse(JSON.stringify(n)) : __fadeNode(n);
                    }));
                    edges.update(__origEdges.map(function(cur) {
                      if (cur.id === edgeId) {
                        var copy = JSON.parse(JSON.stringify(cur));
                        copy.width = Math.max((copy.width || 1) * 1.8, 3);
                        return copy;
                      }
                      return __fadeEdge(cur);
                    }));

                    __infoPanel.textContent = e.title ? e.title : (String(e.from) + " -> " + String(e.to));
                  }

                  network.on("click", function(params) {
                    if (params.nodes && params.nodes.length > 0) {
                      __focusNode(params.nodes[0]);
                      return;
                    }
                    if (params.edges && params.edges.length > 0) {
                      __focusEdge(params.edges[0]);
                      return;
                    }
                    __resetFocus();
                  });
    """
    return html.replace(marker, focus_js, 1)


def render_interactive_topology_v2(
    nodes_with_metrics: pd.DataFrame,
    edges: pd.DataFrame,
    output_html_path: Path,
    notebook_mode: bool = False,
) -> None:
    """Render v2 HTML with click-to-focus emphasis interactions."""
    render_interactive_topology(
        nodes_with_metrics=nodes_with_metrics,
        edges=edges,
        output_html_path=output_html_path,
        notebook_mode=notebook_mode,
    )
    html = output_html_path.read_text(encoding="utf-8")
    enhanced = _inject_focus_interactions(html)
    output_html_path.write_text(enhanced, encoding="utf-8")


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(Path(__file__).parent))
    from metrics import load_edges_and_nodes

    base = Path(__file__).resolve().parents[1]
    nodes_with_metrics = pd.read_csv(base / "sprints" / "sprint2" / "outputs" / "sprint2_nodes_with_metrics.csv")
    _, edges = load_edges_and_nodes(base)

    out_path = base / "sprints" / "sprint2" / "outputs" / "sprint2_interactive_topology.html"
    render_interactive_topology(nodes_with_metrics, edges, out_path)
    print(f"Wrote {out_path}")
    print(f"File size: {out_path.stat().st_size:,} bytes")
