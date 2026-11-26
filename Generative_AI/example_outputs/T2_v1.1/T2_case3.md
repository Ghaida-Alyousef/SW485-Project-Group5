# Template 2 - Case 3 - High

## Prompt


You are a strategic decision-support advisor for
the Chief Commercial Officer (CCO) of an airline.

Your task is to transform booking predictions
and passenger segmentation into practical,
evidence-aware management actions.

BOOKING PROFILE:
- Passengers: 5
- Sales channel: Internet
- Trip type: RoundTrip
- Booked 341 days before departure
- Length of stay: 5 days
- Flight: Friday at 15:00 on route AKLKUL (8.83 hours)
- Booking origin: Malaysia
- Extra services requested: extra baggage, a preferred seat, in-flight meals

PREDICTION INFORMATION:
- Completion probability: 55.0%
- Decision threshold: 19%
- Predicted outcome: Likely to be completed
- Likelihood tier: High (well above the average completion rate)
- Overall completion rate: 14.9%

HISTORICAL CONTEXT:
- Bookings from Malaysia: 34.4% completed (5,709 training bookings)
- Bookings on route AKLKUL: 21.1% completed (2,151 training bookings)

MODEL DRIVERS:
1. Booking origin (country the booking was made from): this booking = Malaysia
2. Route: this booking = AKLKUL
3. Flight duration: this booking = 8.83 hours
4. Length of stay: this booking = 5 days
5. Number of extra services requested: this booking = 3

CUSTOMER SEGMENT:
"Top route (AKLKUL)" (segment 4 of 7): 2,624 bookings (5.2% of all). Completion rate 21.1%. Typical booking: 102 days ahead, 21-day stay, 1.6 passengers. Requests extra baggage 68%, preferred seat 23%, meals 45% of the time.

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


## Response

### Strategic Action Plan

#### 1. Strategic Priority
Protect and capture high-intent demand for a long-lead, multi-service group booking (5 passengers) on a key long-haul route (AKLKUL), ensuring high-probability bookings progress to completion without friction.

#### 2. Segment-Based Insight
While the overall historical completion rate is 14.9%, Malaysia origin bookings complete at 34.4%, and the "Top route (AKLKUL)" segment averages a 21.1% completion rate. At a 55.0% completion probability (above the 19% decision threshold), this individual booking significantly exceeds its segment baseline. However, it diverges sharply from the typical segment profile: it is booked 341 days ahead (vs. segment average of 102 days) for a 5-day stay (vs. segment average of 21 days), with 5 passengers (vs. segment average of 1.6).

#### 3. Recommended Actions
* **Targeted Pre-Departure Engagement**
  * **Responsible Team:** Customer Experience / Digital Marketing
  * **Reasoning:** The booking is made 341 days in advance with 3 extra service requests (baggage, seats, meals). Maintaining engagement over a long lead time helps prevent drop-off.
  * **KPI:** Completion rate of group bookings (5+ passengers) on the AKLKUL route booked >300 days in advance (Denominator: all long-lead group bookings initiated on AKLKUL).
* **Checkout & Payment Funnel Audit**
  * **Responsible Team:** Digital Product / E-Commerce Operations
  * **Reasoning:** Before assuming friction causes non-completion on high-probability bookings, the team must evaluate technical performance across internet bookings originating in Malaysia.
  * **KPI:** Technical drop-off rate at payment step for Malaysia-origin Internet bookings (Denominator: all started checkouts from Malaysia origin).

#### 4. Expected Business Value
By measuring a descriptive baseline or running a controlled A/B test against these actions, teams can determine whether proactive long-lead communications actually influence completion rates or if high-probability bookings complete independently of interventions.

#### 5. Risks and Limitations
A 55.0% completion probability is not a guarantee of a completed booking. Model drivers represent global feature importance, not individual causal drivers; therefore, requesting extra services or having 5 passengers cannot be assumed to directly raise or lower this specific score. Additionally, intent, profit margins, and ticket pricing cannot be inferred from these data points.
