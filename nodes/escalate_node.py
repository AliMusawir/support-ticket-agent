import csv

def escalate_node(state):
    with open("escalation_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            state.get("subject", ""),
            state.get("description", ""),
            state.get("draft", ""),
            state.get("feedback", "")
        ])
    state["status"] = "Escalated"
    return state
