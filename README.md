#### hotelroom.agent.botdesk
## The Web2.5 Layer for AI-Agents in Autonomous Hotel & Room Bookings

BotDesk Hospitality introduceert een cross-chain, open-source hotel- en boekingsdata-architectuur voor AI-agenten en Property Management Systems (PMS). Het overbrugt traditionele Web2-hotelsystemen met geautomatiseerde machine-to-machine (M2M) transactierails.

Neem contact op via [LinkedIn](https://linkedin.com) of via **`hotelroom@agentbotdesk.com`** voor samenwerkingen of integraties.

---

### 🌐 Live Web2.5 Discovery & A2A Gateway Endpoints
* **Official A2A Discovery Manifest:** `https://agentbotdesk.com`
* **JSON-RPC 2.0 Agent Endpoint:** `POST https://agentbotdesk.com`
* **Lightweight ENS Route Resolver:** `GET https://agentbotdesk.com/route?category=hotelroom&step=1`

---

### 🔄 Phased Web2-to-Web3 Adoption
1. **Phase 1 (Web2 / Web2.5 Bridge):** Directe connectie via HTTPS en JSON-RPC voor bestaande PMS-systemen en AI-agenten zoals Google A2A en MCP.
2. **Phase 2 (Deterministic M2M Routing):** Gestandaardiseerde 7-staps uitvoering om scraping en boekingsfouten te voorkomen.
3. **Phase 3 (Full On-Chain Settlement):** Overgang naar `.eth`-endpoints, Zero-Knowledge gastverificatie (ZKP) en smart-contract escrow.

---

### 📂 Repository Structure & 7-Step Taxonomy
De repository bevat modules voor `/core-architecture`, `/schemas`, `/sdk` en `/web25-gateway`, opgebouwd langs de 7 stappen van het ENS-register:
1. **Discovery, Availability & Specifications:** `hotelsearch.eth`, `roomavailable.eth`, `roomtype.eth`, `bedtype.roomfeature.eth`
2. **Rates, Quotes & Taxation:** `roomrate.eth`, `bookingquote.eth`, `citytax.eth`, `touristtax.eth`
3. **Verification & Policy:** `guestidentity.eth`, `guestverification.eth`, `hotelpolicy.eth`
4. **Booking, Escrow & Payment:** Vereist een `settlement_token`; gebruikt `roombooking.eth`, `bookingescrow.eth`
5. **Check-In & Room Access:** `hotelcheckin.eth`, `roomaccess.eth`, `roomkey.eth`
6. **Check-Out & Final Settlement:** `hotelcheckout.eth`, `roomcheckout.eth`
7. **Modifications, Disputes & Reputation:** `bookingmodification.eth`, `hotelreview.eth`

*(Bekijk de volledige technische roadmap, open-source MIT-licentievoorwaarden en details over de propriëtaire settlement-module in de volledige repository).*
