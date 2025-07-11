from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import (
    student, course, enrollment, grade, academic_behavior, payment, attendance_log, exam_session
)
from app.schemas.student import StudentResponse
from app.schemas.parent import ParentCreate, ParentLogin, ParentResponse
from app.crud.parent import create_parent, authenticate_parent, get_parent_by_username
from jose import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Body
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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

@app.get("/students", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(student.Student).offset(skip).limit(limit).all()

# @app.get("/students/{student_id}", response_model=StudentResponse)
# def get_student(student_id: int, db: Session = Depends(get_db)):
#     db_student = db.query(student.Student).filter(student.Student.student_id == student_id).first()
#     if not db_student:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student 

@app.post("/register", response_model=ParentResponse)
def parent_register(parent: ParentCreate, db: Session = Depends(get_db)):
    if get_parent_by_username(db, parent.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_parent(db, parent)

@app.post("/login")
def parent_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    parent = authenticate_parent(db, form_data.username, form_data.password)
    if not parent:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": parent.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 