from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal
from app.models.student import Student, GenderEnum, MaritalStatusEnum, EnrollmentStatusEnum

def add_sample_students():
    db: Session = SessionLocal()
    students = [
        Student(
            university_roll_number="UNI2024001",
            national_id="NID1234567890",
            first_name="Alice",
            middle_name="B.",
            last_name="Smith",
            gender=GenderEnum.female,
            date_of_birth=date(2002, 5, 14),
            blood_group="A+",
            marital_status=MaritalStatusEnum.single,
            photo_url=None,
            personal_email="alice.smith@gmail.com",
            university_email="alice.smith@university.edu",
            personal_phone="1234567890",
            alternate_phone=None,
            current_address="123 Main St, City",
            permanent_address="123 Main St, City",
            father_name="John Smith",
            mother_name="Jane Smith",
            guardian_name=None,
            guardian_relation=None,
            guardian_contact=None,
            family_income=50000.00,
            program="BSc Computer Science",
            department="Computer Science",
            batch_year=2020,
            current_semester=7,
            credit_hours_completed=120,
            cgpa=3.85,
            enrollment_status=EnrollmentStatusEnum.active,
            admission_date=date(2020, 8, 1),
            expected_graduation_date=date(2024, 6, 30),
            last_login=None,
            login_count=0
        ),
        Student(
            university_roll_number="UNI2024002",
            national_id="NID0987654321",
            first_name="Bob",
            middle_name=None,
            last_name="Johnson",
            gender=GenderEnum.male,
            date_of_birth=date(2001, 11, 23),
            blood_group="B-",
            marital_status=MaritalStatusEnum.single,
            photo_url=None,
            personal_email="bob.johnson@gmail.com",
            university_email="bob.johnson@university.edu",
            personal_phone="0987654321",
            alternate_phone=None,
            current_address="456 Elm St, City",
            permanent_address="456 Elm St, City",
            father_name="Michael Johnson",
            mother_name="Sarah Johnson",
            guardian_name=None,
            guardian_relation=None,
            guardian_contact=None,
            family_income=60000.00,
            program="BSc Mathematics",
            department="Mathematics",
            batch_year=2020,
            current_semester=7,
            credit_hours_completed=118,
            cgpa=3.67,
            enrollment_status=EnrollmentStatusEnum.active,
            admission_date=date(2020, 8, 1),
            expected_graduation_date=date(2024, 6, 30),
            last_login=None,
            login_count=0
        )
    ]
    db.add_all(students)
    db.commit()
    db.close()

if __name__ == "__main__":
    add_sample_students() 