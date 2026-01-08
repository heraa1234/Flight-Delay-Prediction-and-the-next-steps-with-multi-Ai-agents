def explain_decision(flight, severity, actions, simulation):
    lines = []

    lines.append("WHY the flight is predicted to be delayed:")

    if flight["delay_minutes"] > 60:
        lines.append("- Significant delay propagated from previous flight")

    if flight["delay_probability"] > 0.5:
        lines.append("- Multiple operational risk factors combined")

    lines.append(f"\nSEVERITY LEVEL: {severity}")

    if severity in ["HIGH", "CRITICAL"]:
        lines.append("\nRECOMMENDED ACTION: Activate disruption recovery plan")
        lines.append("\nOPERATIONAL ACTION STEPS:")
        lines.append(f"- Gate management: {actions['gate_assignment']}")
        lines.append(f"- Crew management: {actions['crew_action']}")
        lines.append(f"- Aircraft management: {actions['aircraft_action']}")
        lines.append(f"- Passenger management: {actions['passenger_action']}")
        lines.append(f"- Estimated cost impact: ${simulation['cost']}")
    else:
        lines.append("\nRECOMMENDED ACTION: Monitor flight")

    return "\n".join(lines)
