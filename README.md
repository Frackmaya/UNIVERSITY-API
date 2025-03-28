# University Management API

A Flask-based REST API for managing student information and academic curriculum, specifically designed for Software Engineering programs.

## Features

- **Student Management**:
  - View all registered students
  - See each student's enrolled program

- **Curriculum Management**:
  - Browse complete Software Engineering curriculum
  - Organized by academic year and semester
  - Includes course codes and full names

## API Endpoints

### `GET /students`
Returns a list of all registered students.

**Example Response:**
```json
[
  {
    "name": "Alice Johnson",
    "enrolled_program": "Computer Science"
  },
  {
    "name": "Bob Smith",
    "enrolled_program": "Software Engineering"
  }
]

GET /subjects
Returns the complete Software Engineering curriculum organized by year and semester

Returns the complete Software Engineering curriculum organized by year and semester.

Example Response
{
  "Year 1": {
    "Semester 1": [
      {
        "code": "CP 111",
        "name": "Principles of Programming Languages",
        "full_name": "Principles of Programming Languages (CP 111)"
      }
    ],
    "Semester 2": [...]
  },
  "Year 2": {...}
}

Installation
Clone the repository:
git clone https://github.com/Frackmaya/UNIVERSITY-API.git

cd UNIVERSITY-API
Set up Python environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

Install dependencies:
pip install -r requirements.txt


Initialize the database:
python init_db.py  # Optional - included in app.py
Running the Application