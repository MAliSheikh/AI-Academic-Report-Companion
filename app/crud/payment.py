from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate
from typing import List, Optional

def get_payment(db: Session, payment_id: int) -> Optional[Payment]:
    return db.query(Payment).filter(Payment.payment_id == payment_id).first()

def get_payments(db: Session, skip: int = 0, limit: int = 100) -> List[Payment]:
    return db.query(Payment).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: PaymentCreate) -> Payment:
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def update_payment(db: Session, payment_id: int, payment: PaymentUpdate) -> Optional[Payment]:
    db_payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
    if not db_payment:
        return None
    for var, value in vars(payment).items():
        if value is not None:
            setattr(db_payment, var, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int) -> bool:
    db_payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
    if not db_payment:
        return False
    db.delete(db_payment)
    db.commit()
    return True 