from fastapi import APIRouter, Query
from app.crud.rag_crud import initialize_rag_system, clean_code_answer


router = APIRouter()

qa_chain = initialize_rag_system()

@router.get("/rag_query/")
async def rag_query(question: str = Query(..., description="Your question for your PDF RAG system")):
    answer = qa_chain.run(question)
    clean_answer = clean_code_answer(answer)
    return {"question": question, "answer": clean_answer}