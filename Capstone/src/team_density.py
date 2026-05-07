"""Sprint 2 (v1.2.1 patch) — Team-to-team directed block-density matrix.

Operationalizes Cross & Parker's (2004) "block density" / group-to-group
communication intensity at Team granularity, answering Martin's Sprint 1
follow-up question with *hard numbers* rather than visual intuition:

    "Does Analytics & BI trade help internally but never with other teams?"

Design
------
- Directed density: rows = source Team (asker); columns = target Team (helper).
- Diagonal (intra-team): density = ties_within_team / (n * (n - 1))
- Off-diagonal (cross-team): density = ties_from_A_to_B / (|A| * |B|)
- Two variants:
    * unweighted (count of nomination rows)
    * weighted   (sum of Interaction_Frequency_Weight 0..1)
- Optional Hard / Soft split so the matrix can be read as a pair of 6x6
  technical vs business-coordination flow maps.

Literature alignment: Cross & Parker (2004) *The Hidden Power of Social
Networks*, block-density / group-level analysis. No Burt / Structural Holes
constructs are used (per Sprint 2 scope decision).
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def _team_sizes(nodes: pd.DataFrame) -> pd.Series:
    return nodes.groupby("Team").size().rename("Member_Count")


def _directed_possible_ties(sizes: pd.Series) -> pd.DataFrame:
    """Matrix of max possible directed ties between each Team pair."""
    teams = list(sizes.index)
    rows = []
    for a in teams:
        n_a = sizes[a]
        row = {}
        for b in teams:
            n_b = sizes[b]
            row[b] = n_a * (n_a - 1) if a == b else n_a * n_b
        rows.append(pd.Series(row, name=a))
    return pd.DataFrame(rows)


def _edge_counts(edges: pd.DataFrame, nodes: pd.DataFrame) -> pd.DataFrame:
    e = edges.copy()
    team_of = dict(zip(nodes["EMP_ID"], nodes["Team"]))
    e["src_team"] = e["Source_EMP_ID"].map(team_of)
    e["tgt_team"] = e["Target_EMP_ID"].map(team_of)
    return e


def compute_team_density(
    nodes: pd.DataFrame,
    edges: pd.DataFrame,
    interaction_type: str | None = None,
    weighted: bool = False,
) -> pd.DataFrame:
    """Return a 6x6 directed density DataFrame.

    Parameters
    ----------
    interaction_type : str | None
        If given, filter edges to this type ("Hard" or "Soft") before counting.
    weighted : bool
        If True, numerator is the sum of `Interaction_Frequency_Weight`;
        otherwise, it is the count of distinct nomination rows.
    """
    sizes = _team_sizes(nodes)
    possible = _directed_possible_ties(sizes)

    e = _edge_counts(edges, nodes)
    if interaction_type is not None:
        e = e[e["Interaction_Type"] == interaction_type]

    if weighted:
        e = e.copy()
        e["observed"] = e["Interaction_Frequency_Weight"].astype(float)
        agg = e.groupby(["src_team", "tgt_team"])["observed"].sum()
    else:
        agg = e.groupby(["src_team", "tgt_team"]).size()

    observed = agg.unstack(fill_value=0).reindex(
        index=possible.index, columns=possible.columns, fill_value=0
    )
    density = observed.astype(float) / possible.replace(0, pd.NA).astype(float)
    density = density.fillna(0.0).round(4)
    density.index.name = "source_team"
    density.columns.name = "target_team"
    return density


def format_density_md(density: pd.DataFrame, title: str) -> list[str]:
    """Produce a markdown table (rows = source, cols = target).

    Diagonal cells are wrapped in bold to visually separate intra vs inter.
    """
    lines = [f"### {title}", ""]
    header = "| source \\ target | " + " | ".join(density.columns) + " |"
    sep = "| :-- | " + " | ".join(["--:" for _ in density.columns]) + " |"
    lines.extend([header, sep])
    for src in density.index:
        cells = []
        for tgt in density.columns:
            val = density.loc[src, tgt]
            cell = f"**{val:.4f}**" if src == tgt else f"{val:.4f}"
            cells.append(cell)
        lines.append(f"| **{src}** | " + " | ".join(cells) + " |")
    return lines


def render_heatmap(
    density: pd.DataFrame,
    output_path: Path,
    title: str,
) -> None:
    """Render a diverging heatmap with annotated cells."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    data = density.values.astype(float)
    diag_mask = np.eye(len(data), dtype=bool)

    fig, ax = plt.subplots(figsize=(9, 7))
    vmax = max(data.max(), 1e-6)
    im = ax.imshow(data, cmap="YlOrRd", vmin=0, vmax=vmax, aspect="equal")

    # Annotate each cell.
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data[i, j]
            color = "black" if val < vmax * 0.55 else "white"
            weight = "bold" if diag_mask[i, j] else "normal"
            ax.text(
                j, i, f"{val:.3f}", ha="center", va="center",
                color=color, fontsize=9, fontweight=weight,
            )

    # Diagonal outline.
    for i in range(data.shape[0]):
        ax.add_patch(
            plt.Rectangle(
                (i - 0.5, i - 0.5), 1, 1, fill=False, edgecolor="#0b3d91", linewidth=2,
            )
        )

    ax.set_xticks(range(len(density.columns)))
    ax.set_xticklabels(density.columns, rotation=30, ha="right", fontsize=9)
    ax.set_yticks(range(len(density.index)))
    ax.set_yticklabels(density.index, fontsize=9)
    ax.set_xlabel("Target Team (who is asked)")
    ax.set_ylabel("Source Team (who asks)")
    ax.set_title(title + "\n(diagonal = intra-team density; off-diagonal = cross-team)", fontsize=11)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Density (observed / possible directed ties)", fontsize=9)

    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(Path(__file__).parent))
    from metrics import load_edges_and_nodes

    base = Path(__file__).resolve().parents[1]
    nodes, edges = load_edges_and_nodes(base)

    dens_all = compute_team_density(nodes, edges, interaction_type=None, weighted=False)
    print("Unweighted directed density (all types):")
    print(dens_all.round(4))
    print()
    dens_w = compute_team_density(nodes, edges, interaction_type=None, weighted=True)
    print("Weighted directed density (all types):")
    print(dens_w.round(4))
