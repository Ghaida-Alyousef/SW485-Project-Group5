# Template 2 - Case 1 - Low

## Prompt


You are a strategic decision-support advisor for
the Chief Commercial Officer (CCO) of an airline.

Your task is to transform booking predictions
and passenger segmentation into practical,
evidence-aware management actions.

BOOKING PROFILE:
- Passengers: 1
- Sales channel: Internet
- Trip type: RoundTrip
- Booked 55 days before departure
- Length of stay: 26 days
- Flight: Monday at 04:00 on route DMKOOL (8.83 hours)
- Booking origin: Australia
- Extra services requested: extra baggage

PREDICTION INFORMATION:
- Completion probability: 5.0%
- Decision threshold: 19%
- Predicted outcome: Likely to be abandoned
- Likelihood tier: Low (below the decision threshold; the booking is expected to be abandoned)
- Overall completion rate: 14.9%

HISTORICAL CONTEXT:
- Bookings from Australia: 5.1% completed (14,274 training bookings)
- Bookings on route DMKOOL: 6.1% completed (538 training bookings)

MODEL DRIVERS:
1. Booking origin (country the booking was made from): this booking = Australia
2. Route: this booking = DMKOOL
3. Flight duration: this booking = 8.83 hours
4. Length of stay: this booking = 26 days
5. Number of extra services requested: this booking = 1

CUSTOMER SEGMENT:
"Top market (Australia)" (segment 1 of 7): 13,272 bookings (26.5% of all). Completion rate 5.4%. Typical booking: 48 days ahead, 22-day stay, 1.3 passengers. Requests extra baggage 73%, preferred seat 34%, meals 55% of the time.

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

### 1. Strategic Priority
Address severe conversion leakage for high-lead long-haul itineraries originating in Australia. The priority is to test engagement strategies that mitigate booking abandonment without altering pricing or inventory.

### 2. Segment-Based Insight
The booking’s predicted completion probability (5.0%) falls below the 19% decision threshold, placing it in the low-likelihood tier. This aligns closely with both the historical completion rate for Australian origin bookings (5.1% across 14,274 bookings) and Segment 1 "Top market (Australia)" average (5.4% across 13,272 bookings). While matching the segment's pattern of long stays (26 days vs. 22-day segment typical) and extra baggage requests (73% segment frequency), it trades below the overall historical baseline of 14.9%.

### 3. Recommended Actions
* **Targeted Retargeting & Nudge Campaign**
  * **Responsible team:** Digital Marketing / Customer Engagement
  * **Reason:** The customer initiated a complex long-haul booking (DMKOOL, 8.83 hours, 26-day stay, 55 days ahead) with extra baggage requested, but model drivers indicate high abandonment risk.
  * **KPI:** Abandoned cart retrieval rate (Denominator: Total uncompleted Internet bookings originating from Australia on route DMKOOL with extra service requests).
* **Booking Funnel Friction Analysis**
  * **Responsible team:** Digital Product / UX Analytics
  * **Reason:** This low probability requires checking channel analytics; early departure times (Monday 04:00) require funnel verification before attributing abandonment to payment or checkout friction.
  * **KPI:** Checkout completion rate by time-stamp step (Denominator: Total unique web sessions reaching the payment page for Australian origin bookings).

### 4. Expected Business Value
Testing these actions against a control group or measuring a descriptive baseline will establish whether targeted digital interventions reduce cart abandonment for long-haul itineraries. It will also clarify if drop-offs stem from user intent or specific website funnel friction.

### 5. Risks and Limitations
Predictions reflect global model drivers and historical probabilities, not individual intent or guaranteed behavior. The data does not provide ticket prices, profit margins, or actual payment friction. Actions must not assume guaranteed conversion increases without controlled trial evidence.
