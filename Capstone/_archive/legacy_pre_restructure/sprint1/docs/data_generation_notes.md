# Sprint 1 Data Generation Notes

- Seed: `5228`
- Nodes generated: `300`
- Edges generated: `1042`
- Profile mix: `{'balanced': 222, 'island': 41, 'broker': 29, 'hub': 8}`
- Edge schema: `Source_EMP_ID, Target_EMP_ID, Interaction_Type, Interaction_Frequency, Awareness_Score, Energy_Score, Nomination_Rank`
- Tie-strength mapping: Daily=4, Weekly=3, Monthly=2, Rarely=1
- Archetype logic: hub (high inbound), broker (cross-team soft ties), island (low outbound)
