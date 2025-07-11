from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import (
    student, course, enrollment, grade, academic_behavior, payment, attendance_log, exam_session
)
from app.schemas.student import StudentResponse

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "AI Academic Report Companion API is running!"}

# @app.get("/students", response_model=list[StudentResponse])
# def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(student.Student).offset(skip).limit(limit).all()

# @app.get("/students/{student_id}", response_model=StudentResponse)
# def get_student(student_id: int, db: Session = Depends(get_db)):
#     db_student = db.query(student.Student).filter(student.Student.student_id == student_id).first()
#     if not db_student:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student 