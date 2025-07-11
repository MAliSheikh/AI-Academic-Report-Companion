from pydantic import BaseModel, EmailStr
from typing import Optional

class ParentBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str]
    student_id: int

class ParentCreate(ParentBase):
    password: str

class ParentLogin(BaseModel):
    username: str
    password: str

class ParentResponse(ParentBase):
    parent_id: int
    disabled: bool
    class Config:
        orm_mode = True 