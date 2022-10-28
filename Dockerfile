# RabbitMQ Dockerfile
#
# https://github.com/dockerfile/rabbitmq
#

# Pull base image.
FROM debian:10-slim

#Install python
RUN apt-get update

RUN apt --yes update && apt --yes upgrade
RUN apt install --yes wget

RUN apt-get install --yes python3
RUN apt-get install --yes python3-pip

COPY ./requirements.txt .