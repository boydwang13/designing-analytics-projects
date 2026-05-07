"""Sprint 2 · WS3 — Isolation Score v1.0.

Composite risk index with four equally weighted (w = 0.25 each) sub-components,
each normalized to [0, 1]. All formulas are defined in `docs/mock_codebook.md`
"Isolation Score" section and mirrored here.

Literature alignment: Cross & Parker (2004); Granovetter (1973).

Inputs
------
- `nodes` DataFrame (for joins)
- `node_metrics` DataFrame produced by `src/metrics.py` (out_degree etc.)
- `edges` DataFrame (for TargetConcentration; needs per-source counts per target)

Output
------
A DataFrame keyed by `EMP_ID` with columns:
- OutboundScarcity, WeakWeightShare, TargetConcentration, WeakBridgeDeficit
- Isolation_Score (weighted 0.25 × each component)
"""

from __future__ import annotations

import pandas as pd


COMPONENT_WEIGHTS = {
    "OutboundScarcity": 0.25,
    "WeakWeightShare": 0.25,
    "TargetConcentration": 0.25,
    "WeakBridgeDeficit": 0.25,
}


def compute_isolation_score(
    nodes: pd.DataFrame,
    node_metrics: pd.DataFrame,
    edges: pd.DataFrame,
) -> pd.DataFrame:
    """Return `EMP_ID` + 4 component scores + Isolation_Score.

    All sub-components are in [0, 1]; higher = more isolated.
    A node with zero outbound is treated as "maximally isolated" on every
    tie-based component (share / concentration / bridge) per codebook.
    """
    m = node_metrics.set_index("EMP_ID")
    out_degree = m["out_degree"]
    weak_out = m["Weak_Tie_Outbound_Count"]
    weak_cross = m["Weak_Cross_Team_Tie_Count"]

    # --- OutboundScarcity ---
    # 1 - (out_degree / max_out_degree). Out_degree = 0 → 1.0 (maximally scarce).
    max_out = out_degree.max()
    if max_out == 0:
        outbound_scarcity = pd.Series(1.0, index=out_degree.index)
    else:
        outbound_scarcity = 1.0 - (out_degree / max_out)

    # --- WeakWeightShare ---
    # count(weight <= 0.33) / total_outbound_count; out_degree=0 → 1.0 (by codebook).
    weak_share = weak_out / out_degree.replace(0, pd.NA)
    weak_share = weak_share.fillna(1.0).astype(float)

    # --- TargetConcentration ---
    # Herfindahl on outbound targets per source; out_degree=0 → 1.0.
    src_tgt_counts = edges.groupby(["Source_EMP_ID", "Target_EMP_ID"]).size()
    src_totals = edges.groupby("Source_EMP_ID").size()

    concentration = {}
    for src in nodes["EMP_ID"]:
        if src not in src_totals.index:
            concentration[src] = 1.0
            continue
        total = src_totals[src]
        counts_to_each = src_tgt_counts.loc[src]
        if isinstance(counts_to_each, pd.Series):
            shares = counts_to_each / total
        else:  # single target
            shares = pd.Series([counts_to_each / total])
        concentration[src] = float((shares ** 2).sum())
    target_concentration = pd.Series(concentration, name="TargetConcentration")

    # --- WeakBridgeDeficit ---
    # 1 - weak_cross_team_tie_count / max_weak_cross_team_tie_count
    max_wc = weak_cross.max()
    if max_wc == 0:
        weak_bridge_deficit = pd.Series(1.0, index=weak_cross.index)
    else:
        weak_bridge_deficit = 1.0 - (weak_cross / max_wc)

    # Assemble
    df = pd.DataFrame(
        {
            "EMP_ID": out_degree.index,
            "OutboundScarcity": outbound_scarcity.round(4).values,
            "WeakWeightShare": weak_share.round(4).values,
            "TargetConcentration": target_concentration.reindex(out_degree.index).round(4).values,
            "WeakBridgeDeficit": weak_bridge_deficit.round(4).values,
        }
    )
    df["Isolation_Score"] = (
        COMPONENT_WEIGHTS["OutboundScarcity"] * df["OutboundScarcity"]
        + COMPONENT_WEIGHTS["WeakWeightShare"] * df["WeakWeightShare"]
        + COMPONENT_WEIGHTS["TargetConcentration"] * df["TargetConcentration"]
        + COMPONENT_WEIGHTS["WeakBridgeDeficit"] * df["WeakBridgeDeficit"]
    ).round(4)
    return df


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    from metrics import compute_node_metrics, load_edges_and_nodes

    nodes, edges = load_edges_and_nodes()
    metrics_df = compute_node_metrics(nodes, edges)
    iso = compute_isolation_score(nodes, metrics_df, edges)

    joined = iso.merge(nodes[["EMP_ID", "Profile_Type"]], on="EMP_ID")
    by_archetype = joined.groupby("Profile_Type")["Isolation_Score"].agg(["mean", "median", "count"])
    print("Isolation Score by archetype:")
    print(by_archetype.round(4))

    print("\nTop 10 highest Isolation_Score:")
    print(
        joined.sort_values("Isolation_Score", ascending=False)
        .head(10)[["EMP_ID", "Profile_Type", "OutboundScarcity", "WeakWeightShare", "TargetConcentration", "WeakBridgeDeficit", "Isolation_Score"]]
        .to_string(index=False)
    )
