# Pull base image:
FROM debian:10-slim
LABEL version="debian_10_slim"
MAINTAINER "Raphael"

RUN apt update
RUN apt upgrade --yes

RUN apt install git --yes
RUN apt install nano

# installing
# Volume Synchronisiert am ende
RUN mkdir /pv_challenge
COPY ./pv_simulator /pv_challenge/pv_simulator
COPY pv_consumer /pv_challenge/pv_simulator_service
COPY ./tests /pv_challenge/tests
COPY ./README.md /pv_challenge/README.md
COPY ./requirements.txt /pv_challenge/requirements.txt
COPY ./setup_debian.sh /pv_challenge/setup_debian.sh