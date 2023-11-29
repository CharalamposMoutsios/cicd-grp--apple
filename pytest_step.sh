#!/bin/bash

hostname

echo "Shell: $SHELL"

python3 -m venv venv

source venv/bin/activate

pip install -r backend/requirements.txt

#echo "Running test_api_req.py..."
#pytest ./backend/tests/test_api_req.py

echo "Running other tests..."
pytest ./backend/tests/test_*
