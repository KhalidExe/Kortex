from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os

# Internal imports
from database import engine, get_db
from services.ai_engine import ask_kortex
import models
import schemas

# Initialize Database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kortex API", version="0.1.0")

# Ensure upload directory exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# --- Health Check ---
@app.get("/")
def health():
    return {"status": "Kortex is Alive", "brain": "Gemini 3 Flash"}

# --- AI Chat ---
@app.get("/ask")
def chat_with_kortex(query: str):
    """General AI chat endpoint."""
    response = ask_kortex(query)
    return {"query": query, "kortex_response": response}

# --- User Management ---
@app.post("/users/", response_model=schemas.User)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = models.User(full_name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# --- Course Management ---
@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    """Create a new course entry."""
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/", response_model=List[schemas.Course])
def read_courses(db: Session = Depends(get_db)):
    """Retrieve all courses."""
    return db.query(models.Course).all()

# --- File Upload ---
@app.post("/courses/{course_id}/upload")
async def upload_course_file(course_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload PDF/PPTX for a specific course and save path to DB."""
    # 1. Define file path
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # 2. Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 3. Update Course in DB
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
        
    course.file_path = file_path
    db.commit()
    
    return {
        "filename": file.filename,
        "course_id": course_id,
        "status": "File uploaded and linked successfully"
    }