.PHONY: help setup install teardown uninstall

export OPENAI_API_KEY ?=
export POETRY_VIRTUALENVS_CREATE ?= false
# export POETRY_VIRTUALENVS_IN_PROJECT ?= true

help:
	@cat $(firstword $(MAKEFILE_LIST))

setup: \
	.env

install: \
	.venv

uninstall:
	rm -rf .venv

teardown:
	rm -rf .env

.env:
	#echo OPENAI_API_KEY=... > $@
	@echo OPENAI_API_KEY=$(OPENAI_API_KEY) > $@

.venv:
	python -m poetry install --no-root
