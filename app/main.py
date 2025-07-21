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
from fastapi.routing import APIRouter
from app.utils import get_db
from app.router.rag_router import router as rag_app 
from app.router.register import router as register_router
from app.router.login import router as login_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Or specify your frontend's URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


# Mount the RAG router under /rag
app.include_router(rag_app)
app.include_router(register_router)
app.include_router(login_router)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "AI Academic Report Companion API is running!"}
