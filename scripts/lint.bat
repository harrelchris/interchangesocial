call .venv\Scripts\activate

python -m black --line-length 120 --exclude migrations app

python -m flake8 app

python -m bandit --recursive --quiet --exclude test,migrations app

python -m reorder_python_imports

python -m pyupgrade
