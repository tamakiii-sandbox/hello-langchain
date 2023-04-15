# hello-langchain
- https://python.langchain.com/en/latest/index.html
- https://python.langchain.com/en/latest/use_cases/code/twitter-the-algorithm-analysis-deeplake.html
- https://docs.activeloop.ai/

## How to use
```sh
read -s OPENAI_API_KEY && export OPENAI_API_KEY
make setup
make -f docker.mk build
make -f docker.mk bash
```
```sh
make -B install
python main.py
```