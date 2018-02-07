FROM python:2-alpine
# Copyright (C) 2018 Mateusz Pawlowski <mateusz@generik.co.uk>

ADD . /app
WORKDIR /app

RUN pip install --editable .

CMD blockshell init

#vim: syntax=Dockerfile
