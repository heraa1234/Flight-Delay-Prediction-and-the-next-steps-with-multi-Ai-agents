class FlightAgent:
    def assess_severity(self, delay_minutes):
        if delay_minutes >= 90:
            return "CRITICAL"
        if delay_minutes >= 60:
            return "HIGH"
        if delay_minutes >= 30:
            return "MEDIUM"
        return "LOW"
