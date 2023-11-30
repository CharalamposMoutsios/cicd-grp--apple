#!/bin/bash

# Debugging
hostname
echo "Shell: $SHELL"

# Running get_container_ip.sh to get the CONTAINER_IP variable
# used by test_api_req.py
source ./get_container_ip.sh

# Creating venv
python3 -m venv venv

# Activating venv
source venv/bin/activate

# Installing requirements.txt
pip install -r backend/requirements.txt

echo "Running tests..."
pytest ./backend/tests/test_api_endpoints.py
pytest ./backend/tests/test_integration.py
pytest ./backend/tests/models.py
pytest ./backend/tests/test_ping.py
pytest ./backend/tests/test_watchurl.py

echo "Running test_api_req.py..."
pytest ./backend/tests/test_api_req.py

