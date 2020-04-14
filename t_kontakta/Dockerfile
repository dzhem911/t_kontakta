 FROM python:3.8
ENV PYTHONUNBEFFERED 1
RUN mkdir /data
WORKDIR /data
ADD . /data
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
ADD . /data
