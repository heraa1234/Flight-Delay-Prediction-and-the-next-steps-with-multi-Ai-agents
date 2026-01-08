class PassengerAgent:
    def optimize(self, pax_df, flight_id):
        connections = pax_df[pax_df["flight_id"] == flight_id]
        return "Auto-rebook passengers" if not connections.empty else "No passenger impact"
