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

## GET /subjects
Returns the complete Software Engineering curriculum organized by year and semester

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



## Installation
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

## Backup Schemes

 1. Full Backup
- **Execution**: Copies all files and databases in their entirety.

- **Advantages**:
  - Simple to restore.
  - Complete data snapshot.

- **Disadvantages**:
  - Time-consuming and storage-intensive.
  - Often redundant if little has changed.

 2. Incremental Backup
- **Execution**: Only backs up data changed since the last backup (full or incremental).

- **Advantages**:
  - Saves time and storage.

- **Disadvantages**:
  - Restoration takes longer (needs last full + all incrementals).
  - Slightly more complex backup chain.

 3. Differential Backup
- **Execution**: Backs up data changed since the last full backup.

- **Advantages**:
  - Faster than full backup.
  - Simpler restoration than incremental.

- **Disadvantages**:
  - Storage usage increases over time.
  - Restoration takes longer than full.


## bash_scripts Directory

Contains three automation scripts:

- **health_check.sh**: Logs CPU, memory, disk, Nginx status, and `/students` & `/subjects` endpoints to `/var/log/server_health.log`.  
- **backup_api.sh**: Archives your Flask project and SQLite DB to `~/backups/`, removes backups older than 7 days, logs to `/var/log/backup.log`.  
- **update_server.sh**: Runs `apt update/upgrade`, `git pull`, restarts `university.service` and Nginx, logs to `/var/log/update.log`.

### Setup
```bash
cd bash_scripts
chmod +x *.sh
```

## Docker-Based University API

```bash
# Clone the repo
git clone https://github.com/Frackmaya/UNIVERSITY-API.git
cd university-api

# Build Docker images
docker-compose build
```

#URL of the Docker regisrty to my images
https://hub.docker.com/r/youn9uru/university-api-flask-api


## Running Front-End with Docker

### Build the Docker Image
```bash
docker build -t university-api-frontend1 ./frontend

```
##To run the Front-end container

```bash

docker run -d -p 3000:3000 university-api-frontend1



```

### 🔁 **2. Load Balancer Setup (Round-Robin + Health Checks)**

## Load Balancer Configuration

We are using **Nginx** as the load balancer, configured to use the **round-robin** algorithm. Here's a snippet of the config:

```bash
nginx
upstream frontend {
    server frontend1:3000;
    server frontend2:3000;
    server frontend3:3000;
}

server {
    listen 80;

    location / {
        proxy_pass http://frontend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```


## Health  checks
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3000"]
  interval: 30s
  timeout: 10s
  retries: 3
