# UNIVERSITY-API
echo '# University Management API

## Description
A Flask API that provides:
- Student information (name and enrolled program)
- Software Engineering curriculum by academic year

## API Endpoints

### GET /students
Returns all students with their programs:
[
  {\"name\": \"Alice Johnson\", \"enrolled_program\": \"Computer Science\"},
  ...
]


### GET /subjects
Returns Software Engineering subjects grouped by year:
{
  \"Year 1\": [\"Principles of Programming Languages\", ...],
  ...
}