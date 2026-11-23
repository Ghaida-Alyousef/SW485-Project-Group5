# T1 | Case 2 - Borderline (row 11278)

Model: `gemini-3.6-flash` | Generated: 2026-11-23T19:59:48+00:00

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
**2. Outlook**: the probability as a percentage, compared with the average completion rate and with the passenger segment's completion rate, and what the likelihood tier means for the business.
**3. Key factors**: 2 or 3 bullet points of one sentence each, each linking one detail of this booking to the historical context, the model drivers or the passenger segment above. At least one bullet must use the passenger segment.
**4. Recommended action**: 1 or 2 concrete commercial actions for bookings like this one, each naming the team that would own it (for example digital sales or ancillary products).
**5. Confidence and caveats**: one or two sentences on how far this estimate can be trusted.

Keep the whole briefing under 180 words.
```

## Response

**1. Headline**
This booking has a moderate completion outlook at 25.0%, driven primarily by the Vietnam booking origin and the HANSYD route.

**2. Outlook**
The estimated completion probability is 25.0%, which sits above the overall average rate of 14.9% and the passenger segment rate of 23.8%. This moderate tier exceeds our 19% decision threshold, meaning the booking is likely to complete, though the individual outcome remains uncertain.

**3. Key factors**
* The booking originates from Vietnam, where historical data shows a 28.4% completion rate across 299 bookings.
* Route HANSYD is associated with a 22.9% historical completion rate across 35 bookings in the training data.
* This passenger belongs to the "Extra-service lovers" segment, which shows a 23.8% completion rate and frequently selects extra baggage and meals.

**4. Recommended action**
* The ancillary products team should ensure requested baggage and meal preferences are confirmed early to secure the trip.
* The digital sales team should send targeted pre-departure engagement communications for short-lead bookings from Vietnam.

**5. Confidence and caveats**
With a test ROC-AUC of 0.78, the model is effective for prioritizing bookings across the business, though it cannot guarantee the outcome for any single reservation.
