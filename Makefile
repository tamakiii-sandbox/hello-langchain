.PHONY: help setup install teardown uninstall
.PHONY: build clean

export OPENAI_API_KEY ?=
export POETRY_VIRTUALENVS_CREATE ?= false
# export POETRY_VIRTUALENVS_IN_PROJECT ?= false

help:
	@cat $(firstword $(MAKEFILE_LIST))

setup: \
	.env

install: \
	/usr/local/lib/python3.11/site-packages

build: \
	dist

clean:
	rm -rf dist

uninstall:
	# rm -rf /usr/local/lib/python3.11/site-packages

teardown:
	rm -rf .env

.env:
	#echo OPENAI_API_KEY=... > $@
	@echo OPENAI_API_KEY=$(OPENAI_API_KEY) > $@

/usr/local/lib/python3.11/site-packages:
	python -m poetry install

dist:
	python3 -m poetry build
