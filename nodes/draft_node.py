from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE")
)

prompt = PromptTemplate.from_template(
    "You are a helpful support agent. Use the context to answer the user's ticket.\n"
    "Subject: {subject}\nDescription: {description}\nContext: {context}\nReply:"
)

chain = LLMChain(llm=llm, prompt=prompt)

def draft_node(state):
    context = ' '.join(state["context"])
    reply = chain.run(
        subject=state["subject"],
        description=state["description"],
        context=context
    ).strip()
    state["draft"] = reply
    return state
