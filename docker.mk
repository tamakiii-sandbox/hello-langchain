.PHONY: help build bash clean

IMAGE := tamakiii-sandbox/hello-langchain
LABEL := latest
WORK_DIR := /usr/local/lib/$(IMAGE)

help:
	@cat $(firstword $(MAKEFILE_LISt))

build: Dockerfile
	docker build -t $(IMAGE):$(LABEL) .

bash:
	docker run -it --rm \
		-v $(PWD):$(WORK_DIR) \
		-w $(WORK_DIR) \
		--env-file .env \
		$(IMAGE):$(LABEL) \
		$@

clean:
	docker image rm $(IMAGE):$(LABEL)
