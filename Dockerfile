FROM python:3.7.7

WORKDIR /opt/project

COPY . .
RUN apt install git
RUN git clone https://github.com/circulosmeos/gdown.pl.git
RUN gdown.pl https://drive.google.com/file/d/1qBP6uB4MAQlLSGi6RkYheek49n5CzrRz/ tensorflow-2.2.0-cp38-cp38-linux_x86_64.whl
RUN ll
RUN pip install $WORKDIR/tensorflow-2.2.0-cp38-cp38-linux_x86_64.whl
RUN pip install pipenv
RUN apt install gcc
RUN pipenv install --skip-lock --system

CMD python -u /opt/project/run_server.py --log_level DEBUG --environment PRODUCTION --processname broker --force FALSE