import pandas as pd
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_dashboard_csvs(results):
    """
    This function ONLY formats output.
    It does NOT change the main program.
    """

    # -------------------------------
    # 1. Flight Delay Summary
    # -------------------------------
    summary_rows = []

    # -------------------------------
    # 2. Decision Explanation
    # -------------------------------
    explanation_rows = []

    for r in results:
        summary_rows.append({
            "flight_id": r.get("flight_id"),
            "airline": r.get("airline"),
            "route": r.get("route"),
            "delay_probability": round(r.get("delay_probability", 0), 2),
            "delay_minutes": int(r.get("delay_minutes", 0)),
            "severity": r.get("severity")
        })

        explanation_rows.append({
            "flight_id": r.get("flight_id"),
            "decision_explanation": r.get("decision_explanation")
        })

    # Write CSVs
    pd.DataFrame(summary_rows).to_csv(
        os.path.join(OUTPUT_DIR, "flight_delay_summary.csv"),
        index=False
    )

    pd.DataFrame(explanation_rows).to_csv(
        os.path.join(OUTPUT_DIR, "decision_explanation.csv"),
        index=False
    )

    print("✅ Dashboard CSVs exported (no program logic changed)")
