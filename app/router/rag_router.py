from fastapi import APIRouter, Query
from app.crud.rag_crud import initialize_rag_system


router = APIRouter()

qa_chain = initialize_rag_system()

@router.get("/rag_query/")
async def rag_query(question: str = Query(..., description="Your question for your PDF RAG system")):
    answer = qa_chain.run(question)
    return {"question": question, "answer": answer}