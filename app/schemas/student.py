from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date, datetime
from decimal import Decimal
import enum

class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class MaritalStatusEnum(str, enum.Enum):
    single = "single"
    married = "married"
    divorced = "divorced"
    widowed = "widowed"

class EnrollmentStatusEnum(str, enum.Enum):
    active = "active"
    leave = "leave"
    graduated = "graduated"
    dropped = "dropped"

class StudentBase(BaseModel):
    university_roll_number: str
    national_id: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    gender: GenderEnum
    date_of_birth: date
    blood_group: Optional[str]
    marital_status: Optional[MaritalStatusEnum]
    photo_url: Optional[str]
    personal_email: Optional[EmailStr]
    university_email: EmailStr
    personal_phone: Optional[str]
    alternate_phone: Optional[str]
    current_address: Optional[str]
    permanent_address: Optional[str]
    father_name: Optional[str]
    mother_name: Optional[str]
    guardian_name: Optional[str]
    guardian_relation: Optional[str]
    guardian_contact: Optional[str]
    family_income: Optional[Decimal]
    program: str
    department: str
    batch_year: int
    current_semester: int
    credit_hours_completed: Optional[int]
    cgpa: Optional[Decimal]
    enrollment_status: EnrollmentStatusEnum
    admission_date: date
    expected_graduation_date: Optional[date]
    last_login: Optional[datetime]
    login_count: Optional[int]

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    university_roll_number: Optional[str]
    national_id: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[GenderEnum]
    date_of_birth: Optional[date]
    blood_group: Optional[str]
    marital_status: Optional[MaritalStatusEnum]
    photo_url: Optional[str]
    personal_email: Optional[EmailStr]
    university_email: Optional[EmailStr]
    personal_phone: Optional[str]
    alternate_phone: Optional[str]
    current_address: Optional[str]
    permanent_address: Optional[str]
    father_name: Optional[str]
    mother_name: Optional[str]
    guardian_name: Optional[str]
    guardian_relation: Optional[str]
    guardian_contact: Optional[str]
    family_income: Optional[Decimal]
    program: Optional[str]
    department: Optional[str]
    batch_year: Optional[int]
    current_semester: Optional[int]
    credit_hours_completed: Optional[int]
    cgpa: Optional[Decimal]
    enrollment_status: Optional[EnrollmentStatusEnum]
    admission_date: Optional[date]
    expected_graduation_date: Optional[date]
    last_login: Optional[datetime]
    login_count: Optional[int]

class StudentResponse(StudentBase):
    student_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True