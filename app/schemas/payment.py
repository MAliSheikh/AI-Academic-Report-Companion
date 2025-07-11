from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
import enum

class PaymentMethodEnum(str, enum.Enum):
    cash = "Cash"
    card = "Card"
    bank_transfer = "Bank Transfer"
    online = "Online"

class PaymentStatusEnum(str, enum.Enum):
    paid = "Paid"
    pending = "Pending"
    partial = "Partial"

class PaymentBase(BaseModel):
    student_id: int
    semester: int
    amount_due: Decimal
    amount_paid: Decimal
    payment_date: str
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
    payment_date: Optional[str]
    payment_method: Optional[PaymentMethodEnum]
    transaction_reference: Optional[str]
    payment_status: Optional[PaymentStatusEnum]

class PaymentResponse(PaymentBase):
    payment_id: int
    class Config:
        orm_mode = True 