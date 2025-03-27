# UNIVERSITY-API
echo '# University Management API

## Description
A Flask API that provides:
- Student information (name and enrolled program)
- Software Engineering curriculum by academic year

## API Endpoints

### GET /students
Returns all students with their programs:
```json
[
  {\"name\": \"Alice Johnson\", \"enrolled_program\": \"Computer Science\"},
  ...
]