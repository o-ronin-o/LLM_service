from fastapi import FastAPI
import requests
import json
import os

app = FastAPI()

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

# Load prompts from external files
def load_prompt(file_name):
    try:
        with open(f'prompts/{file_name}', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"# Error: Prompt file {file_name} not found"

# Load prompts at startup
SYSTEM_PROMPT = load_prompt('system_prompt.txt')
EXAMPLES = load_prompt('examples.txt')

@app.get("/chat")
def chat(prompt: str):
    # Dynamically build the prompt
    full_prompt = f"{SYSTEM_PROMPT}\n\n{EXAMPLES}\n\nUser request: {prompt}\n\nResponse:"
    
    # Optional: Log the token count for monitoring
    token_estimate = len(full_prompt.split())  # Rough estimate
    print(f"Prompt token estimate: {token_estimate}")
    
    payload = {
        "model": "gemma3:1b", 
        "prompt": full_prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.2,  
            "top_p=0": 0,
            "stream": False,
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        data = response.json()
        generated_text = data.get("response", "{}")
        
        # Try to parse the JSON response
        try:
            command_data = json.loads(generated_text)
            return {
                "response": command_data,
            }
        except json.JSONDecodeError:
            return {"error": "LLM did not return valid JSON", "raw_response": generated_text}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request to Ollama failed: {str(e)}"}