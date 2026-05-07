# BUSINESS MASTER OF SCIENCE CAPSTONE PROJECT
## PROJECT INITIATION DOCUMENT

### 1. STUDENT
| Field | Details |
| :--- | :--- |
| **Name** | Bo Wang |
| **Program** | Business Analytics |
| **Telephone** | +43 067763160490 |
| **Email** | Wang_Bo2@student.ceu.edu |

### 2. PROJECT SPONSOR
| Field | Details |
| :--- | :--- |
| **Name** | Martin Brüggemann |
| **Position** | EMEA Solution Consultant |
| **Client organization** | Canon EMEA |
| **Telephone** | |
| **Email** | martin.brueggemann@canon-europe.com |

### 3. CAPSTONE PROJECT MANAGER
| Field | Details |
| :--- | :--- |
| **Name** | Eduardo Arino de la Rubia |

---

## PROJECT DETAILS

### Title 
Social Telemetry (Visualization) - Seeing the Silent Teams - Detecting Hidden Support Needs

### Background (summary of reasons for project sponsor’s interest in/significance of project)
The project focuses on the Professional Services in the Information Management Solutions group of Canon EMEA. In the fast-paced software industry, technical roles must continuously update their skills to remain competitive. Currently, knowledge sharing relies heavily on voluntary community participation. This creates a structural bias: highly confident, "loud" employees dominate the conversation, while "silent" teams (who might have critical knowledge gaps) remain invisible. Furthermore, due to "preferential attachment" (where well-connected nodes act as magnets), employees tend to seek help from the same central figures, creating fragile "star networks" that break down if the central node is unavailable. Management needs a systematic way to identify these "silent islands" and bottleneck nodes to optimize the distribution of support and training resources.

### Statement of key problems, objectives and desired outcomes
* **Key Problem:** How can we identify "silent" teams that have hidden support needs or knowledge gaps, given that they are the least likely to actively participate in community calls or speak up?
* **Objective:** To analyze internal communication relationships and build a network topology visualization map that clearly identifies isolated teams (silent islands) and over-relied-upon individuals (central hubs). Furthermore, the project aims to predict the likelihood of an employee becoming a 'silent island' based on their individual attributes (e.g., skills, tenure, role).
* **Primary Deliverable:** A Network Topology Visualization Map showing cross-team communication flows across EMEA to intuitively identify isolated teams (the "silent islands").
* **Minimum Viable Product / Fallback:** If dynamic visualization proves technically infeasible within the Capstone timeframe, a data-driven List of Silent Teams ranked by their isolation score will be delivered to enable immediate management interventions.

### Interim and final deliverables (incl. format of project presentation and technical discussion, target audience)
* **Interim Deliverables:** Bi-weekly progress updates presented directly via Jupyter Notebooks, following an agile methodology (2-week sprints) to demonstrate iterative findings to the sponsor.
* **Final Deliverables:**
  * **Network Topology Map / List & Isolation Score Model:** A visual map of the network showing who asks whom at the individual level in EMEA. If a map proves too technically complex, a comprehensive "List of silent teams" will serve as the minimum viable product. Along with this, a robustly developed "Isolation Score" will be delivered as a quantifiable metric.
  * **Predictive Risk Model:** Building upon the baseline network map, a predictive model will be delivered. This model will identify individuals at high risk of becoming isolated in the future, enabling proactive rather than reactive management interventions.
  * **Technical Discussion & Project Presentation:** A final consulting-style report and presentation summarizing the methodology and actionable insights for management.
  * **Future Research Paragraph:** A specific section acknowledging analytical biases (e.g., intercultural communication differences or alternative media usage that the data might not capture) as a limitation and area for future research.

### Methods of approach (e.g. data, information resources, software, methodologies, key contacts)
* **Data Source:** To strictly comply with GDPR and avoid corporate privacy conflicts, the student consultant will take ownership of generating a synthetic dataset (Mock Data) using Python/AI. No production email or live IT system data will be accessed.
* **Methodology:** To accommodate the sponsor's specific request for topological mapping while strictly applying the foundational analytical frameworks of this program, the analysis will utilize:
  * **Organizational Network Analysis (ONA):** Using Python to construct the baseline communication topology ("star" vs. "mesh" structures).
  * **Power User Analysis:** Applied to the network data to quantitatively identify the "central hubs". This will assess the concentration of communication flows to reveal the vulnerability of the star network.
  * **Broker Analysis:** Identifying "brokers"—individuals who act as rare communication bridges across otherwise unconnected regional clusters.
  * **Failure Analysis:** An exploratory analysis focused on the "silent islands." We will isolate teams with zero or near-zero outbound connections to systematically categorize the lack of communication signals before management applies interventions.
* **Predictive Modelling & Evaluation Framework:** A classification and probability prediction model will be developed to forecast future isolation risks:
  * **Target Variable (y):** A binary variable indicating isolation status (1= Isolated, 0= Connected), derived by setting a high-risk threshold on the baseline Isolation Score.
  * **Modelling Approach:** Using the generated synthetic data, employee attributes (e.g., tenure, language proficiency, hard/soft skill interactions) will serve as predictor variables (x). We will train and tune classification models, specifically Logistic Regression (for high interpretability) and Random Forest (for capturing non-linear relationships and interactions).
  * **Data Structure & Validation Plan:** The synthetic dataset will be randomly split into an 80% work set and a 20% holdout set. The work set will be used for model building and hyperparameter tuning utilizing 5-fold cross-validation to prevent overfitting.
  * **Performance Metrics:** Model performance will be evaluated using the Area Under the ROC Curve (AUC) and Brier Score for probability prediction. Final classification thresholds will be assessed using a Confusion Matrix to evaluate Sensitivity (True Positive Rate) versus Specificity, ensuring the model effectively flags high-risk individuals without generating excessive false alarms for management.
* **Collaboration:** The student will act as the project manager and external consultant, driving the agenda, proposing solutions, and managing the sponsor's time efficiently.

### Sponsor Validation & Practical Utility of Data
1. **Real Data Application (Post-Handoff):** Due to strict GDPR and corporate compliance constraints, the sponsor will not be able to immediately apply this framework to live production email/IT data after handoff. However, the ultimate practical utility of this project is to provide Canon with a "Data Collection Blueprint." The sponsor will use this validated framework to justify and design future, GDPR-compliant anonymous community surveys to feed the exact same model.
2. **Validation of Accuracy & Credibility:** Since the data is synthetic, the sponsor will evaluate the credibility of the "Isolation Score" through Scenario Injection Testing. The consultant will intentionally inject known behavioral archetypes into the mock data (e.g., a simulated team that ignores community calls to optimize billable hours, mimicking the real-world "Swiss team" behavior observed by the sponsor). If the algorithm accurately flags these intentionally isolated nodes without generating false positives, the model's mathematical logic will be validated as credible.
3. **Practical Utility (Sandbox Simulation):** Once the baseline algorithm is validated, the sponsor will evaluate whether the designed "Isolation Score" and network topology can effectively serve as a baseline to simulate and gauge the success of hypothetical management interventions (e.g., simulating how the network fragility changes if a "broker" leaves or if two siloed teams are forced to interact).

### Assumptions (e.g. expected input from client, possible constraints, expected location of work, exclusions)
* **Constraints & Scope:** The analysis is strictly limited to the Professional Services in the Information Management Solutions group of Canon EMEA, excluding any hardware, printer, or camera divisions.
* **Data Assumption:** The student consultant will generate the mock network data, completely bypassing the need for legal/compliance approvals.
* **Exclusions:** Investigating the psychological or root causes of why certain cultures or teams remain silent (Intercultural aspects) is out of scope for the main analysis and will only be acknowledged as a limitation.
* **Working Style:** The project will be managed by the student acting as an external consultant, proactively driving the agenda, proposing solutions, and managing the sponsor.

---

## INITIAL HIGH-LEVEL PROJECT PLAN AND SCHEDULE

### Work breakdown and timing
* **Sprint 0 (Current):** Draft and sign the Project Initiation Document (PID), and finalize the high-level scope.
* **Sprint 1 (Weeks 1-2): Data Generation & Initial Prototype**
  * Generate a large-scale synthetic dataset (Mock Data) via Python/AI, incorporating node attributes (e.g., skills, tenure, region) and connections to reduce noise.
  * Perform Exploratory Data Analysis (EDA) and build an initial prototype of the basic network topology to establish the data pipeline.
* **Sprint 2 (Weeks 3-4): Core ONA & Descriptive Analysis**
  * Compute Centrality and Isolation Scores to identify "Central Hubs" (Power Users), "Brokers" (bridges), and "Silent Islands" (isolated individuals/teams).
  * Deliver the dynamic Network Topology Map and the actionable "List of silent teams/individuals" for management review (First Iteration).
* **Sprint 3 (Weeks 5-6): Predictive Risk Model**
  * Define isolation as a binary target variable (y) and use the simulated employee attributes as predictor variables (x).
  * Train and tune prediction models (e.g., Logistic Regression, Random Forest) using k-fold cross-validation to predict individuals at high risk of becoming isolated.
* **Sprint 4 (Weeks 7-8): Finalization & Reporting**
  * Consolidate all analyses into the final Jupyter Notebook delivery.
  * Draft the Technical Discussion document (incorporating model diagnostics, counter-metrics, and the intercultural bias limitation paragraph).
  * Prepare the final Project Presentation for the Capstone defense.

### Quality review procedure (review meetings)
* **Agile Methodology:** The project will run on 2-week sprints.
* **Review Cadence:** Brief sync meetings every other week with the Project Sponsor (Martin) to present the latest iteration directly from the Jupyter Notebook and adjust the course if necessary. 

### Anticipated expenses if any (must be covered by project sponsor or client organization)
None anticipated.

---

## SIGNATURES (PROJECT INITIATION)

| Role | Name | Date | Signature |
| :--- | :--- | :--- | :--- |
| **STUDENT** | Bo Wang | | |
| **PROJECT SPONSOR** | Martin Brüggemann | | |
| **CAPSTONE PROJECT MANAGER** | Eduardo Arino de la Rubia | | |

---

# BUSINESS MASTER OF SCIENCE CAPSTONE PROJECT
## LETTER OF TERMS

In order to ensure that the Business Master of Science Capstone Project (the Project) of Central European University (the University) runs smoothly and to mutual advantage, please note the following terms under which the project is undertaken.

1. The Project is undertaken by the Student as part of his or her studies at the University.
2. The student is not an employee of the University, so the University cannot enter agreements on his or her behalf or take any liability for his or her actions.
3. The Project is undertaken as part of an educational program and is supervised and examined by a Faculty Supervisor appointed by the University.
4. The Faculty Supervisor is bound contractually and by law to keep confidential any confidential information disclosed to him or her in the supervision and examination of the Project.
5. The client organization (the Client) must assign a named Project Sponsor, who will be available over the duration of the project to advise and guide the Student.
6. The Project Sponsor is expected to give feedback to the Faculty Supervisor on the conduct of the work.
7. The Student and the Faculty Supervisor sign the General Confidentiality and Non-disclosure Agreement (NDA).
8. The Project Sponsor may request a separate confidentiality and non-disclosure agreement to be signed.
9. The Project is a student educational project and should be seen in this context.
10. The work does not constitute professional advice, and no warranties are made regarding the information presented.
11. Neither the Student nor the University and its faculty accept any liability for the consequences of any action taken as a result of the work, or any recommendations made or inferred.
12. The intellectual property rights to the work undertaken and/or the deliverables produced vest in the Client.
13. The Student is required to declare his or her association with the University and with the Client when collecting information from other organizations.
14. The Project Sponsor must provide support, guidance, and opportunities for consultation to enable the student to carry out the Project effectively.
15. For the purpose of the present agreement the Project Sponsor is not a representative of the Client.
16. The Project Sponsor is agreeing to the terms above as an individual and the agreement does not affect the Project Sponsor’s affiliation with the Client in any way.
17. Expenses incurred in the execution of the Project must be met by the Client and paid directly to the Student.

Please confirm that you have read and agreed the terms of engagement by signing below.

### SIGNATURE (LETTER OF TERMS)
| Role | Name / Client Organization | Date | Signature |
| :--- | :--- | :--- | :--- |
| **PROJECT SPONSOR** | | | |

---

# BUSINESS MASTER OF SCIENCE CAPSTONE PROJECT
## GENERAL CONFIDENTIALITY AND NON-DISCLOSURE AGREEMENT

During the course of the Business Master of Science Capstone Project (the Project) of Central European University (the University), I am likely to discuss and have access to information, technology and ideas that various organizations participating in the program regard as confidential.

I agree for the benefit of the client organization (the Client), the University and other participating organizations that I will make all reasonable efforts to hold in strict confidence any information, technologies and ideas that I am told in advance are confidential, that I will not copy, reveal or disclose such information, technology and ideas to any third party, and that I will not use any such information, technology and ideas for my own benefit or for the benefit of any organization with which I am affiliated now or in the future.

I also agree to abide by such other rules and guidelines that the University may reasonably impose.

**This Agreement shall not apply to any information, technology and ideas which:**
* at the date of this Agreement are in the public domain or subsequently come into the public domain through no fault of mine;
* were already known to me on the date of disclosure, provided that such prior knowledge can be substantiated;
* properly and lawfully become available to me from sources independent of the supplying party;
* are disclosed pursuant to the requirement or request of a governmental agency provided that in such an event I shall inform you of the nature and extent of any disclosure so required.

This Agreement shall come into effect from the date below, and the obligation under the Agreement shall remain in effect indefinitely unless agreed otherwise in writing by the Client. This Agreement shall be subject to Austrian law.

### SIGNATURES (NDA)
| Role | Name | Date | Signature |
| :--- | :--- | :--- | :--- |
| **STUDENT** | Bo Wang | | |
| **CAPSTONE PROJECT MANAGER** | Eduardo Arino de la Rubia | | |
| **PROGRAM COORDINATOR** | Dominika Dash | | |
| **CEU PRO-RECTOR FOR RESEARCH** | Eva Fodor | | |
| **PROGRAM HEAD (IF APPLICABLE)** | Gabor Bekes | | |
| **FACULTY SUPERVISOR (IF APPLICABLE)** | | | |