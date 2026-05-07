from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parents[1]
NODES = BASE / "mock_data_nodes.csv"
EDGES = BASE / "mock_data_edges.csv"
OUT = BASE / "outputs"
NB = BASE / "notebooks"
OUT.mkdir(exist_ok=True)
NB.mkdir(exist_ok=True)

FREQ_ORDER = ["Daily", "Weekly", "Monthly", "Rarely"]
FREQ_WEIGHT = {"Daily": 4, "Weekly": 3, "Monthly": 2, "Rarely": 1}


def run_dq(nodes: pd.DataFrame, edges: pd.DataFrame) -> list[str]:
    issues: list[str] = []

    required_edges = [
        "Source_EMP_ID",
        "Target_EMP_ID",
        "Interaction_Type",
        "Interaction_Frequency",
        "Awareness_Score",
        "Energy_Score",
        "Nomination_Rank",
    ]

    for c in ["EMP_ID", "Team", "Seniority"]:
        if c not in nodes.columns:
            issues.append(f"nodes missing col: {c}")

    for c in required_edges:
        if c not in edges.columns:
            issues.append(f"edges missing col: {c}")

    if not issues:
        if edges[required_edges].isna().any().any():
            issues.append("edges has null in required cols")

        bad_type = edges.loc[~edges["Interaction_Type"].isin(["Hard", "Soft"])]
        bad_freq = edges.loc[~edges["Interaction_Frequency"].isin(FREQ_ORDER)]
        if len(bad_type):
            issues.append(f"invalid Interaction_Type rows: {len(bad_type)}")
        if len(bad_freq):
            issues.append(f"invalid Interaction_Frequency rows: {len(bad_freq)}")

        for s in ["Awareness_Score", "Energy_Score"]:
            bad_score = edges.loc[~edges[s].between(1, 5)]
            if len(bad_score):
                issues.append(f"{s} out of 1..5 rows: {len(bad_score)}")

        bad_rank = edges.loc[~edges["Nomination_Rank"].between(1, 3)]
        if len(bad_rank):
            issues.append(f"Nomination_Rank out of 1..3 rows: {len(bad_rank)}")

        dup_rank = edges.duplicated(["Source_EMP_ID", "Interaction_Type", "Nomination_Rank"]).sum()
        if dup_rank:
            issues.append(f"duplicate rank per source+type: {dup_rank}")

        node_set = set(nodes["EMP_ID"])
        bad_src = (~edges["Source_EMP_ID"].isin(node_set)).sum()
        bad_tgt = (~edges["Target_EMP_ID"].isin(node_set)).sum()
        if bad_src:
            issues.append(f"unknown Source_EMP_ID count: {int(bad_src)}")
        if bad_tgt:
            issues.append(f"unknown Target_EMP_ID count: {int(bad_tgt)}")

    return issues


def build_sandbox(nodes: pd.DataFrame, edges: pd.DataFrame, n_nodes: int = 40, seed: int = 42):
    sample_ids = nodes["EMP_ID"].sample(n=min(n_nodes, len(nodes)), random_state=seed)
    chosen = set(sample_ids)
    e_sub = edges.loc[
        edges["Source_EMP_ID"].isin(chosen) & edges["Target_EMP_ID"].isin(chosen)
    ].copy()

    if len(e_sub) < max(30, n_nodes):
        boost = set(edges["Source_EMP_ID"].value_counts().head(20).index).union(
            set(edges["Target_EMP_ID"].value_counts().head(20).index)
        )
        chosen = chosen.union(boost)
        e_sub = edges.loc[
            edges["Source_EMP_ID"].isin(chosen) & edges["Target_EMP_ID"].isin(chosen)
        ].copy()

    final_ids = set(e_sub["Source_EMP_ID"]).union(set(e_sub["Target_EMP_ID"]))
    n_sub = nodes.loc[nodes["EMP_ID"].isin(final_ids)].copy()
    return n_sub, e_sub


def export_eda(nodes: pd.DataFrame, edges: pd.DataFrame):
    freq = (
        edges["Interaction_Frequency"]
        .value_counts()
        .reindex(FREQ_ORDER, fill_value=0)
        .rename_axis("Interaction_Frequency")
        .reset_index(name="count")
    )
    freq.to_csv(OUT / "sprint1_freq_type_distribution.csv", index=False)

    out_degree = edges.groupby("Source_EMP_ID").size().rename("out_degree")
    in_degree = edges.groupby("Target_EMP_ID").size().rename("in_degree")

    profile = nodes[["EMP_ID", "Team", "Seniority", "Profile_Type", "Isolation_Risk_Flag"]].copy()
    profile = profile.merge(out_degree, left_on="EMP_ID", right_index=True, how="left")
    profile = profile.merge(in_degree, left_on="EMP_ID", right_index=True, how="left")
    profile[["out_degree", "in_degree"]] = profile[["out_degree", "in_degree"]].fillna(0).astype(int)
    profile.to_csv(OUT / "sprint1_node_degree_profile.csv", index=False)


def draw_sandbox_png(nodes_sub: pd.DataFrame, edges_sub: pd.DataFrame):
    # lightweight png drawing (no matplotlib/networkx hard dependency)
    from PIL import Image, ImageDraw

    w, h = 1400, 900
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)

    ids = sorted(set(nodes_sub["EMP_ID"]))
    if not ids:
        img.save(OUT / "sprint1_topology_sandbox.png")
        return

    import math
    pos = {}
    cx, cy = w // 2, h // 2
    rad = min(w, h) * 0.38
    for i, eid in enumerate(ids):
        ang = 2 * math.pi * i / len(ids)
        pos[eid] = (int(cx + rad * math.cos(ang)), int(cy + rad * math.sin(ang)))

    in_deg = Counter(edges_sub["Target_EMP_ID"])

    color_map = {
        "Daily": (215, 48, 39),
        "Weekly": (252, 141, 89),
        "Monthly": (145, 191, 219),
        "Rarely": (69, 117, 180),
    }

    # edges
    for _, r in edges_sub.iterrows():
        x1, y1 = pos[r["Source_EMP_ID"]]
        x2, y2 = pos[r["Target_EMP_ID"]]
        freq = r["Interaction_Frequency"]
        width = max(1, FREQ_WEIGHT.get(freq, 1))
        draw.line((x1, y1, x2, y2), fill=color_map.get(freq, (140, 140, 140)), width=width)

    # nodes
    for eid, (x, y) in pos.items():
        r = 4 + min(16, in_deg.get(eid, 0))
        fill = (220, 90, 90) if in_deg.get(eid, 0) >= 4 else (80, 120, 210)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=fill, outline=(30, 30, 30))

    # top labels
    for eid, deg in in_deg.most_common(10):
        x, y = pos[eid]
        draw.text((x + 6, y + 4), eid, fill=(10, 10, 10))

    draw.text((20, 20), "Sprint 1 Topology Prototype (Sandbox)", fill=(20, 20, 20))
    draw.text((20, 46), "Edge color/width = Interaction_Frequency, node size = in-degree", fill=(55, 55, 55))
    img.save(OUT / "sprint1_topology_sandbox.png")


def write_summary(nodes: pd.DataFrame, edges: pd.DataFrame, nodes_sub: pd.DataFrame, edges_sub: pd.DataFrame, issues: list[str]):
    in_degree = edges.groupby("Target_EMP_ID").size().sort_values(ascending=False)
    out_degree = edges.groupby("Source_EMP_ID").size().sort_values()

    with (OUT / "sprint1_summary_report.md").open("w", encoding="utf-8") as f:
        f.write("# Sprint 1 Summary Report\n\n")
        f.write(f"- Nodes (full): **{len(nodes)}**\n")
        f.write(f"- Edges (full): **{len(edges)}**\n")
        f.write(f"- Sandbox nodes: **{len(nodes_sub)}**\n")
        f.write(f"- Sandbox edges: **{len(edges_sub)}**\n")
        f.write(f"- DQ status: **{'PASS' if not issues else 'FAIL'}**\n")
        if issues:
            f.write("- DQ issues:\n")
            for i in issues:
                f.write(f"  - {i}\n")

        f.write("\n## Key Signals\n")
        f.write(f"- Top 5 hub candidates (in-degree): {list(in_degree.head(5).items())}\n")
        f.write(f"- Top 5 silent candidates (lowest out-degree): {list(out_degree.head(5).items())}\n")
        freq = edges["Interaction_Frequency"].value_counts().to_dict()
        f.write(f"- Frequency distribution: {freq}\n")


def write_notebook_template():
    nb_path = NB / "sprint1_eda_and_topology_prototype.ipynb"
    content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Sprint 1: EDA and Topology Prototype\\n",
                    "\\n",
                    "Social Telemetry - Seeing the Silent Teams"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "from pathlib import Path\\n",
                    "import pandas as pd\\n",
                    "\\n",
                    "base = Path('..').resolve() if Path.cwd().name == 'notebooks' else Path('Capstone')\\n",
                    "nodes = pd.read_csv(base / 'mock_data_nodes.csv')\\n",
                    "edges = pd.read_csv(base / 'mock_data_edges.csv')\\n",
                    "print({'nodes': len(nodes), 'edges': len(edges)})"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "display(edges['Interaction_Frequency'].value_counts())\\n",
                    "display(edges['Interaction_Type'].value_counts())"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "in_deg = edges.groupby('Target_EMP_ID').size().rename('in_degree')\\n",
                    "out_deg = edges.groupby('Source_EMP_ID').size().rename('out_degree')\\n",
                    "display(in_deg.sort_values(ascending=False).head(10))\\n",
                    "display(out_deg.sort_values().head(10))"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Generated Artifacts\\n",
                    "- `Capstone/outputs/sprint1_freq_type_distribution.csv`\\n",
                    "- `Capstone/outputs/sprint1_node_degree_profile.csv`\\n",
                    "- `Capstone/outputs/sprint1_topology_sandbox.png`\\n",
                    "- `Capstone/outputs/sprint1_summary_report.md`"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    import json
    nb_path.write_text(json.dumps(content, ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    nodes = pd.read_csv(NODES)
    edges = pd.read_csv(EDGES)

    issues = run_dq(nodes, edges)
    export_eda(nodes, edges)
    n_sub, e_sub = build_sandbox(nodes, edges, n_nodes=40, seed=42)
    draw_sandbox_png(n_sub, e_sub)
    write_summary(nodes, edges, n_sub, e_sub, issues)
    write_notebook_template()

    print({
        "nodes": len(nodes),
        "edges": len(edges),
        "sandbox_nodes": len(n_sub),
        "sandbox_edges": len(e_sub),
        "dq_pass": len(issues) == 0,
    })


if __name__ == "__main__":
    main()
