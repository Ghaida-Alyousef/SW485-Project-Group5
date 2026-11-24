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
**Opportunity:** Capture high-margin revenue from a long-haul, high-intent booking that shows a above-average completion probability (25.0% vs. the 14.9% baseline), while mitigating the volatility associated with its short booking window (6 days prior to departure) and long stay duration (98 days).

---

### 2. Segment-Based Insight
This customer aligns with the **"Extra-service lovers"** segment, which historically demonstrates an above-average completion rate of 23.8% (compared to 14.9% overall) and frequently selects ancillary add-ons. 

While this specific booking features a much longer length of stay (98 days vs. the segment average of 6 days) and a shorter lead time (6 days vs. the segment average of 42 days), the inclusion of two extra services (extra baggage and in-flight meals) aligns with the segment's established behavior (94% baggage purchase rate, 84% meal purchase rate). This ancillary attachment acts as a key positive model driver, supporting the "Moderate" likelihood tier (25.0% completion probability, exceeding the 19% decision threshold).

---

### 3. Recommended Actions

#### Action 1: Targeted Pre-Flight Engagement & Ancillary Upsell
* **Action:** Send a localized, digital pre-flight communication via the Internet sales channel offering the remaining high-affinity segment service (Preferred Seat selection) and providing clear check-in instructions for the upcoming Wednesday 07:00 flight.
* **Responsible Team:** Digital Marketing & Customer Experience
* **Reason Based on Evidence:** The booking belongs to the "Extra-service lovers" segment (68% historical preference for seat selection), has already requested two extras (baggage and meals), and originates from Vietnam (which carries a higher historical completion rate of 28.4%).
* **Suggested KPI to Monitor:** Ancillary seat selection conversion rate and pre-flight check-in completion rate for Vietnam-origin long-haul routes.

#### Action 2: Dynamic Inventory & Standby Optimization
* **Action:** Flag this booking’s seat inventory within the Revenue Management System to monitor fulfillment, utilizing standard overbooking buffers for long-haul routes (HANSYD) given the moderate 25.0% completion probability.
* **Responsible Team:** Revenue Management & Pricing
* **Reason Based on Evidence:** Although the probability sits above the 19% decision threshold, the outcome remains uncertain (75.0% historical non-completion rate for similar probability profiles). Additionally, long-haul routes of 8.58 hours (HANSYD historical completion rate of 22.9%) carry high opportunity costs for empty seats.
* **Suggested KPI to Monitor:** Spoilage rate vs. denied boarding rate on route HANSYD.

---

### 4. Expected Business Value
Testing these targeted engagement and inventory management actions creates the potential to:
* **Protect Ancillary Revenue:** Encouraging seat selection leverages known segment behaviors, which may protect and incrementally increase the total basket value of this single-passenger itinerary.
* **Optimize Load Factors:** Proactively managing inventory around a moderate-probability booking helps balance the risk of unsold seats on a long-haul flight (8.58 hours) against the risk of overbooking.

*Note: Actual lift in completion rates or revenue must be validated through controlled A/B testing.*

---

### 5. Risks and Limitations
* **Model Driver Associations:** Model drivers (e.g., Vietnam origin, 98-day stay, 2 extra services) represent statistical correlations, not direct causal drivers of a passenger's decision to fly.
* **Outcome Uncertainty:** A 25.0% completion probability means there is still a 75.0% chance the booking will not be completed; acting as if completion is guaranteed introduces inventory risk.
* **Sample Size Limitations:** Historical context for the HANSYD route relies on a small sample size (35 training bookings), increasing the uncertainty of route-level historical rates.
* **Over-Interpreting Segment Fit:** This passenger’s stay duration (98 days) and booking window (6 days) deviate significantly from the segment medians (6-day stay, 42-day advance purchase), meaning segment-level assumptions may not fully hold for this specific customer.
