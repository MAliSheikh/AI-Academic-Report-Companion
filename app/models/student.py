from sqlalchemy import Column, String, Integer, Date, Enum, DECIMAL, Text, TIMESTAMP
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.sql import func
from sqlalchemy.types import Boolean
from app.database import Base
import enum

class GenderEnum(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class MaritalStatusEnum(enum.Enum):
    single = "Single"
    married = "Married"
    divorced = "Divorced"
    widowed = "Widowed"

class EnrollmentStatusEnum(enum.Enum):
    active = "Active"
    leave = "Leave"
    graduated = "Graduated"
    dropped = "Dropped"

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True, index=True)
    university_roll_number = Column(String, unique=True, nullable=False)
    national_id = Column(String, unique=True, nullable=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    blood_group = Column(String, nullable=True)
    marital_status = Column(Enum(MaritalStatusEnum), nullable=True)
    photo_url = Column(String, nullable=True)
    personal_email = Column(String, unique=True, nullable=True)
    university_email = Column(String, unique=True, nullable=False)
    personal_phone = Column(String, nullable=True)
    alternate_phone = Column(String, nullable=True)
    current_address = Column(Text, nullable=True)
    permanent_address = Column(Text, nullable=True)
    father_name = Column(String, nullable=True)
    mother_name = Column(String, nullable=True)
    guardian_name = Column(String, nullable=True)
    guardian_relation = Column(String, nullable=True)
    guardian_contact = Column(String, nullable=True)
    family_income = Column(DECIMAL, nullable=True)
    program = Column(String, nullable=False)
    department = Column(String, nullable=False)
    batch_year = Column(Integer, nullable=False)
    current_semester = Column(Integer, nullable=False)
    credit_hours_completed = Column(Integer, nullable=True)
    cgpa = Column(DECIMAL, nullable=True)
    enrollment_status = Column(Enum(EnrollmentStatusEnum), nullable=False, default=EnrollmentStatusEnum.active)
    admission_date = Column(Date, nullable=False)
    expected_graduation_date = Column(Date, nullable=True)
    last_login = Column(TIMESTAMP, nullable=True)
    login_count = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now()) 