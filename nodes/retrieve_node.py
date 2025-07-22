from utils.rag_utils import get_mocked_context

def retrieve_node(state):
    category = state.get("category", "General")
    state["context"] = get_mocked_context(category)
    return state
