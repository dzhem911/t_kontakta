 FROM python:3.8
ENV PYTHONUNBEFFERED 1
RUN mkdir /data
WORKDIR /data
ADD . /data
RUN pip install -r requirements.txt
ADD . /data
