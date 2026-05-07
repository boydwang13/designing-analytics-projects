# EMPLOYEE COMPETENCY SURVEY — Behavioral Signal Instrument | EMEA Professional Services

This survey measures competence through observable behavioral frequencies — what actually happened — not self-assessed skill levels. All responses are anonymous.

## RESPONDENT PROFILE
Background information about the respondent.

| Variable | Field Label | Response Format | Signal Type |
| :--- | :--- | :--- | :--- |
| **EMP_ID** | Employee ID (auto-assigned) | Identifier | Metadata |
| **Seniority** | Your seniority level | Junior / Mid-level / Senior | Metadata |
| **Team** | Your primary team | Information Management / Data Engineering / Solution Architecture / Client Services / Platform Engineering / Analytics & BI | Metadata |
| **Years_Exp** | Total years of professional experience in your field | Integer (years) | Metadata |

---

## SECTION A — HARD SKILLS: IT / Technical Activity

> **Why this question:** Instead of asking employees to self-rate their skill level, we ask how often each technology appeared in their actual work. Frequency of real deployment is a behavioral proxy for demonstrated competence.

*In the last 12 months, in how many projects did you use each technology as a PRIMARY tool?*
**Scale:** `0` = Never | `1` = 1–2 projects | `2` = 3–5 projects | `3` = 6–10 projects | `4` = 11–20 projects | `5` = More than 20 projects

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **A1_PostgreSQL** | Behavioral frequency | PostgreSQL / Relational Databases |
| **A2_Linux** | Behavioral frequency | Linux / Unix Systems |
| **A3_Python** | Behavioral frequency | Python Programming |
| **A4_Cloud** | Behavioral frequency | Cloud Platforms (AWS / Azure / GCP) |
| **A5_InfoMgmt** | Behavioral frequency | Information Management Systems (ECM, DMS, etc.) |
| **A6_Networking** | Behavioral frequency | Networking & Infrastructure |
| **A7_DataAnalytics**| Behavioral frequency | Data Analytics & BI Tools (Tableau, Power BI, etc.) |
| **A8_API** | Behavioral frequency | API Development & Integration |

### Technical Consultation Frequency
> **Why this question:** Consultation frequency captures the organization's revealed trust in an employee's technical expertise — a system-level signal independent of self-assessment.

*In the last 3 months, how many times did colleagues proactively seek you out for technical advice or problem-solving help?*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **A9_TechConsult** | Behavioral frequency | Colleagues sought me out for technical advice or help debugging / designing solutions |

---

## SECTION B — HARD SKILLS: Language Usage

> **Why this question:** Asking how often a language was used professionally captures active operational proficiency, not self-declared level. A language only counts if it is being deployed in real work interactions.

*In the last 6 months, how many professional interactions (client meetings, emails, written deliverables) did you conduct primarily in each language?*
**Scale:** `0` = None | `1` = 1–5 interactions | `2` = 6–15 interactions | `3` = 16–30 interactions | `4` = 31–50 interactions | `5` = More than 50 interactions

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **B1_English** | Behavioral frequency | English |
| **B2_German** | Behavioral frequency | German |
| **B3_French** | Behavioral frequency | French |
| **B4_OtherLang** | Behavioral frequency | Other relevant language (Arabic, Polish, Dutch, etc.) |

---

## SECTION C — SOFT SKILLS: Business Engagement

> **Why this question:** Business competence is measured through counts of client-facing activities and advisory roles — behaviors that leave an organizational footprint rather than self-reported confidence levels.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **C1_ClientMeetings** | Behavioral frequency | In the last 6 months: client-facing meetings or workshops I led or co-led |
| **C2_ScopingSessions**| Behavioral frequency | In the last 12 months: project scoping or requirements-gathering sessions I facilitated |
| **C3_IndustryAdvice** | Behavioral frequency | In the last 12 months: times I was asked to advise on industry-specific context for a client engagement |

---

## SECTION D — SOFT SKILLS: Knowledge Sharing & Collaboration

> **Why this question:** Collaboration and knowledge-sharing are measured through concrete outputs (sessions organized, people mentored, cross-team contributions) — these are observable, countable organizational behaviors.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **D1_KnowledgeSessions**| Behavioral frequency | In the last 6 months: internal knowledge-sharing sessions, demos, or tech talks I organized or led |
| **D2_MentoringCount** | Behavioral frequency | In the last 12 months: colleagues I actively mentored or coached (at least 2 or more sessions each) |
| **D3_CrossTeamContrib**| Behavioral frequency | In the last 6 months: times I proactively contributed to a project or task outside my primary team |

---

## SECTION E — SOFT SKILLS: Leadership Signals

> **Why this question:** Leadership is captured through escalation patterns and coordination requests — behavioral signals that reflect how the organization actually treats an individual, not how they perceive themselves.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **E1_TeamLeadCount** | Behavioral frequency | In the last 12 months: times I was asked to lead or coordinate a project team |
| **E2_EscalationsToMe** | Behavioral frequency | In the last 6 months: times colleagues or managers escalated a decision to me for guidance or sign-off |
| **E3_UnblockCount** | Behavioral frequency | In the last 12 months: times I stepped in to unblock or resolve a team-level conflict or bottleneck |

---

## SECTION F — SOFT SKILLS: Problem Solving Activity

> **Why this question:** Problem-solving is measured through incident involvement counts, consultation frequency, and adopted innovations — all traceable organizational events rather than self-assessed capability.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **F1_IncidentsCalled** | Behavioral frequency | In the last 6 months: complex issues or incidents I was personally called in to diagnose or resolve |
| **F2_ProblemConsults** | Behavioral frequency | In the last 3 months: times colleagues sought me out to help troubleshoot or solve a problem |
| **F3_InnovationsAdopted**| Behavioral frequency | In the last 12 months: non-standard solutions or process improvements I proposed that were actually adopted |

---

## SECTION G — SOFT SKILLS: Cross-Cultural Collaboration

> **Why this question:** Cultural awareness is captured through multi-country project participation and active facilitation of cross-cultural communication — concrete events rather than self-declared sensitivity.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **G1_MultiCountryProj**| Behavioral frequency | In the last 12 months: projects I worked on involving team members from 3 or more different countries |
| **G2_CulturalBridging**| Behavioral frequency | In the last 12 months: times I actively facilitated communication or resolved misunderstandings arising from cultural differences |

---

## SECTION H — SOFT SKILLS: Communication Output

> **Why this question:** Communication competence is measured through counts of concrete communication outputs — stakeholder explanations delivered, documentation authored, presentations given — not self-rated clarity or confidence.

*Please indicate how many times each of the following occurred in the specified time period.*
**Scale:** `0` = Never | `1` = 1–2 times | `2` = 3–5 times | `3` = 6–10 times | `4` = 11–20 times | `5` = More than 20 times

| Variable | Signal Type | Survey Question / Behavioral Prompt |
| :--- | :--- | :--- |
| **H1_StakeholderExplain**| Behavioral frequency | In the last 6 months: times I translated or explained a technical concept to a non-technical stakeholder |
| **H2_DocsAuthored** | Behavioral frequency | In the last 6 months: documentation artifacts I authored or substantially contributed to (reports, wikis, runbooks, proposals) |
| **H3_PresentationsGiven**| Behavioral frequency | In the last 6 months: times I presented to an audience of 5 or more people (internal or client-facing) |

---

## SECTION I — HELP-SEEKING NETWORK (PEER EDGES + WEIGHTS)

> **Why this section:** To understand collaboration topology under strict data constraints, we collect **who you go to** for help (outbound ties from you) — not message content, email logs, or location. Each row is a **directed edge** `You → Colleague` with a **tie strength** (interaction frequency). Strong ties ("highways") vs weak ties ("hiking paths") inform network visualization and risk analytics.

**Definitions**

- **Hard Skill / Technical problem:** Debugging, solution design, implementation, architecture, data/engineering tooling — not policy or stakeholder politics.
- **Soft Skill / Business coordination problem:** Priorities, stakeholders, resourcing, cross-team alignment, client handling, internal politics — not primarily a technical diagnosis.

**Interaction Frequency (dropdown — required for each nomination)**

Use this to describe how often you **actually** interact with this colleague for help on that *type* of problem (choose one per nomination):

| Code (export) | Label shown in survey |
| :--- | :--- |
| **Daily** | Daily (or most working days) |
| **Weekly** | Weekly |
| **Monthly** | Monthly |
| **Rarely** | Rarely (less than monthly) |

---

### I1 — Hard skill / technical help-seeking (outbound nominations)

*When you encounter a **hard skill / technical** problem at work, **who do you seek help from**?*

For each slot, enter **one colleague `EMP_ID`** and select **Interaction Frequency** for that tie.

| Slot | Field exported | What to answer |
| :--- | :--- | :--- |
| **I1a** | Edge row | Colleague `EMP_ID` #1 + frequency |
| **I1b** | Edge row | Colleague `EMP_ID` #2 + frequency (optional if none) |
| **I1c** | Edge row | Colleague `EMP_ID` #3 + frequency (optional if none) |

**Rules**

- List **up to 3** distinct `EMP_ID`s (no duplicates in I1a–I1c).
- If you genuinely have **no one** you go to for technical help, leave all I1 slots **blank** (this is analytically important).

**Exported variables (edge list):** `Source_EMP_ID` = your `EMP_ID`; `Target_EMP_ID` = nominated colleague; `Interaction_Type` = **Hard**; `Interaction_Frequency` = dropdown value; `Awareness_Score` (1-5); `Energy_Score` (1-5); `Nomination_Rank` = 1, 2, or 3 matching I1a/I1b/I1c.

---

### I2 — Soft skill / business coordination help-seeking (outbound nominations)

*When you encounter a **soft skill / business coordination** problem at work, **who do you go to**?*

For each slot, enter **one colleague `EMP_ID`** and select **Interaction Frequency** for that tie.

| Slot | Field exported | What to answer |
| :--- | :--- | :--- |
| **I2a** | Edge row | Colleague `EMP_ID` #1 + frequency |
| **I2b** | Edge row | Colleague `EMP_ID` #2 + frequency (optional if none) |
| **I2c** | Edge row | Colleague `EMP_ID` #3 + frequency (optional if none) |

**Rules**

- List **up to 3** distinct `EMP_ID`s (no duplicates in I2a–I2c).
- **Do not** repeat the same person already listed in I1 for the same survey wave (if your tool enforces uniqueness across I1+I2); if the tool allows overlap, analysts may de-duplicate by `(Source, Target, Type)`.

**Exported variables (edge list):** `Source_EMP_ID` = your `EMP_ID`; `Target_EMP_ID` = nominated colleague; `Interaction_Type` = **Soft**; `Interaction_Frequency` = dropdown value; `Awareness_Score` (1-5); `Energy_Score` (1-5); `Nomination_Rank` = 1, 2, or 3 matching I2a/I2b/I2c.

---

---

## SECTION J — RELATIONAL ATTRIBUTES ON HELP-SEEKING TIES (Cross & Parker, 2004)

> **Why this section:** Observed help-seeking ties (`Hard`/`Soft`) reveal current information flow, but ONA also needs relational quality dimensions. In this design, **Awareness** and **Energy** are captured as **attributes of each existing help-seeking edge**, not as separate interaction types.

For each nomination entered in **Section I (I1 and I2)**, collect two additional scores:

### J1 — Awareness score (attribute on each Hard/Soft edge)

**Prompt (exact wording):**  
"I understand this person's skills and knowledge. This does not necessarily mean that I have these skills or am knowledgeable in these domains, but that I understand what skills this person has and what domains they are knowledgeable in."

**Scale:** `1` = Strongly disagree | `2` = Disagree | `3` = Neutral | `4` = Agree | `5` = Strongly agree

### J2 — Energy score (attribute on each Hard/Soft edge)

**Prompt (exact wording):**  
"When you interact with this person, how does it affect your energy level?"

**Scale:** `1` = Strongly de-energizing | `2` = Somewhat de-energizing | `3` = Neutral | `4` = Somewhat energizing | `5` = Strongly energizing

**Exported variables (edge list):** `Source_EMP_ID`, `Target_EMP_ID`, `Interaction_Type` = **Hard** or **Soft**, `Interaction_Frequency`, `Awareness_Score` (1-5), `Energy_Score` (1-5), `Nomination_Rank`.

---

### Analysis notes (for researchers / GDPR posture)

- Only **employee identifiers + tie type + frequency + relational scores + competency items** are stored; **no** communications content, **no** geolocation/region fields.
- Inbound visibility (who is nominated heavily) is **derived** by aggregating edges where `Target_EMP_ID` equals an employee; it is not a separate survey question.
