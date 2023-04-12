.PHONY: help setup teardown

export OPENAI_API_KEY ?=

help:
	@cat $(firstword $(MAKEFILE_LIST))

setup: \
	.env

teardown:
	rm -rf .env

.env:
	#echo OPENAI_API_KEY=... > $@
	@echo OPENAI_API_KEY=$(OPENAI_API_KEY) > $@
