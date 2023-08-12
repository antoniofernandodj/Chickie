FROM python:3.11

WORKDIR /usr/app/flow

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY ./requirements/api.txt requirements/api.txt

RUN pip install --no-cache-dir -r ./requirements/api.txt

COPY config/.secrets.toml ./config/.secrets.toml
COPY config/settings.toml ./config/settings.toml

COPY . .