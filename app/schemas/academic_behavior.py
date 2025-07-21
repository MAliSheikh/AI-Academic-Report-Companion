from pydantic import BaseModel
from typing import Optional

class AcademicBehaviorBase(BaseModel):
    student_id: int
    semester: int
    participation_score: Optional[int]
    punctuality_score: Optional[int]
    discipline_score: Optional[int]
    group_work_score: Optional[int]
    class_engagement_score: Optional[int]
    submission_punctuality_score: Optional[int]
    faculty_comments: Optional[str]
    counseling_recommendation: Optional[bool]
    notes: Optional[str]

class AcademicBehaviorCreate(AcademicBehaviorBase):
    pass

class AcademicBehaviorUpdate(BaseModel):
    student_id: Optional[int]
    semester: Optional[int]
    participation_score: Optional[int]
    punctuality_score: Optional[int]
    discipline_score: Optional[int]
    group_work_score: Optional[int]
    class_engagement_score: Optional[int]
    submission_punctuality_score: Optional[int]
    faculty_comments: Optional[str]
    counseling_recommendation: Optional[bool]
    notes: Optional[str]

class AcademicBehaviorResponse(AcademicBehaviorBase):
    behavior_id: int
    class Config:
        from_attributes = True