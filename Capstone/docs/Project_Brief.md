# Capstone Project Brief

**Project Name:** Seeing the Silent Teams - Detecting Hidden Support Needs **Date:** March 2026

**Prepared by:** Bo Wang

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

How can we estimate the support needs of "silent" teams who are least likely to provide direct feedback through voluntary surveys, without relying on self-reporting? Which specific teams should receive proactive support interventions (e.g., workflow redesign, training, additional headcount) this quarter?

**Who is asking, and why now?**

Canon EMEA Management (Sponsor: Martin). Currently, support resources are disproportionately allocated to "loud" and visible teams, leaving vulnerable but silent teams unsupported until post-failure analysis.

**Who is the ultimate decision maker?**

Canon EMEA Management (Sponsor: Martin).

**Hypothesis**

We believe that passive, low-friction digital signals (e.g., IT ticket volume, cross-departmental meeting density, system login frequency) can reliably identify teams experiencing "coordination overload" or isolation before they suffer critical failures.


---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Checkout Completion Rate | `order_complete` events / `checkout_start` events, per session, US users, 24h window from checkout start | 61% | Return to 68% |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Average Order Value | Tradeoff | Simplifying checkout may remove upsell opportunities | AOV trend during/after changes |
| 2. Fraud rate | Guardrail | Removing friction may let fraudulent orders through | Chargebacks per 1,000 orders |
| 3. Support tickets | Guardrail | Confusion from UI changes could increase contacts | Tickets tagged "checkout" per 1,000 orders |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | VP Product, CFO | CEO |
| **Low Power** | Checkout PM, UX team, Mobile team | Warehouse ops |

**Champions:** VP Product (initiated request), Checkout PM (wants to fix their product)

**Blockers:** Mobile team lead — defensive about October launch because they're already under performance review pressure after a delayed Q3 roadmap; any additional blame threatens their position

_Strategy: Share early findings privately with Mobile lead before broader presentation. Frame as "understanding what happened," not blame. Acknowledge October was a tight deadline._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Step-by-step funnel analysis | Which step(s) have largest drop-off? | Checkout step events with timestamps |
| 2. Segmented funnel by device | Is mobile disproportionately affected? | Device type per session |
| 3. Cohort comparison (pre/post Oct) | Does drop correlate with UI launch? | User signup dates, conversion by cohort |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Checkout step events with timestamps | Yes | — |
| Device type per session | Yes | — |
| User ID for repeat vs. new | Partial | Use cookie ID as proxy |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Checkout events firing on all OS versions | Compare event counts by OS vs. session counts | >5% gap between sessions and step 1 events |
| Event timestamps are sequential | Check for step 3 before step 2 anomalies | >1% out-of-order events |

---

## 5. Scope & Deliverables

**In Scope**
- Checkout funnel from cart → confirmation (5 steps)
- Segmentation by device, new vs. returning, payment method
- Time comparison: Q4 2025 vs Q3 2025

**Out of Scope**
- Pre-cart behavior (browse, add-to-cart) — separate project
- A/B test design for fixes — this analysis informs what to test
- International markets — US only

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [ ] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Identify step(s) responsible for >80% of the drop
- Effect size with 95% CI excludes zero and exceeds 2pp minimum practical threshold

**Business Success**
- Product team has clear Q2 prioritization
- Projected revenue recovery estimate if fix is implemented

**Decision Forum:** Product Review (Fridays) **Action Owner:** Checkout PM

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Drop concentrated in one step + one segment | Fast-follow fix targeting that step/segment (2-week sprint) |
| Drop spread across funnel | Broader checkout redesign (Q2 roadmap item) |
| Drop correlated with October launch | Roll back or iterate on new payment UI |
| _(inconclusive / null result)_ | Instrument better logging, run 10 user research interviews, revisit in 4 weeks |

**Action Thresholds**
- We will only recommend a fix if: effect size ≥2pp AND 95% CI excludes zero
- We will not act if: drop <1pp or within normal seasonal variance

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 8 |
| Initial findings review | Jan 15 |
| Final delivery | Jan 22 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Checkout event logging is accurate and complete
2. Q3 2025 is a valid baseline (no major anomalies)

**Data Quality Assumptions**
- Device detection is reliable (no major iOS/Android misclassification)

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Logging gaps in checkout steps | M | H | Validate event counts before analysis |
| Multiple Oct changes confound results | M | M | Review release log, control for other changes |
| Mobile team becomes uncooperative | M | M | Private pre-brief, collaborative framing |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | Using anonymized session IDs |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Standard analytics, no new data collection |

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We identified the payment step as the problem, but the logging was broken — step 3 events weren't firing on iOS 17. We recommended a UI fix when the real issue was measurement. The "fix" didn't improve anything. We should have validated logging accuracy before drawing conclusions.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
