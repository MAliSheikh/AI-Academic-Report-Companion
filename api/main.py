from fastapi import FastAPI
from app.database import engine, Base

# Import all models so that Base.metadata.create_all works
from app.models import student, course, enrollment, grade, academic_behavior, payment, attendance_log

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "AI Academic Report Companion API is running!"} 