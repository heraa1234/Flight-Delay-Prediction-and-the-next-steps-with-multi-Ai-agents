import pandas as pd

def predict_delays(flight_df):
    results = []

    for _, row in flight_df.iterrows():
        delay_minutes = (
            row["previous_flight_delay_min"]
            + row["arrivals_last_hour"] * 2
            + (20 if row["rain_indicator"] == 1 else 0)
        )

        delay_prob = min(delay_minutes / 120, 1.0)

        results.append({
            "flight_id": row["flight_id"],
            "airline": row["airline"],
            "origin": row["origin"],
            "destination": row["destination"],
            "delay_minutes": round(delay_minutes, 1),
            "delay_probability": round(delay_prob, 2)
        })

    return pd.DataFrame(results)
