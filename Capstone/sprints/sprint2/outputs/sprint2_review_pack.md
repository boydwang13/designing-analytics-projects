# Sprint 2 Review Pack — Sponsor Evaluator Checklist

## Review flow (30-minute meeting)

1. **Open `sprint2_interactive_topology.html`** in browser — verify team clustering (spatially separated 6-team layout), hover on EMP_247 for node detail, hover on an edge for interaction info. Duration: 5 min.
2. **Walk through `sprint2_silent_teams_aggregated.md`** — team-level heat map of silence vs health. Duration: 5 min.
3. **Walk through `sprint2_silent_individuals_shortlist.md` Top 20** with dominant-drivers explanation. Duration: 5 min.
4. **Validation walkthrough** — `sprint2_validation_report.md`: AUC 0.9999, confusion matrix TP=41/FP=2/TN=257/FN=0 at τ_ROC=0.6917. Duration: 10 min.
5. **Counter-metrics + hubs + brokers** — `sprint2_counter_metrics.md` (CM-3), `sprint2_power_user_concentration.md` (Top-10 hubs), `sprint2_brokers_shortlist.md` (Top-10 betweenness). Duration: 5 min.

## Definition of Done (base D1–D11 + D12 density + D13 brokers)

- [x] D1  Schema v1.2.0 (2 new columns in `data/mock_data_edges.csv`)
- [x] D2  `sprint2_nodes_with_metrics.csv` (300 × 20 cols)
- [x] D3  `sprint2_silent_individuals_shortlist.md` (Top 20)
- [x] D4  `sprint2_silent_teams_aggregated.md` (6 teams)
- [x] D5  `sprint2_power_user_concentration.md`
- [x] D13 `sprint2_brokers_shortlist.md` (betweenness + cross-team tie-break)
- [x] D6  `sprint2_validation_report.md`
- [x] D7  `sprint2_counter_metrics.md` (CM-1/2/3)
- [x] D8  `sprint2_interactive_topology.html` (pyvis, self-contained ~1 MB)
- [x] D9  `sprint2_summary_report.md` + `sprint2_review_pack.md`
- [x] D10 `run_sprint2.py` + `notebook.ipynb` + `README.md`
- [x] D11 Governance: CHANGELOG v1.2.0 + v1.2.1 + v1.2.2; `requirements.txt` (includes pyvis / scikit-learn)

## Traceability (Sprint 2 coverage vs sources)

| Source | Requirement | Implementation |
| :-- | :-- | :-- |
| PID Sprint 2 | Centrality + Isolation Score | WS2 + WS3 |
| PID Sprint 2 | Silent islands individuals | WS4 → D3 |
| PID Sprint 2 | Silent teams | WS6 → D4 |
| PID Sprint 2 | Dynamic network map | WS7 → D8 |
| PID Sprint 2 | Management shortlist | WS4 + WS6 |
| PID §66 | Scenario Injection Testing | WS5 → D6 |
| Martin #1 | Boundary Spanning | Cross_Team_Tie_Count in WS2; D13 broker shortlist |
| Martin #2 | Scalability | deferred to Sprint 4 |
| Martin #3 | Numeric mapping | WS1 (schema v1.2.0) |
| Martin #4 | Team clustering | WS7 spring_layout + virtual edges |
| Martin #5 | Hover tooltip | WS7 → D8 |
| CEU course | Counter-metrics | WS8 → D7 |