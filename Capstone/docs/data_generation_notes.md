# Data Generation Notes (schema v1.2.0)

- Seed: `5228`
- Nodes generated: `300`
- Edges generated: `1042`
- Profile mix: `{'balanced': 222, 'island': 41, 'broker': 29, 'hub': 8}`
- Edge schema: `Source_EMP_ID, Target_EMP_ID, Interaction_Type, Interaction_Type_Code, Interaction_Frequency, Interaction_Frequency_Weight, Awareness_Score, Energy_Score, Nomination_Rank`
- Tie-strength mapping (Granovetter ordinal): Daily=4, Weekly=3, Monthly=2, Rarely=1
- Tie-strength mapping (v1.2.0 algorithmic, exponential decay): Daily=1.00, Weekly=0.67, Monthly=0.33, Rarely=0.10
- Interaction_Type_Code mapping (v1.2.0): Hard=1, Soft=0 (slots 2/3 reserved)
- Archetype logic: hub (high inbound), broker (cross-team soft ties), island (low outbound)
