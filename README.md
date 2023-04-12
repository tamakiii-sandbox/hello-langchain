# hello-langchain

## How to use
```sh
read -s OPENAI_API_KEY && export OPENAI_API_KEY
make setup
make -f docker.mk build
make -f docker.mk bash
```