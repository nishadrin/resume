FROM python:3.9.16

ENV DockerHOME=.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME
COPY . $DockerHOME

RUN pip install --upgrade pip && pip install -r requirements.txt
