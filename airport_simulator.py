def simulate(delay_minutes, cost_df):
    cost = cost_df[cost_df["delay_minutes"] <= delay_minutes]["cost"].max()
    return {
        "impact": "HIGH" if delay_minutes > 60 else "MEDIUM",
        "cost": int(cost) if cost == cost else 0
    }
