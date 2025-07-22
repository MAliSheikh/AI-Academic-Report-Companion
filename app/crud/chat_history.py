from sqlalchemy.orm import Session
from app.models.chat_history import ChatHistory
from app.schemas.chat_history import ChatHistoryCreate
from typing import List

def create_chat_history(db: Session, chat: ChatHistoryCreate, user_id: str) -> ChatHistory:
    db_chat = ChatHistory(
        user_id=user_id,
        question=chat.question,
        answer=chat.answer
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_user_chat_history(db: Session, user_id: str, skip: int = 0, limit: int = 100) -> List[ChatHistory]:
    return db.query(ChatHistory)\
        .filter(ChatHistory.user_id == user_id)\
        .order_by(ChatHistory.created_at.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()
