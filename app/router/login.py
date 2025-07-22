from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.parent import ParentResponse
from app.crud.parent import authenticate_parent
from app.database import SessionLocal
from datetime import timedelta, timezone, datetime
import os
from jose import jwt
from dotenv import load_dotenv
from app.utils import get_db

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


router = APIRouter()

@router.post("/login")
def parent_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    parent = authenticate_parent(db, form_data.username, form_data.password)
    if not parent:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": parent.email, "username": parent.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 