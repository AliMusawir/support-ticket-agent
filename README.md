# 🛠️ Support Ticket Resolution Agent with Multi-Step Review Loop

This project is an AI-powered support ticket agent built with [LangGraph](https://github.com/langchain-ai/langgraph), [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview), and [FAISS](https://github.com/facebookresearch/faiss) + [Hugging Face Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) for context-aware ticket resolution. It classifies, drafts, reviews, and escalates support tickets through a multi-step reasoning loop using LangGraph’s dynamic state machine.

---

## 🚀 Features

* **Ticket Classification:** Categorizes incoming support tickets using an LLM.
* **Context Retrieval:** Uses FAISS + Hugging Face embeddings to retrieve relevant support knowledge.
* **LLM Drafting:** Automatically drafts a response using Azure OpenAI based on category and context.
* **Review & Feedback Loop:** Simulates a quality reviewer that can approve or reject drafts with feedback.
* **Escalation Path:** If a draft is rejected more than twice, the ticket is escalated and logged.

---

## 📁 Project Structure

```
.
├── main.py                   # Graph definition and execution
├── nodes/
│   ├── classify_node.py      # Classifies ticket category
│   ├── retrieve_node.py      # Retrieves relevant context using FAISS
│   ├── draft_node.py         # Drafts response using LLM
│   ├── review_node.py        # Simulates LLM review of draft
│   └── escalate_node.py      # Escalates and logs tickets after 2 failed reviews
├── utils/
│   └── rag_utils.py          # FAISS setup with HuggingFace embeddings
├── .env                      # Azure OpenAI credentials
├── escalation_log.csv        # Log of escalated tickets
└── README.md
```

---

## 🧠 Technologies Used

* 🧩 **LangGraph:** To model the reasoning flow between nodes.
* 🤖 **Azure OpenAI:** For classification, drafting, and review.
* 🔍 **FAISS + Hugging Face:** For semantic search using `all-MiniLM-L6-v2`.
* 🧪 **LangChain:** For LLM chaining and prompt management.

---

## ⚙️ Setup

1. **Clone this repo:**

   ```bash
   git clone https://github.com/your-org/support-ticket-agent.git
   cd support-ticket-agent
   ```

2. **Create and activate Python 3.10 virtual environment:**

   ```bash
   py -3.10 -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your `.env` file:**

   ```
   OPENAI_API_KEY=
   OPENAI_API_BASE=
   OPENAI_API_VERSION=
   OPENAI_API_TYPE=
   OPENAI_DEPLOYMENT_NAME=
   ```

5. **Run the app:**

   ```bash
   python main.py
   ```

---

## 🧪 Example

```python
ticket = {
    "subject": "Charged twice for subscription",
    "description": "I was billed twice this month for the same plan."
}
```

Depending on review outcomes, the agent will loop through retrieve → draft → review. If rejected twice, it logs the issue via `escalate_node`.

---

## 📌 Notes

* FAISS is initialized once in `rag_utils.py` using Hugging Face sentence transformers.
* You can expand the knowledge base by editing the `docs_by_category` dictionary.
* Escalated tickets are saved to `escalation_log.csv`.

---
