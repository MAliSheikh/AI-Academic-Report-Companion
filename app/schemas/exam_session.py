from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
import enum

class ExamTypeEnum(str, enum.Enum):
    midterm = "Midterm"
    final = "Final"
    quiz = "Quiz"
    viva = "Viva"

class ExamSessionBase(BaseModel):
    course_id: int
    exam_type: ExamTypeEnum
    exam_date: str
    total_marks: Decimal
    duration_minutes: int
    examiner_name: Optional[str]
    room: Optional[str]

class ExamSessionCreate(ExamSessionBase):
    pass

class ExamSessionUpdate(BaseModel):
    course_id: Optional[int]
    exam_type: Optional[ExamTypeEnum]
    exam_date: Optional[str]
    total_marks: Optional[Decimal]
    duration_minutes: Optional[int]
    examiner_name: Optional[str]
    room: Optional[str]

class ExamSessionResponse(ExamSessionBase):
    exam_id: int
    class Config:
        orm_mode = True 