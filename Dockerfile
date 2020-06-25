FROM python:3.8.3-slim-buster

ENV PYTHONUNBUFFERED 1

RUN  mkdir /recomendation

WORKDIR /recommendation

ADD ./Main_Project_code /recommendation

COPY ./Main_Project_code /recommendation

RUN pip install -r requirements.txt

