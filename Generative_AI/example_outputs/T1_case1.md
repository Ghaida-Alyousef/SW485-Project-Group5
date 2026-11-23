# T1 | Case 1 - Low (row 9669)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T20:29:28+00:00

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
**3. Key factors**: 2 or 3 bullet points of one sentence each. Each bullet covers exactly one detail of this booking, quotes its value from the input, and links it to the historical context, the model drivers or the passenger segment above. Do not link factors to each other or claim relationships between them. At least one bullet must use the passenger segment.
**4. Recommended action**: 1 or 2 concrete commercial actions for bookings like this one, each naming the team that would own it (for example digital sales or ancillary products).
**5. Confidence and caveats**: one or two sentences on how far this estimate can be trusted.

Keep the whole briefing under 180 words.
```

## Response

**1. Headline**
This booking has a low 5.0% completion likelihood, primarily driven by its origin in Australia and the DMKOOL route.

**2. Outlook**
The booking's 5.0% completion probability falls well below the 14.9% overall average and the "Top market (Australia)" segment's 5.4% completion rate. Being in the low likelihood tier means this booking is expected to be abandoned.

**3. Key factors**
- The booking origin is Australia, which historical training data shows has a low 5.1% completion rate across 14,274 bookings.
- The flight operates on route DMKOOL, which historically sees only a 6.1% completion rate across 538 training bookings.
- The passenger requested 1 extra service (extra baggage), aligning with the "Top market (Australia)" segment where 73% of bookings request extra baggage.

**4. Recommended action**
- The digital sales team should design targeted engagement strategies for long-lead bookings originating in Australia.
- The ancillary products team should optimize service offerings for passengers booking extra baggage on long-duration routes.

**5. Confidence and caveats**
With a test ROC-AUC of 0.78, the model is useful for prioritizing bookings, but it is not certain for any single booking.
