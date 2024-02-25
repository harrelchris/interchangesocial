#!/usr/bin/env bash

source .venv/bin/activate

python3 -m black app

python3 -m flake8 app
