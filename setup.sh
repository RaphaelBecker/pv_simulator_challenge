#!/bin/bash
DIR="venv"
if [ -d "$DIR" ]; then
  echo "Activate virtual environment ${DIR}..."
  source venv/bin/activate
else
  echo "Setup dependencies..."
  cd ..
  echo  "1. Installing python 3.9.7..."
  apt install wget software-properties-common build-essential libnss3-dev zlib1g-dev libgdbm-dev libncurses5-dev   libssl-dev libffi-dev libreadline-dev libsqlite3-dev libbz2-dev
  wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
  tar xvf Python-3.9.7.tgz
  # shellcheck disable=SC2164
  cd Python-3.9.7/
  ./configure --enable-optimizations
  make altinstall
  python3.9 --version
  python3.9 -m pip install --upgrade pip
  # shellcheck disable=SC2103
  cd ..
  echo "2. Setup RabbitMQ..."
  mkdir rabbitMQ
  # shellcheck disable=SC2164
  cd rabbitMQ
  wget https://packages.erlang-solutions.com/erlang/debian/pool/esl-erlang_23.1.5-1~debian~stretch_amd64.deb
  dpkg -i esl-erlang_23.1.5-1~debian~stretch_amd64.deb
  apt update
  apt install erlang erlang-nox
  apt --fix-broken install
  add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main'
  apt update
  apt install rabbitmq-server
  systemctl enable rabbitmq-server
  systemctl start rabbitmq-server
  cd ..
  # shellcheck disable=SC2164
  cd pv_simulator_challenge
  echo "Creating virtual environment..."
  python3.9 -m venv venv
  echo "Activate virtual environment ${DIR}..."
  source venv/bin/activate
  echo "Upgrade pip..."
  python3.9 -m pip install --upgrade pip
  echo "Installing requirements.txt..."
  pip3 install -r requirements.txt
fi
#chmod u+x app.py
#./app.py
exit 1