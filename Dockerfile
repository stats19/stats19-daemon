FROM python:3.7.7

WORKDIR /opt/project

COPY . .
RUN wget "https://drive.google.com/uc?export=download&id=1qBP6uB4MAQlLSGi6RkYheek49n5CzrRz"
RUN pip install tensorflow-2.2.0-cp38-cp38-linux_x86_64.whl
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock --system

CMD python -u /opt/project/run_server.py --log_level DEBUG --environment PRODUCTION --processname broker --force FALSE