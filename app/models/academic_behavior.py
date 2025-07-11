from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from app.database import Base

class AcademicBehavior(Base):
    __tablename__ = "academic_behavior"
    behavior_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    semester = Column(Integer, nullable=False)
    participation_score = Column(Integer, nullable=True)
    punctuality_score = Column(Integer, nullable=True)
    discipline_score = Column(Integer, nullable=True)
    group_work_score = Column(Integer, nullable=True)
    class_engagement_score = Column(Integer, nullable=True)
    submission_punctuality_score = Column(Integer, nullable=True)
    faculty_comments = Column(Text, nullable=True)
    counseling_recommendation = Column(Boolean, nullable=True)
    notes = Column(Text, nullable=True) 