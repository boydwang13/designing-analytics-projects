# Sprint 2 — Team-to-Team Directed Density Matrix

**Purpose**: Operationalize Cross & Parker (2004) block-density analysis at `Team` granularity. Answers Martin's Sprint 1 follow-up question with hard numbers: *"Is one team genuinely a silo — internally busy but externally disconnected?"*

**Construction**: Rows = source team (who seeks help); columns = target team (who is asked). Density = observed directed ties / maximum possible directed ties.
- Diagonal cell `(A, A)` denominator: `|A| × (|A| − 1)` (no self-loops)
- Off-diagonal cell `(A, B)`, A ≠ B, denominator: `|A| × |B|`

**Team sizes**:

| Team | Members |
| :-- | --: |
| Analytics & BI | 62 |
| Platform Engineering | 56 |
| Solution Architecture | 49 |
| Data Engineering | 47 |
| Client Services | 43 |
| Information Management | 43 |

---

## 1. Primary Matrix — Unweighted, all Interaction_Type

### Unweighted directed density (ties per possible)

| source \ target | Analytics & BI | Client Services | Data Engineering | Information Management | Platform Engineering | Solution Architecture |
| :-- | --: | --: | --: | --: | --: | --: |
| **Analytics & BI** | **0.0085** | 0.0124 | 0.0079 | 0.0124 | 0.0101 | 0.0148 |
| **Client Services** | 0.0139 | **0.0116** | 0.0064 | 0.0135 | 0.0154 | 0.0109 |
| **Data Engineering** | 0.0172 | 0.0114 | **0.0046** | 0.0094 | 0.0137 | 0.0100 |
| **Information Management** | 0.0158 | 0.0124 | 0.0124 | **0.0083** | 0.0120 | 0.0114 |
| **Platform Engineering** | 0.0153 | 0.0158 | 0.0103 | 0.0096 | **0.0081** | 0.0098 |
| **Solution Architecture** | 0.0151 | 0.0138 | 0.0083 | 0.0085 | 0.0149 | **0.0085** |

### Diagonal (intra-team cohesion) vs off-diagonal mean (cross-team reach)

| Team | Intra-team density | Off-diag row mean | Ratio (intra / off-diag) |
| :-- | --: | --: | --: |
| Analytics & BI | 0.0085 | 0.0115 | 0.74 |
| Client Services | 0.0116 | 0.0120 | 0.97 |
| Data Engineering | 0.0046 | 0.0123 | 0.37 |
| Information Management | 0.0083 | 0.0128 | 0.65 |
| Platform Engineering | 0.0081 | 0.0122 | 0.67 |
| Solution Architecture | 0.0085 | 0.0121 | 0.70 |

**Reading the ratio**: a value > 1 means the team seeks help internally *more* than (average) with outside teams. In this synthetic Sprint 2 snapshot, all ratios are < 1, indicating cross-team help-seeking dominates intra-team help-seeking — no team shows a classic silo pattern.

---

## 2. Secondary Matrix — Weighted by `Interaction_Frequency_Weight`

(Numerator = sum of edge weights; accounts for tie strength Daily=1.00 / Weekly=0.67 / Monthly=0.33 / Rarely=0.10.)

### Weighted directed density (tie-strength per possible)

| source \ target | Analytics & BI | Client Services | Data Engineering | Information Management | Platform Engineering | Solution Architecture |
| :-- | --: | --: | --: | --: | --: | --: |
| **Analytics & BI** | **0.0061** | 0.0075 | 0.0034 | 0.0069 | 0.0055 | 0.0092 |
| **Client Services** | 0.0080 | **0.0070** | 0.0041 | 0.0087 | 0.0103 | 0.0059 |
| **Data Engineering** | 0.0102 | 0.0059 | **0.0023** | 0.0055 | 0.0072 | 0.0065 |
| **Information Management** | 0.0091 | 0.0074 | 0.0064 | **0.0049** | 0.0062 | 0.0066 |
| **Platform Engineering** | 0.0086 | 0.0101 | 0.0048 | 0.0061 | **0.0050** | 0.0058 |
| **Solution Architecture** | 0.0087 | 0.0092 | 0.0047 | 0.0063 | 0.0083 | **0.0056** |

---

## 3. Split by Interaction_Type

Compare technical (`Hard`) vs business-coordination (`Soft`) help-seeking matrices to see whether silo patterns differ by channel.

### Unweighted · Hard ties only

| source \ target | Analytics & BI | Client Services | Data Engineering | Information Management | Platform Engineering | Solution Architecture |
| :-- | --: | --: | --: | --: | --: | --: |
| **Analytics & BI** | **0.0056** | 0.0053 | 0.0038 | 0.0053 | 0.0052 | 0.0063 |
| **Client Services** | 0.0094 | **0.0039** | 0.0035 | 0.0054 | 0.0066 | 0.0043 |
| **Data Engineering** | 0.0086 | 0.0064 | **0.0023** | 0.0035 | 0.0068 | 0.0048 |
| **Information Management** | 0.0075 | 0.0038 | 0.0040 | **0.0055** | 0.0075 | 0.0038 |
| **Platform Engineering** | 0.0072 | 0.0083 | 0.0042 | 0.0042 | **0.0052** | 0.0029 |
| **Solution Architecture** | 0.0089 | 0.0052 | 0.0022 | 0.0038 | 0.0066 | **0.0043** |

### Unweighted · Soft ties only

| source \ target | Analytics & BI | Client Services | Data Engineering | Information Management | Platform Engineering | Solution Architecture |
| :-- | --: | --: | --: | --: | --: | --: |
| **Analytics & BI** | **0.0029** | 0.0071 | 0.0041 | 0.0071 | 0.0049 | 0.0086 |
| **Client Services** | 0.0045 | **0.0078** | 0.0030 | 0.0081 | 0.0087 | 0.0066 |
| **Data Engineering** | 0.0086 | 0.0049 | **0.0023** | 0.0059 | 0.0068 | 0.0052 |
| **Information Management** | 0.0083 | 0.0087 | 0.0084 | **0.0028** | 0.0046 | 0.0076 |
| **Platform Engineering** | 0.0081 | 0.0075 | 0.0061 | 0.0054 | **0.0029** | 0.0069 |
| **Solution Architecture** | 0.0063 | 0.0085 | 0.0061 | 0.0047 | 0.0084 | **0.0043** |

---

## 4. Asymmetry — which team depends on which?

Top 5 most asymmetric cross-team pairs (based on unweighted density):

| Source → Target | ρ(A→B) | ρ(B→A) | Asymmetry |
| :-- | --: | --: | --: |
| Analytics & BI ← Data Engineering | 0.0079 | 0.0172 | 0.0093 |
| Analytics & BI ← Platform Engineering | 0.0101 | 0.0153 | 0.0052 |
| Platform Engineering ← Solution Architecture | 0.0098 | 0.0149 | 0.0051 |
| Client Services ← Data Engineering | 0.0064 | 0.0114 | 0.0050 |
| Analytics & BI ← Information Management | 0.0124 | 0.0158 | 0.0034 |

**Reading asymmetry**: if `ρ(A → B) ≫ ρ(B → A)` then team A structurally depends on team B for help but not the other way around. This is exactly the *directional* question behind Boundary Spanning (Cross & Parker, 2004).

---

## 5. Visualization

- `sprint2_team_density_heatmap.png` — primary unweighted matrix as annotated heatmap (diagonal outlined in dark blue).
- `sprint2_team_density_heatmap_weighted.png` — same heatmap with frequency-weighted values.

---

## 6. How to read for Sponsor review

- **Silo signature**: team whose diagonal dominates its row. Check the "Ratio (intra / off-diag)" column.
- **Asymmetry signature**: big asymmetry values in §4 mean one team is a help provider for another but not vice-versa.
- **Channel contrast**: compare Hard vs Soft matrices in §3. A team silent on Soft (low off-diagonal) but active on Hard suggests technically embedded but business-coordination isolated.

## Related outputs

- `sprint2_silent_teams_aggregated.md` — aggregates individual Isolation Scores to team level (complementary)
- `sprint2_brokers_shortlist.md` — individual-level boundary spanners (betweenness-ranked)
- `sprint2_interactive_topology.html` — visual counterpart that this matrix converts into hard numbers