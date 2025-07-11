from pydantic import BaseModel
from typing import Optional
import enum

class AttendanceStatusEnum(str, enum.Enum):
    present = "Present"
    absent = "Absent"
    late = "Late"
    excused = "Excused"

class AttendanceLogBase(BaseModel):
    enrollment_id: int
    date: str
    status: AttendanceStatusEnum
    remarks: Optional[str]

class AttendanceLogCreate(AttendanceLogBase):
    pass

class AttendanceLogUpdate(BaseModel):
    enrollment_id: Optional[int]
    date: Optional[str]
    status: Optional[AttendanceStatusEnum]
    remarks: Optional[str]

class AttendanceLogResponse(AttendanceLogBase):
    attendance_id: int
    class Config:
        orm_mode = True 