from pydantic import BaseModel
from typing import Optional
import enum

class EnrollmentStatusEnum(str, enum.Enum):
    enrolled = "enrolled"
    withdrawn = "withdrawn"
    completed = "completed"

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    semester: int
    year: int
    section: Optional[str]
    enrollment_status: EnrollmentStatusEnum

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentUpdate(BaseModel):
    student_id: Optional[int]
    course_id: Optional[int]
    semester: Optional[int]
    year: Optional[int]
    section: Optional[str]
    enrollment_status: Optional[EnrollmentStatusEnum]

class EnrollmentResponse(EnrollmentBase):
    enrollment_id: int
    class Config:
        from_attributes = True