# Django models relationships 2025 2026

A Django project with 5 models.

## Tech stack

- Python 3
- Django
- Database: SQLite

## Project structure

- `django_models_relationships/`: project settings and root URLs
- `course_enrollment/`: Django app
- Tests: `course_enrollment/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Course` | `course_enrollment` | id, title, description |
| `Student` | `course_enrollment` | id, name, email |
| `Profile` | `course_enrollment` | id, phone, portfolio_url |
| `Tutor` | `course_enrollment` | id, name, email, bio |
| `Enrollment` | `course_enrollment` | — |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
pip install pipenv
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
