# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the course repository for **ECBS5228A "Designing Analytics Projects"**, a 1-credit intensive course for MS in Business Analytics students at Central European University. The course runs over 2 days (January 8 & 12, 2026) and prepares students for their mandatory capstone project.

## Core Architecture

### Three-Pillar Course Structure

1. **Strategic Thinking**: Teaching that data science value extends beyond models in production (the "Webmaster Evolution" narrative)
2. **Foundational Analyses**: 8 analyses structured along the customer journey:
   - Acquisition: Funnel → Channel Attribution → Campaign Effectiveness → Customer Acquisition (CAC/LTV)
   - Retention: Retention Analysis → Power User Analysis → Failure Analysis
   - Growth: Expansion & Monetization Analysis
3. **Capstone Preparation**: Using the Analytics Project Brief framework for professional project design

### Key Course Framework: Analytics Project Brief

The centerpiece teaching tool is the **Analytics Project Brief** (one-page template). Students use this framework across all three assignments:

**Template structure** (see `templates/analytics_project_brief_template.md`):
- Problem & Decision
- Metrics (Primary + 2-3 Counter-Metrics using "What Breaks" framework)
- Stakeholder Map (Power-Interest Grid, Champions & Blockers)
- Foundational Analyses (2-3 selected from the 8 core analyses)
- Scope & Timeline
- Success Criteria
- Assumptions & Risks
- Pre-Mortem Exercise

**Example** (see `templates/analytics_project_brief_example.md`): Netflix Skip Intro feature analysis

### File Organization

```
/Users/earino/CEU/ECBS5228/
├── syllabus.md                    # Official course syllabus (authoritative source)
├── notes.md                        # Teaching implementation notes (detailed lesson plans)
├── templates/
│   ├── analytics_project_brief_template.md   # Blank framework
│   └── analytics_project_brief_example.md    # Netflix case study
├── readings/
│   └── counter_metrics_and_stakeholder_management.md  # Tiered reading list
├── resources/                      # PDFs (capstone regulations, samples, presentation)
├── slides/                         # Marp markdown slides + generated HTML
├── figures/
│   ├── figures.md                  # Image catalog with designer briefs
│   └── images/                     # Designer-created slide images
├── scripts/
│   └── check_overflow.py           # Slide overflow detection tool
├── extract_pdf_text.py             # OCR utility for extracting text from PDFs
├── extract_pdf_with_images.py      # Alternative PDF extraction with image processing
└── *_text.txt                      # Extracted text from PDFs
```

## Common Development Tasks

### PDF Text Extraction

When you need to extract text from PDFs in the `resources/` folder:

```bash
# Extract latest PDF using OCR
python extract_pdf_text.py

# Alternative: extract with full image processing
python extract_pdf_with_images.py
```

**Requirements:**
- PyMuPDF (`pip install PyMuPDF`)
- pytesseract (`pip install pytesseract`)
- Pillow (`pip install pillow`)
- Tesseract OCR binary (`brew install tesseract` on macOS)

The scripts:
- Find the most recently modified PDF in `resources/`
- Convert pages to 300 DPI images
- OCR each page with fallback to direct text extraction
- Output timestamped `course_text_YYYYMMDD_HHMMSS.txt` file

### Viewing Course Materials

Use the `open` command to view files in the default application:

```bash
open /Users/earino/CEU/ECBS5228/syllabus.md
open /Users/earino/CEU/ECBS5228/templates/analytics_project_brief_example.md
```

## Important Course-Specific Concepts

### Counter-Metrics Framework

Counter-metrics prevent Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure"). The "What Breaks" 5-question framework:

1. What directly worsens?
2. What quality degrades?
3. Which user segments are harmed?
4. What long-term metrics suffer?
5. Which other teams' goals are threatened?

Students must identify 2-3 counter-metrics for every analytics project using this framework.

### Stakeholder Management

Uses the **Power-Interest Grid (Mendelow Matrix)** with 4 quadrants:
- High Power + High Interest = Manage Closely
- High Power + Low Interest = Keep Satisfied
- Low Power + High Interest = Keep Informed
- Low Power + Low Interest = Monitor

Students also identify Champions (advocates) and Blockers (potential opponents) with mitigation strategies.

### Assessment Structure

**Assignment 1 (30%)**: Weekend foundational analyses + Analytics Project Brief draft (due Day 2 morning)
**In-Class Assessment (30%)**: 90-minute open-note exam (week of Jan 13-17, exact date TBD)
- Part 1 (60 min): Applied case study - Complete Analytics Project Brief sections
- Part 2 (30 min): Short answer questions on course concepts
**Final Assignment (30%)**: Capstone project preparation (due May 8, 2026)
**Intellectual Presence (10%)**: Attendance and engagement

## Editing Guidelines

### Syllabus Changes

**syllabus.md is the authoritative document**. When making changes:

1. Maintain consistency with course code: `ECBS5228A (T2, AY 2025/26)`
2. All dates reference January 2026 (Day 1: Jan 8, Day 2: Jan 12)
3. Keep 6 blocks × 100 minutes structure (3 blocks per day)
4. This is a **Python-only** program - never reference R or other languages
5. Total suggested pre-Day 1 reading should remain ~27 minutes (2 articles)

### notes.md Structure

Implementation notes organized by:
- Core philosophy & teaching approach
- Detailed breakdown of each foundational analysis (with datasets, deliverables, timing)
- Module-by-module lesson plans (counter-metrics, stakeholder management)
- Assignment grading rubrics

**notes.md informs teaching, syllabus.md is student-facing.**

### Analytics Project Brief Updates

If updating the framework:
1. Update `templates/analytics_project_brief_template.md` (blank version)
2. Update `templates/analytics_project_brief_example.md` (Netflix example)
3. Update references in syllabus.md sections: Learning Outcome #4, Block 3 schedule, all 3 assignments
4. Update `notes.md` teaching modules if pedagogical approach changes

## Course Philosophy Reminders

Key messages to preserve in all materials:

1. **"Your job is never to optimize a metric; it's to improve the experience that the metric measures."**
2. **"Job titles are fragile, responsibilities are durable"** (from the Webmaster Evolution narrative)
3. **"The future of data science value is NOT in models in production"**
4. Foundational analyses follow the **customer journey** (Acquisition → Retention → Expansion)
5. Analytics projects require **adversarial thinking** (counter-metrics, pre-mortem, stakeholder blockers)

## Reading List Tiers

From `readings/counter_metrics_and_stakeholder_management.md`:

- **Suggested** (pre-Day 1): 2 articles, ~27 minutes total
- **Strongly Recommended**: 5 articles with clear "read when relevant" guidance
- **Optional/Reference**: 10+ articles for deep dives

**Do not add to Suggested readings without removing something else** - reading equity is a design constraint.

---

## Slide Generation Standards

Slides are generated using **Marp** (markdown slide generator).

### Slide Build Workflow

**Every time you regenerate slides, follow this workflow:**

1. **Build the HTML:**
   ```bash
   cd slides/
   marp --no-stdin block_XX_name.md --html -o block_XX_name.html
   ```

2. **Check for text overflow:**
   ```bash
   cd /Users/earino/CEU/ECBS5228
   python scripts/check_overflow.py
   ```
   This script loads each HTML file in a headless browser and reports slides where content exceeds the 720px height. Fix any overflowing slides before considering the build complete.

3. **Verify visually** by opening the HTML file and spot-checking flagged slides.

### Overflow Detection Tool

**File:** `scripts/check_overflow.py`

**Requirements:**
- `pip install playwright`
- `playwright install chromium`

**What it does:**
- Loads each HTML file in `slides/` using headless Chromium
- Checks every slide's `scrollHeight` vs the 720px container
- Reports which slides overflow and by how many pixels

**Example output:**
```
block_02_acquisition_analyses.html:
  Slide 10: OVERFLOW (950px, +230px)
  Slide 13: OVERFLOW (750px, +30px)
```

**Fixing overflows:** Split content across slides, reduce text, or use smaller tables/code blocks.

### Analysis Section Checklist

Every foundational analysis section MUST include these elements in order:

1. **What is it?** (1-2 slides)
   - Clear definition in plain language
   - The core question it answers
   - When/why you'd use this analysis

2. **The Data You Need** (1-2 slides)
   - Specific fields required (e.g., `user_id`, `timestamp`, `event_type`)
   - Data structure (show example tables)
   - What's optional vs. required

3. **How to Do It** (3-5 slides)
   - Step-by-step mechanics
   - Formulas or SQL snippets where appropriate
   - Different methods/approaches if applicable

4. **What the Output Looks Like** (1-2 slides)
   - Example output table or visualization description
   - How to read/interpret the results
   - What "good" vs. "bad" looks like

5. **Common Pitfalls / Data Quality Issues** (1 slide)
   - What goes wrong in practice
   - How to detect problems
   - Impact of each issue

6. **Scenario + Brief Application** (2-3 slides, compressed)
   - Company scenario from example Briefs
   - Primary metric + counter-metrics (condensed)
   - Key blocker + pre-mortem lesson

7. **Key Takeaways** (1 slide)
   - 4-6 bullet points
   - Actionable, memorable

### What NOT to Do

- ❌ Don't just show Brief sections without teaching the analysis itself
- ❌ Don't define terms without explaining mechanics
- ❌ Don't skip data structure — students need to know what tables they're querying
- ❌ Don't skip output examples — students need to know what deliverable looks like
- ❌ Don't spend more time on Brief framework than on the actual analysis

### Image Placeholders

Mark with clear HTML comments:
```markdown
<!--
IMAGE PLACEHOLDER: [Description of what image should show]
[Specific details: axes, labels, example data]
-->
```

### Timing Guidelines

- Each foundational analysis: ~12-17 slides for 20-25 minutes
- Include stretch breaks every 45-50 minutes
- Instructor notes in HTML comments for cold-call questions and discussion prompts
