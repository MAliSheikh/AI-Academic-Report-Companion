from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_and_merge_documents(pdf_files):
    documents = []
    for file in pdf_files:
        loader = PyPDFLoader(file)
        documents.extend(loader.load())
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

def create_and_save_faiss_index(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_index")
    print("✅ FAISS index created and saved locally.")
    return db

def main():
    pdf_files = [
        "pdfs/ACADEMIC CALENDAR SUMMER-2025.pdf",
        "pdfs/Introduction_to_Python_Programming_-_WEB.pdf"
    ]
    documents = load_and_merge_documents(pdf_files)
    docs = split_documents(documents)
    create_and_save_faiss_index(docs)

if __name__ == "__main__":
    main()
