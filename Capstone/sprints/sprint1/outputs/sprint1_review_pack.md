# Sprint 1 Review Pack (Week 1-2)

## Scope Achieved
- Synthetic data pipeline established with reproducible seed.
- Nodes and edges regenerated at scale with hub/broker/island archetype injection.
- Data quality gate executed with strict schema/domain/rank checks.
- Initial network topology artifact produced for sponsor walkthrough.

## Data Version (Sprint 1)
- Nodes file: `Capstone/mock_data_nodes.csv`
- Edges file: `Capstone/mock_data_edges.csv`
- Generation seed: `5228`

## Volume Summary
- Nodes: 300
- Edges: 1042

## Data Quality Gate
- Status: PASS
- Null checks: PASS
- Domain checks (`Interaction_Type`, `Interaction_Frequency`, score ranges): PASS
- Nomination rank integrity (unique in `Source_EMP_ID x Interaction_Type`, max 3): PASS
- Detailed report: `Capstone/outputs/dq_gate_report.md`

## Initial ONA Signals (for sponsor discussion)
- Hub pattern is visible via high inbound concentration.
- Broker pattern is visible through Soft ties across teams.
- Silent-island candidates are visible from zero/near-zero outbound degree.

## Artifacts for Demo
- EDA profile table: `Capstone/outputs/eda_profile_v1.csv`
- Topology prototype image: `Capstone/outputs/network_prototype_v1.png`
- Reproducible notebook: `Capstone/notebooks/sprint1_pipeline.ipynb`

## Sprint 2 Input Contract
Use this data snapshot as baseline for:
1. In-degree / Out-degree / Betweenness computation
2. Isolation score formulation and thresholding
3. First management-facing shortlist of silent teams/individuals
