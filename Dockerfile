FROM ubuntu:latest

WORKDIR /opt/project

RUN apt install python3.7
COPY . .
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock

CMD python -u /opt/project/main/src/run_server.py --log_level DEBUG --environment PRODUCTION --processname broker --force FALSE