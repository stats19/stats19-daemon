FROM python:3.7.7-alpine

WORKDIR /opt/project

COPY . .
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock

CMD python -u /opt/project/main/src/run_server.py --log_level DEBUG --environment PRODUCTION --processname broker --force FALSE