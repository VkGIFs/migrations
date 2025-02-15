poetry run flake8 --toml-config pyproject.toml
poetry run isort .
poetry run black --config pyproject.toml .

poetry run mypy src
poetry run pylint --rcfile=pyproject.toml src
