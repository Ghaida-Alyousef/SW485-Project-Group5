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
Explain how the segment's historical behavior
relates to this booking's predicted completion.

3. Recommended Actions
Provide TWO specific business actions.
For each action include:
- Action
- Responsible team
- Reason based on supplied evidence
- Suggested KPI to monitor

4. Expected Business Value
Explain the potential benefit of testing these
actions without promising a guaranteed outcome.

5. Risks and Limitations
Identify uncertainty, data limitations,
and any risks of overinterpreting the prediction.

RULES:
- Use only the provided booking and model information.
- Do not invent statistics, prices, or customer details.
- Treat model drivers as associations, not causes.
- Do not assume that a high completion probability
  guarantees a completed booking.
- Prioritize actions using the available context.
- Do not claim that an action will increase conversion
  without experimental evidence.
- Use clear business English.
- Keep the response concise and actionable.


## Response

### 1. Strategic Priority

**Opportunity:** High-value revenue protection and completion assurance for an ultra-long-lead group booking. 

This 5-passenger round-trip booking demonstrates high purchase intent with 3 ancillary add-ons (extra baggage, preferred seat, and meals). With a 55.0% predicted completion probability—well above the overall average (14.9%) and the baseline decision threshold (19%)—the primary strategic objective is to secure this high-intent itinerary while mitigating the churn risks inherent to extreme booking lead times (341 days).

---

### 2. Segment-Based Insight

The booking belongs to **Segment 4 ("Top route (AKLKUL)")**, which historically exhibits a 21.1% completion rate. However, this specific booking’s profile diverges significantly from the segment average in ways that correlate with its higher predicted completion probability (55.0%):

* **Ancillary Commitment:** The booking requests 3 extra services. By comparison, the segment averages a 68% rate for baggage, 45% for meals, and only 23% for preferred seats. High ancillary attachment aligns with the top model drivers (Number of extra services requested).
* **Booking Origin:** The booking originates from Malaysia, a country driver with a 34.4% historical completion rate (5,709 training bookings), outperforming the AKLKUL route baseline (21.1%).
* **Lead Time & Stay Duration Discrepancies:** The segment typically books 102 days ahead for a 21-day stay with 1.6 passengers. This booking is an outlier: 5 passengers, a short 5-day stay, and booked 341 days early. While long lead times historically introduce cancellation risk, the high passenger count combined with full ancillary selection strongly lifts its predicted completion score.

---

### 3. Recommended Actions

#### Action 1: Proactive Schedule Integrity & Retention Engagement
* **Action:** Place this high-probability group booking onto an automated schedule-change safeguard list. If operational or schedule changes occur over the 341-day window, provide priority re-accommodation notifications and direct customer support outreach.
* **Responsible Team:** Customer Experience / Revenue Operations
* **Reason Based on Evidence:** The booking is scheduled 341 days in advance for a short 5-day stay. Because "Length of stay" and "Route" are top model drivers, schedule disruptions on a short-stay itinerary pose a major threat to completion.
* **Suggested KPI:** Booking Retention Rate following schedule adjustments (or Cancellation Rate of high-probability lead bookings prior to departure).

#### Action 2: Targeted Pre-Trip Ancillary & Group Confirmation Triggers
* **Action:** Design a automated multi-stage communication workflow tailored for long-lead Malaysian origin bookings to re-confirm party details and offer complementary schedule management tools (e.g., calendar syncs, flexible rebooking options).
* **Responsible Team:** Direct Marketing / Digital Sales
* **Reason Based on Evidence:** "Booking origin" (Malaysia, 34.4% historical completion) and "Number of extra services requested" (3 requested here) are key model drivers positively associated with higher completion. Maintaining engagement over the 341-day horizon reinforces the passenger's existing high intent.
* **Suggested KPI:** Offer engagement rate (open/click rates) and Booking Completion Rate compared to a control group.

---

### 4. Expected Business Value

* **Revenue Safeguarding:** Testing proactive retention strategies on high-probability, multi-passenger bookings may help protect high-value fare and ancillary revenue over long lead times.
* **Ancillary Yield Optimization:** Preserving bookings with high ancillary attachment (baggage, seats, meals) protects overall route yield on long-haul flights (8.83 hours).
* **Improved Operations Understanding:** Controlled testing of re-engagement workflows will generate empirical evidence on whether proactive touchpoints reduce mid-funnel drop-offs for long-lead international trips.

---

### 5. Risks and Limitations

* **Correlation vs. Causation:** Model drivers (e.g., origin, route, extra services) represent statistical associations, not direct causal relationships. Adding ancillaries does not inherently cause a customer to complete their trip.
* **Extreme Lead Time Uncertainty:** A 341-day lead time carries significant unobserved external risks (e.g., personal plan changes, visa issues, competitive price changes) that historical model features may not fully capture.
* **Non-Guaranteed Outcome:** A 55.0% completion probability indicates a higher relative likelihood compared to the 19% threshold, but it still carries a 45.0% chance of non-completion or cancellation. 
* **Over-Interpreting Segment Profiles:** This booking differs from typical Segment 4 behavior (5 passengers vs. 1.6; 5-day stay vs. 21 days; 341 lead days vs. 102). Relying strictly on segment averages without accounting for specific booking variances could lead to misaligned marketing actions.
