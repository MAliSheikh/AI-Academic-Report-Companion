from sqlalchemy import Column, String, Integer, Enum, Text, DECIMAL
from sqlalchemy.dialects.sqlite import JSON
from app.database import Base
import enum

class CourseTypeEnum(enum.Enum):
    core = "Core"
    elective = "Elective"
    lab = "Lab"

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, unique=True, nullable=False)
    course_name = Column(String, nullable=False)
    credit_hours = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    semester_offered = Column(Integer, nullable=False)
    course_description = Column(Text, nullable=True)
    course_type = Column(Enum(CourseTypeEnum), nullable=False)
    prerequisites = Column(JSON, nullable=True) 