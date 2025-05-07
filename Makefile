# Instruction for user how to ↓ the software

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	python -m pytest -vv --cov=main --cov=calCLI
format:
	# black *.py mylib/*.py

lint
	pylint --disable=R --extension-pkg-whitelists='pydantic' main.py --ignore-patterns=test_.**py mylib/*.py

container-lint
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
	docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/logistics:latest

all: install lint test format deploy