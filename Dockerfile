# Blockshell in a docker
FROM python:2.7-wheezy
MAINTAINER agentcobra <agentcobra@free.fr>
LABEL maintainer="agentcobra@free.fr"

RUN apt-get update
RUN apt-get install -y git screen vim

WORKDIR /opt/

RUN git clone https://github.com/agentcobra/blockshell.git
WORKDIR /opt/blockshell
RUN virtualenv venv
CMD source venv/bin/activate
RUN pip install --editable .

RUN blockshell --help

EXPOSE 5000

RUN python web.py
#CMD script /dev/null
