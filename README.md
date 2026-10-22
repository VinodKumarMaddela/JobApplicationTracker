# Job Application Tracker Pro

A web-based application built with Django and MySQL to help job seekers organize, track, and manage their job applications in one place.

## Features

- **Dashboard:** View job application statistics at a glance.
- **Add Applications:** Record company names, job titles, job links, locations, application dates, salary details, and notes.
- **Edit and Delete:** Update application records or remove them when needed.
- **Search:** Find applications by company name, job title, or location.
- **Status Filtering:** Filter applications by their current status.
- **Application Status Tracking:** Track Applied, Assessment, Interview, Offer, Rejected, and Withdrawn statuses.
- **REST API:** Access application records through Django REST Framework.
- **Admin Panel:** Manage application records through Django's admin interface.
- **Automated Tests:** Test model behavior and dashboard page responses.

## Technology Stack

- **Backend:** Python, Django
- **REST API:** Django REST Framework
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap
- **Testing:** Django Test Framework
- **Version Control:** Git and GitHub

## Getting Started

### Prerequisites

- Python 3.12 or compatible version
- MySQL Server
- Git

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd JobApplicationTracker
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root, alongside `manage.py`, with your local MySQL configuration:

```dotenv
DB_NAME=job_tracker_db
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3307
```

Replace the example username and password with your own local MySQL credentials. Never commit your `.env` file to GitHub.

Create the `job_tracker_db` database in MySQL if it does not already exist.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrator

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

Admin panel: `http://127.0.0.1:8000/admin/`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/applications/` | List applications |
| POST | `/api/applications/` | Create an application |
| GET | `/api/applications/<id>/` | Retrieve an application |
| PUT/PATCH | `/api/applications/<id>/` | Update an application |
| DELETE | `/api/applications/<id>/` | Delete an application |

API access follows the authentication and permission settings configured in Django REST Framework.

## Running Tests

Run the automated tests with:

```bash
python manage.py test applications
```

## Project Goal

This project demonstrates practical experience with Django web development, relational databases, CRUD operations, REST API development, search and filtering, and automated testing.

## Future Improvements

- User accounts and private application records
- Pagination and enhanced dashboard analytics
- Deployment with production security settings
- Improved API and form validation tests
