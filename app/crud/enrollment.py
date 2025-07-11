from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate, EnrollmentUpdate
from typing import List, Optional

def get_enrollment(db: Session, enrollment_id: int) -> Optional[Enrollment]:
    return db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()

def get_enrollments(db: Session, skip: int = 0, limit: int = 100) -> List[Enrollment]:
    return db.query(Enrollment).offset(skip).limit(limit).all()

def create_enrollment(db: Session, enrollment: EnrollmentCreate) -> Enrollment:
    db_enrollment = Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def update_enrollment(db: Session, enrollment_id: int, enrollment: EnrollmentUpdate) -> Optional[Enrollment]:
    db_enrollment = db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()
    if not db_enrollment:
        return None
    for var, value in vars(enrollment).items():
        if value is not None:
            setattr(db_enrollment, var, value)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def delete_enrollment(db: Session, enrollment_id: int) -> bool:
    db_enrollment = db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()
    if not db_enrollment:
        return False
    db.delete(db_enrollment)
    db.commit()
    return True 