# ECBS5228A: Designing Analytics Projects — Sample Exam

**Purpose:** Practice exam with the same structure as the final exam
**Duration:** 90 minutes
**Format:** Closed book, one A4 cheat sheet allowed (handwritten or printed, both sides)

---

## Part A: Concepts (30 minutes, 30 points)

### Section A1: Definitions (12 points, 2 points each)

Provide a clear, concise definition for each term. Include an example where helpful.

1. **Champion** (in stakeholder management)

2. **First-touch attribution vs. Last-touch attribution** (define both and explain the difference)

3. **Selection bias** (in the context of analytics)

4. **Cohort-based LTV**

5. **Scope creep**

6. **Data validity check / Stop-Go gate**

---

### Section A2: Short Answer (18 points, 6 points each)

Answer each question in 3-5 sentences.

**Question 1:** Red Flags in Project Proposals

A potential capstone sponsor says: "We have tons of data — terabytes of logs. I'm sure there's something valuable in there. Just explore and find interesting patterns."

What red flags do you see in this proposal? What questions would you ask before agreeing to take on this project?

---

**Question 2:** Pre-Briefing Blockers

You're presenting analysis findings next week to the leadership team. You've identified that one VP is likely to push back because your findings suggest their team underperformed.

What does "pre-briefing a blocker" mean, and why is it important? What would you do before the meeting?

---

**Question 3:** Multi-Touch Attribution

Your marketing team runs campaigns across Google Search, Instagram, and email. A customer typically sees an Instagram ad, then clicks a Google ad a week later, then converts after receiving an email.

a) Why is this situation challenging for attribution?

b) What are two different approaches you could take to allocate credit, and what are the tradeoffs of each?

---

## Part B: Analysis Matching (15 minutes, 15 points)

### Instructions

Match each business problem (left) with the most appropriate foundational analysis (right). Each analysis may be used once, more than once, or not at all.

**Analyses:**
- A. Funnel Analysis
- B. Channel Attribution
- C. Campaign Effectiveness
- D. CAC/LTV Analysis
- E. Retention Analysis
- F. Power User Analysis
- G. Failure Analysis
- H. Expansion & Monetization Analysis
- I. Ecosystem Analysis

---

**Problems (3 points each):**

1. "We're spending $200K/month across five marketing channels. We need to know which channels are actually driving conversions so we can reallocate budget."

   **Answer:** ___

2. "A small percentage of our users generate 60% of our revenue. We want to understand who they are, what behaviors they share, and how to find more of them."

   **Answer:** ___

3. "Our D7 retention has dropped from 40% to 32% over the past quarter. We need to understand what's driving users away in the first week."

   **Answer:** ___

4. "We offer a free tier and a premium tier at $9.99/month. We want to understand what triggers free users to upgrade and whether we should change the feature limits."

   **Answer:** ___

5. "Our checkout flow has four steps: cart → shipping → payment → confirmation. Leadership wants to know if we should simplify the payment step or improve the shipping step first."

   **Answer:** ___

---

## Part C: Applied (45 minutes, 55 points)

### Scenario: BeatStream

**BeatStream** is a music streaming app with 8 million monthly active users. They offer both a free ad-supported tier and a Premium tier at $9.99/month.

**Business Model:**
- Free tier: Ad-supported, shuffle-only listening, limited skips
- Premium: Ad-free, on-demand listening, offline downloads, high-quality audio

**Current Situation:**
BeatStream has 8 million MAU but only 420,000 Premium subscribers (5.25% conversion). The industry benchmark is 8-12%. The CEO believes this represents a major revenue opportunity.

Two teams are debating the solution:

- **The Product team** believes the problem is the free tier is "too good." Users can listen to music for free, so they have no reason to upgrade. They want to add more restrictions to the free tier (fewer skips, more ads, no lyrics).

- **The Growth team** believes the problem is users don't understand Premium's value. They want to invest in a 30-day free trial campaign and better Premium feature education.

Recent data shows:
- Users who try Premium (via trial) convert at 35%
- But only 8% of free users ever start a trial
- Users who hit the skip limit on free tier churn at 2x the rate of those who don't

**Available Data:**
- `users`: user_id, signup_date, tier (free/premium), trial_start_date, trial_end_date, conversion_date
- `listening`: user_id, session_date, songs_played, skips_used, skip_limit_hit, ads_served
- `features`: user_id, date, feature_used (offline_download, lyrics, high_quality, playlist_create)
- `surveys`: user_id, survey_date, reason_not_premium (too_expensive/dont_need_features/using_competitor/other)

---

### Question C1: Problem & Decision (8 points)

Write the Problem & Decision section for this analysis.

Include:
- The business question (1 sentence)
- Who is asking and why now
- What decision this analysis will inform
- Your hypothesis (if any)

---

### Question C2: Metrics (12 points)

Define the metrics for this analysis.

**Primary Metric (6 points):**
Write a precise, operational definition of your primary metric. It should be specific enough that someone could write SQL from your definition.

**Counter-Metrics (6 points):**
Identify 2 counter-metrics. For each:
- Define the metric
- Label it as Guardrail or Tradeoff
- Explain what could break if you succeed on the primary metric

---

### Question C3: Stakeholders (10 points)

**Power-Interest Grid (5 points):**
Place at least 4 stakeholders from the scenario into the appropriate quadrants. Use their titles/roles.

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | | |
| **Low Power** | | |

**Blocker Analysis (5 points):**
Identify one potential blocker from this scenario. Explain:
- Their role
- Why they might block or resist findings
- One specific mitigation strategy

---

### Question C4: Methodology (10 points)

Select 2-3 foundational analyses appropriate for this problem. For each:
- Name the analysis
- Explain what specific question it answers in this scenario
- Note what data from the scenario you would use

---

### Question C5: Pre-Mortem (15 points)

Write a pre-mortem for this analysis. Imagine the project has failed and you're looking back 6 months from now.

Your pre-mortem should:
- Tell a specific "story from the future" (not generic failure)
- Identify what went wrong and why
- Show a plausible causal chain (ideally involving correlation/causation confusion or stakeholder dynamics)
- Suggest what should have been done differently

**Length:** 1-2 paragraphs (approximately 150-250 words)

---

## End of Sample Exam

**Scoring Summary:**
- Part A: 30 points
- Part B: 15 points
- Part C: 55 points
- **Total: 100 points**

---

# Answer Key

## Part A Answers

### A1 Definitions

1. **Champion:** A stakeholder who actively advocates for your project. They have influence within the organization and will speak positively about your work to others, especially decision-makers. Champions can be armed with talking points to help sell your findings.

2. **First-touch vs. Last-touch attribution:**
   - First-touch: Gives 100% credit to the first marketing touchpoint the customer encountered (e.g., the Instagram ad they saw first)
   - Last-touch: Gives 100% credit to the final touchpoint before conversion (e.g., the email they clicked to purchase)
   - Difference: First-touch favors awareness channels; last-touch favors conversion channels. Neither captures the full customer journey.

3. **Selection bias:** When the sample you're analyzing is systematically different from the population you want to understand. Example: Analyzing only users who completed onboarding to understand onboarding effectiveness — the users who struggled and quit aren't in your data.

4. **Cohort-based LTV:** Lifetime value calculated by tracking a specific group of customers who started at the same time (e.g., January 2025 signups) and measuring their cumulative revenue over time. More accurate than cross-sectional LTV because it accounts for how customer behavior evolves.

5. **Scope creep:** The gradual expansion of a project's goals beyond the original agreement. Starts with "while you're at it, could you also..." and ends with a project that's impossible to complete on time. Prevented by clear scope documentation and saying no to additions.

6. **Data validity check / Stop-Go gate:** A checkpoint before proceeding with analysis to verify that the data meets required assumptions. Example: "Before analyzing conversion rates, verify that tracking was consistent across all channels." If the check fails, you stop rather than produce misleading results.

### A2 Short Answer

1. **Red Flags:**
   - No clear business question or decision
   - "Explore and find interesting patterns" = undefined scope
   - No hypothesis to test
   - Questions to ask: "What decision will this inform? What would you do differently if we found X vs. Y? Who will act on this?"

2. **Pre-Briefing Blockers:**
   - Meet with the potential blocker before the main meeting
   - Share findings privately so they're not surprised publicly
   - Understand their concerns and incorporate valid points
   - Give them a chance to prepare a response
   - Why: Reduces public resistance, shows respect, may surface legitimate issues you missed

3. **Multi-Touch Attribution:**
   - a) Challenging because multiple touchpoints contributed; giving all credit to one is arbitrary
   - b) Approaches:
     - Linear attribution: Split credit equally (simple, but treats all touchpoints as equal)
     - Time-decay: Give more credit to touchpoints closer to conversion (favors conversion channels)
     - Data-driven/algorithmic: Use statistical models to estimate contribution (most accurate, most complex)

## Part B Answers

1. B - Channel Attribution
2. F - Power User Analysis
3. E - Retention Analysis
4. H - Expansion & Monetization Analysis
5. A - Funnel Analysis

## Part C Answer Guide

**C1 Problem & Decision:**
- Question: "Should we restrict the free tier or invest in trial promotion to increase Premium conversion?"
- Who: CEO; now because conversion rate is below industry benchmark
- Decision: Resource allocation between Product (restrictions) vs. Growth (trials)
- Hypothesis: The problem may be trial awareness, not free tier quality — given that trial converters hit 35% but only 8% try trials

**C2 Metrics:**
- Primary: Free-to-Premium conversion rate = (users who convert to Premium in month M) / (free users at start of month M)
  - Denominator: users with tier='free' on first day of month
  - Numerator: users whose conversion_date is within month M
- Counter-metrics:
  - Free tier churn rate (Guardrail) — restricting free tier might drive users away entirely
  - Premium churn rate (Tradeoff) — more conversions might mean lower-quality subscribers who cancel quickly

**C3 Stakeholders:**
- Grid should include: CEO (High Power, High Interest), Product team lead (HP, HI), Growth team lead (HP, HI), Engineering (LP, LI — they just build what's decided)
- Blocker: Product or Growth team lead — findings will favor one approach over the other
- Mitigation: Pre-brief both teams, frame as data-informed decision, acknowledge valid points from both perspectives

**C4 Methodology:**
- Retention Analysis: Do users who hit skip limits churn faster? Is the restriction hurting or helping?
- Expansion & Monetization: What triggers trial starts and conversions? What features matter?
- Funnel Analysis: Where in the trial flow do users drop off?

**C5 Pre-Mortem:**
Strong answers should include:
- Correlation/causation: "We found that users who hit skip limits churned more, so we removed the skip limit. But it turned out skip-limit users were casual listeners who were going to churn anyway — the limit wasn't causing churn."
- Stakeholder dynamics: "The Product team rejected our findings because we didn't pre-brief them. They felt attacked and blocked implementation."
- Specific mitigation: "We should have run an A/B test before making permanent changes."
