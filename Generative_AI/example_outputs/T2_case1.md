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
**Addressing High Drop-Off in High-Volume Australian Long-Haul Bookings**  
The primary strategic objective is to mitigate booking abandonment on long-haul routes originating from Australia. While Australia represents a massive share of total booking volume (26.5%), its low baseline completion rate (5.4%) combined with this specific itinerary's critically low predicted completion probability (5.0% vs. a 19% decision threshold) highlights significant revenue leakage in a core market.

---

### 2. Segment-Based Insight
This itinerary closely aligns with the behavioral profile of **Segment 1: "Top market (Australia)"**:
* **Itinerary Profile:** Long stay (26 days vs. segment average of 22 days), booked far in advance (55 days vs. segment average of 48 days), long flight duration (8.83 hours on route DMKOOL), and a single passenger requesting extra baggage (73% of segment bookings request extra baggage).
* **Behavioral Connection:** Australia-originating bookings historically yield a very low completion rate (5.1% across 14,274 training bookings), and route DMKOOL similarly underperforms at a 6.1% historical completion rate. The model's top drivers (booking origin, route, flight duration, length of stay, and extra service count) associate this long-stay, long-haul pattern with a high risk of abandonment (5.0% predicted completion). 

---

### 3. Recommended Actions

#### Action 1: Targeted Retargeting & Hold-Incentive Strategy
* **Action:** Deploy automated, personalized re-engagement triggers (e.g., tailored email follow-ups or flexible booking hold options) specifically emphasizing ancillary benefits like extra baggage for uncompleted Australian bookings.
* **Responsible Team:** Digital Marketing & E-Commerce Team
* **Reason Based on Evidence:** Booking origin (Australia), long length of stay (26 days), and extra baggage selection are key drivers associated with this booking's low completion probability (5.0%). Segment 1 historical data shows a high propensity for extra baggage (73%), making ancillary-focused engagement relevant to this segment.
* **Suggested KPI:** Abandoned cart recovery rate for Australian long-haul itineraries.

#### Action 2: Schedule & Channel Friction Audit for Early-Morning Long-Haul Routes
* **Action:** Conduct an end-to-end review of the internet booking funnel and payment pathways for Australian bookings on early-morning, long-haul flights (specifically Monday 04:00 departures on route DMKOOL).
* **Responsible Team:** Customer Experience (CX) & Revenue Management Teams
* **Reason Based on Evidence:** Route DMKOOL has a historically low completion rate of 6.1%, and Australian web bookings overall complete at only 5.1%. The combination of a 04:00 departure time, an 8.83-hour flight duration, and an internet sales channel may introduce friction or hesitation during the checkout process.
* **Suggested KPI:** Step-by-step digital funnel drop-off rate for route DMKOOL bookings.

---

### 4. Expected Business Value
Testing these actions offers the potential to recover high-value long-haul bookings from the airline’s largest customer segment (26.5% of total volume). Given the existing low baseline completion rate (5.4% for the segment), even incremental improvements validated through A/B testing could meaningfully enhance overall top-line revenue without increasing broad acquisition costs.

---

### 5. Risks and Limitations
* **Causality vs. Association:** Model drivers (e.g., flight duration, booking origin, length of stay) represent historical correlations with abandonment, not direct causes. Altering user flows or marketing communications does not guarantee an increase in conversion without controlled experimental validation.
* **Over-Interpreting Low Probabilities:** A 5.0% completion probability indicates a low likelihood of booking completion based on pattern recognition, but it does not mean the customer is guaranteed to abandon.
* **Data Context Limitations:** The provided prediction data lacks qualitative context regarding customer price sensitivity, payment failure rates, or competing carrier alternatives on the DMKOOL route at 04:00 on Mondays. Over-indexing on incentives could needlessly erode margins if non-price factors drive the drop-off.
