class AircraftAgent:
    def optimize(self, rotation_df, flight_id):
        affected = rotation_df[rotation_df["current_flight_id"] == flight_id]
        return "Swap aircraft rotation" if not affected.empty else "No rotation change"
