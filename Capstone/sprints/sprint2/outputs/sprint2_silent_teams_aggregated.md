# Sprint 2 — Silent Teams Aggregated View

**Purpose**: Answer PID's "silent **teams**/individuals" question at the *team* level. Sponsor (Martin) Sprint 1 follow-up question: *"Is an entire team becoming an island?"*

**Method**: Aggregate per-node `Isolation_Score` and `Isolation_Risk_Tier` across 6 functional teams. A team is labeled *Silent* if ≥40% of members are `High`-tier, *At Risk* if 20–40%, *Healthy* if <20%.

| Team | Members | Avg Iso Score | Median Iso | % High | % Medium | Zero-Outbound Members | Status |
| :-- | --: | --: | --: | --: | --: | --: | :-- |
| Analytics & BI | 62 | 0.5253 | 0.4583 | 19.4% | 40.3% | 6 | Healthy ●○○ |
| Data Engineering | 47 | 0.5164 | 0.4208 | 19.1% | 31.9% | 7 | Healthy ●○○ |
| Platform Engineering | 56 | 0.5105 | 0.4270 | 14.3% | 39.3% | 7 | Healthy ●○○ |
| Information Management | 43 | 0.4879 | 0.4208 | 14.0% | 44.2% | 4 | Healthy ●○○ |
| Solution Architecture | 49 | 0.4806 | 0.4583 | 10.2% | 46.9% | 1 | Healthy ●○○ |
| Client Services | 43 | 0.4770 | 0.4208 | 7.0% | 51.2% | 3 | Healthy ●○○ |

---

## Interpretation

- **● filled circles** represent risk density (3/3 = silent, 2/3 = at risk, 1/3 = healthy). The ranking is by `Avg_Isolation_Score` descending.
- **Zero-Outbound Members**: employees who did not nominate anyone in Section I of the survey. A team with many zero-outbound members is a strong team-level silent signal.

## Recommended management actions (per tier)

| Status | Action |
| :-- | :-- |
| **Silent Team** (≥40% High) | Immediate team health review with HR; consider cross-team rotation |
| **At Risk** (20–40% High) | Monitor 1 wave; investigate single-manager / structural constraints |
| **Healthy** (<20% High) | No intervention; benchmark peer |

## Related outputs

- `sprint2_silent_individuals_shortlist.md`
- `sprint2_power_user_concentration.md`
- `sprint2_brokers_shortlist.md`
- `sprint2_interactive_topology.html`