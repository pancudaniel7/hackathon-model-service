FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y firefox

RUN apt install -y wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv geckodriver /usr/bin/
RUN rm geckodriver*

WORKDIR /app

RUN apt install -y python3-pip

RUN pip3 install pipenv

ENV NG C.UTF-8
ENV LC_ALL C.UTF-8

COPY Pipfile /app/Pipfile
RUN pipenv install Pipfile


COPY ./src/ /app/src/

ENV FLASK_APP src/xbot/app.py

CMD pipenv run flask run --host=0.0.0.0