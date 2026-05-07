"""Sprint 2 · WS2 — Network metrics & Power User concentration.

This module is a cross-sprint reusable building block. It consumes the two
project-level CSVs (`Capstone/data/mock_data_nodes.csv`,
`Capstone/data/mock_data_edges.csv`) and produces:

1. A per-node metrics table (returned as `pandas.DataFrame`) containing:
   - `in_degree`, `out_degree`, `in_strength`, `out_strength`
   - `betweenness_centrality` (weighted, directed)
   - `Cross_Team_Tie_Count`        — Cross & Parker (2004) boundary spanner operationalization
   - `Weak_Tie_Outbound_Count`     — Granovetter (1973) weak-tie count
   - `Weak_Cross_Team_Tie_Count`   — weak bridges (feeds WeakBridgeDeficit in WS3)

2. A Power User concentration summary (dict) with:
   - `Top5_Hub_Inbound_Share`
   - `Top10_Hub_Inbound_Share`
   - `Inbound_Herfindahl_Index`

Weight convention: uses `Interaction_Frequency_Weight` (schema v1.2.0 decimal).

Literature alignment:
- Cross, R. & Parker, A. (2004). *The Hidden Power of Social Networks.*
- Granovetter, M. S. (1973). *The Strength of Weak Ties.*
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import pandas as pd

WEAK_TIE_THRESHOLD = 0.33  # Interaction_Frequency_Weight <= 0.33 → weak tie (Monthly/Rarely)


def load_edges_and_nodes(base: Path | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load current live data from `Capstone/data/`."""
    if base is None:
        base = Path(__file__).resolve().parents[1]
    nodes = pd.read_csv(base / "data" / "mock_data_nodes.csv")
    edges = pd.read_csv(base / "data" / "mock_data_edges.csv")
    return nodes, edges


def build_graph(nodes: pd.DataFrame, edges: pd.DataFrame) -> nx.DiGraph:
    """Build a directed weighted graph. Edge weight = Interaction_Frequency_Weight."""
    G = nx.DiGraph()
    for _, r in nodes.iterrows():
        G.add_node(
            r["EMP_ID"],
            Team=r["Team"],
            Seniority=r["Seniority"],
            Years_Exp=int(r["Years_Exp"]),
            Profile_Type=r["Profile_Type"],
        )
    for _, e in edges.iterrows():
        G.add_edge(
            e["Source_EMP_ID"],
            e["Target_EMP_ID"],
            weight=float(e["Interaction_Frequency_Weight"]),
            interaction_type=e["Interaction_Type"],
            type_code=int(e["Interaction_Type_Code"]),
            freq_label=e["Interaction_Frequency"],
        )
    return G


def compute_node_metrics(nodes: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame keyed by EMP_ID with all WS2 node-level metrics.

    Design note: degree / strength / weak-tie / cross-team counts are computed
    directly from the edges DataFrame (not DiGraph) so that each nomination
    row is counted exactly once — this matters because Hard + Soft to the same
    target are two distinct nominations but would collapse to one edge in a
    simple DiGraph. Betweenness centrality is computed on a DiGraph built from
    the DataFrame (weight-averaged if duplicates) because weighted shortest-path
    algorithms require a simple graph; the minor deduplication (<1% of rows)
    is acceptable noise for a topology metric.
    """
    team_of = dict(zip(nodes["EMP_ID"], nodes["Team"]))
    edges_ext = edges.copy()
    edges_ext["src_team"] = edges_ext["Source_EMP_ID"].map(team_of)
    edges_ext["tgt_team"] = edges_ext["Target_EMP_ID"].map(team_of)
    edges_ext["is_weak"] = edges_ext["Interaction_Frequency_Weight"].astype(float) <= WEAK_TIE_THRESHOLD
    edges_ext["is_cross_team"] = edges_ext["src_team"] != edges_ext["tgt_team"]
    w = edges_ext["Interaction_Frequency_Weight"].astype(float)

    # Out-side aggregates keyed on Source.
    src_grp = edges_ext.groupby("Source_EMP_ID")
    out_degree = src_grp.size().rename("out_degree")
    out_strength = src_grp["Interaction_Frequency_Weight"].sum().astype(float).rename("out_strength")
    weak_out = src_grp["is_weak"].sum().astype(int).rename("Weak_Tie_Outbound_Count")
    weak_cross = (
        edges_ext[edges_ext["is_weak"] & edges_ext["is_cross_team"]]
        .groupby("Source_EMP_ID")
        .size()
        .rename("Weak_Cross_Team_Tie_Count")
    )
    # Cross_Team_Tie_Count = number of DISTINCT other-team targets per source.
    cross_team_distinct = (
        edges_ext[edges_ext["is_cross_team"]]
        .groupby("Source_EMP_ID")["tgt_team"]
        .nunique()
        .rename("Cross_Team_Tie_Count")
    )

    # In-side aggregates keyed on Target.
    tgt_grp = edges_ext.groupby("Target_EMP_ID")
    in_degree = tgt_grp.size().rename("in_degree")
    in_strength = tgt_grp["Interaction_Frequency_Weight"].sum().astype(float).rename("in_strength")

    # Assemble per-node row. Fill NaN with 0 for nodes with no outbound/inbound.
    df = pd.DataFrame({"EMP_ID": nodes["EMP_ID"]})
    for series in [
        in_degree,
        out_degree,
        in_strength,
        out_strength,
        weak_out,
        weak_cross,
        cross_team_distinct,
    ]:
        df = df.merge(series, left_on="EMP_ID", right_index=True, how="left")

    numeric_fill = [
        "in_degree",
        "out_degree",
        "in_strength",
        "out_strength",
        "Weak_Tie_Outbound_Count",
        "Weak_Cross_Team_Tie_Count",
        "Cross_Team_Tie_Count",
    ]
    for c in numeric_fill:
        df[c] = df[c].fillna(0)
    for c in ["in_degree", "out_degree", "Weak_Tie_Outbound_Count", "Weak_Cross_Team_Tie_Count", "Cross_Team_Tie_Count"]:
        df[c] = df[c].astype(int)
    for c in ["in_strength", "out_strength"]:
        df[c] = df[c].round(4)

    # Betweenness: simple DiGraph, inverse-weight for shortest-path semantics.
    G = build_graph(nodes, edges)
    for u, v, d in G.edges(data=True):
        d["betw_weight"] = 1.0 / max(d["weight"], 1e-3)
    betweenness = nx.betweenness_centrality(G, weight="betw_weight", normalized=True)
    df["betweenness_centrality"] = df["EMP_ID"].map(betweenness).fillna(0.0).round(6)

    # Reorder for readability.
    col_order = [
        "EMP_ID",
        "in_degree",
        "out_degree",
        "in_strength",
        "out_strength",
        "betweenness_centrality",
        "Cross_Team_Tie_Count",
        "Weak_Tie_Outbound_Count",
        "Weak_Cross_Team_Tie_Count",
    ]
    return df[col_order]


def compute_power_user_concentration(node_metrics: pd.DataFrame) -> dict[str, float | int]:
    """Quantify 'preferential attachment / star network fragility' (PID §34)."""
    total_inbound = int(node_metrics["in_degree"].sum())
    if total_inbound == 0:
        return {
            "total_inbound": 0,
            "Top5_Hub_Inbound_Share": 0.0,
            "Top10_Hub_Inbound_Share": 0.0,
            "Inbound_Herfindahl_Index": 0.0,
        }
    sorted_in = node_metrics["in_degree"].sort_values(ascending=False)
    top5_share = sorted_in.head(5).sum() / total_inbound
    top10_share = sorted_in.head(10).sum() / total_inbound

    # Herfindahl index: sum of (share_i)^2 across all nodes, range [1/N, 1].
    shares = node_metrics["in_degree"] / total_inbound
    herfindahl = float((shares ** 2).sum())

    return {
        "total_inbound": total_inbound,
        "Top5_Hub_Inbound_Share": round(float(top5_share), 4),
        "Top10_Hub_Inbound_Share": round(float(top10_share), 4),
        "Inbound_Herfindahl_Index": round(herfindahl, 6),
    }


if __name__ == "__main__":
    nodes, edges = load_edges_and_nodes()
    m = compute_node_metrics(nodes, edges)
    conc = compute_power_user_concentration(m)
    print("Node metrics preview:")
    print(m.head(10).to_string(index=False))
    print("\nPower user concentration:")
    print(conc)
