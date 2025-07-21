from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
import enum
from datetime import date

class PaymentMethodEnum(str, enum.Enum):
    cash = "cash"
    card = "card"
    bank_transfer = "bank_transfer"
    online = "online"

class PaymentStatusEnum(str, enum.Enum):
    paid = "paid"
    pending = "pending"
    partial = "partial"

class PaymentBase(BaseModel):
    student_id: int
    semester: int
    amount_due: Decimal
    amount_paid: Decimal
    payment_date: date
    payment_method: PaymentMethodEnum
    transaction_reference: Optional[str]
    payment_status: PaymentStatusEnum

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    student_id: Optional[int]
    semester: Optional[int]
    amount_due: Optional[Decimal]
    amount_paid: Optional[Decimal]
    payment_date: Optional[date]
    payment_method: Optional[PaymentMethodEnum]
    transaction_reference: Optional[str]
    payment_status: Optional[PaymentStatusEnum]

class PaymentResponse(PaymentBase):
    payment_id: int
    class Config:
        from_attributes = True