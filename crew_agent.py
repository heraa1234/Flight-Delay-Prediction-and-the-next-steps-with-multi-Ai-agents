class CrewAgent:
    def optimize(self, staff_df, flight_id):
        available = staff_df[
            (staff_df["available"] == 1) &
            (staff_df["current_flight_id"] != flight_id)
        ]
        return "Reassign backup crew" if not available.empty else "No action needed"
