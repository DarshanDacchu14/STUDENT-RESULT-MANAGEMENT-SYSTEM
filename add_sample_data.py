from app import app, db, Student, Result
from datetime import date

def add_sample_data():
    with app.app_context():
        # Drop all existing data
        db.drop_all()
        db.create_all()
        
        # Sample students with date of birth
        students = [
            {
                'usn': '1MS21CS001',
                'name': 'DARSHAN A',
                'semester': 4,
                'date_of_birth': date(2004, 12, 14),
                'results': [
                    {'subject_code':  'CS401', 'subject_name': 'Data Structures', 'internal_marks': 45, 'external_marks': 85, 'total_marks': 130, 'grade': 'A+'},
                    {'subject_code': 'CS402', 'subject_name': 'Database Systems', 'internal_marks': 42, 'external_marks': 88, 'total_marks': 130, 'grade': 'A+'},
                    {'subject_code': 'CS403', 'subject_name': 'Computer Networks', 'internal_marks': 38, 'external_marks': 82, 'total_marks': 120, 'grade': 'A'}
                ]
            },
            {
                'usn': '1MS21CS002',
                'name': 'D CHANDANA',
                'semester': 4,
                'date_of_birth': date(2005, 6, 29),
                'results': [
                    {'subject_code': 'CS401', 'subject_name': 'Data Structures', 'internal_marks': 40, 'external_marks': 90, 'total_marks': 130, 'grade': 'A+'},
                    {'subject_code': 'CS402', 'subject_name': 'Database Systems', 'internal_marks': 35, 'external_marks': 75, 'total_marks': 110, 'grade': 'B+'},
                    {'subject_code': 'CS403', 'subject_name': 'Computer Networks', 'internal_marks': 32, 'external_marks': 68, 'total_marks': 100, 'grade': 'B'}
                ]
            },
            {
                'usn': '1MS21CS003',
                'name': 'MONIKA HA',
                'semester': 4,
                'date_of_birth': date(2005, 12, 22),
                'results': [
                    {'subject_code': 'CS401', 'subject_name': 'Data Structures', 'internal_marks': 38, 'external_marks': 82, 'total_marks': 120, 'grade': 'A'},
                    {'subject_code': 'CS402', 'subject_name': 'Database Systems', 'internal_marks': 36, 'external_marks': 84, 'total_marks': 120, 'grade': 'A'},
                    {'subject_code': 'CS403', 'subject_name': 'Computer Networks', 'internal_marks': 34, 'external_marks': 76, 'total_marks': 110, 'grade': 'B+'}
                ]
            },
            {
                'usn': '1MS21CS004',
                'name': 'HARSHAVARDHAN S',
                'semester': 4,
                'date_of_birth': date(2005, 10, 24),
                'results': [
                    {'subject_code': 'CS401', 'subject_name': 'Data Structures', 'internal_marks': 43, 'external_marks': 87, 'total_marks': 130, 'grade': 'A+'},
                    {'subject_code': 'CS402', 'subject_name': 'Database Systems', 'internal_marks': 39, 'external_marks': 81, 'total_marks': 120, 'grade': 'A'},
                    {'subject_code': 'CS403', 'subject_name': 'Computer Networks', 'internal_marks': 37, 'external_marks': 83, 'total_marks': 120, 'grade': 'A'}
                ]
            }
        ]
        
        # Add students and their results
        for student_data in students:
            student = Student(
                usn=student_data['usn'],
                name=student_data['name'],
                semester=student_data['semester'],
                date_of_birth=student_data['date_of_birth']
            )
            db.session.add(student)
            db.session.flush()  # Flush to get the student ID
            
            for result_data in student_data['results']:
                result = Result(
                    subject_code=result_data['subject_code'],
                    subject_name=result_data['subject_name'],
                    internal_marks=result_data['internal_marks'],
                    external_marks=result_data['external_marks'],
                    total_marks=result_data['total_marks'],
                    grade=result_data['grade'],
                    student_id=student.id
                )
                db.session.add(result)
        
        db.session.commit()
        print("Sample data added successfully!")

if __name__ == '__main__':
    add_sample_data() 