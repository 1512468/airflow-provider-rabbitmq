install:
	poetry install
	poetry run whippet -y

lint:
	poetry run black --check .
	poetry run bandit -r  . -x ./test
	poetry run flake8 .
	poetry run isort .