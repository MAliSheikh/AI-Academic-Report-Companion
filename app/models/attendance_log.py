from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Text
from app.database import Base
import enum
from typing import Optional
from datetime import date

class AttendanceStatusEnum(enum.Enum):
    present = "present"
    absent = "absent"
    late = "late"
    excused = "excused"

class AttendanceLog(Base):
    __tablename__ = "attendance_logs"
    attendance_id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.enrollment_id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatusEnum), nullable=False)
    remarks = Column(Text, nullable=True) 