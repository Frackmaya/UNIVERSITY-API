from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    enrolled_program = db.Column(db.String(100), nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    academic_year = db.Column(db.Integer, nullable=False)
    program = db.Column(db.String(100), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()
    
    # Insert sample data if tables are empty
    if Student.query.count() == 0:
        students = [
            Student(name="Alice Johnson", enrolled_program="Computer Science"),
            Student(name="Bob Smith", enrolled_program="Software Engineering"),
            Student(name="Charlie Brown", enrolled_program="Software Engineering"),
            Student(name="Diana Prince", enrolled_program="Computer Science"),
            Student(name="Ethan Hunt", enrolled_program="Software Engineering"),
            Student(name="Fiona Green", enrolled_program="Data Science"),
            Student(name="George Wilson", enrolled_program="Software Engineering"),
            Student(name="Hannah Baker", enrolled_program="Computer Science"),
            Student(name="Ian Cooper", enrolled_program="Software Engineering"),
            Student(name="Jenny Taylor", enrolled_program="Data Science")
        ]
        db.session.bulk_save_objects(students)
        db.session.commit()
    
    if Subject.query.count() == 0:
        subjects = [
            # Year 1
            Subject(name="Principles of Programming Languages(CP 111)", academic_year=1, program="Software Engineering"),
            Subject(name='Numerical Analysis for ICT(MT 1211)', academic_year=1, program="Software Engineering"),
            Subject(name='Introduction to Probability and Statistics(ST 1210)', academic_year=1, program="Software Engineering"),
            Subject(name='Introduction to High Level Programming(CP 123)', academic_year=1, program="Software Engineering"),
            Subject(name='Development Perspectives(DS 102)', academic_year=1, program="Software Engineering"),
            Subject(name='Introduction to Information Technology(IT 111)', academic_year=1, program="Software Engineering"),
            Subject(name='Calculus(MT 1112)', academic_year=1, program="Software Engineering"),
            Subject(name='Introduction to Computer Networking(CN 121)', academic_year=1, program="Software Engineering"),
            
            # Year 2
            Subject(name="Data Structures and Algorithms", academic_year=2, program="Software Engineering"),
            Subject(name="Database Systems", academic_year=2, program="Software Engineering"),
            Subject(name="Object-Oriented Programming", academic_year=2, program="Software Engineering"),
            Subject(name="Software Engineering Principles", academic_year=2, program="Software Engineering"),
            
            # Year 3
            Subject(name="Software Design and Architecture", academic_year=3, program="Software Engineering"),
            Subject(name="Operating Systems", academic_year=3, program="Software Engineering"),
            Subject(name="Computer Networks", academic_year=3, program="Software Engineering"),
            Subject(name="Software Testing", academic_year=3, program="Software Engineering"),
            
            # Year 4
            Subject(name="Distributed Systems", academic_year=4, program="Software Engineering"),
            Subject(name="Machine Learning for Software Engineering", academic_year=4, program="Software Engineering"),
            Subject(name="Software Project Management", academic_year=4, program="Software Engineering"),
            Subject(name="Capstone Project", academic_year=4, program="Software Engineering")
        ]
        db.session.bulk_save_objects(subjects)
        db.session.commit()

# API Endpoints
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    students_list = [
        {"name": student.name, "enrolled_program": student.enrolled_program}
        for student in students
    ]
    return jsonify(students_list)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.filter_by(program="Software Engineering").order_by(Subject.academic_year).all()
    
    # Organize subjects by academic year
    subjects_by_year = {}
    for subject in subjects:
        year_key = f"Year {subject.academic_year}"
        if year_key not in subjects_by_year:
            subjects_by_year[year_key] = []
        subjects_by_year[year_key].append(subject.name)
    
    return jsonify(subjects_by_year)

if __name__ == '__main__':
    app.run(debug=True)