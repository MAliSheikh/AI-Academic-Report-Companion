from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Text
from sqlalchemy.dialects.sqlite import JSON
from app.database import Base

class Grade(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.enrollment_id"), nullable=False)
    quiz_marks = Column(JSON, nullable=True)
    assignment_marks = Column(JSON, nullable=True)
    project_marks = Column(DECIMAL, nullable=True)
    midterm_marks = Column(DECIMAL, nullable=True)
    final_exam_marks = Column(DECIMAL, nullable=True)
    practical_marks = Column(DECIMAL, nullable=True)
    viva_marks = Column(DECIMAL, nullable=True)
    total_marks = Column(DECIMAL, nullable=True)
    grade_letter = Column(String, nullable=True)
    gpa_points = Column(DECIMAL, nullable=True)
    attendance_percentage = Column(DECIMAL, nullable=True)
    marks_breakdown_notes = Column(Text, nullable=True) 