from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kortex API",
    description="The brain behind the Student Operating System",
    version="0.1.0"
)

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = models.User(full_name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/")
def read_root():
    return {"message": "Kortex Brain is Active 🧠", "status": "Database Connected"}