from sqlalchemy.orm import Session
from app.models.academic_behavior import AcademicBehavior
from app.schemas.academic_behavior import AcademicBehaviorCreate, AcademicBehaviorUpdate

def create_academic_behavior(db: Session, behavior: AcademicBehaviorCreate):
    db_behavior = AcademicBehavior(**behavior.dict())
    db.add(db_behavior)
    db.commit()
    db.refresh(db_behavior)
    return db_behavior

def get_academic_behavior(db: Session, behavior_id: int):
    return db.query(AcademicBehavior).filter(AcademicBehavior.behavior_id == behavior_id).first()

def get_academic_behaviors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AcademicBehavior).offset(skip).limit(limit).all()


def update_academic_behavior(db: Session, behavior_id: int, behavior: AcademicBehaviorUpdate):
    db_behavior = db.query(AcademicBehavior).filter(AcademicBehavior.behavior_id == behavior_id).first()
    if db_behavior:
        for key, value in behavior.dict(exclude_unset=True).items():
            setattr(db_behavior, key, value)
        db.commit()
        db.refresh(db_behavior)
    return db_behavior

def delete_academic_behavior(db: Session, behavior_id: int):
    db_behavior = db.query(AcademicBehavior).filter(AcademicBehavior.behavior_id == behavior_id).first()
    if db_behavior:
        db.delete(db_behavior)
        db.commit()
    return db_behavior