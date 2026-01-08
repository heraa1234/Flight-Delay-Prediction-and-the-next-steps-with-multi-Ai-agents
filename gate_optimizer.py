class GateOptimizer:
    def assign_gate(self, gate_df):
        free = gate_df[gate_df["occupied"] == 0]
        if free.empty:
            return "Remote stand"
        return free.iloc[0]["gate_id"]
