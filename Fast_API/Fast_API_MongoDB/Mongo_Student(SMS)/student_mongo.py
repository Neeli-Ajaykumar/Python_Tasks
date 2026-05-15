# ============================================================
# 📝 FastAPI Student Management System
# MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    FloatField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://ajayneeli15_db_user:Ajay1515@ajay.cbkpfe5.mongodb.net/student_db?retryWrites=true&w=majority"

connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 MongoDB Model
# ------------------------------------------------------------
class StudentDB(Document):

    # Custom Student ID
    student_id = IntField(required=True, unique=True)

    name = StringField(required=True)

    age = IntField(required=True)

    course = StringField(required=True)

    marks = FloatField(required=True)

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):

    student_id: int

    name: str

    age: int

    course: str

    marks: float

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "FastAPI + MongoDB Atlas 🚀"
    }

# ------------------------------------------------------------
# ✅ ADD STUDENT
# ------------------------------------------------------------
@app.post("/students")
def add_student(student: Student):

    # Check duplicate student ID
    existing = StudentDB.objects(
        student_id=student.student_id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    # Create new student
    new_student = StudentDB(

        student_id=student.student_id,

        name=student.name,

        age=student.age,

        course=student.course,

        marks=student.marks
    )

    new_student.save()

    return {
        "message": "Student added successfully",
        "data": {
            "student_id": new_student.student_id,
            "name": new_student.name,
            "age": new_student.age,
            "course": new_student.course,
            "marks": new_student.marks
        }
    }

# ------------------------------------------------------------
# ✅ GET ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_all_students():

    students = StudentDB.objects()

    data = []

    for student in students:

        data.append({

            "student_id": student.student_id,

            "name": student.name,

            "age": student.age,

            "course": student.course,

            "marks": student.marks
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ GET SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {

        "student_id": student.student_id,

        "name": student.name,

        "age": student.age,

        "course": student.course,

        "marks": student.marks
    }

# ------------------------------------------------------------
# ✅ UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update values
    student.name = updated.name

    student.age = updated.age

    student.course = updated.course

    student.marks = updated.marks

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }
