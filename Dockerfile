FROM python:3.6-onbuild

LABEL maintainer "Andrey Petkevich <pandreyn@gmail.com>"

# ENV FLASK_APP=microblog.py
# ENV DATABASE_URL=postgresql://postgres:pgpwd@b98bc2631469:5432

# CMD bash -c "flask db upgrade && flask run --host=0.0.0.0"
# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade