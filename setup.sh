#!/bin/bash
DIR="venv"
if [ -d "$DIR" ]; then
  echo "Virtual Environment already exists: ${DIR}..."
else
  echo  "Installing python 3.9.7..."
  apt install wget software-properties-common build-essential libnss3-dev zlib1g-dev libgdbm-dev libncurses5-dev   libssl-dev libffi-dev libreadline-dev libsqlite3-dev libbz2-dev
  wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
  tar xvf Python-3.9.7.tgz
  # shellcheck disable=SC2164
  cd Python-3.9.7/
  ./configure --enable-optimizations
  make altinstall
  python3.9 --version
  python3.9 -m pip install --upgrade pip
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