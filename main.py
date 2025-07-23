from langgraph.graph import StateGraph
from nodes.classify_node import classify_node
from nodes.retrieve_node import retrieve_node
from nodes.draft_node import draft_node
from nodes.review_node import review_node
from nodes.escalate_node import escalate_node
from dotenv import load_dotenv

load_dotenv()

def review_result_selector(state):
    attempts = int(state.get("attempts", 0))

    if state.get("review_result") == "Approved":
        return "end"
    elif state.get("review_result") == "Rejected" and attempts >= 2:
        return "escalate"
    else:
        return "retrieve"

graph = StateGraph(state_schema=dict)


graph.add_node("classify", classify_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("draft", draft_node)
graph.add_node("review", review_node)
graph.add_node("escalate", escalate_node)


graph.set_entry_point("classify")
graph.add_edge("classify", "retrieve")
graph.add_edge("retrieve", "draft")
graph.add_edge("draft", "review")
graph.add_conditional_edges("review", review_result_selector)

app = graph.compile()

if __name__ == "__main__":
    ticket = {
        "subject": "Charged twice for subscription",
        "description": "I was billed twice this month for the same plan.",
        "attempts": 0
    }
    result = app.invoke(ticket)
    print("Final State:", result)
