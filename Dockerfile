FROM python:3
RUN apt -y update && apt -y upgrade
RUN apt -y install postgresql-client
COPY ./back/requirements.txt /tmp/
RUN pip install -U -r /tmp/requirements.txt