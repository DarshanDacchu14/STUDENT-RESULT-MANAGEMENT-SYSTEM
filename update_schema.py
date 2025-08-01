from app import app, db, Student
from datetime import datetime
import sqlite3

def update_database():
    # Connect to the database
    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    
    try:
        # Add date_of_birth column if it doesn't exist
        cursor.execute('ALTER TABLE student ADD COLUMN date_of_birth DATE')
        print("Added date_of_birth column to student table")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("date_of_birth column already exists")
        else:
            raise e
    
    # Dictionary of students and their DOBs
    student_dobs = {
        'DARSHAN A': '14/12/2004',
        'D CHANDANA': '29/06/2005',
        'MONIKA HA': '22/12/2005',
        'HARSHAVARDHAN S': '24/10/2005'
    }

    # Update the DOB for each student
    for name, dob_str in student_dobs.items():
        # Convert string date to datetime object
        dob = datetime.strptime(dob_str, '%d/%m/%Y').date()
        
        # Update the student's DOB
        cursor.execute('''
            UPDATE student 
            SET date_of_birth = ? 
            WHERE name = ?
        ''', (dob, name))
        
        if cursor.rowcount > 0:
            print(f"Updated DOB for {name}")
        else:
            print(f"Student {name} not found")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("All updates completed successfully!")

if __name__ == '__main__':
    update_database() 