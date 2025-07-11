from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate
from typing import List, Optional

def get_student(db: Session, student_id: int) -> Optional[Student]:
    return db.query(Student).filter(Student.student_id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100) -> List[Student]:
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentCreate) -> Student:
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: StudentUpdate) -> Optional[Student]:
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        return None
    for var, value in vars(student).items():
        if value is not None:
            setattr(db_student, var, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int) -> bool:
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        return False
    db.delete(db_student)
    db.commit()
    return True 