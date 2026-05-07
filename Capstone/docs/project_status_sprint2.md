# Project Status Briefing — End of Sprint 2

**Project**: Social Telemetry — Seeing the Silent Teams: Detecting Hidden Support Needs  
**Student / Consultant**: Bo Wang (MS Business Analytics, Central European University)  
**Sponsor**: Martin Brüggemann, EMEA Solution Consultant, Canon EMEA  
**Capstone Project Manager**: Eduardo Arino de la Rubia (CEU)  
**Status as of**: 2026-04-24 (end of Sprint 2, Weeks 3–4, including v1.2.1 and v1.2.2 patch deliverables)  
**Document purpose**: Self-contained status snapshot for agentic AI and human reviewers. This document describes the **current implemented state** after Sprint 2. It does not prescribe future work.

---

## 1. Executive Summary

Sprint 2 is complete and operationally stable. The project moved from data-foundation prototype status (Sprint 1) to a full ONA analysis package: centrality metrics, Isolation Score v1.0, ROC-calibrated thresholding, management-facing shortlists (silent individuals, silent teams, hubs, brokers), interactive topology visualization, and scenario-injection validation. Core outputs are reproducible from one runner script and governance is versioned through `CHANGELOG.md` and `PID_delta_log.md`. In this synthetic snapshot, no whole team shows classic silo behavior; isolation risk is concentrated at the individual level and aligns strongly with injected island archetypes.

---

## 2. Project Scope and Constraints (Current State)

| Item | Current status |
| :-- | :-- |
| Business unit in scope | Canon EMEA — Information Management Solutions, Professional Services only |
| Problem in scope | Detect structurally silent individuals/teams and network fragility from help-seeking patterns |
| Data policy | Synthetic-only analysis; no production communications data |
| Privacy posture | GDPR-constrained design; no geolocation field (`Region` removed) |
| Network unit of analysis | Directed help-seeking nominations (`Source_EMP_ID -> Target_EMP_ID`) |
| Current visualization posture | Interactive pyvis HTML + static density heatmaps |
| Explicitly deferred in PID traceability | Scalability stress testing at larger N (mapped to later sprint) |

Reference contract remains in `docs/PID.md`. Registered implementation deltas are tracked in `docs/PID_delta_log.md`.

---

## 3. What Changed in Sprint 2 (vs End of Sprint 1)

### 3.1 Schema and data-level changes

- Schema upgraded to **v1.2.0** in `data/mock_data_edges.csv`:
  - `Interaction_Type_Code` (`Hard=1`, `Soft=0`)
  - `Interaction_Frequency_Weight` (`Daily=1.00`, `Weekly=0.67`, `Monthly=0.33`, `Rarely=0.10`)
- Seed remained unchanged (`5228`); core volume remained `300 nodes / 1042 edges`.

### 3.2 Analytical capabilities added

- Node metrics expanded to include in/out degree, in/out strength, weighted betweenness, cross-team and weak-tie bridge metrics.
- Isolation Score v1.0 implemented as a 4-component composite score.
- ROC-based threshold derivation implemented (`tau_ROC` via Youden's J).
- Team-level directed block-density matrices added (unweighted, weighted, hard-only, soft-only).

### 3.3 Visualization changes

- Interactive topology delivered as self-contained pyvis HTML with team-clustered spatial layout and tooltips.
- A V2 interactive topology variant adds click-to-focus behavior (node/edge focus with strong fade of non-selected elements).

### 3.4 Management outputs added

- Silent individuals shortlist (Top 20).
- Silent teams aggregate view (6 teams).
- Power user concentration report (Top hubs + concentration indices).
- Brokers shortlist (Top betweenness-based boundary spanners).
- Validation report (Scenario Injection Testing).

---

## 4. Current Methodological Framework (As Implemented)

### 4.1 Network and role metrics

- **Central Hubs**: primarily identified via `in_degree` (with `in_strength` used as tie-break in presentation table ordering).
- **Brokers / Boundary Spanners**: identified via `betweenness_centrality` (shortest paths on inverse edge weights), complemented by cross-team tie information.
- **Weak-tie logic**: weak ties defined by `Interaction_Frequency_Weight <= 0.33` (Monthly/Rarely).

### 4.2 Isolation Score v1.0

Implemented in `src/isolation_score.py`:

`Isolation_Score = 0.25*OutboundScarcity + 0.25*WeakWeightShare + 0.25*TargetConcentration + 0.25*WeakBridgeDeficit`

All sub-components are normalized to `[0,1]` with higher values interpreted as higher isolation risk.

### 4.3 Binary and tier risk labels

Implemented in `src/threshold.py`:

- `Isolation_Risk_Flag = 1` if `Isolation_Score >= tau_ROC`
- `tau_ROC` selected by maximizing `Youden's J = TPR - FPR` on injected synthetic ground truth (`Profile_Type == 'island'`)
- Tiering:
  - `High`: `score >= p75` and `score >= tau_ROC`
  - `Medium`: `p50 <= score < p75`
  - `Low`: below `p50`

---

## 5. Data and Schema State

### 5.1 Live data sources

- `data/mock_data_nodes.csv`
- `data/mock_data_edges.csv`

### 5.2 Current run-time metric table

- `sprints/sprint2/outputs/sprint2_nodes_with_metrics.csv`
- Shape: `300 x 20`
- Includes centrality, weak-tie bridge metrics, Isolation Score components, `Isolation_Risk_Flag`, and `Isolation_Risk_Tier`.

### 5.3 Version state

- Schema baseline: `v1.2.0`
- Sprint 2 patch extensions:
  - `v1.2.1`: team directed density matrix package
  - `v1.2.2`: brokers shortlist package

Version history and rationale are in `docs/CHANGELOG.md`.

---

## 6. Implemented Pipeline and Components

### 6.1 Runner

- `sprints/sprint2/run_sprint2.py` orchestrates Sprint 2 end-to-end outputs.

### 6.2 Core reusable modules in `src/`

| Module | Current responsibility |
| :-- | :-- |
| `metrics.py` | Node centrality, strength, weak-tie and boundary-spanning features; power-user concentration metrics |
| `isolation_score.py` | Isolation Score v1.0 and 4 normalized components |
| `threshold.py` | ROC-based threshold derivation and risk flag/tier assignment |
| `viz.py` | Interactive topology rendering; V2 click-focus enhancement path |
| `team_density.py` | Team-to-team directed density matrices and heatmap rendering |

### 6.3 Reproducibility

Primary Sprint 2 command (from `Capstone/`):

```bash
PYTHONPATH=../.venv_lib python3 sprints/sprint2/run_sprint2.py
```

Machine-readable run summary is emitted to `sprints/sprint2/outputs/sprint2_summary.json`.

---

## 7. Sprint 2 Deliverables and Output Inventory (Current)

### 7.1 Core analysis outputs

- `sprint2_nodes_with_metrics.csv`
- `sprint2_silent_individuals_shortlist.md`
- `sprint2_silent_teams_aggregated.md`
- `sprint2_power_user_concentration.md`
- `sprint2_brokers_shortlist.md`
- `sprint2_validation_report.md`
- `sprint2_counter_metrics.md`

### 7.2 Network visualization outputs

- `sprint2_interactive_topology.html` (base interactive network)
- `sprint2_interactive_topology_v2.html` (click-focus enhanced variant)
- `sprint2_team_density_heatmap.png` (unweighted team matrix)
- `sprint2_team_density_heatmap_weighted.png` (weighted team matrix)

### 7.3 Team density matrix package

- `sprint2_team_density_matrix.md`
- `sprint2_team_density_matrix.csv`
- `sprint2_team_density_matrix_weighted.csv`
- `sprint2_team_density_matrix_hard.csv`
- `sprint2_team_density_matrix_soft.csv`

### 7.4 Sprint-level packaging outputs

- `sprint2_summary_report.md`
- `sprint2_review_pack.md`
- `sprint2_summary.json`
- `sprints/sprint2/presentation.html`
- `sprints/sprint2/presentation_v2.html`

---

## 8. Key Quantitative Results (Current Snapshot)

### 8.1 Volume and concentration

| Metric | Observed |
| :-- | --: |
| Nodes / Edges | 300 / 1042 |
| Total inbound nominations | 1042 |
| Top-5 hub inbound share | 14.49% |
| Top-10 hub inbound share | 23.32% |
| Inbound Herfindahl Index | 0.009354 |

### 8.2 Isolation scoring and thresholding

| Metric | Observed |
| :-- | --: |
| ROC-AUC | 0.9999 |
| `tau_ROC` | 0.6917 |
| Sensitivity / Specificity | 1.0000 / 0.9923 |
| Confusion matrix | TP=41, FP=2, TN=257, FN=0 |
| Tier counts | High=43, Medium=126, Low=131 |

### 8.3 Archetype recovery signals

- All 8 seeded `hub` archetypes appear in Top-8 central connectors (100% precision at that cutoff).
- All 41 seeded `island` archetypes are flagged high risk (0 false negatives).
- Two non-island nodes are flagged at the boundary (`Isolation_Score = tau_ROC`), documented as investigation candidates.

### 8.4 Team-level structural findings

From `sprint2_team_density_matrix.md`:

- All six teams have `intra/off-diag < 1` (range: 0.37 to 0.97), indicating no classic team silo signature in this synthetic wave.
- Analytics & BI appears as net help provider by directional density profile.
- Data Engineering shows strongest outward dependency pattern, notably toward Analytics & BI.

---

## 9. Validation Status and Interpretation Limits

### 9.1 Validation status (current)

Scenario Injection Testing objective in PID §66 is satisfied under the synthetic setting:

- Very high ranking/separation performance (`AUC = 0.9999`)
- No injected-island miss at operational threshold
- Low false-positive count (`FP = 2`)

### 9.2 Interpretation limits (current)

- Current validation uses synthetic archetype ground truth, not production behavioral labels.
- `Isolation_Risk_Flag` is an algorithmic screening signal; it is not equivalent to confirmed organizational diagnosis.
- High betweenness and high popularity can overlap in some nodes; role interpretation should remain context-dependent.
- Team-level absence of silo signature in this snapshot does not imply persistence across future waves.

---

## 10. Governance and Audit Trail

### 10.1 Authoritative governance files

- `docs/PID.md` (signed contract baseline)
- `docs/PID_delta_log.md` (registered implementation deltas; current big-picture check remains OK)
- `docs/CHANGELOG.md` (schema and delivery evolution through v1.2.2)

### 10.2 Sprint 2 governance state

- Sprint 2 DoD tracked and marked complete in `sprints/sprint2/outputs/sprint2_review_pack.md`
- Version trace:
  - `v1.2.0` core Sprint 2 delivery
  - `v1.2.1` team density matrix patch
  - `v1.2.2` brokers shortlist patch

---

## 11. Current Limitations and Risk Notes

1. **Data realism boundary**: findings are structurally valid within the synthetic generator assumptions; external generalization remains unproven.
2. **Threshold sensitivity at boundary**: FP cases occur exactly at `tau_ROC`, indicating expected ambiguity near the decision cut.
3. **Scalability evidence not expanded**: larger-N stress behavior is not part of the current Sprint 2 evidence package.
4. **Interpretation dependency**: network role metrics (hub/broker/island risk) should be used with managerial context, not as standalone HR decisions.

---

## 12. Companion Files for Rapid AI Context Loading (Current-State Focus)

### Tier A — always load first

1. `docs/project_status_sprint2.md` (this file)
2. `docs/PID.md`
3. `docs/mock_codebook.md`
4. `docs/PID_delta_log.md`
5. `docs/CHANGELOG.md`

### Tier B — core Sprint 2 evidence

6. `sprints/sprint2/outputs/sprint2_summary_report.md`
7. `sprints/sprint2/outputs/sprint2_validation_report.md`
8. `sprints/sprint2/outputs/sprint2_team_density_matrix.md`
9. `sprints/sprint2/outputs/sprint2_silent_individuals_shortlist.md`
10. `sprints/sprint2/outputs/sprint2_silent_teams_aggregated.md`
11. `sprints/sprint2/outputs/sprint2_power_user_concentration.md`
12. `sprints/sprint2/outputs/sprint2_brokers_shortlist.md`

### Tier C — implementation context

13. `sprints/sprint2/run_sprint2.py`
14. `src/metrics.py`
15. `src/isolation_score.py`
16. `src/threshold.py`
17. `src/viz.py`
18. `src/team_density.py`

---

*End of Sprint 2 status briefing.*
