# T1 | Case 2 - Borderline (row 11278)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T19:58:18+00:00

## Prompt

```text
## Booking under review
- Passengers: 1
- Sales channel: Internet
- Trip type: RoundTrip
- Booked 6 days before departure
- Length of stay: 98 days
- Flight: Wednesday at 07:00 on route HANSYD (8.58 hours)
- Booking origin: Vietnam
- Extra services requested: extra baggage, in-flight meals

## Model output (Random Forest, test ROC-AUC 0.78)
- Probability that this booking will be completed: 25.0%
- Decision threshold used by the team: 19%
- Model decision: Likely to be completed
- Completion likelihood tier: Moderate (above the threshold, but the outcome is uncertain)
- Average completion rate across all bookings: 14.9%

## Historical context (training data)
- Bookings from Vietnam: 28.4% completed (299 training bookings)
- Bookings on route HANSYD: 22.9% completed (35 training bookings)

## Strongest model drivers overall, with this booking's values
1. Booking origin (country the booking was made from): this booking = Vietnam
2. Route: this booking = HANSYD
3. Flight duration: this booking = 8.58 hours
4. Length of stay: this booking = 98 days
5. Number of extra services requested: this booking = 2

## Passenger segment
"Extra-service lovers" (segment 6 of 7): 9,577 bookings (19.2% of all). Completion rate 23.8%. Typical booking: 42 days ahead, 6-day stay, 1.5 passengers. Requests extra baggage 94%, preferred seat 68%, meals 84% of the time.

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
This booking has a moderate 25.0% completion likelihood, driven primarily by historical trends associated with its country of origin and route.

**2. Outlook**
The estimated completion probability is 25.0%, which is well above the average completion rate of 14.9%. Because it exceeds the 19% decision threshold, it sits in the moderate likelihood tier, meaning the booking is classified as likely to be completed, though the final outcome remains uncertain. Note: passenger segment details were not provided for this specific booking.

**3. Key factors**
* **Booking origin**: The booking originated in Vietnam, a country historical data associates with a higher completion rate of 28.4%.
* **Route and flight duration**: The booking is on the 8.58-hour HANSYD route, which historically sees a 22.9% completion rate.
* **Requested extra services**: The passenger selected 2 extra services (extra baggage and in-flight meals), which is one of the top overall model drivers associated with completion.

**4. Recommended action**
* **Digital sales team**: Optimize direct internet booking workflows for short lead-time bookings (booked 6 days before departure) originating in Vietnam to convert moderate-likelihood demand.
* **Ancillary products team**: Tailor pre-flight communication for long-stay bookings (98 days) to confirm and manage requested extra services like baggage and meals.

**5. Confidence and caveats**
This estimate can be moderately trusted based on the model's test performance metric (ROC-AUC of 0.78). However, these drivers reflect learned historical associations rather than proven causes, and historical route data is based on a small sample of 35 training bookings.
