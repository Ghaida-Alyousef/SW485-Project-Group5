# Template 2 prompt design and evaluation

## Purpose and design

The Segment-Aware Strategic Action Plan (T2 v1.1) helps an airline Chief Commercial Officer assign follow-up work after reviewing a Random Forest booking completion score and one of seven K-Means segments. T1, Member C's Structured Executive Briefing, summarizes the outlook. T2 uses zero-shot role prompting, a fixed output structure, and explicit evidence constraints to propose two actions with named owners and measurable KPIs. Each action should connect to a supplied observation and support an experiment or a descriptive baseline.

| Prompt section | Input placeholders or expected content |
| --- | --- |
| Booking profile | `booking_profile` |
| Prediction | `completion_probability`, `decision_threshold`, `predicted_outcome`, `likelihood_tier`, `baseline_rate` |
| Historical context | `origin_context`, `route_context` |
| Global model drivers | `top_model_drivers` |
| Customer segment | `segment_profile` |
| Output | Strategic Priority, Segment-Based Insight, Recommended Actions, Expected Business Value, Risks and Limitations |

The revised prompt requests 200–300 words, separates origin, route and segment rates, and distinguishes booking completion from check-in, cancellation and boarding. It directs the model to preserve the distinction between service requests and purchases and between medians and means. It excludes price and inventory interventions based on the score, requires checkout data before attributing friction, and prevents global feature importance from being used to assign individual effects.

## Inputs and test procedure

Both archived result sets identify the model as `gemini-3.6-flash`. The T2 runner defaults to that model, respects `GEMINI_MODEL` when configured, and uses temperature 0.2, a 2,048-token output cap and minimal thinking. The three inputs come from [the shared reference cases](../../T1_test_cases_reference.json). Predictions and segment profiles were checked against the existing [prediction export](../../Supervised_Learning/evaluation_results/model1_predictions.csv) and [cluster profiles](../../Unsupervised_Learning/cluster_profiles.txt). The 19% model threshold and 14.9% overall rate apply to all three rows.

| Case | Row ID | Predicted completion | Segment rate | Observed outcome |
| --- | ---: | ---: | ---: | --- |
| Low | 9669 | 5% | 5.4% | Incomplete |
| Borderline | 11278 | 25% | 23.8% | Incomplete |
| High | 35092 | 55% | 21.1% | Complete |

Case 1 is a one-passenger web booking from Australia on DMKOOL with a baggage request, 55 days of lead time, and a 26-day stay. Its origin and route completion rates are 5.1% and 6.1%. The archived Gemini response includes this action KPI:

> Step-by-step digital funnel drop-off rate for route DMKOOL bookings.

The full prompt and generated baseline are available in the [Case 1 transcript](../example_outputs/T2_case1.md).

## T2 v1.1 validation

The local runner generated three complete Gemini responses after the earlier connection failure in the agent environment. The [versioned JSON](../example_outputs/T2_v1.1/T2_results.json) and its three case transcripts identify the same model and bookings as the archives. The saved prompts match the current v1.1 renderer. The original T1 and T2 outputs remain the baseline.

## Quantitative comparison

The [comparison script](../compare_templates.py) recomputes the metrics from the nine response strings across all three versions. Use `python Generative_AI/compare_templates.py --include-revised` to reproduce the [per-case comparison](../example_outputs/template_comparison_final.csv) and [template averages](../example_outputs/template_comparison_summary.csv). The [original comparison CSV](../example_outputs/template_comparison.csv) remains intact.

- **Word count** is the number of whitespace-delimited tokens in the saved Markdown response. Markdown punctuation separated by spaces can count as a token.
- **Keyword alignment** equals 100 × distinct matched keywords ÷ 12. The evaluator lowercases the text and extracts contiguous ASCII letters. Matches are exact, so plural forms and synonyms can be missed. The list is booking, completion, probability, segment, passenger, route, risk, recommendation, conversion, action, customer, and flight.
- **Flesch–Kincaid grade** equals 0.39 × words per sentence + 11.8 × syllables per word − 15.59, using Textstat's counts. Markdown headings, lists and route codes can affect sentence and syllable estimates. Higher scores suggest more demanding prose. The grade estimates readability, and says little about factual accuracy.
- The means weight all three cases equally. Keyword coverage can increase with length. Three selected examples from one model are insufficient to infer population-wide differences.

| Row ID | Words T1 / T2 / v1.1 | Keywords T1 / T2 / v1.1 | Grade T1 / T2 / v1.1 |
| --- | ---: | ---: | ---: |
| 9669 | 185 / 584 / 324 | 66.67% / 91.67% / 66.67% | 9.78 / 13.81 / 15.21 |
| 11278 | 193 / 587 / 350 | 58.33% / 91.67% / 83.33% | 10.45 / 14.52 / 16.82 |
| 35092 | 184 / 676 / 344 | 58.33% / 75.00% / 58.33% | 9.63 / 14.09 / 13.73 |
| Mean | 187.33 / 615.67 / 339.33 | 61.11% / 86.11% / 69.44% | 9.95 / 14.14 / 15.25 |

V1.1 was about 45% shorter than the original T2, and all three responses still exceeded the requested 300-word upper target. Keyword coverage fell by 16.67 percentage points and remained above T1. Mean readability grade rose by 1.11 points relative to the original T2, with improvements confined to row 35092. Dense sentences and technical KPI language remain editorial issues.

## Qualitative rubric and case scores

The nine outputs were reviewed against the supplied booking, prediction and historical context. All dimensions use 1 for poor and 5 for strong. For hallucination risk, a higher score means lower risk.

| Dimension | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Relevance (R) | Off topic | Mostly tangential | Mix of relevant and tangential | Mostly relevant | Directly serves the completion decision |
| Detail and completeness (D) | Core sections missing | Major omissions | Core sections present, limited execution detail | Most expected detail present | Complete for its purpose with concrete follow-up |
| Clarity (C) | Hard to follow | Dense throughout | Navigable with substantial reading effort | Clear with minor issues | Concise and easy to scan |
| Personalization (P) | Generic | One case detail | Several details with limited use | Segment and booking context support the response | Segment fit and deviations inform actions |
| Safety and factual accuracy (S) | Serious actionable factual error | Material unsupported claims | Mostly grounded with consequential overstatement | Supported with minor qualification issues | Fully grounded and appropriately cautious |
| Hallucination risk (H) | Invented evidence tied to a consequential action | Multiple unsupported inferences | One material inference or several minor ones | Limited speculative wording | Every factual claim traceable to the input |

| Case | Template | R | D | C | P | S | H | Evidence |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 9669 | T1 | 5 | 4 | 5 | 4 | 3 | 3 | Centers the 5% completion estimate and compares it with segment and overall rates. Five concise sections name owners, with broad actions and no measures. Tailors them to Australian long-lead and baggage bookings. “Primarily driven” implies an unsupported individual explanation, and “expected to be abandoned” sounds overly definitive. |
| 9669 | T2 | 4 | 5 | 3 | 5 | 2 | 2 | Focuses on completion but speculates that the ?04:00 departure time? may ?introduce friction or hesitation.? Gives two named owners and KPIs in five detailed, repetitive sections. Uses the 55-day lead, 26-day stay and baggage request. Conflates origin and segment metrics, narrows a historical rate to web bookings without evidence, and infers revenue leakage. |
| 11278 | T1 | 5 | 4 | 5 | 4 | 3 | 3 | Keeps the decision threshold and uncertain outcome central. Gives concise actions for sales and ancillary products without measures. Uses Vietnam, HANSYD and the segment's baggage and meal requests, while omitting the unusual stay and lead time. The headline overstates what the model says about individual drivers. |
| 11278 | T2 | 3 | 5 | 3 | 5 | 1 | 1 | Booking engagement is relevant, while check-in and overbooking fall outside the decision. Teams and metrics are explicit, but inventory detail adds substantial reading effort. The 98-day stay and 6-day lead establish the segment deviations. The response invents a ?75.0% historical non-completion rate for similar probability profiles?, assumes high margins, and uses these inferences to support overbooking. |
| 35092 | T1 | 5 | 4 | 5 | 4 | 3 | 3 | Gives a short completion outlook with comparisons and named teams. Uses route, origin and three service requests, but leaves KPI and cohort definitions open. “Driven primarily” and “high-value booking” imply unsupported attribution and economic value. |
| 35092 | T2 | 4 | 5 | 3 | 5 | 2 | 2 | Includes a completion KPI and a control comparison, but shifts into schedule and retention claims. Two owners and metrics are explicit across lengthy sections. Tailors actions to the five passengers, 341-day lead and service requests. Claims party size and service selection ?strongly lifts its predicted completion score? without local explanations, and infers fare value and cancellation risk. |
| 9669 | T2 v1.1 | 5 | 5 | 3 | 5 | 4 | 3 | Centers the 5.0% score and separates the 5.1% origin and 5.4% segment rates. Both actions name teams and denominators, and the DMKOOL cohort ties the KPI to the case. Dense phrases such as ?trades below? hurt clarity. ?Require funnel verification before attributing abandonment? avoids the original payment-cause assertion, but the departure-time focus still lacks case evidence, and a funnel audit alone cannot establish whether drop-offs ?stem from user intent.? |
| 11278 | T2 v1.1 | 4 | 5 | 3 | 5 | 3 | 3 | Uses the 98-day stay and six-day lead to differentiate the booking from the segment. Both actions specify owners, cohorts and denominators. The long KPI labels and grade 16.82 limit readability. Overbooking and the invented historical rate are absent. ?Reduces pre-flight operational friction? asserts an untested benefit, service fulfillment is downstream of booking completion, and the before-08:00 cutoff is an analyst choice without supporting evidence. |
| 35092 | T2 v1.1 | 4 | 5 | 4 | 5 | 3 | 3 | The cohort of five-plus passengers on AKLKUL ties the completion KPI to the case, and both actions name owners and denominators. The response is easier to read than the original T2 for this row. It states that party size and extras ?cannot be assumed to directly raise or lower this specific score,? addressing the main baseline error. Yet ?high-intent demand? infers intent, ?helps prevent drop-off? asserts an untested effect, and the 102-day lead and 21-day stay are medians described as averages. |

## Simulated user preference and template selection

The simulated reader is a CCO screening recommendations for action. Preference is an explicitly simulated weighted mean on the 1–5 scale, using 25% relevance, 15% detail, 20% clarity, 10% personalization, 20% safety and factual accuracy, and 10% hallucination risk. The two factual dimensions distinguish the seriousness of an action from the traceability of its evidence. Together they account for 30% of the score. The weights reflect this hypothetical role and use the same reviewer scores, without independent validation or human preference data.

| Case | T1 | T2 | T2 v1.1 |
| --- | ---: | ---: | ---: |
| 9669 | 4.15 | 3.45 | 4.20 |
| 11278 | 4.15 | 2.90 | 3.75 |
| 35092 | 4.15 | 3.45 | 3.95 |
| Mean | 4.15 | 3.27 | 3.97 |

T2 v1.1 improved on the three targeted factual issues: it qualified the friction hypothesis, removed overbooking and its invented historical rate, and explicitly rejected individual attribution to party size or extras. It kept named teams and measurable KPIs while improving simulated preference by 0.70 points. Residual intent claims, unsupported intervention effects, mislabelled medians and the higher average readability grade limit the improvement.

Use **T1 as the default executive dashboard briefing**. Its 187.33-word average, grade 9.95 and simulated CCO score of 4.15 favor quick screening. Review its individual attribution wording before display. T2 v1.1 fits a secondary action-planning view after review of the proposed cohorts, KPIs and evidence for each intervention. The comparison covers one response per case and version from one model, and the preference weights and qualitative scores are reviewer judgments.

## Ethics, limitations, and development notes

Historical cohort rates can vary with time and sample size. HANSYD has 35 training observations. Segment membership describes historical patterns and does not establish individual intent. ROC-AUC describes discrimination and provides no direct evidence of score calibration. Route and origin can proxy for market or demographic differences. Any outreach experiment should check consent, exposure and outcomes across groups before rollout. Humans should review proposed interventions, especially when they could change customer access or operational policy.

A general instruction about causality was insufficient to prevent specific unsupported explanations. Effective prompt practices here include labeling global importance, keeping historical and individual quantities distinct, defining the action scope, and specifying the measurement unit. The project references are Member C's T1 prompt specification on `origin/Amira`, the cluster and prediction exports linked above, and the implementation of Flesch–Kincaid in the local comparison script.

Gemini produced the archived responses. Codex assisted with prompt revisions, reproducible baseline evaluation, rubric drafting, notebook integration, and local verification. The qualitative scores and preferences are analytical judgments generated for this review and require independent review before use as study results.
