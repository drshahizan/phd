
# 📘 Chapter 3: Methodology – Detailed Feedback


### 📌 **1. Research Design**

#### 🔎 Weakness:
- The chapter does not explicitly justify **why a quantitative approach** is used over qualitative or mixed methods.
- There's no strong linkage between the **research objectives/questions** and the chosen design.

#### ✅ Recommendations:
- Clearly explain **why quantitative survey** is the most appropriate method for this study—e.g., suitable for testing technology adoption models like TAM/UTAUT.
- Use a phrase like:  
  > "This research adopts a quantitative design due to its ability to test hypothesized relationships between latent variables in a structured and generalizable way."

- Provide a table aligning **each research objective** with the **research question, hypothesis, and data collection method**.

---

### 📌 **2. Population, Sampling, and Sample Size**

#### 🔎 Weakness:
- Sampling method is mentioned (simple random), but **population size and sampling frame are vague**.
- No statistical justification (e.g., G*Power or Krejcie & Morgan table) is given for the sample size.

#### ✅ Recommendations:
- Define the **target population** precisely (e.g., final-year students from 5 federal polytechnics).
- Explain the **sampling process**, e.g., stratified by institution or program?
- Include a statistical formula or tool to justify your sample size.

**Example**:
> The sample size of 380 was determined using the Krejcie and Morgan (1970) formula for a population size of approximately 10,000 students with a 95% confidence level.

---

### 📌 **3. Instrumentation**

#### 🔎 Weakness:
- The questionnaire constructs are not clearly mapped to **previous studies or validated instruments**.
- Some constructs may lack operational definitions or references.

#### ✅ Recommendations:
- Provide a **table mapping each construct to source articles**, item counts, and measurement scale used (e.g., 5-point Likert scale).
- Clearly state if **items were adapted or adopted**, and what validation process (e.g., expert review, pilot test) was conducted.

---

### 📌 **4. Validity and Reliability**

#### 🔎 Weakness:
- There is **no detailed plan for testing construct validity**, including convergent, discriminant, and content validity.
- Reliability is mentioned (Cronbach’s alpha), but thresholds and decision criteria are not specified.

#### ✅ Recommendations:
- Outline a clear **measurement model validation plan**:
  - **Content validity** via expert review
  - **Construct validity** via Confirmatory Factor Analysis (CFA)
  - **Convergent validity** using Average Variance Extracted (AVE > 0.5)
  - **Discriminant validity** using Fornell-Larcker criterion or HTMT ratio
- Clarify that Cronbach’s alpha > 0.7 indicates acceptable internal consistency.

---

### 📌 **5. Data Analysis Techniques**

#### 🔎 Weakness:
- The mention of PLS-SEM is appropriate but not well justified.
- There's no step-by-step breakdown of **how PLS-SEM will be applied** (e.g., model evaluation stages).

#### ✅ Recommendations:
- Justify PLS-SEM due to:
  - Model complexity
  - Non-normal data tolerance
  - Predictive focus
- Outline analysis stages:
  1. Outer model assessment (reliability and validity)
  2. Inner model assessment (path coefficients, R², effect size, predictive relevance)
  3. Hypothesis testing (bootstrapping)

---

### 📌 **6. Ethical Considerations**

#### 🔎 Weakness:
- Briefly mentioned with no details about **confidentiality, voluntary participation, or data protection**.
  
#### ✅ Recommendations:
- Expand the section to include:
  - Ethical clearance from university
  - Informed consent
  - Anonymous data handling
  - Secure data storage

---

## 📈 Reflection: Alignment with Information Systems (IS) Research Steps

A robust IS research methodology typically follows these steps:

| **Step** | **Your Chapter** | **Comment** |
|----------|------------------|-------------|
| **1. Define research problem** | Covered in Chapter 1 | ✓ Good |
| **2. Establish theoretical foundation** | Partial in Chapter 2 | Needs stronger model justification |
| **3. Develop research model & hypotheses** | Implicit | Needs to be explicitly stated in Chapter 3 |
| **4. Select research methods** | Quantitative method chosen | ✓ Valid, but needs better justification |
| **5. Design instrument** | Survey described | Needs construct mapping and reference to validated instruments |
| **6. Collect data** | Planned | Sampling frame & method need clarification |
| **7. Analyze data** | PLS-SEM proposed | ✓ Good choice, but execution plan should be detailed |
| **8. Interpret results** | (Expected in Chapter 4) | Not yet done |
| **9. Contribute to theory & practice** | (Expected in Chapter 5) | Not yet done |

---

## ✅ **1. Expert Validation**

### 🔎 Weaknesses in Your Chapter 3:
- There’s **no mention** of expert validation to ensure the content validity of the questionnaire items.
- Items were adapted, but it's unclear whether domain experts reviewed the adaptations for contextual suitability (e.g., Nigerian polytechnic education, generative AI).

### 🛠️ Recommendations:
Expert validation ensures the **content validity** of your instrument—that the items **adequately represent** the constructs in your conceptual model.

### 🔁 Suggested Steps:
1. **Select Experts**:
   - Minimum of 3–5 experts in IS, educational technology, or AI in education.
   - Preferably include at least one practitioner from the polytechnic sector.

2. **Prepare an Evaluation Rubric**:
   Experts should rate each item based on:
   - Relevance (e.g., 1 = not relevant, 4 = highly relevant)
   - Clarity (wording and syntax)
   - Appropriateness to local context (Nigeria/polytechnics)

3. **Calculate Content Validity Index (CVI)**:
   - **I-CVI (Item-level CVI)**: Proportion of experts rating an item as 3 or 4.
   - **S-CVI (Scale-level CVI)**: Average I-CVI across all items.
   - Acceptable threshold: I-CVI ≥ 0.78 for 3–5 experts.

4. **Revise Questionnaire**:
   Based on expert feedback—clarify wording, remove ambiguous items, or add locally relevant indicators.

### 📌 How to Report in Chapter 3:
> To ensure content validity, the initial instrument was reviewed by five experts in Information Systems and Educational Technology. Each item was rated for relevance and clarity. The Content Validity Index (CVI) was calculated, and items with an I-CVI score below 0.78 were revised or eliminated.

---

## ✅ **2. Pilot Study**

### 🔎 Weaknesses in Your Chapter 3:
- The **pilot study** is mentioned only vaguely, with **no detail** on how it will be executed, how many participants are involved, or how reliability will be tested.

### 🛠️ Recommendations:
A pilot study helps to **test instrument clarity, reliability, and timing** before full data collection.

### 🔁 Suggested Steps:

1. **Sample Size**:
   - 30–50 participants from a similar population (e.g., students in polytechnics not included in main study)
   - Avoid institutions targeted in final data collection to prevent contamination

2. **Objectives of Pilot**:
   - Assess understanding of questionnaire items
   - Detect issues in wording or layout
   - Estimate internal consistency using **Cronbach’s alpha**
   - Ensure response timing is manageable

3. **Reliability Testing**:
   - Use **Cronbach’s alpha** for internal consistency (α ≥ 0.7 is acceptable)
   - Optionally: run **Exploratory Factor Analysis (EFA)** to assess factor structure before Confirmatory Factor Analysis (CFA) in full study

4. **Instrument Revision**:
   Based on results (e.g., low alpha values, ambiguous questions), refine the items.

### 📌 How to Report in Chapter 3:
> A pilot study was conducted with 40 students from a non-targeted Nigerian polytechnic. Participants completed the draft questionnaire, and reliability analysis was performed using Cronbach’s alpha. Constructs with alpha values below 0.70 were revised for clarity. The feedback from the pilot also informed layout improvements and timing estimates for the main study.

---

## ✅ Suggested Table: Summary of Validation & Pilot Procedures

| **Step**               | **Purpose**                           | **Method**                       | **Expected Output**                |
|------------------------|---------------------------------------|----------------------------------|------------------------------------|
| Expert Validation      | Ensure content relevance & clarity    | CVI scores by 5 experts          | Refined and context-validated items |
| Pilot Study            | Test reliability and clarity          | 30–50 participants, Cronbach’s α | Reliable instrument for full study |
| Final Instrument Prep  | Confirm structure and usability       | Minor revisions post-pilot       | Final questionnaire                |

---

## 🎓 Academic Justification (for Chapter 3 write-up)
Include a paragraph like:

> The validation process followed best practices in IS research methodology (Straub et al., 2004; Hair et al., 2017), ensuring both content and construct validity. Expert judgment contributed to content adequacy, while a pilot study enabled empirical testing of reliability and usability. These steps enhance the overall instrument quality and the rigor of subsequent SEM analysis.


## ✅ Final Suggestions

1. Include a **summary diagram or table** showing the overall methodology flow.
2. Add **hypothesis statements** based on your model at the end of Chapter 3.
3. Clarify your **measurement model and evaluation criteria** for SEM.
4. Strengthen **construct reliability and validity strategy** with references.
5. Ensure that all constructs are clearly defined and traceable to theory.
