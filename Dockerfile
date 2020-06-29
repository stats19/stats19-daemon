FROM python:3.7.7

ARG USERNAME
ARG PASSWORD
ARG SOURCE_BROKER_USERNAME
ARG SOURCE_BROKER_PASSWORD
ARG SOURCE_BROKER_QUEUE
ARG SOURCE_BROKER_PORT
ARG SOURCE_BROKER_HOST
ARG SOURCE_BROKER_VHOST

ENV USERNAME $USERNAME
ENV PASSWORD $PASSWORD
ENV SOURCE_BROKER_USERNAME $SOURCE_BROKER_USERNAME
ENV SOURCE_BROKER_PASSWORD $SOURCE_BROKER_PASSWORD
ENV SOURCE_BROKER_QUEUE $SOURCE_BROKER_QUEUE
ENV SOURCE_BROKER_PORT $SOURCE_BROKER_PORT
ENV SOURCE_BROKER_HOST $SOURCE_BROKER_HOST
ENV SOURCE_BROKER_VHOST $SOURCE_BROKER_VHOST

WORKDIR /opt/project

COPY . .
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock --system

CMD python -u /opt/project/run_server.py --log_level INFO --environment PRODUCTION --processname broker --force FALSE