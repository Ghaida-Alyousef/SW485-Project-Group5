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
| F | يمنى سعدالدين بيطار | 444204759 | Comparative analysis and final recommendation |

The detailed responsibilities, planned internal deadlines, and learning reflection template are in [docs/task_distribution.md](docs/task_distribution.md).

## Project Overview and Motivation

This project develops an executive classification and decision-support system for a Chief Commercial Officer (CCO) in the airline industry. The planned dashboard combines booking predictions, passenger segmentation, and Generative AI explanations to help commercial managers understand booking behavior and prioritize potential interventions.

Booking completion is commercially relevant because incomplete bookings represent opportunities for further investigation and customer engagement. An airline booking dataset provides a practical setting for comparing classification methods and connecting their outputs to an executive advisory workflow.

## Problem Definition and Domain Selection

**Domain:** Airline commercial operations and passenger booking analytics.

**Business problem:** Commercial managers need to identify booking attempts that are less likely to be completed and understand the associated booking characteristics. Reviewing individual records manually does not provide a consistent way to prioritize attention or summarize patterns.

**Classification task:** Predict whether a booking will be completed (`booking_complete`: 0 = incomplete, 1 = completed) using 13 booking and passenger-related features. This is a binary classification problem.

**Intended decision support:** Present estimated booking completion likelihood, relevant model drivers, passenger segments, and suggested commercial actions. Example actions include targeted re-engagement or reviewing ancillary bundles. Model associations will inform hypotheses; they will not establish that an intervention causes higher conversion.

The system is an academic prototype. Real pricing and intervention decisions would require additional data and validation. The dataset does not include price, so the dashboard will not claim to estimate the effect of price changes.

## Dataset Selection and Justification

**Selected dataset:** Airlines Seat Booking  
**Provider:** anandshaw2001 on Kaggle  
**Source:** [Kaggle dataset page](https://www.kaggle.com/datasets/anandshaw2001/airlines-booking-csv/data)

The supplied domain approval screenshot identifies the project as a **Chief Commercial Officer (CCO) Flight Booking & Passenger Advisory Dashboard**.

| Criterion | Justification |
| --- | --- |
| Relevance | The dataset contains airline booking records with sales channel, trip type, purchase lead time, route, booking origin, flight duration, and optional service preferences. Its target, `booking_complete`, directly matches the CCO booking advisory problem. |
|Completeness|  50,000 bookings, 13 input features, and no missing values. This meets the handbook requirements of several hundred rows, at least 10–15 features, and at least two classes. |
| Quality |No missing values. 719 fully duplicated rows were found; since there is no booking ID, they were kept and a group-aware split was used. The target is imbalanced (85.04% incomplete, 14.96% completed), which is handled in evaluation. |
| Accessibility | The data is a single CSV file that can be read directly in Python. The raw file is kept unchanged in `Dataset/customer_booking.csv`.|

The source URL, license, and original purpose are recorded in [Dataset/dataset_info.txt](Dataset/dataset_info.txt).

## Phase 1 Results at a Glance

| Item | Result |
| --- | --- |
| Dataset | 50,000 bookings, 13 input features, binary target `booking_complete` |
| Class balance | 85% incomplete, 15% completed |
| Models compared | Random Forest and Logistic Regression |
| Evaluation | 5-fold grouped cross-validation and a held-out test set of 10,011 bookings |
| Best model | **Random Forest** |
| Test ROC-AUC | **0.782** (Logistic Regression: 0.691) |
| Test F1-score (completed class) | **0.438** at threshold 0.19 (Logistic Regression: 0.354 at threshold 0.16) |
| Strongest predictor | Booking origin |

## Phase 1 Scope

**Handbook deadline: October 22, 2026.**

1. Define the problem and justify the selected dataset.
2. Inspect the data and document feature and target distributions, statistical summaries, relationships, and key insights.
3. Document preprocessing and feature engineering with justifications.
4. Train at least two different supervised classification algorithms and justify their selection.
5. Tune hyperparameters and use 5- or 10-fold cross-validation.
6. Evaluate accuracy, precision, recall, F1-score, confusion matrices, and ROC-AUC for a binary target; include suitable visualizations.
7. Compare errors, interpretability, and computational cost, then recommend a model for Phase 2.

Both models use the same target definition, train/test split, cross-validation folds, and evaluation metrics, so the comparison is fair. Encoders and the scaler were fitted on the training data only to prevent data leakage.

## Phase 1 Repository Structure

| Path | Purpose |
| --- | --- |
| `README.md` | Project overview, motivation, team details, results, and navigation |
| `.gitignore` | Excludes secrets, local environments, caches, and notebook checkpoints |
| `Dataset/customer_booking.csv` | Original downloaded CSV, unchanged |
| `Dataset/dataset_info.txt` | Source URL, license, and original purpose |
| `Dataset/preprocessed_data.csv` | Encoded and scaled data for modeling, with a `data_split` column marking training and testing rows |
| `Dataset/train_preprocessed.csv`, `Dataset/test_preprocessed.csv` | The same training and testing sets saved separately |
| `Phase1_Data_Exploration.ipynb` | Problem statement, dataset justification, inspection, EDA, preprocessing, and insights |
| `Supervised_Learning/Phase1_Supervised_Learning.ipynb` | Both models, tuning, evaluation, comparison, and Phase 2 next steps |
| `Supervised_Learning/evaluation_results/` | Saved metrics, test predictions, cross-validation folds, tuning results, and feature importance for both models |
| `Supervised_Learning/plots/` | Evaluation plots for both models |
| `docs/task_distribution.md` | Individual responsibilities, handoffs, deadlines, and learning reflections |

## How to Run

1. Open `Supervised_Learning/Phase1_Supervised_Learning.ipynb` in Google Colab or Jupyter and run all cells. If the local data file is not found, the notebook reads it directly from this GitHub repository.
2. The results are saved in `evaluation_results/` and the plots in `plots/`, next to the notebook.

The results in this repository were produced in Google Colab with scikit-learn 1.6.1 and random seed 42. The Random Forest hyperparameter search takes about 35 minutes on a free Colab session. Running on a different computer can produce slightly different cross-validation folds.

## Phase 2 Plan

**Handbook deadline: December 3, 2026.**

- Compare at least two clustering methods, interpret passenger segments, and explain their integration with supervised predictions.
- Integrate Generative AI to turn model outputs into executive briefings and tailored intervention suggestions.
- Build an interactive dashboard with supported scenario controls, confidence information, key driver charts, and executive KPI summaries.
- Document prompt design, testing, limitations, and the final interface link.

Phase 2 roles will be assigned separately. All members must participate in at least one ML component across the project, and role rotation is recommended by the handbook.

## Dashboard
The dashboard link will be added here in Phase 2.

## Collaboration and Assistive Tools

Each member is responsible for documenting and interpreting her own work and reviewing the full pipeline. One designated member will submit the GitHub link through LMS.

ChatGPT was used to help organize and draft these two Markdown documents from the supplied project handbook, approved domain information, and team role allocation. The team must review and adapt this draft to reflect its own reasoning, verify dataset claims, and complete implementation and personal reflections. This disclosure follows the handbook's requirement to explain assistive tool use; it is not a record of completed analysis.
