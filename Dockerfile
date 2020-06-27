FROM python:3.7.7

WORKDIR /opt/project

COPY . .
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock --system

CMD python -u /opt/project/run_server.py --log_level DEBUG --environment PRODUCTION --processname broker --force FALSE