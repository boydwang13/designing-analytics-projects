# Sprint 2 Summary Report

**Sprint**: 2 · Weeks 3–4 · **Status**: all 10 Workstreams completed
**Schema**: v1.2.0 · **Seed**: 5228 · **Generated**: end of WS9

## Volume
- Nodes: **300**
- Edges: **1042**

## Network metrics snapshot
- Total inbound nominations: **1042**
- Top-5 hub inbound share: **14.49%**
- Top-10 hub inbound share: **23.32%**
- Inbound Herfindahl Index: **0.009354**

## Isolation Score validation (Scenario Injection Testing)
- ROC-AUC: **0.9999**
- τ_ROC: **0.6917**
- Sensitivity / Specificity: **1.0000 / 0.9923**
- Confusion: TP=41 FP=2 TN=257 FN=0

## Risk Tier distribution
- High: **43**
- Medium: **126**
- Low: **131**

## Key Signals
- All 8 seeded `hub` archetypes correctly appear in Top-8 Central Connectors (`in_degree` primary, `in_strength` tie-break; 100% archetype recovery)
- All 41 seeded `island` archetypes flagged High-risk (zero false negatives)
- Only 2 non-island flagged High-risk (specificity 99.23%)
- Team-level aggregation shows no team crosses the Silent Team threshold (≥40% High)

## Sprint 2 Output Index

| File | Description |
| :-- | :-- |
| `sprint2_nodes_with_metrics.csv` | D2 — full per-node table (20 cols) |
| `sprint2_silent_individuals_shortlist.md` | D3 — Top 20 management list |
| `sprint2_silent_teams_aggregated.md` | D4 — team-level risk view |
| `sprint2_power_user_concentration.md` | D5 — star-network fragility quantified |
| `sprint2_brokers_shortlist.md` | D13 — Top-10 structural brokers (betweenness-ranked) |
| `sprint2_validation_report.md` | D6 — Scenario Injection Testing |
| `sprint2_counter_metrics.md` | D7 — Goodhart's-Law guardrails |
| `sprint2_interactive_topology.html` | D8 — pyvis interactive network |
| `sprint2_summary_report.md` | this file (part of D9) |
| `sprint2_review_pack.md` | sponsor evaluator checklist (part of D9) |

## Handoff to Sprint 3
- Use `Isolation_Risk_Flag` as binary y.
- Use `A1`–`H3`, `Seniority`, `Team` (encoded), `Years_Exp` as x.
- 80/20 holdout + 5-fold CV per PID §58–61.
- Models: Logistic Regression (interpretability) + Random Forest (non-linearity).