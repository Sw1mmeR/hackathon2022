FROM python:latest

ADD /scripts/server.py /server/

RUN pip install --upgrade pip && \
    pip install pymysql

WORKDIR /server/