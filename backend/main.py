from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os

# Internal imports
from database import engine, get_db
from services.ai_engine import ask_kortex, extract_text_from_pdf, ask_kortex_with_context
import models
import schemas

# Initialize Database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kortex API", version="0.1.0")

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# --- Health Check ---
@app.get("/")
def health():
    return {"status": "Kortex is Alive", "brain": "Gemini 3 Flash"}

# --- Context-Aware Chat (NEW) ---
@app.get("/courses/{course_id}/ask")
def ask_about_course(course_id: int, query: str, db: Session = Depends(get_db)):
    """Extracts PDF text and asks Gemini based on the course material."""
    # 1. Fetch course from DB
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course or not course.file_path:
        raise HTTPException(status_code=404, detail="Course material not found")

    # 2. Extract text from the saved PDF
    context = extract_text_from_pdf(course.file_path)
    
    # 3. Get AI response using the extracted context
    response = ask_kortex_with_context(context, query)
    
    return {
        "course": course.title,
        "query": query,
        "kortex_response": response
    }

# --- General AI Chat ---
@app.get("/ask")
def chat_with_kortex(query: str):
    response = ask_kortex(query)
    return {"query": query, "kortex_response": response}

# --- File Upload ---
@app.post("/courses/{course_id}/upload")
async def upload_course_file(course_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
        
    course.file_path = file_path
    db.commit()
    
    return {"status": "File uploaded", "course_id": course_id}

# --- Course & User Management ---
@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/", response_model=List[schemas.Course])
def read_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()