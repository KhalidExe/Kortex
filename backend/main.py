from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db  
from services.ai_engine import ask_kortex
import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kortex API", version="0.1.0")

@app.get("/")
def health():
    return {"status": "Kortex is Alive", "brain": "Gemini 3 Flash"}

@app.get("/ask")
def chat_with_kortex(query: str):
    """Simple AI chat endpoint."""
    response = ask_kortex(query)
    return {"query": query, "kortex_response": response}


@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = models.User(full_name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user