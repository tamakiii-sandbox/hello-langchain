.PHONY: help install uninstall

help:
	@cat $(firstword $(MAKEFILE_LIST))

install: \
	dependency/twitter/the-algorithm

uninstall:
	rm -rf dependency

dependency/twitter/the-algorithm: dependency/twitter
	git clone https://github.com/twitter/the-algorithm.git $@

dependency/twitter: dependency
	mkdir $@

dependency:
	mkdir $@
