from pydantic import BaseModel
from typing import Optional
import enum
from datetime import date

class AttendanceStatusEnum(str, enum.Enum):
    present = "present"
    absent = "absent"
    late = "late"
    excused = "excused"

class AttendanceLogBase(BaseModel):
    enrollment_id: int
    date: date
    status: AttendanceStatusEnum
    remarks: Optional[str]

class AttendanceLogCreate(AttendanceLogBase):
    pass

class AttendanceLogUpdate(BaseModel):
    enrollment_id: Optional[int]
    date: Optional[date]
    status: Optional[AttendanceStatusEnum]
    remarks: Optional[str]

class AttendanceLogResponse(AttendanceLogBase):
    attendance_id: int
    class Config:
        orm_mode = True 