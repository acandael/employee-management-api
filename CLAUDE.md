# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`employeemanagement` is a Django 5.2 project scaffolded with `django-admin startproject`. It is currently a bare skeleton — no apps exist yet beyond Django's built-in contrib apps, and `urls.py` only routes `/admin/`. Building out employee-management apps is the expected work.

## Environment

- A virtualenv lives in `.venv/` (Python 3.13). Activate with `source .venv/bin/activate` or call binaries directly via `.venv/bin/python`.
- **Django is not yet installed in `.venv`.** Before running anything: `.venv/bin/pip install django` (the scaffold targets 5.2.x). There is no `requirements.txt` — create one (`pip freeze > requirements.txt`) when dependencies are added.

## Commands

Run from the project root (where `manage.py` lives):

```bash
python manage.py runserver          # start dev server at http://127.0.0.1:8000
python manage.py startapp <name>    # create a new app
python manage.py makemigrations     # generate migrations from model changes
python manage.py migrate            # apply migrations (also bootstraps db.sqlite3)
python manage.py createsuperuser    # create an admin login for /admin/
python manage.py test               # run the full test suite
python manage.py test <app>.tests.<Class>.<method>   # run a single test
python manage.py shell              # interactive shell with Django loaded
```

## Architecture notes

- Settings: `employeemanagement/settings.py`. `DEBUG=True`, SQLite (`db.sqlite3`), and the `SECRET_KEY` is the insecure dev default — none of these are production-ready.
- New apps must be added to `INSTALLED_APPS` in settings, and their URLs wired into `employeemanagement/urls.py` (typically via `include()`).
- Templates use `APP_DIRS=True` with no project-level `DIRS`, so templates belong inside each app's `templates/` directory.
