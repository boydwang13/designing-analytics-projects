# Analytics Project Brief

**Project Name:** Content Strategy Analysis **Date:** January 2026

**Prepared by:** Bo Wang

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

Advertising revenue dropped 22% year-over-year. So the company needs to decide on what proportion the company should focus on "hard news" or on "evergreen content". Meanwhile, newsletter engagement is declining. Company needs to know whether that is because email is dying.

**Who is asking, and why now?**

CFO wants to find out the best way to allocate resources between hard news and evergreen content, and CEO to settle internal debates by presenting data-driven recommendations. The problems should be settled now because the growing subscription business cannot offset ad declines.

**Who is the ultimate decision maker?**

CEO and CFO.

**Hypothesis**

We believe we should focus more on evergreen content because it drives higher engagement and retention, which can offset the decline in advertising revenue. Meanwhile, we believe that newsletter engagement is not really declining because external factors like changes in iOS privacy rules are impacting open rates.


---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Advertising Revenue Per Article | 12-month average total Pageviews of each article × (RPM / 1000) | Unknown | improving by 22% |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Number of Pro subscribers | Guardrail | The adjustment of content may reduce the number of Pro subscribers | Monthly Pro subscriber count |
| 2. Pageviews per article | Tradeoff | The adjustment of content may reduce pageviews if users prefer evergreen content | Average monthly pageviews per article |
| 3. Newsletter open rate | Tradeoff | The adjustment of content may reduce newsletter open rates if users prefer evergreen content | Monthly newsletter open rate |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | Manage Closely:CEO | Keep Satisfied:CFO |
| **Low Power** | Keep Informed:TechInsider Editor, CultureDrop Editor | Monitor:VP Audience Development (Christina Lee) |

**Champions:** CEO(needs data to settle internal debates), CFO (wants data to optimize investment strategy)

**Blockers:** TechInsider Editor(threats to quit if hard news coverage is reduced).

_If >2 blockers, what's your strategy?_

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Content Cohort Analysis | How does the performance of hard news vs. evergreen content vary over time? | Article-level data, including publication date, content type, and engagement metrics |
| 2. Failure Analysis (for Email Newsletter)| newsletter engagement going down is not the result of email being dying | Newsletter open rate, send_date, the time when iOS privacy changes |
| 3. | | |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| article data| Yes | — |
| newsletter data | Yes | — |

**Data Validity Checks (Stop/Go)**

_What must be true before analysis proceeds? List checks to validate before drawing conclusions._

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Ad revenue attribution to specific articles | Sum of revenue from Ad impressions table compared with numbers from Finance division | Discrepancy > 5% |
| RPM | within reasonable scope of the industry | 20% more or 20% less than industry average |

---

## 5. Scope & Deliverables

**In Scope**
-3 brands: TechInsider, BusinessBeat, and CultureDrop
-data from last 12 months

**Out of Scope** _(what won't you do, but someone might assume you will?)_
-Sponsored content
-Time on site
-Average pages per session

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [x] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset
- [ ] Other: _______________

---

## 6. Success & Decision Criteria

**Analytical Success** _(how do we know the analysis was sound?)_
- Ad revenue attribution to specific articles is validated within 5% of Finance numbers
- Clear segmentation by content type and time period

**Business Success** _(how do we know it drove impact?)_
- Clear budget recommendation according to findings
- CEO accepts methodology and findings

**Decision Forum:** Management Meeting **Action Owner:** CEO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| newsletter engagement only declines when iOS privacy changes | not reduce newsletter frequency |
| ROI of evergreen content exceeds breaking news by >20% | increase budget for evergreen content |
| _(inconclusive / null result)_ | _(what's the next-best action?)_ |

**Action Thresholds**

_What minimum effect size or confidence level justifies action?_
- We will only recommend action if: The Advertising Revenue Per Article of Evergreen content exceeds Breaking News by >20%
- We will not act if: There is no statistically significant difference between the two content types.

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 23 |
| Initial findings review | Feb 6 |
| Final delivery | Feb 13 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Customers' content preferences remain stable
2. Characteristics of newsletter do not change significantly over the last 12 months

**Data Quality Assumptions**
- Ad revenue data is accurately attributed to articles
- Newsletter open rate data is reliable and not significantly affected by other factors

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Evergreen content and breaking news can not be clearly distinguished | L  | H | create a quantitative criteria to distinguish them |
| iOS privacy changes have fundamentally broken Open Rate tracking, making historical comparisons invalid.| M | H | Switch primary KPI to Click-Through Rate (CTR) or Session Starts from email, which are immune to pixel blocking. |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [ ] | [x] | |

_If any "Yes" above, describe mitigation:_

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We suggested shifting budget to evergreen content, but the CEO rejected it because the analysis did not convincingly show the impact on Pro subscription. As a result, no action was taken, and advertising revenue continued to decline.
---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_

## AI Usage Note

I used Gemini to help me understand some terms and concepts related to content strategy and media industry. I am a bit new to this field, so I found it helpful to get quick explanations.
I also used it to help me brainstorm potential risks and mitigations for the project.