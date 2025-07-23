from utils.rag_utils import db

def retrieve_node(state):
    query = state["description"]
    relevant_docs = db.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    state["context"] = context
    return state
