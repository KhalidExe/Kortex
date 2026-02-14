from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    course_id: int

class Task(TaskBase):
    id: int
    is_completed: bool
    
    class Config:
        from_attributes = True

# --- Course Schemas ---
class CourseBase(BaseModel):
    title: str
    code: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    owner_id: int

class Course(CourseBase):
    id: int
    file_path: Optional[str] = None
    tasks: List[Task] = []
    
    class Config:
        from_attributes = True

# --- User Schemas ---
class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    courses: List[Course] = []
    
    class Config:
        from_attributes = True