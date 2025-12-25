from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"] ,
allow_headers=["*"],
)


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

class ChatRequest(BaseModel):
	message: str


@app.post("/chat")
def chat(request: ChatRequest):
	payload = {
		"model": MODEL_NAME,
		"prompt": request.message,
		"stream": False,
	}

	try:
		response = requests.post(OLLAMA_URL, json=payload, timeout=120)
		response.raise_for_status()
		result = response.json()
	except Exception as e:
		return {"reply": f"Error contacting model: {e}"}

	# Try common response keys; fallback to stringified result
	reply = result.get("response") or result.get("text") or result.get("generated_text") or str(result)
	return {"reply": reply}