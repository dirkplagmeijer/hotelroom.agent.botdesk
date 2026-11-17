from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

def resolve_m2m_endpoint(category: str, step: int) -> dict:
    """Maps the 7-step hospitality lifecycle to verified BotDesk ENS endpoints while keeping settlement proprietary."""
    routes = {
        "hotelroom": {
            1: {"endpoint": "hotelsearch.eth", "action": "discovery"},
            2: {"endpoint": "roomrate.eth", "action": "quotation"},
            3: {"endpoint": "guestverification.eth", "action": "verification"},
            4: {"endpoint": "roombooking.eth", "action": "booking_lock", "requires": "certified_settlement_token"},
            5: {"endpoint": "roomaccess.eth", "action": "digital_access"},
            6: {"endpoint": "hotelcheckout.eth", "action": "completion_invoicing", "requires": "certified_settlement_token"},
            7: {"endpoint": "bookingdispute.eth", "action": "arbitration"},
        }
    }
    return routes.get(category.lower(), {}).get(step, {"error": "Invalid step or category"})

# The ADK Gateway Agent handling incoming A2A requests
gateway_agent = Agent(
    name="botdesk_hotelroom_gateway",
    model="gemini-2.5-flash",
    instruction=(
        "Route incoming hotel room and hospitality requests across the 7-step M2M lifecycle. "
        "Return the corresponding verified .eth endpoint and enforce a certified settlement_token for booking and finalization."
    ),
    tools=[resolve_m2m_endpoint]
)

# Exposes the agent directly as an A2A server (reads your existing agent-card.json)
a2a_app = to_a2a(gateway_agent, agent_card="agent-card.json")
