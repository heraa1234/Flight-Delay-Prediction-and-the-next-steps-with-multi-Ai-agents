from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from control_tower_core import run_control_tower

app = FastAPI(title="Airport AI Control Tower")


@app.get("/", response_class=HTMLResponse)
def dashboard():
    results = run_control_tower()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Airport AI Control Tower</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 20px;
            }
            h1, h2 {
                color: #003366;
            }
            .card {
                background: white;
                padding: 15px;
                margin-bottom: 30px;
                border-left: 6px solid #003366;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #003366;
                color: white;
            }
            .CRITICAL { color: red; font-weight: bold; }
            .HIGH { color: orange; font-weight: bold; }
            .MEDIUM { color: #cc9900; font-weight: bold; }
            .LOW { color: green; font-weight: bold; }
            pre {
                background: #f2f2f2;
                padding: 10px;
                border-left: 4px solid #003366;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>

    <h1>✈️ Airport AI Control Tower – Operational Dashboard</h1>
    """

    for r in results:

        # Build flight details table dynamically
        flight_rows = ""
        for k, v in r["flight_details"].items():
            flight_rows += f"<tr><th>{k}</th><td>{v}</td></tr>"

        html += f"""
        <div class="card">

            <h2>Flight Details</h2>
            <table>
                {flight_rows}
            </table>

            <h2>Delay Prediction</h2>
            <table>
                <tr><th>Delay Probability</th><td>{r['delay_probability']}</td></tr>
                <tr><th>Delay Minutes</th><td>{r['delay_minutes']}</td></tr>
                <tr>
                    <th>Severity</th>
                    <td class="{r['severity']}">{r['severity']}</td>
                </tr>
            </table>

            <h2>Reasons for Delay</h2>
            <ul>
                {''.join(f"<li>{x}</li>" for x in r['reasons'])}
            </ul>

            <h2>AI Agent Actions</h2>
            <ul>
                {''.join(
                    f"<li><b>{agent}:</b> {info['action']} — {info['reason']}</li>"
                    for agent, info in r['agent_actions'].items()
                )}
            </ul>

            <h2>Digital Twin Simulation</h2>
            <table>
                <tr><th>Impact</th><td>{r['simulation']['impact']}</td></tr>
                <tr><th>Estimated Cost</th><td>${r['simulation']['cost']}</td></tr>
                <tr><th>Network Risk</th><td>{r['simulation']['risk']}</td></tr>
            </table>

            <h2>Recommended Action</h2>
            <pre>{r['recommended_action']}</pre>

        </div>
        """

    html += """
    </body>
    </html>
    """

    return html
