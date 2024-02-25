#!/usr/bin/env bash

source .venv/bin/activate

python3 -m black --line-length 120 --exclude migrations app

python3 -m flake8 app

python3 -m bandit --recursive --quiet --exclude test,migrations app

python3 -m reorder_python_imports
