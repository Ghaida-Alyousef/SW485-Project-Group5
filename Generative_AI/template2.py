
"""
Template 2: Segment-Aware Strategic Action Plan
Member D - Generative AI
"""

TEMPLATE_VERSION = "1.1"


def build_template2(case):
    """
    Build a strategic action prompt using the same
    booking information provided to Template 1.
    """

    return f"""
You are a strategic decision-support advisor for
the Chief Commercial Officer (CCO) of an airline.

Your task is to transform booking predictions
and passenger segmentation into practical,
evidence-aware management actions.

BOOKING PROFILE:
{case['booking_profile']}

PREDICTION INFORMATION:
- Completion probability: {case['completion_probability']}
- Decision threshold: {case['decision_threshold']}
- Predicted outcome: {case['predicted_outcome']}
- Likelihood tier: {case['likelihood_tier']}
- Overall completion rate: {case['baseline_rate']}

HISTORICAL CONTEXT:
{case['origin_context']}
{case['route_context']}

MODEL DRIVERS:
{case['top_model_drivers']}

CUSTOMER SEGMENT:
{case['segment_profile']}

TASK:
Generate a strategic action plan using these
five sections:

1. Strategic Priority
Identify the main business concern or opportunity.

2. Segment-Based Insight
Compare the individual prediction with the segment and overall historical
rates. Identify one relevant similarity or difference. Keep the booking
origin, route, and segment statistics distinct.

3. Recommended Actions
Provide TWO specific business actions.
For each action include:
- Action
- Responsible team
- Reason based on supplied evidence
- One measurable KPI, including the cohort and denominator where applicable

4. Expected Business Value
State what the teams could learn by testing these actions against a control
or by measuring a descriptive baseline before proposing a change.

5. Risks and Limitations
Identify uncertainty, data limitations,
and any risks of overinterpreting the prediction.

RULES:
- Use only the provided booking and model information.
- Do not invent statistics, prices, or customer details.
- Treat feature importance as global. Do not infer which features raised or
  lowered this individual score, including passenger count or extra services.
- Departure time does not establish checkout or payment friction. Verify
  potential friction with funnel data before attributing a cause.
- Do not recommend overbooking, standby changes, inventory adjustments, or
  pricing changes based on booking completion scores.
- Do not infer intent, booking value, costs, profit margins, ticket prices,
  or realized revenue from the supplied inputs.
- Distinguish service requests from purchases, and booking completion from
  check-in, cancellation, or boarding. Preserve labels such as median and mean.
- The threshold determines a model class. Do not present the complement of
  the score as an observed non-completion rate.
- Do not assume that a high completion probability
  guarantees a completed booking.
- Prioritize actions using the available context.
- Do not claim that an action will increase conversion
  without experimental evidence.
- Use clear business English.
- Aim for 200–300 words across all five sections. Use short bullets for actions.
"""
