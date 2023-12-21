#!/usr/bin/make -f

.ONESHELL:

-include .env

SHELL = /bin/bash

init:
	pipenv install -d

test:
	pipenv run pytest tests

coverage:
	pipenv run pytest --cov=redfish_client --cov-report=html tests
	xdg-open htmlcov/index.html

lint:
	pipenv run ruff redfish_client

publish:
	rm -f dist/*

	pipenv --rm
	rm Pipfile.lock
	pipenv --python 3.11
	pipenv install --dev
	pipenv run python setup.py sdist bdist_wheel

	pipenv run python -m twine upload -r metify-internal dist/*
