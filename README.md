# hotelroom.agent.botdesk
### The Web2.5 Layer for AI-Agents in Agentic Hotel & Room Bookings

**AgentBotDesk Hospitality** introduces a cross-chain, open-source hotel and booking data architecture for AI-agents and Property Management Systems (PMS). It bridges traditional Web2 hotel systems with automated machine-to-machine (M2M) transaction rails.

📩 Reach out via [LinkedIn](https://linkedin.com) or **`hotelroom@agentbotdesk.com`** for partnerships or integrations.

---

### 🌐 Live Web2.5 Discovery & A2A Gateway Endpoints
* **Official A2A Discovery Manifest:** `GET https://agentbotdesk.com`
* **JSON-RPC 2.0 Agent Endpoint:** `POST https://hotelroom.agentbotdesk.com`
* **Lightweight ENS Route Resolver:** `GET https://hotelroom.agentbotdesk.com/route?category=hotelroom&step=1`

---

### 🔄 Phased Web2-to-Web3 Adoption
* **Phase 1 (Web2 / Web2.5 Bridge):** Direct connection via HTTPS and JSON-RPC for existing PMS systems and AI-agents such as Google A2A and MCP.
* **Phase 2 (Deterministic M2M Routing):** Standardized 7-step execution to prevent scraping and booking errors.
* **Phase 3 (Full On-Chain Settlement):** Transition to `.eth` endpoints, Zero-Knowledge guest verification (ZKP), and smart-contract escrow.

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

---

### 🚀 AgentBotDesk Ecosystem Verticals
* 🚕 **[Passenger Mobility (`mobility.agent.botdesk`)](https://github.com)** — 7-step deterministic M2M routing for agentic Robotaxi rides and Rental fleets (`roboride.eth`, `carrental.eth`).
* 🏨 **Hotel Room Hospitality (`hotelroom.agent.botdesk`)** — Agentic room discovery, binding rate quotes, ZKP guest verification, and deposit escrow (`hotelsearch.eth`, `roombooking.eth`).
* 🚤 **[Canal Cruises (`canalcruise.agent.botdesk`)](https://github.com)** — Direct M2M availability, ticketing, and settlement for urban boat tours and private charters (`canalcruise.eth`, `boatticket.eth`).

---

**Focus & Architecture Keywords:**  
`AgentBotDesk` • `Agentic AI` • `Web2.5` • `Google A2A` • `Model Context Protocol (MCP)` • `Hotel Booking Protocol` • `PMS Integration` • `M2M Routing` • `ENS Registry` • `Zero-Knowledge Proofs (ZKP)` • `Smart Escrow`

