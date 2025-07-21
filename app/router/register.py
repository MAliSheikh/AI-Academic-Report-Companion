from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.parent import ParentCreate, ParentResponse
from app.crud.parent import create_parent, get_parent_by_username
from app.database import SessionLocal
from app.utils import get_db


router = APIRouter()

@router.post("/register", response_model=ParentResponse)
def parent_register(parent: ParentCreate, db: Session = Depends(get_db)):
    if get_parent_by_username(db, parent.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_parent(db, parent) 