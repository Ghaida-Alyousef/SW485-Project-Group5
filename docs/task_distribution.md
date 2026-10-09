# Phase 1 Task Distribution — Group 5

**Project:** CCO Flight Booking & Passenger Advisory Dashboard  
**Course:** SWE485 — Selected Topics in Software Engineering  
**Repository:** `SW485-Project-Group5`  
**Official Phase 1 deadline:** October 22, 2026

## Confirmed Role Allocation

| Member | Student Name | Student ID | Assigned Role |
| --- | --- | --- | --- |
| A | غيداء اليوسف | 444200315 | Part A documentation and repository setup |
| B | غلا آل الشيخ | 444200226 | Data inspection and EDA |
| C | أميرة السيف | 444200329 | Preprocessing and feature engineering |
| D | منار بن دحمان | 444204602 | Supervised Model 1 |
| E | ريم العليان | 444203000 | Supervised Model 2 and evaluation results |
| F | يمنى سعدالدين نطار | 444204759 | Comparative analysis |

## Responsibilities and Deliverables

### Member A — غيداء اليوسف

- Create the GitHub repository, required folders, and `.gitignore`.
- Maintain `README.md` with member names and IDs, project title, and motivation.
- Document the CCO booking advisory problem and domain selection.
- Write dataset selection and justification, using verified inspection findings from Members B and C.
- Prepare `Dataset/dataset_info.txt` with the Kaggle URL, verified license, and original purpose.
- Maintain this task distribution document and collect each member's own learning reflection.
- Coordinate the documentation sections of `Phase1_Data_Exploration.ipynb` with Members B, C, and F.

**Deliverables:** Repository setup, `.gitignore`, `README.md`, `Dataset/dataset_info.txt`, this document, and Part A introductory documentation.

**Boundary:** Member A coordinates documentation; every member writes and interprets the technical work assigned to her.

### Member B — غلا آل الشيخ

- Inspect the raw data: observations, features, data types, target column, and target classes.
- Calculate mean, standard deviation, minimum, and maximum for applicable numeric features.
- Plot feature distributions using histograms and box plots.
- Examine feature–target relationships, correlations, class distribution, and missing values.
- Write an interpretation beneath each plot and share data quality findings with Member C.

**Deliverables:** Initial inspection and EDA sections in `Phase1_Data_Exploration.ipynb`, with reproducible code, plots, and interpretation.

### Member C — أميرة السيف

- Handle missing values and duplicates; inspect and justify treatment of outliers.
- Define categorical encoding and scaling or normalization where appropriate.
- Engineer, remove, or discretize features only when justified.
- Document each preprocessing decision and identify possible leakage risks.
- Export `Dataset/preprocessed_data.csv` early and share the schema and processing notes with Members D and E.
- Coordinate with the modelers so learned transformations are fitted on training data and within cross-validation folds rather than on the full dataset.

**Deliverables:** Preprocessing sections in `Phase1_Data_Exploration.ipynb`, cleaned CSV, feature definitions, and reproducible preprocessing code.

### Member D — منار بن دحمان

- Choose Supervised Model 1 and justify it using dataset size, feature types, linearity, and interpretability.
- Write well-structured, commented training code.
- Tune hyperparameters and apply 5- or 10-fold cross-validation.
- Calculate accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC for a binary target.
- Plot a confusion matrix heatmap and ROC curve for a binary target. Include feature importance for a tree-based model or a justified alternative explanation method.
- Save metrics, held-out predictions, tuning results, and plots for Member F.

**Deliverables:** Model 1 sections in `Supervised_Learning/Phase1_Supervised_Learning.ipynb` and saved results in `evaluation_results/`.

### Member E — ريم العليان

- Implement Supervised Model 2 using a different algorithm from Member D's.
- Document algorithm rationale, commented training code, and hyperparameter tuning.
- Use the same split and evaluation protocol as Model 1, including cross-validation and required metrics.
- Plot the confusion matrix, ROC curve for a binary target, and applicable feature importance or a justified alternative explanation method.
- Save evaluation outputs in a reusable format so comparison does not require retraining.

**Deliverables:** Model 2 sections in `Supervised_Learning/Phase1_Supervised_Learning.ipynb` and saved results in `evaluation_results/`.

### Member F — يمنى سعدالدين نطار

- Compare both models using the saved outputs and explain which performed best for the business objective.
- Analyze misclassified records, error patterns, and classes that were difficult to predict.
- Discuss predictive performance, interpretability, and computational cost.
- Recommend the final model with evidence and state its limitations.
- Write the supervised notebook's conclusion and “Next Steps for Phase 2 Integration.”
- Write “Key Insights & Challenges” in the data exploration notebook using Members B and C's findings.

**Deliverables:** Model comparison, error analysis, final recommendation, Phase 2 integration steps, and the EDA insights section.

## Handoffs and Shared Evaluation Requirements

| Handoff | Required Information |
| --- | --- |
| B → C and A | Dataset dimensions, target/classes, data types, missingness, duplicates, and EDA findings |
| C → D and E | Cleaned CSV, feature schema, target definition, processing decisions, and leakage prevention instructions |
| D ↔ E | Different algorithm choices; agreed split, seed, cross-validation strategy, positive class, and metric definitions |
| D and E → F | Metrics CSVs, held-out labels and predictions, class probabilities/scores, confusion matrices, tuning summaries, and measured runtime |
| B and C → F | Main exploration insights, preprocessing limitations, and challenges |
| All → A | Reviewed documentation, actual contribution evidence, and individually written learning reflections |

Suggested result filenames are `model1_metrics.csv`, `model2_metrics.csv`, `model1_predictions.csv`, and `model2_predictions.csv` under `evaluation_results/`. These are planned outputs, not existing results. Prediction files should retain a consistent held-out record identifier so Member F can compare errors on the same records.

## Proposed Internal Schedule

Only the October 22 deadline is specified by the handbook. The dates below are suggested coordination dates and must be agreed by the team.

| Owner | Milestone | Proposed Internal Deadline |
| --- | --- | --- |
| A | Repository setup and initial documentation | October 11, 2026 |
| B | Initial inspection and EDA handoff | October 13, 2026 |
| C | Cleaned dataset and preprocessing handoff | October 15, 2026 |
| D and E | Model training, tuning, and saved evaluation results | October 18, 2026 |
| F | Comparison, error analysis, and recommendation | October 20, 2026 |
| All; A coordinates | Final review, notebook execution, documentation, and reflections | October 21, 2026 |
| Designated LMS submitter — to be assigned | Submit the GitHub link | October 22, 2026 |

Members D and E can prepare model code while preprocessing is underway. Member F can draft comparison criteria early, but performance conclusions depend on actual results.

## Individual Learning Reflections

Each member must write her own reflection after completing the work. Reflections must describe actual learning and challenges; the entries below are placeholders, not completed reflections.

| Member | Reflection Status |
| --- | --- |
| A — غيداء اليوسف | Pending — to be written by Member A |
| B — غلا آل الشيخ | Pending — to be written by Member B |
| C — أميرة السيف | Pending — to be written by Member C |
| D — منار بن دحمان | Pending — to be written by Member D |
| E — ريم العليان | Pending — to be written by Member E |
| F — يمنى سعدالدين نطار | Pending — to be written by Member F |

### Reflection Template

Copy this template once for each member and replace the prompts with an individual account:

- **Name and role:**
- **Actual contributions:** Which files or notebook sections did you complete? Include relevant commit or pull request references when available.
- **What I learned:** Explain a technical or collaboration skill gained through the work.
- **Challenge and response:** Describe one concrete challenge and how you addressed it.
- **Understanding of the full pipeline:** Explain how your contribution connects to the other members' work.
- **Next improvement:** State what you would improve or learn in Phase 2.

## Shared Responsibilities and Phase 2 Rotation

All members contribute to documentation, interpretation, integration, and final review. Each member should understand the complete pipeline and record her actual contributions rather than relying only on this planned allocation.

The handbook requires every member to participate in at least one ML component across the project. Phase 2 allocation must therefore include an ML role for anyone whose Phase 1 work did not satisfy that requirement. Phase 2 roles are not assigned by this document.

## Assistive Tool Use

ChatGPT assisted with organizing and drafting the README and this task distribution document from the team's supplied materials and confirmed allocation. Each member must review the relevant content, contribute her own reasoning and technical work, and write her own learning reflection. Record any further assistive tool use accurately in the final submission.
