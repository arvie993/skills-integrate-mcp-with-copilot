# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

1. Install the dependencies (from project root):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application with Uvicorn (from `src` directory or specify module path):

   ```bash
   uvicorn app:app --reload
   ```

   By default this uses an SQLite database file `app.db` in the project root. Override with:

   ```bash
   DATABASE_URL=sqlite:///./local.db uvicorn app:app --reload
   ```

3. Open your browser:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is persisted using SQLModel (SQLAlchemy) to an SQLite database. Tables are auto-created on startup if they do not exist. A seed dataset of activities and participants is inserted only when the activities table is empty.

## Development Notes

- Unique constraint prevents duplicate signups per user/activity.
- Future enhancements (capacity enforcement, waitlists, auth) will build on this schema.
- Migrations: Alembic is listed as a dependency; migrations not yet initialized. Run `alembic init migrations` in the project root before adding structured migrations.
