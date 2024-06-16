# Python version
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as python-base

# Working directory
WORKDIR /app

# Install odbc sql server
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential \
    curl \
    apt-utils \
    gnupg2 &&\
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip


RUN apt-get update
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN exit
RUN apt-get update
RUN env ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Install Requirements
COPY ./requirements.txt .

#Copiar odbc.ini
COPY ./odbc.ini / 
RUN odbcinst -i -s -f /odbc.ini -l
RUN cat /etc/odbc.ini

RUN pip install -r requirements.txt