export interface HotelroomClientOptions {
  endpoint?: string;
  settlementToken?: string;
  sandbox?: boolean;
}

export class BotDeskHotelroomClient {
  private endpoint: string;
  private settlementToken?: string;
  private sandbox: boolean;

  constructor(options: HotelroomClientOptions = {}) {
    this.endpoint = (options.endpoint || "https://hotelroom.agentbotdesk.com").replace(/\/$/, "");
    this.settlementToken = options.settlementToken;
    this.sandbox = options.sandbox ?? true;
  }

  async getAgentCard(): Promise<any> {
    const res = await fetch(`${this.endpoint}/.well-known/agent-card.json`);
    return res.json();
  }

  async resolveStep(step: number): Promise<any> {
    if (step < 1 || step > 7) throw new Error("Step must be between 1 and 7.");
    const res = await fetch(`${this.endpoint}/route?category=hotelroom&step=${step}`);
    return res.json();
  }

  async createBindingReservation(payload: Record<string, any>): Promise<any> {
    if (!this.settlementToken && !this.sandbox) {
      throw new Error("A certified settlement_token is required for live hotel bookings and escrow.");
    }
    if (this.sandbox) {
      return { status: "sandbox_simulated", ens: "roombooking.eth", escrow: "bookingescrow.eth", payload };
    }
    const res = await fetch(this.endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${this.settlementToken}` },
      body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "message/send", params: payload })
    });
    return res.json();
  }
}
