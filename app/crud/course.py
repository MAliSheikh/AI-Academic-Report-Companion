from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate
from typing import List, Optional

def get_course(db: Session, course_id: int) -> Optional[Course]:
    return db.query(Course).filter(Course.course_id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100) -> List[Course]:
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: CourseCreate) -> Course:
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: CourseUpdate) -> Optional[Course]:
    db_course = db.query(Course).filter(Course.course_id == course_id).first()
    if not db_course:
        return None
    for var, value in vars(course).items():
        if value is not None:
            setattr(db_course, var, value)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int) -> bool:
    db_course = db.query(Course).filter(Course.course_id == course_id).first()
    if not db_course:
        return False
    db.delete(db_course)
    db.commit()
    return True 