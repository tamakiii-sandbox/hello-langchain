.PHONY: help setup install teardown uninstall

export OPENAI_API_KEY ?=
export POETRY_VIRTUALENVS_CREATE ?= false
# export POETRY_VIRTUALENVS_IN_PROJECT ?= true

help:
	@cat $(firstword $(MAKEFILE_LIST))

setup: \
	.env

install: \
	/usr/local/lib/python3.11/site-packages

uninstall:
	# rm -rf /usr/local/lib/python3.11/site-packages

teardown:
	rm -rf .env

.env:
	#echo OPENAI_API_KEY=... > $@
	@echo OPENAI_API_KEY=$(OPENAI_API_KEY) > $@

/usr/local/lib/python3.11/site-packages:
	python -m poetry install --no-root
