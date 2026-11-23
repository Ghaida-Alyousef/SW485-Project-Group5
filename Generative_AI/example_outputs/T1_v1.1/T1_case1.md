# T1 | Case 1 - Low (row 9669)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T19:59:40+00:00

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
**2. Outlook**: the probability as a percentage, compared with the average completion rate and with the passenger segment's completion rate, and what the likelihood tier means for the business.
**3. Key factors**: 2 or 3 bullet points of one sentence each, each linking one detail of this booking to the historical context, the model drivers or the passenger segment above. At least one bullet must use the passenger segment.
**4. Recommended action**: 1 or 2 concrete commercial actions for bookings like this one, each naming the team that would own it (for example digital sales or ancillary products).
**5. Confidence and caveats**: one or two sentences on how far this estimate can be trusted.

Keep the whole briefing under 180 words.
```

## Response

**1. Headline**
This booking has a 5.0% completion probability and is likely to be abandoned, primarily driven by the booking origin and route.

**2. Outlook**
At 5.0%, the completion probability is below both the 14.9% overall average and the 5.4% segment average. Being in the low likelihood tier means this booking is expected to be abandoned, making it a candidate for commercial intervention.

**3. Key factors**
- The booking originates from Australia and operates on route DMKOOL, which are the model's top drivers and historically show low completion rates of 5.1% and 6.1% respectively.
- This booking fits the "Top market (Australia)" segment, which historically sees a low 5.4% completion rate despite high demand for extras like baggage.

**4. Recommended action**
- The Digital Sales team should deploy targeted digital re-engagement prompts for internet bookings originating from Australia.
- The Ancillary Products team should optimize service bundles for customers requesting extra baggage to encourage booking completion.

**5. Confidence and caveats**
With an AUC of 0.78, the model effectively prioritizes bookings for intervention, though it cannot provide absolute certainty for any single booking.
