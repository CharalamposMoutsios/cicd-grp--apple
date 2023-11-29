#!/bin/bash

#Creating enviroment

if [ ! -d "backend/venv" ]; then
    python -m venv backend/venv
fi

#Activating enviroment
source backend/venv/Scripts/activate

# Installning requirements.txt
pip install -r backend/requirements.txt

# Running Pylint
python -m pylint --fail-under=8 --recursive true --ignore=venv backend

# Running Black
black backend/

# Running tests
echo "Running tests..."
pytest ./backend/tests/test_api_endpoints.py
pytest ./backend/tests/__init__.py
pytest ./backend/tests/test_delete_url_route.py
pytest ./backend/tests/test_models.py
pytest ./backend/tests/test_ping.py
pytest ./backend/tests/test_send_ping_timeout.py
pytest ./backend/tests/test_watched_url.py
pytest ./backend/tests/test_watchurl.py

# Build docker image ping-url .
docker build -t ping-url .

# Run docker container
CONTAINER_ID=$(docker run --network=host -d ping-url)

# Docker - stop and remove container.
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID

echo "Working!"