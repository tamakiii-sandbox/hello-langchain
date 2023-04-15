.PHONY: help login

export DEEPLAKE_API_KEY ?=

help:
	@cat $(firstword $(MAKEFILE_LIST))

login:
	#activeloop login -t ...
	@activeloop login -t $(DEEPLAKE_API_KEY)
