import os
os.environ["USE_TF"] = "0"
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

# 1. Knowledge base
docs_by_category = {
    "Technical": "If the app crashes, try force closing, checking your internet, and updating the app. Contact support if the issue persists.",
    "Billing": "For double charges or wrong billing, check your statement, then reach out with proof and your user ID.",
    "Account": "To reset your password, click 'Forgot Password'. For account issues, verify your identity by email."
}

# 2. Convert to Document format with metadata
documents = [
    Document(page_content=text, metadata={"category": cat})
    for cat, text in docs_by_category.items()
]

# 3. Split into chunks
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
docs = splitter.split_documents(documents)

# 4. Initialize FAISS with HuggingFace embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding_model)
