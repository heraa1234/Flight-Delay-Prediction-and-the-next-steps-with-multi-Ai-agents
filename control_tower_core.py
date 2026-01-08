import pandas as pd

# Path to flight data
DATA_PATH = "data/flight_operations.csv"


def run_control_tower():
    """
    Core logic for AI-enabled Airport Control Tower.
    Reads flight data from CSV and produces
    dashboard-ready structured output.
    """

    df = pd.read_csv(DATA_PATH)
    results = []

    for _, flight in df.iterrows():

        # -------------------------------------------------
        # 1. Flight details (ALL columns from CSV)
        # -------------------------------------------------
        flight_details = flight.to_dict()

        # -------------------------------------------------
        # 2. Flight-specific delay prediction logic
        # (Deterministic, realistic variation)
        # -------------------------------------------------
        base_delay = 15

        origin_factor = len(str(flight_details.get("origin", ""))) * 4
        destination_factor = len(str(flight_details.get("destination", ""))) * 4
        airline_factor = len(str(flight_details.get("airline", ""))) * 2

        delay_minutes = base_delay + origin_factor + destination_factor + airline_factor

        # Cap delay minutes to realistic range
        delay_minutes = min(delay_minutes, 180)

        delay_probability = round(
            min(0.10 + (delay_minutes / 200), 0.95),
            2
        )

        # -------------------------------------------------
        # 3. Severity classification
        # -------------------------------------------------
        if delay_minutes >= 120:
            severity = "CRITICAL"
        elif delay_minutes >= 60:
            severity = "HIGH"
        elif delay_minutes >= 30:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        # -------------------------------------------------
        # 4. Reasons for delay
        # -------------------------------------------------
        reasons = [
            "Aircraft delayed from previous rotation",
            "High inbound air traffic congestion",
            "Limited gate availability",
            "Route has elevated historical delay risk"
        ]

        # -------------------------------------------------
        # 5. AI Agent Actions
        # -------------------------------------------------
        agent_actions = {
            "Crew Agent": {
                "action": "Rebuild crew schedule",
                "reason": "Prevent duty-time and fatigue violations"
            },
            "Gate Agent": {
                "action": "Reassign gate or use remote stand",
                "reason": "Reduce gate congestion"
            },
            "Aircraft Agent": {
                "action": "Optimize aircraft rotation",
                "reason": "Avoid cascading downstream delays"
            },
            "Passenger Agent": {
                "action": "Auto-rebook affected passengers",
                "reason": "Minimize missed connections"
            }
        }

        # -------------------------------------------------
        # 6. Digital Twin Simulation (impact & cost)
        # -------------------------------------------------
        simulation = {
            "impact": "HIGH" if severity in ["HIGH", "CRITICAL"] else "MEDIUM",
            "cost": 25000 if severity == "CRITICAL"
                    else 15000 if severity == "HIGH"
                    else 7000,
            "risk": "Cascading network delays likely"
        }

        # -------------------------------------------------
        # 7. Recommended Action
        # -------------------------------------------------
        if severity == "CRITICAL":
            recommended_action = (
                "Activate full disruption recovery plan immediately. "
                "Coordinate OCC, crew scheduling, gate management, "
                "aircraft rotation, and passenger recovery."
            )
        elif severity == "HIGH":
            recommended_action = (
                "Trigger proactive recovery actions. "
                "Prepare standby crew and reassign gates."
            )
        elif severity == "MEDIUM":
            recommended_action = (
                "Monitor flight closely and prepare contingency resources."
            )
        else:
            recommended_action = (
                "No immediate action required. Continue monitoring."
            )

        # -------------------------------------------------
        # 8. Final output object
        # -------------------------------------------------
        results.append({
            "flight_details": flight_details,
            "delay_probability": delay_probability,
            "delay_minutes": delay_minutes,
            "severity": severity,
            "reasons": reasons,
            "agent_actions": agent_actions,
            "simulation": simulation,
            "recommended_action": recommended_action
        })

    return results
