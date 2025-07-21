from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from pydantic import field_validator

class GradeBase(BaseModel):
    enrollment_id: int
    quiz_marks: Optional[List[Decimal]]
    assignment_marks: Optional[List[Decimal]]
    project_marks: Optional[Decimal]
    midterm_marks: Optional[Decimal]
    final_exam_marks: Optional[Decimal]
    practical_marks: Optional[Decimal]
    viva_marks: Optional[Decimal]
    total_marks: Optional[Decimal]
    grade_letter: Optional[str]
    gpa_points: Optional[Decimal]
    attendance_percentage: Optional[Decimal]
    marks_breakdown_notes: Optional[str]

class GradeCreate(GradeBase):
    pass

    @field_validator('quiz_marks', 'assignment_marks', mode='before')
    @classmethod
    def convert_decimals_to_float(cls, v):
        if v is None:
            return v
        return [float(x) for x in v]

class GradeUpdate(BaseModel):
    enrollment_id: Optional[int]
    quiz_marks: Optional[List[Decimal]]
    assignment_marks: Optional[List[Decimal]]
    project_marks: Optional[Decimal]
    midterm_marks: Optional[Decimal]
    final_exam_marks: Optional[Decimal]
    practical_marks: Optional[Decimal]
    viva_marks: Optional[Decimal]
    total_marks: Optional[Decimal]
    grade_letter: Optional[str]
    gpa_points: Optional[Decimal]
    attendance_percentage: Optional[Decimal]
    marks_breakdown_notes: Optional[str]

class GradeResponse(GradeBase):
    grade_id: int
    class Config:
        orm_mode = True 