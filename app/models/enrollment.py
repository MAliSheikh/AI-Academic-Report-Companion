from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.database import Base
import enum

class EnrollmentStatusEnum(enum.Enum):
    enrolled = "Enrolled"
    withdrawn = "Withdrawn"
    completed = "Completed"

class Enrollment(Base):
    __tablename__ = "enrollments"
    enrollment_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    semester = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    section = Column(String, nullable=True)
    enrollment_status = Column(Enum(EnrollmentStatusEnum), nullable=False) 