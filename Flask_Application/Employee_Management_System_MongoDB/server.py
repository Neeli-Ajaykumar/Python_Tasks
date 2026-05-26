from flask import Flask, request, jsonify
from pymongo import MongoClient
import certifi

app = Flask(__name__)

# ==========================================================
# MONGODB CONNECTION
# ==========================================================

MONGO_URL = "mongodb+srv://ajayneeli15_db_user:Ajay1515@ajay.cbkpfe5.mongodb.net/emp_db?retryWrites=true&w=majority"

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["emp_db"]

employees_col = db["employees"]
departments_col = db["departments"]
salary_col = db["salary"]
attendance_col = db["attendance"]

# ==========================================================
# EMPLOYEES API
# ==========================================================

@app.route('/employees', methods=['GET', 'POST'])
def employees():

    if request.method == 'POST':
        data = request.json
        employees_col.insert_one(data)
        return jsonify({"message": "Employee Added Successfully"})

    employees = list(employees_col.find({}, {"_id": 0}))
    return jsonify({"data": employees})


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    emp = employees_col.find_one({"id": id}, {"_id": 0})
    return jsonify(emp)


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json

    employees_col.update_one(
        {"id": id},
        {"$set": data}
    )

    return jsonify({"message": "Employee Updated Successfully"})


@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employees_col.delete_one({"id": id})
    return jsonify({"message": "Employee Deleted Successfully"})


# ==========================================================
# DEPARTMENTS API
# ==========================================================

@app.route('/departments', methods=['GET', 'POST'])
def departments():

    if request.method == 'POST':
        data = request.json
        departments_col.insert_one(data)
        return jsonify({"message": "Department Added Successfully"})

    departments = list(departments_col.find({}, {"_id": 0}))
    return jsonify({"data": departments})


@app.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):
    data = request.json

    departments_col.update_one(
        {"id": id},
        {"$set": data}
    )

    return jsonify({"message": "Department Updated Successfully"})


@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    departments_col.delete_one({"id": id})
    return jsonify({"message": "Department Deleted Successfully"})


# ==========================================================
# SALARY API
# ==========================================================

@app.route('/salary', methods=['GET', 'POST'])
def salary():

    if request.method == 'POST':
        data = request.json
        salary_col.insert_one(data)
        return jsonify({"message": "Salary Added Successfully"})

    salaries = list(salary_col.find({}, {"_id": 0}))
    return jsonify({"data": salaries})


@app.route('/salary/<int:employee_id>', methods=['PUT'])
def update_salary(employee_id):
    data = request.json

    salary_col.update_one(
        {"employee_id": employee_id},
        {"$set": data}
    )

    return jsonify({"message": "Salary Updated Successfully"})


@app.route('/salary/<int:employee_id>', methods=['DELETE'])
def delete_salary(employee_id):
    salary_col.delete_one({"employee_id": employee_id})
    return jsonify({"message": "Salary Deleted Successfully"})


# ==========================================================
# ATTENDANCE API
# ==========================================================

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():

    if request.method == 'POST':
        data = request.json
        attendance_col.insert_one(data)
        return jsonify({"message": "Attendance Added Successfully"})

    attendance = list(attendance_col.find({}, {"_id": 0}))
    return jsonify({"data": attendance})


@app.route('/attendance/<int:employee_id>', methods=['PUT'])
def update_attendance(employee_id):
    data = request.json

    attendance_col.update_one(
        {"employee_id": employee_id},
        {"$set": data}
    )

    return jsonify({"message": "Attendance Updated Successfully"})


@app.route('/attendance/<int:employee_id>', methods=['DELETE'])
def delete_attendance(employee_id):
    attendance_col.delete_one({"employee_id": employee_id})
    return jsonify({"message": "Attendance Deleted Successfully"})


# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True, port=5001)
