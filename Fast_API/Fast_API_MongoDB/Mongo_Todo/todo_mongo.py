# ============================================================
# 📝 FastAPI TODO App - MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    BooleanField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://ajayneeli15_db_user:Ajay1515@ajay.cbkpfe5.mongodb.net/todo_db?retryWrites=true&w=majority"

connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 MongoDB Model
# ------------------------------------------------------------
class TodoDB(Document):

    # Custom ID field
    todo_id = IntField(required=True, unique=True)

    title = StringField(required=True)

    completed = BooleanField(default=False)

    meta = {
        "collection": "todos"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Todo(BaseModel):

    todo_id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "FastAPI + MongoDB Atlas 🚀"
    }

# ------------------------------------------------------------
# ✅ CREATE TODO
# ------------------------------------------------------------
@app.post("/todos")
def create_todo(todo: Todo):

    # Check duplicate
    existing = TodoDB.objects(
        todo_id=todo.todo_id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Todo ID already exists"
        )

    # Create new todo
    new_todo = TodoDB(

        todo_id=todo.todo_id,

        title=todo.title,

        completed=todo.completed
    )

    new_todo.save()

    return {
        "message": "Todo created successfully",
        "data": {
            "todo_id": new_todo.todo_id,
            "title": new_todo.title,
            "completed": new_todo.completed
        }
    }

# ------------------------------------------------------------
# ✅ READ ALL TODOS
# ------------------------------------------------------------
@app.get("/todos")
def get_all_todos():

    todos = TodoDB.objects()

    data = []

    for todo in todos:

        data.append({

            "todo_id": todo.todo_id,

            "title": todo.title,

            "completed": todo.completed
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ READ SINGLE TODO
# ------------------------------------------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    todo = TodoDB.objects(
        todo_id=todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {

        "todo_id": todo.todo_id,

        "title": todo.title,

        "completed": todo.completed
    }

# ------------------------------------------------------------
# ✅ UPDATE TODO
# ------------------------------------------------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: Todo):

    todo = TodoDB.objects(
        todo_id=todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = updated.title

    todo.completed = updated.completed

    todo.save()

    return {
        "message": "Todo updated successfully"
    }

# ------------------------------------------------------------
# ✅ DELETE TODO
# ------------------------------------------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    todo = TodoDB.objects(
        todo_id=todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.delete()

    return {
        "message": "Todo deleted successfully"
    }
