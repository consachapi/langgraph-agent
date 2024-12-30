## Create enviroment from scratch

```
conda create -n agents python=3.12
conda activate agents
conda install -c conda-forge poetry
conda env export --from-history > environment.yml

```

## Run initialize poetry

```
poetry init

```

## Install poetry

```
poetry install

```

## Install packages

```
poetry add langgraph
poetry add langchain-openia
poetry add langchain_ollama
poetry add pydantic
poetry add langchain_core
poetry add typing_extensions
poetry add langchain_community
poetry add chromadb
poetry add "langgraph-cli[inmem]"
poetry add "fastapi[standard]"
```

## Run cli langgraph

```
langgraph dev
```

## Run cli fastapi

```
fastapi dev app/api.py
```

## Create environment from file
```
conda env create -f environment.yml
```