from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
import os
import re

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def clean_code_answer(answer: str) -> str:
    # Remove Markdown code fences
    answer = re.sub(r"```(?:\w+)?\n?", "", answer)
    # Optionally, unescape newlines (if needed)
    # answer = answer.replace("\\n", "\n")  # Only if double-escaped
    return answer.strip()


def initialize_rag_system():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # db = FAISS.load_local("../../rag_model/faiss_index", embeddings, allow_dangerous_deserialization=True)
    faiss_index_path = str(Path(__file__).parent.parent.parent / "rag_model" / "faiss_index")
    db = FAISS.load_local(faiss_index_path, embeddings, allow_dangerous_deserialization=True)
    # ... rest of your code ...
    llm = ChatGroq(
        model_name="llama3-70b-8192",  # or any Groq-supported model
        api_key=os.environ["GROQ_API_KEY"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        chain_type="stuff"
    )
    return qa_chain
