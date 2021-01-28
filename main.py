from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


fakeDb = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"greetings": "Welcome to Digital Rama"}

@app.get("/all_courses")
def get_courses():
    return fakeDb


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = course_id - 1
    return fakeDb[course]

@app.post("/courses")
def add_course(course: Course):
    fakeDb.append(course.dict())
    return fakeDb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakeDb.pop(course_id-1)
    return {"task": "deletion successful"}
