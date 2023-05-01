#!/bin/bash

# Este arquivo foi criado para realizar o setup
# do ambiente de desenvovlimento

echo "Installing libpq-dev..."
sudo apt-get install libpq-dev

echo "Installing virtualenv..."
pip install virtualenv

echo "Creating virtual environment..."
python3 -m virtualenv .venv

echo "Configuring virtual environment..."
echo '' >> '.venv/bin/activate'
echo 'export PYTHONDONTWRITEBYTECODE=1' >> '.venv/bin/activate'

echo "Activating virtual environment..."
source .venv/bin/activate
echo 'Virtualenv activated!'

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Deactivating virtual environment..."
deactivate
echo 'Virtualenv deactivated.'

echo "Setup complete."
