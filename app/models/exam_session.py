from sqlalchemy import Column, Integer, String, Enum, Date, DECIMAL, ForeignKey
from app.database import Base
import enum

class ExamTypeEnum(enum.Enum):
    midterm = "midterm"
    final = "final"
    quiz = "quiz"
    viva = "viva"

class ExamSession(Base):
    __tablename__ = "exam_sessions"
    exam_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    exam_type = Column(Enum(ExamTypeEnum), nullable=False)
    exam_date = Column(Date, nullable=False)
    total_marks = Column(DECIMAL, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    examiner_name = Column(String, nullable=True)
    room = Column(String, nullable=True) 