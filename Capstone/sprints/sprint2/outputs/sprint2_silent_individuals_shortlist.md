# Sprint 2 — Silent Individuals Shortlist (Top 20)

**Generated from**: `sprint2_nodes_with_metrics.csv` · **Threshold method**: ROC-optimal τ (Youden's J) + 3-tier layering · **Sponsor intended use**: immediate-intervention candidates for Canon EMEA Professional Services management review.

**Ranking**: primary key `Isolation_Score` (desc); ties broken by `OutboundScarcity` then `TargetConcentration`.

| Rank | EMP_ID | Team | Seniority | Years_Exp | Profile_Type | Isolation_Score | Tier | Dominant Drivers | Validation |
| :-- | :-- | :-- | :-- | --: | :-- | --: | :-- | :-- | :-- |
| 1 | EMP_006 | Solution Architecture | Junior | 5 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 2 | EMP_022 | Client Services | Mid-level | 3 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 3 | EMP_030 | Client Services | Junior | 7 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 4 | EMP_036 | Information Management | Junior | 4 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 5 | EMP_037 | Platform Engineering | Junior | 3 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 6 | EMP_051 | Data Engineering | Junior | 4 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 7 | EMP_059 | Platform Engineering | Junior | 10 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 8 | EMP_067 | Information Management | Mid-level | 2 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 9 | EMP_087 | Platform Engineering | Junior | 1 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 10 | EMP_089 | Data Engineering | Junior | 9 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 11 | EMP_100 | Platform Engineering | Mid-level | 9 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 12 | EMP_106 | Platform Engineering | Junior | 9 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 13 | EMP_110 | Data Engineering | Mid-level | 1 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 14 | EMP_122 | Platform Engineering | Junior | 7 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 15 | EMP_128 | Analytics & BI | Mid-level | 1 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 16 | EMP_135 | Information Management | Junior | 4 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 17 | EMP_139 | Data Engineering | Mid-level | 5 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 18 | EMP_142 | Analytics & BI | Junior | 10 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 19 | EMP_175 | Analytics & BI | Mid-level | 3 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |
| 20 | EMP_201 | Platform Engineering | Junior | 7 | island | 1.0000 | High | OutboundScarcity=1.00 · WeakWeightShare=1.00 | True positive (island) |

---

## Interpretation for management

- **Rows labeled "True positive (island)"** correspond to synthetic employees seeded as the `island` archetype; the algorithm successfully flagged them. In production, such employees would warrant immediate HR / manager outreach.
- **Rows labeled "False positive"** carry high scores despite not being seeded as `island`. Sprint 2 observes 2 FPs total at τ_ROC across 300 nodes (specificity 99.2%). Inspect their `Dominant_Drivers` and treat as flagged-for-investigation rather than confirmed silent-island.
- **Dominant drivers** explain *why* an employee is flagged. OutboundScarcity=1.0 with TargetConcentration=1.0 means zero outbound nominations (strongest structural silence signal). High `WeakBridgeDeficit` indicates intact local ties but missing cross-team weak bridges (Granovetter 1973).

## Related outputs

- `sprint2_validation_report.md` — AUC / ROC / confusion matrix underpinning τ_ROC
- `sprint2_silent_teams_aggregated.md` — team-level aggregate view
- `sprint2_counter_metrics.md` — guardrails against misuse
- `sprint2_brokers_shortlist.md` — structural brokers (betweenness-ranked)