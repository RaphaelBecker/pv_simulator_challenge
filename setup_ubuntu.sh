#!/bin/bash
DIR="venv"
if [ -d "$DIR" ]; then
  echo "Virtual Environment already exists: ${DIR}..."
else
  echo  "Installing python 3.9.7..."
  apt install python3.9
  apt install python3.9-venv
  echo "Creating virtual environment..."
  python3.9 -m venv venv
  echo "Activate virtual environment ${DIR}..."
  source venv/bin/activate
  python3.9 --version
  echo "Upgrade pip..."
  python3.9 -m pip install --upgrade pip
  echo "Installing requirements.txt..."
  pip3 install -r requirements.txt
fi
#chmod u+x app.py
#./app.py
exit 1