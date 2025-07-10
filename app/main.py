from fastapi import FastAPI
from .model import MistralChat
from pydantic import BaseModel


app = FastAPI()
mistral = MistralChat()
mistral.load()  

class Query(BaseModel):
    text: str

@app.post("/ask")
async def ask_question(query: Query):
    """Endpoint for Q&A."""
    print("Received payload:", query.model_dump())  
    return {"response": mistral.generate(query.text)}

@app.get("/health")
async def health():
    return {"status": "alive"}