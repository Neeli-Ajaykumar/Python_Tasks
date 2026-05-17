# ============================================================
# 📝 FastAPI Employee Management System - MySQL Version
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/employee_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Employee Table Model
# ------------------------------------------------------------
class EmployeeDB(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    department = Column(String(255))
    salary = Column(Float)
    attendance = Column(Boolean, default=False)

# Create Table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float
    attendance: bool = False

    class Config:
        orm_mode = True

# ------------------------------------------------------------
# 🔌 Database Dependency
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home API
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI + Employee Management System(MySQL) 🚀"}

# ------------------------------------------------------------
# ✅ ADD EMPLOYEE
# POST /employees
# ------------------------------------------------------------
@app.post("/employees")
def add_employee(employee: Employee, db: Session = Depends(get_db)):

    existing_employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee.id
    ).first()

    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    new_employee = EmployeeDB(
        id=employee.id,
        name=employee.name,
        department=employee.department,
        salary=employee.salary,
        attendance=employee.attendance
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "Employee Added Successfully",
        "data": new_employee
    }

# ------------------------------------------------------------
# ✅ GET ALL EMPLOYEES
# GET /employees
# ------------------------------------------------------------
@app.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):

    employees = db.query(EmployeeDB).all()

    return {
        "count": len(employees),
        "data": employees
    }

# ------------------------------------------------------------
# ✅ GET EMPLOYEE BY ID
# GET /employees/{id}
# ------------------------------------------------------------
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee

# ------------------------------------------------------------
# ✅ UPDATE EMPLOYEE
# PUT /employees/{id}
# ------------------------------------------------------------
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: Employee,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    employee.name = updated_employee.name
    employee.department = updated_employee.department
    employee.salary = updated_employee.salary
    employee.attendance = updated_employee.attendance

    db.commit()
    db.refresh(employee)

    return {
        "message": "Employee Updated Successfully",
        "data": employee
    }

# ------------------------------------------------------------
# ✅ DELETE EMPLOYEE
# DELETE /employees/{id}
# ------------------------------------------------------------
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee Deleted Successfully"
    }

# ------------------------------------------------------------
# ✅ GET EMPLOYEES BY DEPARTMENT
# GET /employees/department/{name}
# ------------------------------------------------------------
@app.get("/employees/department/{department_name}")
def get_department_employees(
    department_name: str,
    db: Session = Depends(get_db)
):

    employees = db.query(EmployeeDB).filter(
        EmployeeDB.department == department_name
    ).all()

    return {
        "count": len(employees),
        "data": employees
    }

# ------------------------------------------------------------
# ✅ MARK ATTENDANCE
# POST /attendance/{id}
# ------------------------------------------------------------
@app.post("/attendance/{employee_id}")
def mark_attendance(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    employee.attendance = True

    db.commit()
    db.refresh(employee)

    return {
        "message": "Attendance Marked Successfully",
        "data": employee
    }

"""# ------------------------------------------------------------
# ✅ GET ATTENDANCE RECORDS
# GET /attendance
# ------------------------------------------------------------
@app.get("/attendance")
def get_attendance_records(db: Session = Depends(get_db)):

    #employees = db.query(EmployeeDB).filter(EmployeeDB.attendance == True).all()
    employees = db.query(EmployeeDB.id, EmployeeDB.attendance).all()

    return {
        "count": len(employees),
        "data": employees
    }"""
# ------------------------------------------------------------
# ✅ GET ATTENDANCE RECORDS
# GET /attendance
# ------------------------------------------------------------
@app.get("/attendance")
def get_attendance_records(db: Session = Depends(get_db)):

    employees = db.query(
        EmployeeDB.id,
        EmployeeDB.attendance
    ).all()

    result = []

    for emp in employees:
        result.append({
            "id": emp.id,
            "attendance": emp.attendance
        })

    return {
        "count": len(result),
        "data": result
    }

# ------------------------------------------------------------
# ✅ GET HIGH SALARY EMPLOYEES
# GET /high-salary-employees
# ------------------------------------------------------------
@app.get("/high-salary-employees")
def high_salary_employees(db: Session = Depends(get_db)):

    employees = db.query(EmployeeDB).filter(
        EmployeeDB.salary > 50000
    ).all()

    return {
        "count": len(employees),
        "data": employees
    }

# ------------------------------------------------------------
# ✅ SEARCH EMPLOYEE BY NAME
# GET /search-employee/{name}
# ------------------------------------------------------------
@app.get("/search-employee/{name}")
def search_employee(name: str, db: Session = Depends(get_db)):

    employees = db.query(EmployeeDB).filter(
        EmployeeDB.name.ilike(f"%{name}%")
    ).all()

    return {
        "count": len(employees),
        "data": employees
    }
