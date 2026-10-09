# CCO Flight Booking & Passenger Advisory Dashboard

**Course:** SWE485 — Selected Topics in Software Engineering  
**Institution:** Software Engineering Department, King Saud University  
**Group:** 5  
**Repository name:** `SW485-Project-Group5`

## Team Members

Names are retained in Arabic as provided in the group sheet to avoid guessing official English spellings.

| Role | Student Name | Student ID | Phase 1 Responsibility |
| --- | --- | --- | --- |
| A | غيداء اليوسف | 444200315 | Part A documentation and repository setup |
| B | غلا آل الشيخ | 444200226 | Data inspection and exploratory data analysis |
| C | أميرة السيف | 444200329 | Preprocessing and feature engineering |
| D | منار بن دحمان | 444204602 | Supervised Model 1 |
| E | ريم العليان | 444203000 | Supervised Model 2 and evaluation results |
| F | يمنى سعدالدين نطار | 444204759 | Comparative analysis and final recommendation |

The detailed responsibilities, planned internal deadlines, and learning reflection template are in [docs/task_distribution.md](docs/task_distribution.md).

## Project Overview and Motivation

This project develops an executive classification and decision-support system for a Chief Commercial Officer (CCO) in the airline industry. The planned dashboard combines booking predictions, passenger segmentation, and Generative AI explanations to help commercial managers understand booking behavior and prioritize potential interventions.

Booking completion is commercially relevant because incomplete bookings represent opportunities for further investigation and customer engagement. An airline booking dataset provides a practical setting for comparing classification methods and connecting their outputs to an executive advisory workflow.

## Problem Definition and Domain Selection

**Domain:** Airline commercial operations and passenger booking analytics.

**Business problem:** Commercial managers need to identify booking attempts that are less likely to be completed and understand the associated booking characteristics. Reviewing individual records manually does not provide a consistent way to prioritize attention or summarize patterns.

**Proposed classification task:** Predict whether a booking will be completed using the available booking and passenger-related attributes. The team will confirm the target column, class definitions, feature availability, and dataset dimensions during initial inspection before training.

**Intended decision support:** Present estimated booking completion likelihood, relevant model drivers, passenger segments, and suggested commercial actions. Example actions include targeted re-engagement or reviewing ancillary bundles. Model associations will inform hypotheses; they will not establish that an intervention causes higher conversion.

The system is an academic prototype. Real pricing and intervention decisions would require additional data and validation. In particular, scenario controls must use supported inputs, and the dashboard must not claim to estimate the effect of price changes if price is absent from the dataset.

## Dataset Selection and Justification

**Selected dataset:** Airlines Seat Booking  
**Provider:** anandshaw2001 on Kaggle  
**Source:** [Kaggle dataset page](https://www.kaggle.com/datasets/anandshaw2001/airlines-booking-csv/data)

The supplied domain approval screenshot identifies the project as a **Chief Commercial Officer (CCO) Flight Booking & Passenger Advisory Dashboard**.

| Criterion | Justification and verification plan |
| --- | --- |
| Relevance | The dataset concerns airline bookings and aligns with the selected CCO booking advisory domain. Initial inspection will confirm that its target supports booking completion classification. |
| Completeness | Member B will record the row count, feature count, data types, target classes, and missingness. The dataset must satisfy the handbook requirements of several hundred rows, at least 10–15 features, and at least two classes. |
| Quality | Members B and C will inspect missing values, duplicates, inconsistent categories, unusual values, and class imbalance. Quality conclusions will be based on the actual CSV rather than assumed from its source. |
| Accessibility | The selected source provides a tabular dataset suitable for a Python-based analysis workflow. The downloaded raw file will be retained separately from processed outputs. |

The exact CSV filename, verified dimensions, license, and original purpose must be recorded in `Dataset/dataset_info.txt` after checking the downloaded data and source metadata. These details have not been independently established in this documentation draft.

## Phase 1 Scope

**Handbook deadline: October 22, 2026.**

1. Define the problem and justify the selected dataset.
2. Inspect the data and document feature and target distributions, statistical summaries, relationships, and key insights.
3. Document preprocessing and feature engineering with justifications.
4. Train at least two different supervised classification algorithms and justify their selection.
5. Tune hyperparameters and use 5- or 10-fold cross-validation.
6. Evaluate accuracy, precision, recall, F1-score, confusion matrices, and ROC-AUC for a binary target; include suitable visualizations.
7. Compare errors, interpretability, and computational cost, then recommend a model for Phase 2.

For a fair comparison, both models should use the same target definition, data split, and evaluation protocol. Learned preprocessing must be fitted only on training data and within cross-validation folds to prevent data leakage.

## Planned Repository Structure

This table describes the intended repository layout. Only this README and the task distribution document are supplied in the current documentation package; the remaining files will be added by their assigned owners.

| Path | Purpose |
| --- | --- |
| `README.md` | Project overview, motivation, team details, and navigation |
| `.gitignore` | Exclude secrets, local environments, caches, and notebook checkpoints |
| `Dataset/<raw_dataset_filename>.csv` | Original downloaded CSV, unchanged |
| `Dataset/dataset_info.txt` | Source URL, verified license, and original purpose |
| `Dataset/preprocessed_data.csv` | Cleaned data for the modeling handoff; fitted transformations remain in model pipelines |
| `Phase1_Data_Exploration.ipynb` | Problem statement, dataset justification, inspection, EDA, preprocessing, and insights |
| `Supervised_Learning/Phase1_Supervised_Learning.ipynb` | Both models, tuning, evaluation, comparison, and integration recommendations |
| `evaluation_results/` | Saved metrics, predictions, tuning summaries, and evaluation plots |
| `docs/task_distribution.md` | Individual responsibilities, handoffs, deadlines, and learning reflections |

## Phase 2 Plan

**Handbook deadline: December 3, 2026.**

- Compare at least two clustering methods, interpret passenger segments, and explain their integration with supervised predictions.
- Integrate Generative AI to turn model outputs into executive briefings and tailored intervention suggestions.
- Build an interactive dashboard with supported scenario controls, confidence information, key driver charts, and executive KPI summaries.
- Document prompt design, testing, limitations, and the final interface link.

Phase 2 roles will be assigned separately. All members must participate in at least one ML component across the project, and role rotation is recommended by the handbook.

## Current Status and Reproducibility

This README records the agreed domain and Phase 1 role allocation. It does not claim that analysis, model training, evaluation, or dashboard deployment has been completed.

Once implementation is available, the team will add verified environment requirements, execution instructions, random seeds, dataset dimensions, actual results, and the final dashboard URL.

## Collaboration and Assistive Tools

Each member is responsible for documenting and interpreting her own work and reviewing the full pipeline. One designated member will submit the GitHub link through LMS.

ChatGPT was used to help organize and draft these two Markdown documents from the supplied project handbook, approved domain information, and team role allocation. The team must review and adapt this draft to reflect its own reasoning, verify dataset claims, and complete implementation and personal reflections. This disclosure follows the handbook's requirement to explain assistive tool use; it is not a record of completed analysis.
