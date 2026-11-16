
#### hotelroom.agent.botdesk
## The Web2.5 Layer for AI-Agents in Autonomous Hotel & Room Bookings

BotDesk Hospitality introduces a cross-chain, open-source hotel and booking data architecture for AI-agents and Property Management Systems (PMS). It bridges traditional Web2 hotel systems with automated machine-to-machine (M2M) transaction rails.

📩 Reach out via [LinkedIn](https://linkedin.com) or **`hotelroom@agentbotdesk.com`** for partnerships or integrations.

---

### 🌐 Live Web2.5 Discovery & A2A Gateway Endpoints
* **Official A2A Discovery Manifest:** `https://agentbotdesk.com`
* **JSON-RPC 2.0 Agent Endpoint:** `POST https://hotelroom.agentbotdesk.com`
* **Lightweight ENS Route Resolver:** `GET https://hotelroom.agentbotdesk.com/route?category=hotelroom&step=1`

---

### 🔄 Phased Web2-to-Web3 Adoption
1. **Phase 1 (Web2 / Web2.5 Bridge):** Direct connection via HTTPS and JSON-RPC for existing PMS systems and AI-agents such as Google A2A and MCP.
2. **Phase 2 (Deterministic M2M Routing):** Standardized 7-step execution to prevent scraping and booking errors.
3. **Phase 3 (Full On-Chain Settlement):** Transition to `.eth` endpoints, Zero-Knowledge guest verification (ZKP), and smart-contract escrow.

---

### 📂 Repository Structure & 7-Step Taxonomy
This repository contains modules for `/core-architecture`, `/schemas`, `/sdk`, and `/web25-gateway`, structured along the 7 steps of the ENS registry:

1. **Discovery, Availability & Specifications:** `hotelsearch.eth`, `roomavailable.eth`, `roomtype.eth`, `bedtype.roomfeature.eth`
2. **Rates, Quotes & Taxation:** `roomrate.eth`, `bookingquote.eth`, `citytax.eth`, `touristtax.eth`
3. **Verification & Policy:** `guestidentity.eth`, `guestverification.eth`, `hotelpolicy.eth`
4. **Booking, Escrow & Payment:** Requires a certified `settlement_token`; utilizes `roombooking.eth`, `bookingescrow.eth`
5. **Check-In & Room Access:** `hotelcheckin.eth`, `roomaccess.eth`, `roomkey.eth`
6. **Check-Out & Final Settlement:** `hotelcheckout.eth`, `roomcheckout.eth`
7. **Modifications, Disputes & Reputation:** `bookingmodification.eth`, `hotelreview.eth`

*(See the full technical roadmap, open-source MIT license terms, and details regarding the proprietary settlement module within the repository).*
