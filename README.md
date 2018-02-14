microblog-python-flex
=====================

1. Install virtual env:
    * python -m venv venv
    * virtualenv venv

2. Run virtual env:
    * venv\Scripts\activate

3. Run
    * set FLASK_APP=microblog.py
    * flask run

Used packages
-------------

* [Flask](http://flask.pocoo.org/) - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) - Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
* [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate) - SQLAlchemy database migrations for Flask applications using Alembic
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
