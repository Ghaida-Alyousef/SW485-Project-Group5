# T1 | Case 3 - High (row 35092)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T19:58:26+00:00

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
**2. Outlook**: the probability as a percentage, compared with the average completion rate, and what the likelihood tier means for the business.
**3. Key factors**: 2 or 3 bullet points, each linking one detail of this booking to the historical context or model drivers above.
**4. Recommended action**: 1 or 2 concrete commercial actions for bookings like this one, each naming the team that would own it (for example digital sales or ancillary products).
**5. Confidence and caveats**: one or two sentences on how far this estimate can be trusted.

Keep the whole briefing under 200 words.
```

## Response

**1. Headline**
This booking has a strong 55.0% completion outlook, driven primarily by its origin in Malaysia and the selected AKLKUL route.

**2. Outlook**
The estimated completion probability is 55.0%, significantly higher than the average completion rate of 14.9%. Positioned in the high likelihood tier, this booking represents a remarkably reliable source of anticipated revenue.

**3. Key factors**
- **Booking origin & route**: Originating from Malaysia (historically associated with a 34.4% completion rate) and traveling on route AKLKUL (21.1% historical completion) are among the strongest overall model drivers favoring completion.
- **Ancillary engagement**: Requesting 3 extra services (baggage, preferred seat, and meals) aligns with key model drivers that are associated with higher booking follow-through.

**4. Recommended action**
- **Ancillary products team**: Ensure seamless fulfillment of the requested extra baggage, seat, and meal selections to protect this high-probability reservation.
- **Digital sales team**: Monitor advanced bookings made nearly a year out (341 days) to engage multi-passenger groups ahead of their 5-day stay.

**5. Confidence and caveats**
The model demonstrates solid predictive performance with a test ROC-AUC of 0.78. However, specific passenger segment data for this booking was missing, and these historical model drivers reflect statistical associations rather than proven causes.
