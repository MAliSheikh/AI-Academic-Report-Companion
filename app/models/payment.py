from sqlalchemy import Column, Integer, String, DECIMAL, Date, Enum, ForeignKey
from app.database import Base
import enum

class PaymentMethodEnum(enum.Enum):
    cash = "Cash"
    card = "Card"
    bank_transfer = "Bank Transfer"
    online = "Online"

class PaymentStatusEnum(enum.Enum):
    paid = "Paid"
    pending = "Pending"
    partial = "Partial"

class Payment(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    semester = Column(Integer, nullable=False)
    amount_due = Column(DECIMAL, nullable=False)
    amount_paid = Column(DECIMAL, nullable=False)
    payment_date = Column(Date, nullable=False)
    payment_method = Column(Enum(PaymentMethodEnum), nullable=False)
    transaction_reference = Column(String, nullable=True)
    payment_status = Column(Enum(PaymentStatusEnum), nullable=False)