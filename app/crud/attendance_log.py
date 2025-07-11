from sqlalchemy.orm import Session
from app.models.attendance_log import AttendanceLog
from app.schemas.attendance_log import AttendanceLogCreate, AttendanceLogUpdate
from typing import List, Optional

def get_attendance_log(db: Session, attendance_id: int) -> Optional[AttendanceLog]:
    return db.query(AttendanceLog).filter(AttendanceLog.attendance_id == attendance_id).first()

def get_attendance_logs(db: Session, skip: int = 0, limit: int = 100) -> List[AttendanceLog]:
    return db.query(AttendanceLog).offset(skip).limit(limit).all()

def create_attendance_log(db: Session, log: AttendanceLogCreate) -> AttendanceLog:
    db_log = AttendanceLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def update_attendance_log(db: Session, attendance_id: int, log: AttendanceLogUpdate) -> Optional[AttendanceLog]:
    db_log = db.query(AttendanceLog).filter(AttendanceLog.attendance_id == attendance_id).first()
    if not db_log:
        return None
    for var, value in vars(log).items():
        if value is not None:
            setattr(db_log, var, value)
    db.commit()
    db.refresh(db_log)
    return db_log

def delete_attendance_log(db: Session, attendance_id: int) -> bool:
    db_log = db.query(AttendanceLog).filter(AttendanceLog.attendance_id == attendance_id).first()
    if not db_log:
        return False
    db.delete(db_log)
    db.commit()
    return True 