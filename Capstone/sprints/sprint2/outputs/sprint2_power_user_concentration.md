# Sprint 2 — Power User Concentration Report

**Purpose**: Quantify whether help-seeking concentrates on a small number of "central connectors" (Cross & Parker, 2004), producing the *star-network fragility* signal raised in PID §34 ("preferential attachment").

**Source**: `sprints/sprint2/outputs/sprint2_nodes_with_metrics.csv`
**Scope**: 300 nodes / 1042 directed help-seeking nominations
**Weight scheme**: Schema v1.2.0 exponential-decay decimal (Daily=1.0 / Weekly=0.67 / Monthly=0.33 / Rarely=0.10)

---

## Headline Numbers

| Metric | Value | Interpretation |
| :-- | :-- | :-- |
| Total inbound nominations | **1042** | Every edge contributes one inbound count |
| `Top5_Hub_Inbound_Share` | **14.49%** | Top 5 hubs = 1.67% of workforce but absorb ~14.5% of all help-seeking |
| `Top10_Hub_Inbound_Share` | **23.32%** | Top 10 hubs = 3.33% of workforce but absorb ~23.3% of all help-seeking |
| `Inbound_Herfindahl_Index` | **0.009354** | Ranges from 1/300 ≈ 0.00333 (uniform) to 1.0 (monopoly) |

---

## Top 10 Central Connectors

**Ranking**: `in_degree` descending; ties broken by `in_strength` descending.

| EMP_ID | Team | Seniority | Profile_Type | in_degree | in_strength | Betweenness | Cross-Team Tie Count |
| :-- | :-- | :-- | :-- | --: | --: | --: | --: |
| EMP_159 | Analytics & BI | Senior | hub | 33 | 20.67 | 0.065263 | 2 |
| EMP_126 | Analytics & BI | Senior | hub | 33 | 20.18 | 0.037998 | 2 |
| EMP_198 | Platform Engineering | Senior | hub | 32 | 19.33 | 0.073343 | 1 |
| EMP_166 | Analytics & BI | Senior | hub | 29 | 19.57 | 0.059378 | 2 |
| EMP_247 | Client Services | Senior | hub | 24 | 14.19 | 0.065092 | 2 |
| EMP_218 | Client Services | Mid-level | hub | 22 | 11.74 | 0.033426 | 1 |
| EMP_068 | Platform Engineering | Senior | hub | 21 | 11.08 | 0.049123 | 2 |
| EMP_219 | Information Management | Senior | hub | 20 | 12.63 | 0.089780 | 2 |
| EMP_298 | Data Engineering | Senior | broker | 15 | 7.99 | 0.082881 | 2 |
| EMP_210 | Client Services | Mid-level | broker | 14 | 10.01 | 0.084158 | 2 |

**Archetype recovery**: rows 1–8 are `Profile_Type == 'hub'` (100% precision at top-8 cutoff). Rows 9–10 are `broker` — consistent with Cross & Parker's observation that hubs and brokers overlap at the high-influence end.

---

## Interpretation — Star-Network Fragility (PID §34)

If the 10 most-nominated employees were simultaneously unavailable, roughly **23.3%** of all help-seeking routes would need to reroute. For 300 people, **3.3% of headcount absorbs 23.3% of load** — this is the quantitative footprint of a star network.

Sprint 2's Isolation Score provides the opposite-tail counterpart: the two together give management both "who is over-relied-on" and "who is under-reached" signals for balanced triage.

---

## Methodological Notes

- `in_degree` counts each nomination as 1 (unweighted). `in_strength` weights by `Interaction_Frequency_Weight`.
- `Inbound_Herfindahl_Index` is bounded in `[1/N, 1]`. Observed value is ≈ 2.8× the uniform floor.
- Betweenness centrality uses **inverse weights** (`1/Interaction_Frequency_Weight`) so strong ties correspond to short shortest-path distances (Granovetter 1973).