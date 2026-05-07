# Sprint 2 — Brokers (Boundary Spanners) Shortlist

**Purpose**: Identify the strongest **structural brokers** in the help-seeking graph — nodes on many shortest paths between others (betweenness) who also **bridge functional teams** (Cross & Parker, 2004). Management-readable counterpart to sorting `sprint2_nodes_with_metrics.csv` on `betweenness_centrality`.

**Complement to D5**: `sprint2_power_user_concentration.md` ranks **popularity** (`in_degree` / hub load). Brokers can overlap hubs at the high-influence end but are not the same construct.

**Source**: `sprints/sprint2/outputs/sprint2_nodes_with_metrics.csv`

**Ranking**: `betweenness_centrality` descending → `Cross_Team_Tie_Count` descending → `in_degree` descending.

**CM-3 context**: CM-3 counts `betweenness > p75` **and** `Isolation_Risk_Flag=1` as a broker false-positive. Here `p75` = **0.015516** — see `sprint2_counter_metrics.md`.

---

## Top 10 Brokers

| Rank | EMP_ID | Team | Seniority | Profile_Type | Betweenness | Cross-Team Ties | in_degree | Isolation_Risk_Flag | Tier |
| :--: | :-- | :-- | :-- | :-- | --: | --: | --: | --: | :-- |
| 1 | EMP_259 | Client Services | Mid-level | broker | 0.095352 | 3 | 8 | 0 | Low |
| 2 | EMP_219 | Information Management | Senior | hub | 0.089780 | 2 | 20 | 0 | Medium |
| 3 | EMP_210 | Client Services | Mid-level | broker | 0.084158 | 2 | 14 | 0 | Medium |
| 4 | EMP_298 | Data Engineering | Senior | broker | 0.082881 | 2 | 15 | 0 | Medium |
| 5 | EMP_207 | Information Management | Mid-level | broker | 0.076300 | 3 | 6 | 0 | Low |
| 6 | EMP_198 | Platform Engineering | Senior | hub | 0.073343 | 1 | 32 | 0 | Medium |
| 7 | EMP_159 | Analytics & BI | Senior | hub | 0.065263 | 2 | 33 | 0 | Medium |
| 8 | EMP_247 | Client Services | Senior | hub | 0.065092 | 2 | 24 | 0 | Medium |
| 9 | EMP_196 | Platform Engineering | Mid-level | broker | 0.059876 | 2 | 11 | 0 | Low |
| 10 | EMP_157 | Data Engineering | Mid-level | balanced | 0.059460 | 4 | 1 | 0 | Low |

---

## Interpretation

- **High betweenness + high Cross_Team_Tie_Count**: boundary-spanning profile — structurally important for flow across team boundaries.
- **`Isolation_Risk_Flag = 1` on a broker-ranked row**: treat as CM-3 tension (isolation score vs network role); triage manually.

## Related outputs

- `sprint2_power_user_concentration.md` — hub / star-network load
- `sprint2_counter_metrics.md` — CM-3 broker guardrail
- `sprint2_interactive_topology.html` — hover shows betweenness and cross-team ties