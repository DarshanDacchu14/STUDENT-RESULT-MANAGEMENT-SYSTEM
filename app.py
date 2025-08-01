from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    results = db.relationship('Result', backref='student', lazy=True)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_code = db.Column(db.String(10), nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    internal_marks = db.Column(db.Float, nullable=False)
    external_marks = db.Column(db.Float, nullable=False)
    total_marks = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    captcha_text = generate_captcha()
    session['captcha'] = captcha_text
    return render_template('index.html', captcha_text=captcha_text)

@app.route('/result', methods=['POST'])
def get_result():
    usn = request.form.get('usn')
    dob = request.form.get('dob')
    user_captcha = request.form.get('captcha')
    stored_captcha = session.get('captcha')

    if not stored_captcha or user_captcha != stored_captcha:
        flash('Invalid CAPTCHA! Please try again.')
        return redirect(url_for('home'))

    session.pop('captcha', None)
    new_captcha = generate_captcha()
    session['captcha'] = new_captcha

    student = Student.query.filter_by(usn=usn).first()
    
    if student:
        dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
        if student.date_of_birth != dob_date:
            flash('Invalid Date of Birth! Please try again.')
            return redirect(url_for('home'))
        return render_template('result.html', student=student)
    else:
        flash('Student not found! Please check your USN.')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000) 