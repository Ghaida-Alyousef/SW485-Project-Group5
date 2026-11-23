# T1 | Case 3 - High (row 35092)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T20:29:42+00:00

## Prompt

```text
## Booking under review
- Passengers: 5
- Sales channel: Internet
- Trip type: RoundTrip
- Booked 341 days before departure
- Length of stay: 5 days
- Flight: Friday at 15:00 on route AKLKUL (8.83 hours)
- Booking origin: Malaysia
- Extra services requested: extra baggage, a preferred seat, in-flight meals

## Model output (Random Forest, test ROC-AUC 0.78)
- Probability that this booking will be completed: 55.0%
- Decision threshold used by the team: 19%
- Model decision: Likely to be completed
- Completion likelihood tier: High (well above the average completion rate)
- Average completion rate across all bookings: 14.9%

## Historical context (training data)
- Bookings from Malaysia: 34.4% completed (5,709 training bookings)
- Bookings on route AKLKUL: 21.1% completed (2,151 training bookings)

## Strongest model drivers overall, with this booking's values
1. Booking origin (country the booking was made from): this booking = Malaysia
2. Route: this booking = AKLKUL
3. Flight duration: this booking = 8.83 hours
4. Length of stay: this booking = 5 days
5. Number of extra services requested: this booking = 3

## Passenger segment
"Top route (AKLKUL)" (segment 4 of 7): 2,624 bookings (5.2% of all). Completion rate 21.1%. Typical booking: 102 days ahead, 21-day stay, 1.6 passengers. Requests extra baggage 68%, preferred seat 23%, meals 45% of the time.

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
This booking has a 55.0% completion probability, driven primarily by historical patterns associated with its Malaysian booking origin and AKLKUL route.

**2. Outlook**
The 55.0% completion probability is well above the 14.9% overall average and the 21.1% segment rate, placing it in the High likelihood tier.

**3. Key factors**
- The booking origin is Malaysia, which historically sees a 34.4% completion rate and is the model's top overall driver.
- The route is AKLKUL, which is the model's second strongest driver and historically has a 21.1% completion rate.
- This booking requests 3 extra services, whereas the "Top route (AKLKUL)" segment typically requests preferred seats 23% of the time and meals 45% of the time.

**4. Recommended action**
- The ancillary products team should ensure all 3 requested extra services are seamlessly confirmed to support this high-value booking.
- The digital sales team should monitor long lead-time bookings to maintain customer engagement prior to departure.

**5. Confidence and caveats**
With a test ROC-AUC of 0.78, this model is useful for prioritising bookings, but its estimate is not certain for any single booking.
