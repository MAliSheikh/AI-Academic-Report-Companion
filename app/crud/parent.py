from sqlalchemy.orm import Session
from app.models.parent import Parent
from app.schemas.parent import ParentCreate
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_parent_by_username(db: Session, username: str) -> Optional[Parent]:
    return db.query(Parent).filter(Parent.username == username).first()

def get_parent_by_email(db: Session, email: str) -> Optional[Parent]:
    return db.query(Parent).filter(Parent.email == email).first()

def create_parent(db: Session, parent: ParentCreate) -> Parent:
    hashed_password = pwd_context.hash(parent.password)
    db_parent = Parent(
        username=parent.username,
        email=parent.email,
        full_name=parent.full_name,
        hashed_password=hashed_password,
        student_id=parent.student_id
    )
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent

def authenticate_parent(db: Session, email: str, password: str) -> Optional[Parent]:
    parent = get_parent_by_email(db, email)
    if not parent:
        return None
    if not pwd_context.verify(password, parent.hashed_password):
        return None
    return parent 