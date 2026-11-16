import urllib.request
import json

class BotDeskHotelroomClient:
    def __init__(self, endpoint="https://agentbotdesk.com", settlement_token=None, sandbox=True):
        self.endpoint = endpoint.rstrip("/")
        self.settlement_token = settlement_token
        self.sandbox = sandbox

    def get_agent_card(self):
        with urllib.request.urlopen(f"{self.endpoint}/.well-known/agent-card.json") as res:
            return json.loads(res.read().decode())

    def resolve_step(self, step: int):
        if step not in range(1, 8):
            raise ValueError("Step must be between 1 and 7.")
        with urllib.request.urlopen(f"{self.endpoint}/route?category=hotelroom&step={step}") as res:
            return json.loads(res.read().decode())

    def create_binding_reservation(self, payload: dict):
        if not self.settlement_token and not self.sandbox:
            raise PermissionError("A certified settlement_token is required for live hotel bookings and escrow.")
        if self.sandbox:
            return {"status": "sandbox_simulated", "ens": "roombooking.eth", "escrow": "bookingescrow.eth", "payload": payload}
        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "message/send", "params": payload}).encode(),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.settlement_token}"}
        )
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode())
