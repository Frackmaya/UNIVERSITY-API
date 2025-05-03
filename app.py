from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
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

# Create database tables and add sample data
with app.app_context():
    db.create_all()
    
    # Insert sample students if empty
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
    
    # Insert Software Engineering subjects if empty
    if Subject.query.count() == 0:
        subjects = [
            # Year 1 - Semester 1
            Subject(name="Principles of Programming Languages (CP 111)", academic_year=1, program="Software Engineering"),
            Subject(name="Numerical Analysis for ICT (MT 1211)", academic_year=1, program="Software Engineering"),
            Subject(name="Introduction to Probability and Statistics (ST 1210)", academic_year=1, program="Software Engineering"),
            
            # Year 1 - Semester 2
            Subject(name="Introduction to High Level Programming (CP 123)", academic_year=1, program="Software Engineering"),
            Subject(name="Development Perspectives (DS 102)", academic_year=1, program="Software Engineering"),
            Subject(name="Introduction to Information Technology (IT 111)", academic_year=1, program="Software Engineering"),
            Subject(name="Calculus (MT 1112)", academic_year=1, program="Software Engineering"),
            Subject(name="Introduction to Computer Networking (CN 121)", academic_year=1, program="Software Engineering"),
            
            # Year 2 - Semester 1
            Subject(name="Data Structures and Algorithms (CP 211)", academic_year=2, program="Software Engineering"),
            Subject(name="Database Systems (CP 212)", academic_year=2, program="Software Engineering"),
            
            # Year 2 - Semester 2
            Subject(name="Object-Oriented Programming (CP 223)", academic_year=2, program="Software Engineering"),
            Subject(name="Software Engineering Principles (SE 222)", academic_year=2, program="Software Engineering"),
            
            # Year 3 - Semester 1
            Subject(name="Software Design and Architecture (SE 311)", academic_year=3, program="Software Engineering"),
            Subject(name="Operating Systems (CP 312)", academic_year=3, program="Software Engineering"),
            
            # Year 3 - Semester 2
            Subject(name="Computer Networks (CN 321)", academic_year=3, program="Software Engineering"),
            Subject(name="Software Testing (SE 322)", academic_year=3, program="Software Engineering"),
            
            # Year 4 - Semester 1
            Subject(name="Distributed Systems (SE 411)", academic_year=4, program="Software Engineering"),
            Subject(name="Machine Learning for Software Engineering (AI 412)", academic_year=4, program="Software Engineering"),
            
            # Year 4 - Semester 2
            Subject(name="Software Project Management (SE 421)", academic_year=4, program="Software Engineering"),
            Subject(name="Capstone Project (SE 422)", academic_year=4, program="Software Engineering")
        ]
        db.session.bulk_save_objects(subjects)
    
    db.session.commit()

# API Endpoints
@app.route('/')
def index():
    return 'Hello, Flask is running!'


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
    
    # Organize by year and semester
    curriculum = {
        "Year 1": {
            "Semester 1": [],
            "Semester 2": []
        },
        "Year 2": {
            "Semester 1": [],
            "Semester 2": []
        },
        "Year 3": {
            "Semester 1": [],
            "Semester 2": []
        },
        "Year 4": {
            "Semester 1": [],
            "Semester 2": []
        }
    }
    
    for subject in subjects:
        year_key = f"Year {subject.academic_year}"
        semester_key = "Semester 1" if subject.id % 2 == 1 else "Semester 2"
        curriculum[year_key][semester_key].append({
            "code": subject.name.split("(")[-1].replace(")", ""),
            "name": subject.name.split("(")[0].strip(),
            "full_name": subject.name
        })
    
    return jsonify(curriculum)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
