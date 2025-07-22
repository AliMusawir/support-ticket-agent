from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_type=os.getenv("OPENAI_API_TYPE"),
    deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    temperature=0
)

prompt = PromptTemplate.from_template(
    "Classify the following support ticket into one of these categories: Billing, Technical, Security, General.\n"
    "Subject: {subject}\nDescription: {description}\nCategory:"
)

chain = LLMChain(llm=llm, prompt=prompt)

def classify_node(state):
    result = chain.run(subject=state["subject"], description=state["description"]).strip()
    state["category"] = result
    return state
