# ============================================================
# 📝 FastAPI Employee Management System
# MongoDB Atlas + MongoEngine
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    FloatField,
    BooleanField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://ajayneeli15_db_user:Ajay1515@ajay.cbkpfe5.mongodb.net/employee_db?retryWrites=true&w=majority"

connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 MongoDB Model
# ------------------------------------------------------------
class EmployeeDB(Document):

    # Custom Employee ID
    employee_id = IntField(
        required=True,
        unique=True
    )

    name = StringField(
        required=True
    )

    department = StringField(
        required=True
    )

    salary = FloatField(
        required=True
    )

    attendance = BooleanField(
        default=False
    )

    meta = {
        "collection": "employees"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Employee(BaseModel):

    employee_id: int

    name: str

    department: str

    salary: float

    attendance: bool = False

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "FastAPI + MongoDB Employee Management System(MongoDB Atlas) 🚀"
    }

# ------------------------------------------------------------
# ✅ ADD EMPLOYEE
# ------------------------------------------------------------
@app.post("/employees")
def add_employee(employee: Employee):

    # Check duplicate employee ID
    existing = EmployeeDB.objects(
        employee_id=employee.employee_id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    # Create employee
    new_employee = EmployeeDB(

        employee_id=employee.employee_id,

        name=employee.name,

        department=employee.department,

        salary=employee.salary,

        attendance=employee.attendance
    )

    new_employee.save()

    return {
        "message": "Employee added successfully",

        "data": {

            "employee_id": new_employee.employee_id,

            "name": new_employee.name,

            "department": new_employee.department,

            "salary": new_employee.salary,

            "attendance": new_employee.attendance
        }
    }

# ------------------------------------------------------------
# ✅ GET ALL EMPLOYEES
# ------------------------------------------------------------
@app.get("/employees")
def get_all_employees():

    employees = EmployeeDB.objects()

    data = []

    for employee in employees:

        data.append({

            "employee_id": employee.employee_id,

            "name": employee.name,

            "department": employee.department,

            "salary": employee.salary,

            "attendance": employee.attendance
        })

    return {

        "count": len(data),

        "data": data
    }

# ------------------------------------------------------------
# ✅ GET SINGLE EMPLOYEE
# ------------------------------------------------------------
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    employee = EmployeeDB.objects(
        employee_id=employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {

        "employee_id": employee.employee_id,

        "name": employee.name,

        "department": employee.department,

        "salary": employee.salary,

        "attendance": employee.attendance
    }

# ------------------------------------------------------------
# ✅ UPDATE EMPLOYEE
# ------------------------------------------------------------
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated: Employee
):

    employee = EmployeeDB.objects(
        employee_id=employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # Update values
    employee.name = updated.name

    employee.department = updated.department

    employee.salary = updated.salary

    employee.attendance = updated.attendance

    employee.save()

    return {
        "message": "Employee updated successfully"
    }

# ------------------------------------------------------------
# ✅ DELETE EMPLOYEE
# ------------------------------------------------------------
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    employee = EmployeeDB.objects(
        employee_id=employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.delete()

    return {
        "message": "Employee deleted successfully"
    }

# ------------------------------------------------------------
# ✅ GET EMPLOYEES BY DEPARTMENT
# ------------------------------------------------------------
@app.get("/employees/department/{department_name}")
def get_department_employees(
    department_name: str
):

    employees = EmployeeDB.objects(
        department=department_name
    )

    data = []

    for employee in employees:

        data.append({

            "employee_id": employee.employee_id,

            "name": employee.name,

            "department": employee.department,

            "salary": employee.salary
        })

    return {

        "count": len(data),

        "data": data
    }

# ------------------------------------------------------------
# ✅ MARK ATTENDANCE
# ------------------------------------------------------------
@app.post("/attendance/{employee_id}")
def mark_attendance(employee_id: int):

    employee = EmployeeDB.objects(
        employee_id=employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.attendance = True

    employee.save()

    return {
        "message": "Attendance marked successfully"
    }

# ------------------------------------------------------------
# ✅ GET ATTENDANCE RECORDS
# ------------------------------------------------------------
@app.get("/attendance")
def get_attendance():

    employees = EmployeeDB.objects()

    data = []

    for employee in employees:

        data.append({

            "employee_id": employee.employee_id,

            "attendance": employee.attendance
        })

    return {

        "count": len(data),

        "data": data
    }

# ------------------------------------------------------------
# ✅ HIGH SALARY EMPLOYEES
# ------------------------------------------------------------
@app.get("/high-salary-employees")
def high_salary_employees():

    employees = EmployeeDB.objects(
        salary__gt=50000
    )

    data = []

    for employee in employees:

        data.append({

            "employee_id": employee.employee_id,

            "name": employee.name,

            "salary": employee.salary
        })

    return {

        "count": len(data),

        "data": data
    }

# ------------------------------------------------------------
# ✅ SEARCH EMPLOYEE BY NAME
# ------------------------------------------------------------
@app.get("/search-employee/{name}")
def search_employee(name: str):

    employees = EmployeeDB.objects(
        name__icontains=name
    )

    data = []

    for employee in employees:

        data.append({

            "employee_id": employee.employee_id,

            "name": employee.name,

            "department": employee.department
        })

    return {

        "count": len(data),

        "data": data
    }
