FROM amazonlinux:2023.0.20230322.0

RUN dnf update && \
		dnf install -y \
			which \
			man \
			make \
			less \
			python3-pip \
			&& \
		dnf clean all

RUN alternatives --install /usr/bin/python python /usr/bin/python3.9 1
