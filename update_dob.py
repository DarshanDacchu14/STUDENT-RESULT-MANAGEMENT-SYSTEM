from app import app, db, Student
from datetime import datetime

def update_student_dob():
    with app.app_context():
        # Dictionary of students and their DOBs
        student_dobs = {
            'DARSHAN A': '14/12/2004',
            'D CHANDANA': '29/06/2005',
            'MONIKA HA': '22/12/2005',
            'HARSHAVARDHAN S': '24/10/2005'
        }

        for name, dob_str in student_dobs.items():
            # Convert string date to datetime object
            dob = datetime.strptime(dob_str, '%d/%m/%Y').date()
            
            # Find and update the student
            student = Student.query.filter_by(name=name).first()
            if student:
                student.date_of_birth = dob
                print(f"Updated DOB for {name}")
            else:
                print(f"Student {name} not found")

        # Commit the changes
        db.session.commit()
        print("All updates completed successfully!")

if __name__ == '__main__':
    update_student_dob() 