from fastapi import FastAPI
from app.agent import graph

app = FastAPI()

@app.get("/")
def agent():
    result = graph.invoke({"question": "Who is the owner of bella vista?"})
    return result["llm_output"]
