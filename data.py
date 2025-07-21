import sys
import os
# Add project root to sys.path for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import student as student_model, parent as parent_model, grade as grade_model, academic_behavior as ab_model, course as course_model, enrollment as enrollment_model, attendance_log as attendance_model, exam_session as exam_model, payment as payment_model
from app.schemas.student import StudentCreate
from app.schemas.parent import ParentCreate
from app.schemas.grade import GradeCreate
from app.schemas.academic_behavior import AcademicBehaviorCreate
from app.schemas.course import CourseCreate
from app.schemas.enrollment import EnrollmentCreate
from app.schemas.attendance_log import AttendanceLogCreate
from app.schemas.exam_session import ExamSessionCreate
from app.schemas.payment import PaymentCreate
from app.crud.student import create_student
from app.crud.parent import create_parent
from app.crud.grade import create_grade
from app.crud.academic_behavior import create_academic_behavior
from app.crud.course import create_course
from app.crud.enrollment import create_enrollment
from app.crud.attendance_log import create_attendance_log
from app.crud.exam_session import create_exam_session
from app.crud.payment import create_payment
import datetime
from datetime import date
from decimal import Decimal
import random


def clear_all_tables(db: Session):
    # Order matters due to FKs
    db.query(payment_model.Payment).delete()
    db.query(attendance_model.AttendanceLog).delete()
    db.query(grade_model.Grade).delete()
    db.query(ab_model.AcademicBehavior).delete()
    db.query(enrollment_model.Enrollment).delete()
    db.query(parent_model.Parent).delete()
    db.query(exam_model.ExamSession).delete()
    db.query(course_model.Course).delete()
    db.query(student_model.Student).delete()
    db.commit()

def main():
    db = SessionLocal()
    clear_all_tables(db)

    # Real student data
    real_students_data = [
        {"first_name": "Ahmed", "last_name": "Hassan", "gender": "male", "dob": date(2001, 3, 15), "blood": "O+", "email": "ahmed.hassan", "phone": "03001234567", "father": "Muhammad Hassan", "mother": "Fatima Hassan", "income": 75000.00},
        {"first_name": "Fatima", "last_name": "Khan", "gender": "female", "dob": date(2002, 7, 22), "blood": "A+", "email": "fatima.khan", "phone": "03012345678", "father": "Ali Khan", "mother": "Ayesha Khan", "income": 95000.00},
        {"first_name": "Muhammad", "last_name": "Ali", "gender": "male", "dob": date(2001, 11, 8), "blood": "B+", "email": "muhammad.ali", "phone": "03023456789", "father": "Omar Ali", "mother": "Zainab Ali", "income": 120000.00},
        {"first_name": "Aisha", "last_name": "Malik", "gender": "female", "dob": date(2002, 1, 30), "blood": "AB+", "email": "aisha.malik", "phone": "03034567890", "father": "Tariq Malik", "mother": "Sadia Malik", "income": 85000.00},
        {"first_name": "Usman", "last_name": "Sheikh", "gender": "male", "dob": date(2001, 5, 12), "blood": "O-", "email": "usman.sheikh", "phone": "03045678901", "father": "Rashid Sheikh", "mother": "Nadia Sheikh", "income": 110000.00},
        {"first_name": "Zara", "last_name": "Ahmed", "gender": "female", "dob": date(2002, 9, 18), "blood": "A-", "email": "zara.ahmed", "phone": "03056789012", "father": "Imran Ahmed", "mother": "Rukhsana Ahmed", "income": 90000.00},
        {"first_name": "Hassan", "last_name": "Raza", "gender": "male", "dob": date(2001, 12, 3), "blood": "B-", "email": "hassan.raza", "phone": "03067890123", "father": "Saqib Raza", "mother": "Samina Raza", "income": 105000.00},
        {"first_name": "Mariam", "last_name": "Siddique", "gender": "female", "dob": date(2002, 4, 25), "blood": "AB-", "email": "mariam.siddique", "phone": "03078901234", "father": "Kashif Siddique", "mother": "Lubna Siddique", "income": 80000.00},
        {"first_name": "Bilal", "last_name": "Qureshi", "gender": "male", "dob": date(2001, 8, 14), "blood": "O+", "email": "bilal.qureshi", "phone": "03089012345", "father": "Nadeem Qureshi", "mother": "Farah Qureshi", "income": 130000.00},
        {"first_name": "Sana", "last_name": "Butt", "gender": "female", "dob": date(2002, 6, 7), "blood": "A+", "email": "sana.butt", "phone": "03090123456", "father": "Waseem Butt", "mother": "Shazia Butt", "income": 70000.00},
        {"first_name": "Faisal", "last_name": "Iqbal", "gender": "male", "dob": date(2001, 10, 29), "blood": "B+", "email": "faisal.iqbal", "phone": "03101234567", "father": "Javaid Iqbal", "mother": "Nasreen Iqbal", "income": 115000.00},
        {"first_name": "Hira", "last_name": "Shahid", "gender": "female", "dob": date(2002, 2, 16), "blood": "AB+", "email": "hira.shahid", "phone": "03112345678", "father": "Shahid Mahmood", "mother": "Rafia Shahid", "income": 88000.00},
        {"first_name": "Osama", "last_name": "Farooq", "gender": "male", "dob": date(2001, 7, 11), "blood": "O-", "email": "osama.farooq", "phone": "03123456789", "father": "Farooq Ahmed", "mother": "Shaista Farooq", "income": 100000.00},
        {"first_name": "Amna", "last_name": "Tariq", "gender": "female", "dob": date(2002, 12, 4), "blood": "A-", "email": "amna.tariq", "phone": "03134567890", "father": "Tariq Hussain", "mother": "Mehreen Tariq", "income": 92000.00},
        {"first_name": "Saad", "last_name": "Nawaz", "gender": "male", "dob": date(2001, 9, 27), "blood": "B-", "email": "saad.nawaz", "phone": "03145678901", "father": "Nawaz Sharif", "mother": "Kulsoom Nawaz", "income": 125000.00}
    ]

    # 1. Students
    students = []
    for i, student_data in enumerate(real_students_data):
        s = StudentCreate(
            university_roll_number=f"2020-CS-{i+1:03}",
            national_id=f"42101-{random.randint(1000000, 9999999)}-{random.randint(1, 9)}",
            first_name=student_data["first_name"],
            middle_name=None,
            last_name=student_data["last_name"],
            gender=student_data["gender"],
            date_of_birth=student_data["dob"],
            blood_group=student_data["blood"],
            marital_status="single",
            photo_url=f"https://university.edu/photos/{student_data['first_name'].lower()}.jpg",
            personal_email=f"{student_data['email']}@gmail.com",
            university_email=f"{student_data['email']}@university.edu.pk",
            personal_phone=student_data["phone"],
            alternate_phone=None,
            current_address=f"House #{random.randint(1, 999)}, Block {chr(65 + random.randint(0, 7))}, {random.choice(['Gulshan-e-Iqbal', 'DHA', 'Clifton', 'North Nazimabad', 'Federal B Area'])}, Karachi",
            permanent_address=f"House #{random.randint(1, 999)}, {random.choice(['Lahore', 'Islamabad', 'Rawalpindi', 'Multan', 'Faisalabad', 'Gujranwala'])}, Pakistan",
            father_name=student_data["father"],
            mother_name=student_data["mother"],
            guardian_name=None,
            guardian_relation=None,
            guardian_contact=None,
            family_income=student_data["income"],
            program="BS Computer Science",
            department="Computer Science",
            batch_year=2020,
            current_semester=random.randint(5, 8),
            credit_hours_completed=random.randint(90, 130),
            cgpa=round(random.uniform(2.5, 3.8), 2),
            enrollment_status="active",
            admission_date=date(2020, 8, 15),
            expected_graduation_date=date(2024, 6, 15),
            last_login=datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30)),
            login_count=random.randint(50, 200),
        )
        students.append(create_student(db, s))

    # Real Computer Science courses
    real_courses_data = [
        {"code": "CS101", "name": "Introduction to Programming", "credits": 3, "semester": 1, "type": "core", "desc": "Basic programming concepts using C++"},
        {"code": "CS102", "name": "Object Oriented Programming", "credits": 3, "semester": 2, "type": "core", "desc": "OOP principles and implementation"},
        {"code": "CS201", "name": "Data Structures and Algorithms", "credits": 4, "semester": 3, "type": "core", "desc": "Fundamental data structures and algorithm design"},
        {"code": "CS202", "name": "Database Systems", "credits": 3, "semester": 4, "type": "core", "desc": "Database design, SQL, and database management"},
        {"code": "CS301", "name": "Software Engineering", "credits": 3, "semester": 5, "type": "core", "desc": "Software development lifecycle and methodologies"},
        {"code": "CS302", "name": "Computer Networks", "credits": 3, "semester": 5, "type": "core", "desc": "Network protocols, architecture, and communication"},
        {"code": "CS401", "name": "Web Development", "credits": 3, "semester": 6, "type": "elective", "desc": "Frontend and backend web technologies"},
        {"code": "CS402", "name": "Mobile App Development", "credits": 3, "semester": 6, "type": "elective", "desc": "Android and iOS application development"},
        {"code": "CS501", "name": "Artificial Intelligence", "credits": 4, "semester": 7, "type": "elective", "desc": "AI fundamentals, machine learning basics"},
        {"code": "CS502", "name": "Machine Learning", "credits": 3, "semester": 7, "type": "elective", "desc": "Advanced ML algorithms and applications"},
        {"code": "CS503", "name": "Computer Graphics", "credits": 3, "semester": 7, "type": "elective", "desc": "2D/3D graphics programming and visualization"},
        {"code": "CS601", "name": "Final Year Project I", "credits": 3, "semester": 8, "type": "core", "desc": "Research and development project - Phase 1"},
        {"code": "CS602", "name": "Cybersecurity", "credits": 3, "semester": 8, "type": "elective", "desc": "Information security and ethical hacking"},
        {"code": "MT101", "name": "Calculus and Analytical Geometry", "credits": 3, "semester": 1, "type": "core", "desc": "Mathematical foundations for computer science"},
        {"code": "PH101", "name": "Applied Physics", "credits": 3, "semester": 2, "type": "core", "desc": "Physics concepts relevant to computing"}
    ]

    # 2. Courses
    courses = []
    for course_data in real_courses_data:
        c = CourseCreate(
            course_code=course_data["code"],
            course_name=course_data["name"],
            credit_hours=course_data["credits"],
            department="Computer Science" if course_data["code"].startswith("CS") else "Mathematics" if course_data["code"].startswith("MT") else "Physics",
            semester_offered=course_data["semester"],
            course_description=course_data["desc"],
            course_type=course_data["type"],
            prerequisites=[],  # Simplified for this example
        )
        courses.append(create_course(db, c))

    # 3. Parents
    parents = []
    for i, student_data in enumerate(real_students_data):
        p = ParentCreate(
            username=f"{student_data['father'].lower().replace(' ', '.')}.parent",
            email=f"{student_data['father'].lower().replace(' ', '.')}.parent@gmail.com",
            full_name=student_data["father"],
            password="parent123",
            student_id=students[i].student_id,
        )
        parents.append(create_parent(db, p))

    # 4. Enrollments
    enrollments = []
    for i in range(15):
        # Each student enrolled in multiple courses
        course_idx = i % len(courses)
        e = EnrollmentCreate(
            student_id=students[i].student_id,
            course_id=courses[course_idx].course_id,
            semester=random.randint(5, 8),
            year=2024,
            section=random.choice(['A', 'B', 'C']),
            enrollment_status="enrolled",
        )
        enrollments.append(create_enrollment(db, e))

    # 5. Grades - realistic grade distributions
    grades = []
    grade_letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
    gpa_points = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0]
    
    for i in range(15):
        grade_idx = random.choices(range(len(grade_letters)), weights=[5, 15, 20, 25, 20, 10, 3, 2])[0]
        total = round(random.uniform(65, 95), 1)
        
        g = GradeCreate(
            enrollment_id=enrollments[i].enrollment_id,
            quiz_marks=[round(random.uniform(7, 10), 1), round(random.uniform(6, 10), 1)],
            assignment_marks=[round(random.uniform(8, 10), 1), round(random.uniform(7, 10), 1)],
            project_marks=round(random.uniform(15, 20), 1),
            midterm_marks=round(random.uniform(20, 30), 1),
            final_exam_marks=round(random.uniform(25, 35), 1),
            practical_marks=round(random.uniform(8, 15), 1),
            viva_marks=round(random.uniform(6, 10), 1),
            total_marks=total,
            grade_letter=grade_letters[grade_idx],
            gpa_points=gpa_points[grade_idx],
            attendance_percentage=round(random.uniform(75, 98), 1),
            marks_breakdown_notes=random.choice([
                "Excellent performance in practical work",
                "Good theoretical understanding, needs improvement in practicals",
                "Consistent performance throughout semester",
                "Strong project work, average exam performance",
                "Improved significantly in second half of semester"
            ]),
        )
        grades.append(create_grade(db, g))

    # 6. Academic Behavior - realistic behavioral scores
    behaviors = []
    for i in range(15):
        ab = AcademicBehaviorCreate(
            student_id=students[i].student_id,
            semester=random.randint(5, 8),
            participation_score=random.randint(6, 10),
            punctuality_score=random.randint(7, 10),
            discipline_score=random.randint(8, 10),
            group_work_score=random.randint(6, 9),
            class_engagement_score=random.randint(5, 10),
            submission_punctuality_score=random.randint(6, 10),
            faculty_comments=random.choice([
                "Active participant in class discussions",
                "Shows good leadership skills in group work",
                "Needs to improve class participation",
                "Excellent problem-solving abilities",
                "Consistent attendance and good behavior",
                "Creative thinking and innovative approach"
            ]),
            counseling_recommendation=random.choice([True, False]) if random.random() < 0.2 else False,
            notes=random.choice([
                "Student shows potential for academic excellence",
                "Recommended for advanced courses next semester",
                "May benefit from additional mentoring",
                "Strong candidate for research projects",
                "Good overall academic progress"
            ]),
        )
        behaviors.append(create_academic_behavior(db, ab))

    # 7. Attendance Logs - realistic attendance patterns
    attendance_logs = []
    for i in range(15):
        # Generate attendance for random dates
        attendance_date = datetime.date(2024, random.randint(1, 12), random.randint(1, 28))
        attendance_status = random.choices(['present', 'absent', 'late'], weights=[80, 15, 5])[0]
        
        al = AttendanceLogCreate(
            enrollment_id=enrollments[i].enrollment_id,
            date=attendance_date,
            status=attendance_status,
            remarks=random.choice([
                "On time", "Participated well", "Submitted assignment", 
                "Medical leave", "Family emergency", "Late due to transport",
                "Excused absence", "Make-up class attended"
            ]) if attendance_status != 'present' else None,
        )
        attendance_logs.append(create_attendance_log(db, al))

    # 8. Exam Sessions - realistic exam data
    exams = []
    exam_types = ["midterm", "final", "quiz", "viva"]
    rooms = ["CS-Lab1", "CS-Lab2", "Room-301", "Room-302", "Auditorium", "LT-1", "LT-2"]
    examiners = ["Dr. Ahmad Ali", "Prof. Sarah Khan", "Dr. Muhammad Tariq", "Dr. Fatima Sheikh", "Prof. Hassan Raza"]
    
    for i in range(15):
        course_idx = i % len(courses)
        ex = ExamSessionCreate(
            course_id=courses[course_idx].course_id,
            exam_type=random.choice(exam_types),
            exam_date=str(datetime.date(2024, random.randint(10, 12), random.randint(1, 28))),
            total_marks=random.choice([25.0, 30.0, 50.0, 100.0]),
            duration_minutes=random.choice([60, 90, 120, 180]),
            examiner_name=random.choice(examiners),
            room=random.choice(rooms),
        )
        exams.append(create_exam_session(db, ex))

    # 9. Payments - realistic fee structure
    payments = []
    fee_amounts = [45000.00, 47000.00, 49000.00, 51000.00]  # Different semester fees
    payment_methods = ["bank_transfer", "cash", "online", "card"]
    
    for i in range(15):
        semester_fee = random.choice(fee_amounts)
        amount_paid = semester_fee if random.random() < 0.85 else semester_fee * 0.5  # Some partial payments
        
        pay = PaymentCreate(
            student_id=students[i].student_id,
            semester=random.randint(5, 8),
            amount_due=semester_fee,
            amount_paid=amount_paid,
            payment_date=str(datetime.date(2024, random.randint(1, 3), random.randint(1, 28))),
            payment_method=random.choice(payment_methods),
            transaction_reference=f"TXN{random.randint(100000, 999999)}",
            payment_status="paid" if amount_paid >= semester_fee else "partial",
        )
        payments.append(create_payment(db, pay))

    print("Real data inserted successfully. All previous data overwritten.")
    print(f"Inserted: {len(students)} students, {len(courses)} courses, {len(enrollments)} enrollments")
    print(f"Generated: {len(grades)} grades, {len(attendance_logs)} attendance records, {len(payments)} payment records")
    db.close()

if __name__ == "__main__":
    main()