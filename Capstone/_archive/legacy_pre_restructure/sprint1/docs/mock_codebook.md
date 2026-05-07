# DATA DICTIONARY — Social Telemetry (Nodes + Edges)

This codebook defines variables for **synthetic survey data** used to build organizational network topology maps and isolation-risk models under **no communications content and no geolocation** constraints.

Data are delivered as **two tables**:

1. **`mock_data_nodes.csv`** — one row per employee (node attributes / predictor space).
2. **`mock_data_edges.csv`** — one row per directed help-seeking tie (`Hard`/`Soft`) with tie strength plus relational attribute scores.

---

## Table 1 — Node attributes (`mock_data_nodes.csv`)

| Variable | Category | Description | Scale / Values |
| :--- | :--- | :--- | :--- |
| **EMP_ID** | Meta | Unique employee identifier | e.g. `EMP_001`–`EMP_200` (synthetic) |
| **Seniority** | Meta | Seniority level | `Junior` / `Mid-level` / `Senior` |
| **Team** | Meta | Primary team assignment | `Information Management` / `Data Engineering` / `Solution Architecture` / `Client Services` / `Platform Engineering` / `Analytics & BI` |
| **Years_Exp** | Meta | Total years of professional experience in field | Integer ≥ 0 |
| **Profile_Type** | Meta | Simulation label for prototype validation (optional in live surveys) | `balanced` / `hub` / `broker` / `island` |
| **A1_PostgreSQL** | Hard / Tech | Projects in last 12 months where PostgreSQL / RDBMS was primary tool | `0`–`5` (see [Scale A](#behavioral-scale-sections-a-h)) |
| **A2_Linux** | Hard / Tech | Linux / Unix as primary tool | `0`–`5` |
| **A3_Python** | Hard / Tech | Python as primary tool | `0`–`5` |
| **A4_Cloud** | Hard / Tech | Cloud (AWS/Azure/GCP) as primary tool | `0`–`5` |
| **A5_InfoMgmt** | Hard / Tech | Information management systems as primary tool | `0`–`5` |
| **A6_Networking** | Hard / Tech | Networking & infrastructure as primary tool | `0`–`5` |
| **A7_DataAnalytics** | Hard / Tech | Data analytics & BI tools as primary tool | `0`–`5` |
| **A8_API** | Hard / Tech | API development & integration as primary tool | `0`–`5` |
| **A9_TechConsult** | Hard / Tech | Times in last 3 months colleagues sought respondent for technical advice | `0`–`5` (same scale as Section A frequency bands) |
| **B1_English** | Hard / Lang | Professional interactions primarily in English (last 6 months) | `0`–`5` (see [Scale B](#behavioral-scale-sections-a-h)) |
| **B2_German** | Hard / Lang | Professional interactions primarily in German | `0`–`5` |
| **B3_French** | Hard / Lang | Professional interactions primarily in French | `0`–`5` |
| **B4_OtherLang** | Hard / Lang | Professional interactions in other relevant languages | `0`–`5` |
| **C1_ClientMeetings** | Soft / Business | Client-facing meetings or workshops led/co-led (last 6 months) | `0`–`5` |
| **C2_ScopingSessions** | Soft / Business | Scoping / requirements sessions facilitated (last 12 months) | `0`–`5` |
| **C3_IndustryAdvice** | Soft / Business | Times asked to advise on industry context (last 12 months) | `0`–`5` |
| **D1_KnowledgeSessions** | Soft / Collab | Internal knowledge-sharing sessions organized/led (last 6 months) | `0`–`5` |
| **D2_MentoringCount** | Soft / Collab | Colleagues actively mentored/coached (last 12 months) | `0`–`5` |
| **D3_CrossTeamContrib** | Soft / Collab | Times contributed outside primary team (last 6 months) | `0`–`5` |
| **E1_TeamLeadCount** | Soft / Lead | Times asked to lead/coordinate a project team (last 12 months) | `0`–`5` |
| **E2_EscalationsToMe** | Soft / Lead | Escalations for guidance/sign-off (last 6 months) | `0`–`5` |
| **E3_UnblockCount** | Soft / Lead | Times unblocked team conflict/bottleneck (last 12 months) | `0`–`5` |
| **F1_IncidentsCalled** | Soft / ProbSolve | Complex incidents called in to diagnose (last 6 months) | `0`–`5` |
| **F2_ProblemConsults** | Soft / ProbSolve | Times colleagues sought help troubleshooting (last 3 months) | `0`–`5` |
| **F3_InnovationsAdopted** | Soft / ProbSolve | Adopted innovations / process improvements proposed (last 12 months) | `0`–`5` |
| **G1_MultiCountryProj** | Soft / Cultural | Projects with teammates from 3+ countries (last 12 months) | `0`–`5` |
| **G2_CulturalBridging** | Soft / Cultural | Times facilitated cross-cultural communication (last 12 months) | `0`–`5` |
| **H1_StakeholderExplain** | Soft / Comm | Times translated tech for non-technical stakeholders (last 6 months) | `0`–`5` |
| **H2_DocsAuthored** | Soft / Comm | Documentation artifacts authored/substantially contributed (last 6 months) | `0`–`5` |
| **H3_PresentationsGiven** | Soft / Comm | Presentations to audience ≥ 5 (last 6 months) | `0`–`5` |
| **Isolation_Risk_Flag** | **Target ($y$)** | **Binary label for supervised models:** `1` = high risk of becoming / behaving as a **silent island** (future or structural isolation); `0` = not high risk. See [Isolation Score](#isolation-score-and-isolation_risk_flag) below. | `0` or `1` |

### Behavioral scale (Sections A–H)

Survey scales are defined in `survey.md`. For analysis, codes are integers from the instrument.

**Section A / A9 / C–H (event frequency bands):** `0` Never → `5` highest band (exact cut-points per survey text).

**Section B (language interaction bands):** `0` None → `5` highest band.

### Optional derived features (not in CSV; compute in Python)

These support EDA and feature engineering but are **not** required in the synthetic CSV:

| Variable | Formula |
| :--- | :--- |
| **Hard_Tech_Score** | Mean of `A1`–`A8` |
| **Tech_Consult_Score** | `A9` |
| **Lang_Score** | Mean of `B1`–`B4` |
| **Hard_Score** | Mean of `A1`–`A9`, `B1`–`B4` |
| **Biz_Score** | Mean of `C1`–`C3` |
| **Collab_Score** | Mean of `D1`–`D3` |
| **Lead_Score** | Mean of `E1`–`E3` |
| **ProbSolve_Score** | Mean of `F1`–`F3` |
| **Cultural_Score** | Mean of `G1`–`G2` |
| **Comm_Score** | Mean of `H1`–`H3` |
| **Soft_Score** | Mean of `C1`–`H3` |
| **Competence_Score** | `0.5 * Hard_Score + 0.5 * Soft_Score` |

---

## Table 2 — Directed edges (`mock_data_edges.csv`)

Each row is one **outbound** help-seeking nomination from the survey respondent (**Source**) toward a nominated colleague (**Target**), with tie type, frequency, and mandatory relational attribute scores.

| Variable | Category | Description | Scale / Values |
| :--- | :--- | :--- | :--- |
| **Source_EMP_ID** | Network | Respondent who **seeks help** (tail of directed edge) | `EMP_*` |
| **Target_EMP_ID** | Network | Colleague **nominated for help** (head of directed edge) | `EMP_*` |
| **Interaction_Type** | Network | Help-seeking tie type for this nomination | `Hard` = technical help-seeking; `Soft` = business coordination help-seeking |
| **Interaction_Frequency** | Network / Weight | Self-reported **recency-style frequency** of interacting with this colleague in the nominated tie context; used for tie-strength mapping | `Daily` / `Weekly` / `Monthly` / `Rarely` |
| **Awareness_Score** | Network / Relational attribute | Agreement score describing whether respondent understands the target person's skills/knowledge (Cross & Parker latent knowledge awareness construct). Recorded for every row. | `1`–`5` |
| **Energy_Score** | Network / Relational attribute | Relational energy score describing whether interaction with target is de-energizing or energizing. Recorded for every row. | `1`–`5` |
| **Nomination_Rank** | Network | Order of nomination **within the same (`Source_EMP_ID`, `Interaction_Type`)** in one survey response | `1`, `2`, or `3` |

### Tie strength mapping (Granovetter, 1973)

To align with Granovetter's "The Strength of Weak Ties" framework:

- **Strong ties**: `Daily`, `Weekly`  
  These ties support local cohesion, trust, and rapid coordination inside teams.
- **Weak ties**: `Monthly`, `Rarely`  
  These ties function as crucial bridges between clusters/functions and reduce whole-network fragmentation.

Recommended ordinal coding for graph weighting:

| Label | **Weight_W** (example) |
| :--- | :---: |
| Daily | 4 |
| Weekly | 3 |
| Monthly | 2 |
| Rarely | 1 |

Teams may instead use the raw categorical labels in graph tools that support ordinal edges.

### Derived network metrics (Cross & Parker terminology; computed from edges)

Examples used in ONA dashboards:

- **Out-degree centrality:** count (or weighted sum) of rows where `Source_EMP_ID` = employee.  
  Use: identify peripheral people/silent islands and compute isolation risk.
- **In-degree centrality:** count (or weighted sum) of rows where `Target_EMP_ID` = employee.  
  Use: identify central connectors/hubs and potential bottlenecks.
- **Betweenness centrality:** shortest-path intermediary importance on the directed graph.  
  Use: identify boundary spanners / information brokers.

---

## Isolation Score and `Isolation_Risk_Flag`

### Isolation Score (construct)

**Isolation Score** is a **composite risk index** built from **ego-network / help-seeking behavior** (primarily from the **edge list**). It is **not** a survey question field; it is computed in analysis (example recipe below).

It is designed to reflect **silent island** risk:

1. **Extremely low outbound activity:** very few or no outbound edges from the employee (`Source_EMP_ID` row count ≈ 0).
2. **Weak tie profile quality:** outbound edges mostly `Monthly` / `Rarely` (predominantly “hiking paths”) *within the same local cluster* but with limited bridging value.
3. **Single point of failure (help concentration):** when the employee does seek help, **most outbound nominations** go to **one** `Target_EMP_ID` (high Herfindahl-style concentration of outbound targets).
4. **Weak-bridge deficit (critical penalty):** strong penalty when the employee lacks outbound **weak ties** that connect to other teams/functions. Under Granovetter's logic, this deficit is a structural root cause of silent silos.

A simple illustrative formula (all components normalized to comparable scales before summing; coefficients tunable):

> **Isolation_Score** =  
> **w1** × *OutboundScarcity*  
> + **w2** × *WeakWeightShare*  
> + **w3** × *TargetConcentration*  
> + **w4** × *WeakBridgeDeficit*

Where:

- **OutboundScarcity** increases as outbound count decreases.
- **WeakWeightShare** increases as the share of `Monthly`+`Rarely` weights on outbound edges increases.
- **TargetConcentration** increases as the proportion of outbound ties to the **modal** target approaches 1.
- **WeakBridgeDeficit** increases when outbound weak ties (`Monthly`/`Rarely`) to cross-functional targets approach zero.

Exact functional forms and weights are **project parameters** (set in Python, validated with stakeholders).

### **`Isolation_Risk_Flag` (target $y$)**

**`Isolation_Risk_Flag`** is a **binary label derived from Isolation Score**:

- Compute **Isolation_Score** for each employee from edges (and optionally node covariates if desired).
- Choose a **high-risk threshold** $\tau$ on `Isolation_Score` (e.g., upper tertile, calibrated to business prevalence assumptions, or ROC-driven in backtests on synthetic ground truth).
- **`Isolation_Risk_Flag` = 1** if `Isolation_Score` ≥ $\tau$, else **0**.

**Intended use:** supervised **binary classification** predicting which employees are at **high risk** of being (or becoming) **silent islands**, using node attributes **$x$** = columns `Seniority`, `Team` (encoded), `Years_Exp`, `A1`–`H3`, and optionally derived scores — **$y$** = `Isolation_Risk_Flag`.

**Important:** In production research, avoid **label leakage**: do not define `Isolation_Score` using the same features you hope to prove are predictors unless the temporal story is explicit (e.g., edges at $t$ predict flag at $t+1$). For this capstone’s synthetic wave, flags are **documented** as aligned with archetypes (`island` prototype) for teaching.

---

## Removed / obsolete fields (vs earlier single-table mock)

The following are **not** used in the new design:

| Removed variable | Reason |
| :--- | :--- |
| **Region** | Client GDPR / privacy posture: no geolocation. |
| **Peer_Nom_Tech**, **Peer_Nom_Client**, **Peer_Nom_Leader**, **Peer_Nom_Total** | Replaced by **row-level edges** in `mock_data_edges.csv` with `Interaction_Type`, `Interaction_Frequency`, `Awareness_Score`, and `Energy_Score`. |

---

## File linkage

- Join **nodes ↔ edges** on `EMP_ID` equal to `Source_EMP_ID` or `Target_EMP_ID`.
- One employee may appear **multiple times** in the edge table (multiple nominations across colleagues or ranks).

---

*Last updated: April 2026 — Social Telemetry capstone (synthetic data specification).*
