FROM amazonlinux:2023.0.20230322.0

RUN dnf update && \
		dnf install -y \
			which \
			man \
			make \
			less \
			findutils \
			python3.11 \
			python3.11-pip \
			&& \
		dnf clean all

RUN alternatives --install /usr/bin/python python /usr/bin/python3.11 1

RUN python -m pip install poetry

WORKDIR /usr/local/lib/tamakiii-sandbox/hello-langchain
