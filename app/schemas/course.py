from pydantic import BaseModel
from typing import Optional, List
import enum

class CourseTypeEnum(str, enum.Enum):
    core = "Core"
    elective = "Elective"
    lab = "Lab"

class CourseBase(BaseModel):
    course_code: str
    course_name: str
    credit_hours: int
    department: str
    semester_offered: int
    course_description: Optional[str]
    course_type: CourseTypeEnum
    prerequisites: Optional[List[int]]

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    course_code: Optional[str]
    course_name: Optional[str]
    credit_hours: Optional[int]
    department: Optional[str]
    semester_offered: Optional[int]
    course_description: Optional[str]
    course_type: Optional[CourseTypeEnum]
    prerequisites: Optional[List[int]]

class CourseResponse(CourseBase):
    course_id: int
    class Config:
        orm_mode = True 