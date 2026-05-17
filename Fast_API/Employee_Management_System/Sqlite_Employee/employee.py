# ============================================================
# 📝 FastAPI Employee Management System
# SQLite Version (List Based)
# ============================================================

# ------------------------------------------------------------
# 📦 Import Libraries
# ------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ------------------------------------------------------------
# 🚀 Create FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🧾 Employee Schema
# ------------------------------------------------------------
class Employee(BaseModel):

    employee_id: int

    name: str

    department: str

    salary: float

    attendance: bool = False

# ------------------------------------------------------------
# 🗂️ Temporary Database (List)
# ------------------------------------------------------------
employees = []

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "FastAPI + Employee Management System(SQLite) 🚀"
    }

# ------------------------------------------------------------
# ✅ ADD EMPLOYEE
# ------------------------------------------------------------
@app.post("/employees")
def add_employee(employee: Employee):

    # Check duplicate employee ID
    for emp in employees:

        if emp.employee_id == employee.employee_id:

            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )

    employees.append(employee)

    return {

        "message": "Employee added successfully",

        "data": employee
    }

# ------------------------------------------------------------
# ✅ GET ALL EMPLOYEES
# ------------------------------------------------------------
@app.get("/employees")
def get_all_employees():

    return {

        "count": len(employees),

        "data": employees
    }

# ------------------------------------------------------------
# ✅ GET SINGLE EMPLOYEE
# ------------------------------------------------------------
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:

        if employee.employee_id == employee_id:

            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# ------------------------------------------------------------
# ✅ UPDATE EMPLOYEE
# ------------------------------------------------------------
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: Employee
):

    for index, employee in enumerate(employees):

        if employee.employee_id == employee_id:

            employees[index] = updated_employee

            return {

                "message": "Employee updated successfully",

                "data": updated_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# ------------------------------------------------------------
# ✅ DELETE EMPLOYEE
# ------------------------------------------------------------
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, employee in enumerate(employees):

        if employee.employee_id == employee_id:

            deleted = employees.pop(index)

            return {

                "message": "Employee deleted successfully",

                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# ------------------------------------------------------------
# ✅ DELETE ALL EMPLOYEES
# ------------------------------------------------------------
@app.delete("/employees/")
def delete_all_employees():

    employees.clear()

    return {
        "message": "All employees deleted successfully"
    }

# ------------------------------------------------------------
# ✅ GET EMPLOYEES BY DEPARTMENT
# ------------------------------------------------------------
@app.get("/employees/department/{department_name}")
def get_department_employees(
    department_name: str
):

    data = []

    for employee in employees:

        if employee.department.lower() == department_name.lower():

            data.append(employee)

    return {

        "count": len(data),

        "data": data
    }

# ------------------------------------------------------------
# ✅ MARK ATTENDANCE
# ------------------------------------------------------------
@app.post("/attendance/{employee_id}")
def mark_attendance(employee_id: int):

    for employee in employees:

        if employee.employee_id == employee_id:

            employee.attendance = True

            return {
                "message": "Attendance marked successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# ------------------------------------------------------------
# ✅ GET ATTENDANCE RECORDS
# ------------------------------------------------------------
@app.get("/attendance")
def get_attendance():

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
# ✅ GET HIGH SALARY EMPLOYEES
# ------------------------------------------------------------
@app.get("/high-salary-employees")
def high_salary_employees():

    data = []

    for employee in employees:

        if employee.salary > 50000:

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

    data = []

    for employee in employees:

        if name.lower() in employee.name.lower():

            data.append({

                "employee_id": employee.employee_id,

                "name": employee.name,

                "department": employee.department
            })

    return {

        "count": len(data),

        "data": data
    }
