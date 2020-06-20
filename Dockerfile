FROM python:3

ENV PYTHONUNBUFFERED 1

RUN  mkdir /recomendation

WORKDIR /recommendation

ADD ./integration_trial /recommendation

COPY ./integration_trial /recommendation

RUN pip install -r requirements.txt

