from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatHistoryBase(BaseModel):
    question: str
    answer: str

class ChatHistoryCreate(ChatHistoryBase):
    pass

class ChatHistoryResponse(ChatHistoryBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
