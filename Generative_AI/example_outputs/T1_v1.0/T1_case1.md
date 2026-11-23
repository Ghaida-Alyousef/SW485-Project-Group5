# T1 | Case 1 - Low (row 9669)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T19:56:52+00:00

## Prompt

```text
## Booking under review
- Passengers: 1
- Sales channel: Internet
- Trip type: RoundTrip
- Booked 55 days before departure
- Length of stay: 26 days
- Flight: Monday at 04:00 on route DMKOOL (8.83 hours)
- Booking origin: Australia
- Extra services requested: extra baggage

## Model output (Random Forest, test ROC-AUC 0.78)
- Probability that this booking will be completed: 5.0%
- Decision threshold used by the team: 19%
- Model decision: Likely to be abandoned
- Completion likelihood tier: Low (below the decision threshold; the booking is expected to be abandoned)
- Average completion rate across all bookings: 14.9%

## Historical context (training data)
- Bookings from Australia: 5.1% completed (14,274 training bookings)
- Bookings on route DMKOOL: 6.1% completed (538 training bookings)

## Strongest model drivers overall, with this booking's values
1. Booking origin (country the booking was made from): this booking = Australia
2. Route: this booking = DMKOOL
3. Flight duration: this booking = 8.83 hours
4. Length of stay: this booking = 26 days
5. Number of extra services requested: this booking = 1

## Passenger segment
"Top market (Australia)" (segment 1 of 7): 13,272 bookings (26.5% of all). Completion rate 5.4%. Typical booking: 48 days ahead, 22-day stay, 1.3 passengers. Requests extra baggage 73%, preferred seat 34%, meals 55% of the time.

## Task
Write an executive briefing using exactly these five headings, in this order, and nothing else:

**1. Headline**: one sentence (at most 25 words) stating the completion outlook and the main reason.
**2. Outlook**: the probability as a percentage, compared with the average completion rate, and what the likelihood tier means for the business.
**3. Key factors**: 2 or 3 bullet points, each linking one detail of this booking to the historical context or model drivers above.
**4. Recommended action**: 1 or 2 concrete commercial actions for bookings like this one, each naming the team that would own it (for example digital sales or ancillary products).
**5. Confidence and caveats**: one or two sentences on how far this estimate can be trusted.

Keep the whole briefing under 200 words.
```

## Response

**1. Headline**
This booking has a 5.0% completion probability, driven primarily by historical patterns associated with the origin market and flight route.

**2. Outlook**
The estimated completion probability is 5.0%, which is well below the average completion rate of 14.9%. Positioned in the low likelihood tier, this booking falls below our 19% decision threshold and is expected to be abandoned.

**3. Key factors**
* **Booking origin**: The booking originated in Australia, a key driver associated with low completion rates (5.1% historically for Australia; 5.4% for the Australian passenger segment).
* **Route and duration**: The booking is on route DMKOOL (8.83 hours flight duration), which historically sees only a 6.1% completion rate.
* **Length of stay**: A 26-day stay is identified as one of the top five drivers associated with completion rates for this booking. 

**4. Recommended action**
* **Digital Sales**: Target Australian bookings for early digital re-engagement sequences to encourage completion prior to the 55-day departure window.
* **Ancillary Products**: Prompt customers with targeted add-on offers, leveraging their interest in extra baggage to increase booking commitment.

**5. Confidence and caveats**
This evaluation relies on a model with a 0.78 ROC-AUC score, indicating reliable performance. Note that these factors reflect historical associations, not proven causes.
