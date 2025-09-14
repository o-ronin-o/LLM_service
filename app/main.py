from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + Ollama!"}

@app.get("/chat")
def chat(prompt: str):
    payload = {"model": "gemma:1b", "prompt": prompt}
    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    output = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            output += data
    return {"response": output}
