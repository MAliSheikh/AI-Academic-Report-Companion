from sqlalchemy.orm import Session
from app.models.exam_session import ExamSession
from app.schemas.exam_session import ExamSessionCreate, ExamSessionUpdate
from typing import List, Optional

def get_exam_session(db: Session, exam_id: int) -> Optional[ExamSession]:
    return db.query(ExamSession).filter(ExamSession.exam_id == exam_id).first()

def get_exam_sessions(db: Session, skip: int = 0, limit: int = 100) -> List[ExamSession]:
    return db.query(ExamSession).offset(skip).limit(limit).all()

def create_exam_session(db: Session, exam: ExamSessionCreate) -> ExamSession:
    db_exam = ExamSession(**exam.dict())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def update_exam_session(db: Session, exam_id: int, exam: ExamSessionUpdate) -> Optional[ExamSession]:
    db_exam = db.query(ExamSession).filter(ExamSession.exam_id == exam_id).first()
    if not db_exam:
        return None
    for var, value in vars(exam).items():
        if value is not None:
            setattr(db_exam, var, value)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def delete_exam_session(db: Session, exam_id: int) -> bool:
    db_exam = db.query(ExamSession).filter(ExamSession.exam_id == exam_id).first()
    if not db_exam:
        return False
    db.delete(db_exam)
    db.commit()
    return True 