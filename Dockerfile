FROM node:16

ENV PYTHONUNBUFFERED=0

COPY . /app

WORKDIR /app/kafka-nodejs-getting-started

RUN npm i node-rdkafka
