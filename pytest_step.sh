#!/bin/bash

hostname

echo "Shell: $SHELL"

source venv/bin/activate

pytest ./backend/tests/test_api_req.py