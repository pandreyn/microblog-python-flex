microblog-python-flex
=====================

[![Build Status](https://travis-ci.org/pandreyn/microblog-python-flex.svg?branch=master)](https://travis-ci.org/pandreyn/microblog-python-flex) [![Heroku](https://heroku-badge.herokuapp.com/?app=peaceful-woodland-31936&style=flat)](https://peaceful-woodland-31936.herokuapp.com/)



1. Install virtual env:
    * pip install pipenv
    * pipenv install

2. Run virtual env:
    * pipenv shell

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

DB Update
---------

In virtual env type:

* flask db migrate -m "description message"
* flask db upgrade

To enable debug mode in flask:

* set FLASK_DEBUG=1

Enviroment variables to be able to send mails:

* set MAIL_SERVER=smtp.googlemail.com
* set MAIL_PORT=587
* set MAIL_USE_TLS=1
* set MAIL_USERNAME=< your-gmail-username >
* set MAIL_PASSWORD=< your-gmail-password >