from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Parent(Base):
    __tablename__ = "parents"
    parent_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    disabled = Column(Boolean, default=False)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False) 