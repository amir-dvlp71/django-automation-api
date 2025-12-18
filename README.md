# Automation File Processing API

A Django REST API for processing uploaded CSV/Excel files and generating automated reports.

## Features

- Upload CSV or Excel files
- Automated data processing using Pandas
- Generate summary reports (rows, totals, averages)
- Store processing results and output files
- RESTful API built with Django Rest Framework
- Ready for async processing (Celery-friendly design)

## Tech Stack

- Python 3.x
- Django
- Django Rest Framework
- Pandas
- SQLite (can be replaced with PostgreSQL)

## API Endpoints

### Create Automation Job
POST /api/automation-jobs/

Upload a CSV or Excel file and start processing.

### List Jobs
GET /api/automation-jobs/

### Retrieve Job Details
GET /api/automation-jobs/{id}/

## Setup & Run

1. Clone the repository
git clone https://github.com/amir-dvlp71/automation-api.git
cd automation-api

2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run server
python manage.py runserver

## Example Response

{
  "id": 1,
  "status": "done",
  "report": {
    "rows": 120,
    "total_sum": 54000,
    "average_price": 450
  },
  "result_file": "/media/results/result_1.csv"
}

## Future Improvements

- Async processing with Celery + Redis
- Large file support
- User-based job isolation
- Docker support

## Author

Developed by [Amir]  
Backend Developer | Python & Django
