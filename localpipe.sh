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

# Adding run pytest
python -m pytest backend/tests/

# Build docker image ping-url .
docker build -t ping-url .

# Run docker container
CONTAINER_ID=$(docker run --network=host -d ping-url)

# Docker - stop and remove container.
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID

echo "Working!"
