# Template 2 - Case 2 - Borderline

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
- Booked 6 days before departure
- Length of stay: 98 days
- Flight: Wednesday at 07:00 on route HANSYD (8.58 hours)
- Booking origin: Vietnam
- Extra services requested: extra baggage, in-flight meals

PREDICTION INFORMATION:
- Completion probability: 25.0%
- Decision threshold: 19%
- Predicted outcome: Likely to be completed
- Likelihood tier: Moderate (above the threshold, but the outcome is uncertain)
- Overall completion rate: 14.9%

HISTORICAL CONTEXT:
- Bookings from Vietnam: 28.4% completed (299 training bookings)
- Bookings on route HANSYD: 22.9% completed (35 training bookings)

MODEL DRIVERS:
1. Booking origin (country the booking was made from): this booking = Vietnam
2. Route: this booking = HANSYD
3. Flight duration: this booking = 8.58 hours
4. Length of stay: this booking = 98 days
5. Number of extra services requested: this booking = 2

CUSTOMER SEGMENT:
"Extra-service lovers" (segment 6 of 7): 9,577 bookings (19.2% of all). Completion rate 23.8%. Typical booking: 42 days ahead, 6-day stay, 1.5 passengers. Requests extra baggage 94%, preferred seat 68%, meals 84% of the time.

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
Protect and validate a moderate-probability, long-stay booking (25.0% completion probability) originating from a high-converting region (Vietnam) with pre-requested ancillaries, without assuming guaranteed conversion or pricing flexibility.

### 2. Segment-Based Insight
While the passenger belongs to the **"Extra-service lovers"** segment (23.8% historical segment completion rate; typical 6-day stay, 42-day lead time), this specific booking exhibits a significantly longer length of stay (98 days) and a shorter booking window (6 days before departure). Despite these individual differences, the booking's 25.0% completion probability remains aligned with strong historical baselines from Vietnam (28.4% completion across 299 bookings) and the HANSYD route (22.9% completion across 35 bookings), both well above the overall 14.9% baseline.

### 3. Recommended Actions
*   **Action 1: Proactive Pre-Departure Service Confirmation**
    *   *Responsible team:* Customer Experience / Ground Operations
    *   *Reason:* The booking includes extra baggage and in-flight meals requested just 6 days prior to an 8.58-hour flight. Ensuring these pre-requested services are confirmed reduces pre-flight operational friction.
    *   *Measurable KPI:* Service fulfillment rate (Denominator: Total requested ancillary items for HANSYD bookings originating in Vietnam; Cohort: Internet bookings 1–7 days before departure).
*   **Action 2: Digital Funnel Drop-Off Audit**
    *   *Responsible team:* Digital Product / E-Commerce Operations
    *   *Reason:* The 07:00 departure time must not be assumed as a cause of friction without verifying funnel data to evaluate whether early-morning departures correlate with payment or checkout drop-offs.
    *   *Measurable KPI:* Web checkout completion rate (Denominator: Total Internet booking sessions initiated for HANSYD flights departing before 08:00; Cohort: Vietnam-origin web users).

### 4. Expected Business Value
By measuring descriptive baselines and testing these actions against a control group, commercial teams can determine whether dedicated ancillary confirmation and digital funnel optimizations directly stabilize completion rates for short-lead, long-stay bookings, rather than relying on unverified assumptions about customer intent.

### 5. Risks and Limitations
A 25.0% completion probability indicates the outcome remains highly uncertain and does not guarantee a completed booking. Feature importances are global drivers and do not indicate individual feature impact. Furthermore, ticket prices, profitability, payment friction, and actual cancellation intent cannot be inferred from the provided data.
