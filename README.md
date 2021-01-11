# Talent-Planet Backend
This is the initial backend for Talent-Planet

Presently, there is an event app that can be used to manage events via the admin panel

# Set ups for dev
Steps:

1. Clone/pull/download this repository
2. Create a virtualenv with `python -m venv env`
3. Activate virtual environment `source env/bin/activate`
4. Install dependencies with `pip install -r requirements.txt`

### Create superuser
`python manage.py createsuper`

### Collect Static
`python manage.py collectstatic`

### Finally runserver
`python manage.py runserver`
