# M2M ENS Registry — Hotelroom (`hotelroom.agent.botdesk`)
### The Definitive On-Chain Routing Directory for Hospitality & Autonomous Room Bookings

#### Core Protocol & Shared Agent Layer (Universal)
* **Protocol Root:** `botdesk.eth`
* **Agent Permissions & Budgets:** `agentconsent.eth`, `agentallowance.eth`, `agentallowances.eth`

---

#### Step 1: Discovery, Availability & Specifications (The Market Scan)
* **Hotel Search & Entities:** `hotelsearch.eth`, `hotelidentity.eth`, `hotelidentities.eth`
* **Room Availability & Inventory:** `roomavailable.eth`, `roomsavailable.eth`, `roomavailability.eth`, `roomsavailability.eth`, `roomoccupancy.eth`, `roominventory.eth`, `roominventories.eth`
* **Room Types, Features & Amenities:** `roomtype.eth`, `roomtypes.eth`, `roomfeature.eth`, `roomfeatures.eth`, `hotelamenity.eth`, `hotelamenities.eth`, `roomaddon.eth`, `roomaddons.eth`
* **Standardized Subdomain Extensions (Zero-Gas Hierarchy):**
  * *Under `roomfeature.eth`:* `bedtype.roomfeature.eth`, `view.roomfeature.eth`, `accessibility.roomfeature.eth`
  * *Under `roomtype.eth`:* `capacity.roomtype.eth`
  * *Under `roomaddon.eth`:* `mealplan.roomaddon.eth`

#### Step 2: Rates, Quotes & Taxation (Real-Time Binding Pricing)
* **Room Rates:** `roomrate.eth`, `roomrates.eth`
* **Quotes & Expiration:** `bookingquote.eth`, `bookingquotes.eth`, `bookingexpiration.eth`
* **Local Taxes:** `citytax.eth`, `touristtax.eth`

#### Step 3: Verification & Policy (Identity & Terms)
* **Guest & Hotel Identity (DID / ZKP):** `guestidentity.eth`, `guestidentities.eth`, `guestverification.eth`, `hotelverification.eth`
* **Policies & Cancellation Terms:** `hotelpolicy.eth`, `hotelpolicies.eth`, `cancellationterms.eth`

#### Step 4: Booking, Escrow & Payment (Locking the Transaction)
* **Shared Settlement Layer:** Requires a certified `settlement_token` issued by the proprietary settlement module to authorize binding bookings and on-chain escrow.
* **Room Booking & Reservation:** `roombooking.eth`, `roombookings.eth`, `roomreservation.eth`, `roomreservations.eth`, `makereservation.eth`
* **Inventory Locks & Confirmation:** `bookinglock.eth`, `bookinglocks.eth`, `bookingconfirmation.eth`, `bookingconfirmations.eth`, `bookingstatus.eth`
* **Escrow, Payments & Billing:** `bookingescrow.eth`, `paymentescrow.eth`, `bookingpayment.eth`, `bookingpayments.eth`, `bookinginvoice.eth`

#### Step 5: Check-In & Room Access (Physical Handover)
* **Check-In & Digital Access:** `hotelcheckin.eth`, `roomcheckin.eth`, `roomaccess.eth`
* **Cooldown / Watchlist Targets (Physical/Digital Keys):** `roomkey.eth`, `roomkeys.eth`

#### Step 6: Check-Out & Final Settlement (Completion & Release)
* **Check-Out & Escrow Release:** `hotelcheckout.eth`, `roomcheckout.eth`

#### Step 7: Modifications, Disputes & Reputation (Post-Stay & Incidents)
* **Changes, Cancellations & Refunds:** `bookingmodification.eth`, `roomcancellation.eth`, `bookingcancellation.eth`, `bookingrefund.eth`, `bookingdispute.eth`
* **Verified Ratings & Reviews:** `hotelrating.eth`, `hotelratings.eth`, `hotelreview.eth`
