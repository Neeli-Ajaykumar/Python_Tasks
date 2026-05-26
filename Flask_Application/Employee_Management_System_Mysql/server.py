from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# ==========================================================
# MYSQL CONNECTION
# ==========================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_db"
)

cursor = db.cursor(dictionary=True)

# ==========================================================
# EMPLOYEE API
# ==========================================================

@app.route('/employees', methods=['GET', 'POST'])
def employees():

    # ======================================================
    # ADD EMPLOYEE
    # ======================================================

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO employees
        (
        id,
        name,
        age,
        gender,
        email,
        phone,
        designation
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data['id'],
            data['name'],
            data['age'],
            data['gender'],
            data['email'],
            data['phone'],
            data['designation']
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({
            "message": "Employee Added Successfully"
        })

    # ======================================================
    # GET ALL EMPLOYEES
    # ======================================================

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    return jsonify({
        "data": employees
    })


# ==========================================================
# GET SINGLE EMPLOYEE
# ==========================================================

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (id,)
    )

    employee = cursor.fetchone()

    return jsonify(employee)


# ==========================================================
# UPDATE EMPLOYEE
# ==========================================================

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):

    data = request.json

    query = """
    UPDATE employees
    SET
    name=%s,
    age=%s,
    gender=%s,
    email=%s,
    phone=%s,
    designation=%s
    WHERE id=%s
    """

    values = (
        data['name'],
        data['age'],
        data['gender'],
        data['email'],
        data['phone'],
        data['designation'],
        id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({
        "message": "Employee Updated Successfully"
    })


# ==========================================================
# DELETE EMPLOYEE
# ==========================================================

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):

    # DELETE ATTENDANCE FIRST
    cursor.execute(
        "DELETE FROM attendance WHERE employee_id=%s",
        (id,)
    )

    # DELETE SALARY FIRST
    cursor.execute(
        "DELETE FROM salaries WHERE employee_id=%s",
        (id,)
    )

    # DELETE EMPLOYEE
    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    db.commit()

    return jsonify({
        "message": "Employee Deleted Successfully"
    })


# ==========================================================
# DEPARTMENT API
# ==========================================================

@app.route('/departments', methods=['GET', 'POST'])
def departments():

    # ======================================================
    # ADD DEPARTMENT
    # ======================================================

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO departments
        (
        department_name,
        department_head,
        department_location,
        total_employees
        )
        VALUES (%s,%s,%s,%s)
        """

        values = (
            data['department_name'],
            data['department_head'],
            data['department_location'],
            data['total_employees']
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({
            "message": "Department Added Successfully"
        })

    # ======================================================
    # GET ALL DEPARTMENTS
    # ======================================================

    cursor.execute("SELECT * FROM departments")

    departments = cursor.fetchall()

    return jsonify({
        "data": departments
    })


# ==========================================================
# UPDATE DEPARTMENT
# ==========================================================

@app.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):

    data = request.json

    query = """
    UPDATE departments
    SET
    department_name=%s,
    department_head=%s,
    department_location=%s,
    total_employees=%s
    WHERE id=%s
    """

    values = (
        data['department_name'],
        data['department_head'],
        data['department_location'],
        data['total_employees'],
        id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({
        "message": "Department Updated Successfully"
    })


# ==========================================================
# DELETE DEPARTMENT
# ==========================================================

@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):

    cursor.execute(
        "DELETE FROM departments WHERE id=%s",
        (id,)
    )

    db.commit()

    return jsonify({
        "message": "Department Deleted Successfully"
    })


# ==========================================================
# SALARY API
# ==========================================================

@app.route('/salary', methods=['GET', 'POST'])
def salary():

    # ======================================================
    # ADD SALARY
    # ======================================================

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO salaries
        (
        employee_id,
        basic_salary,
        bonus,
        deduction,
        net_salary
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (
            data['employee_id'],
            data['basic_salary'],
            data['bonus'],
            data['deduction'],
            data['net_salary']
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({
            "message": "Salary Added Successfully"
        })

    # ======================================================
    # GET ALL SALARIES
    # ======================================================

    cursor.execute("SELECT * FROM salaries")

    salaries = cursor.fetchall()

    return jsonify({
        "data": salaries
    })


# ==========================================================
# UPDATE SALARY
# ==========================================================

@app.route('/salary/<int:employee_id>', methods=['PUT'])
def update_salary(employee_id):

    data = request.json

    query = """
    UPDATE salaries
    SET
    basic_salary=%s,
    bonus=%s,
    deduction=%s,
    net_salary=%s
    WHERE employee_id=%s
    """

    values = (
        data['basic_salary'],
        data['bonus'],
        data['deduction'],
        data['net_salary'],
        employee_id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({
        "message": "Salary Updated Successfully"
    })


# ==========================================================
# DELETE SALARY
# ==========================================================

@app.route('/salary/<int:employee_id>', methods=['DELETE'])
def delete_salary(employee_id):

    cursor.execute(
        "DELETE FROM salaries WHERE employee_id=%s",
        (employee_id,)
    )

    db.commit()

    return jsonify({
        "message": "Salary Deleted Successfully"
    })


# ==========================================================
# ATTENDANCE API
# ==========================================================

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():

    # ======================================================
    # ADD ATTENDANCE
    # ======================================================

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO attendance
        (
        employee_id,
        attendance_date,
        check_in_time,
        check_out_time,
        status
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (
            data['employee_id'],
            data['attendance_date'],
            data['check_in_time'],
            data['check_out_time'],
            data['status']
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({
            "message": "Attendance Added Successfully"
        })

    # ======================================================
    # GET ALL ATTENDANCE
    # ======================================================

    cursor.execute("SELECT * FROM attendance")

    attendance = cursor.fetchall()

    return jsonify({
        "data": attendance
    })


# ==========================================================
# UPDATE ATTENDANCE
# ==========================================================

@app.route('/attendance/<int:employee_id>', methods=['PUT'])
def update_attendance(employee_id):

    data = request.json

    query = """
    UPDATE attendance
    SET
    attendance_date=%s,
    check_in_time=%s,
    check_out_time=%s,
    status=%s
    WHERE employee_id=%s
    """

    values = (
        data['attendance_date'],
        data['check_in_time'],
        data['check_out_time'],
        data['status'],
        employee_id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({
        "message": "Attendance Updated Successfully"
    })


# ==========================================================
# DELETE ATTENDANCE
# ==========================================================

@app.route('/attendance/<int:employee_id>', methods=['DELETE'])
def delete_attendance(employee_id):

    cursor.execute(
        "DELETE FROM attendance WHERE employee_id=%s",
        (employee_id,)
    )

    db.commit()

    return jsonify({
        "message": "Attendance Deleted Successfully"
    })


# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == '__main__':
    app.run(debug=True, port=5001)
