from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    temperature=0
)

prompt = PromptTemplate.from_template(
    "You are a support quality reviewer. Evaluate this draft.\n"
    "Subject: {subject}\nDescription: {description}\nDraft: {draft}\n"
    "If it's good, respond with 'Approved'. If not, respond 'Rejected' and give a reason."
)

chain = LLMChain(llm=llm, prompt=prompt)

def review_node(state):
    output = chain.run(
        subject=state["subject"],
        description=state["description"],
        draft=state["draft"]
    )
    if "Approved" in output:
        state["review_result"] = "Approved"
    else:
        state["review_result"] = "Rejected"
        state["feedback"] = output
        state["attempts"] = int(state.get("attempts", 0)) + 1
    return state
