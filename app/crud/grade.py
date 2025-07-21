from sqlalchemy.orm import Session
from app.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeUpdate
from decimal import Decimal

def create_grade(db: Session, grade: GradeCreate):
    data = grade.dict()
    for key in ['quiz_marks', 'assignment_marks', 'project_marks', 'midterm_marks', 'final_exam_marks', 'practical_marks', 'viva_marks', 'total_marks', 'gpa_points', 'attendance_percentage']:
        if isinstance(data.get(key), Decimal):
            data[key] = float(data[key])
        elif isinstance(data.get(key), list):
            data[key] = [float(x) if isinstance(x, Decimal) else x for x in data[key]]
    db_grade = Grade(**data)
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

def get_grade(db: Session, grade_id: int):
    return db.query(Grade).filter(Grade.grade_id == grade_id).first()

def get_grades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Grade).offset(skip).limit(limit).all()

def update_grade(db: Session, grade_id: int, grade: GradeUpdate):
    db_grade = db.query(Grade).filter(Grade.grade_id == grade_id).first()
    if db_grade:
        for key, value in grade.dict(exclude_unset=True).items():
            setattr(db_grade, key, value)
        db.commit()
        db.refresh(db_grade)
    return db_grade

def delete_grade(db: Session, grade_id: int):
    db_grade = db.query(Grade).filter(Grade.grade_id == grade_id).first()
    if db_grade:
        db.delete(db_grade)
        db.commit()
    return db_grade