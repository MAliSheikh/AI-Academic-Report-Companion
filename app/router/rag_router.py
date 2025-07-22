from fastapi import APIRouter, Query, Depends, HTTPException
from app.crud.rag_crud import get_rag_system, clean_code_answer
from app.utils import get_current_user, get_db
from sqlalchemy.orm import Session
from app.crud import chat_history as chat_crud
from app.schemas.chat_history import ChatHistoryCreate, ChatHistoryResponse
from typing import List


router = APIRouter()

@router.get("/rag_query/")
async def rag_query(
    question: str = Query(..., description="Your question for your PDF RAG system"),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    qa_chain = get_rag_system()
    answer = qa_chain.run(question)
    clean_answer = clean_code_answer(answer)
    
    # Store the chat in history
    chat_create = ChatHistoryCreate(question=question, answer=clean_answer)
    chat_crud.create_chat_history(db, chat_create, current_user)
    
    return {
        "question": question,
        "answer": clean_answer,
        "user": current_user
    }

@router.get("/chat_history/", response_model=List[ChatHistoryResponse])
async def get_chat_history(
    skip: int = 0,
    limit: int = 10,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve chat history for the logged-in user.
    - skip: Number of records to skip (pagination)
    - limit: Maximum number of records to return
    """
    chats = chat_crud.get_user_chat_history(db, current_user, skip, limit)
    return chats