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
# LOGIN API
# ==========================================================

@app.route('/login', methods=['POST'])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

# ==========================================================
# EMPLOYEES API
# ==========================================================

@app.route('/employees', methods=['GET', 'POST'])
def employees():

    # ADD EMPLOYEE
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
            address,
            designation,
            joining_date,
            department_id
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data['id'],
            data['name'],
            data['age'],
            data['gender'],
            data['email'],
            data['phone'],
            data.get('address', ''),
            data['designation'],
            data.get('joining_date', ''),
            data['department_id']
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({"message": "Employee Added Successfully"})

    # GET ALL EMPLOYEES
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    return jsonify({"data": employees})


# ==========================================================
# GET SINGLE EMPLOYEE (IMPORTANT FIX)
# ==========================================================

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()

    if employee:
        return jsonify(employee)

    return jsonify({"error": "Employee not found"}), 404


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
        address=%s,
        designation=%s,
        joining_date=%s,
        department_id=%s
    WHERE id=%s
    """

    values = (
        data['name'],
        data['age'],
        data['gender'],
        data['email'],
        data['phone'],
        data.get('address', ''),
        data['designation'],
        data.get('joining_date', ''),
        data['department_id'],
        id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Employee Updated Successfully"})


# ==========================================================
# DELETE EMPLOYEE
# ==========================================================

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):

    cursor.execute("DELETE FROM attendance WHERE employee_id=%s", (id,))
    cursor.execute("DELETE FROM salaries WHERE employee_id=%s", (id,))
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))

    db.commit()

    return jsonify({"message": "Employee Deleted Successfully"})


# ==========================================================
# DEPARTMENTS API
# ==========================================================

@app.route('/departments', methods=['GET', 'POST'])
def departments():

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

        return jsonify({"message": "Department Added Successfully"})

    cursor.execute("SELECT * FROM departments")
    return jsonify({"data": cursor.fetchall()})


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

    return jsonify({"message": "Department Updated Successfully"})


# ==========================================================
# DELETE DEPARTMENT
# ==========================================================

@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):

    cursor.execute("DELETE FROM departments WHERE id=%s", (id,))
    db.commit()

    return jsonify({"message": "Department Deleted Successfully"})


# ==========================================================
# SALARY API
# ==========================================================

@app.route('/salary', methods=['GET', 'POST'])
def salary():

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO salaries
        (
            employee_id,
            basic_salary,
            bonus,
            deduction,
            net_salary,
            salary_month
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            data['employee_id'],
            data['basic_salary'],
            data['bonus'],
            data['deduction'],
            data['net_salary'],
            data.get('salary_month', '')
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({"message": "Salary Added Successfully"})

    cursor.execute("SELECT * FROM salaries")
    return jsonify({"data": cursor.fetchall()})


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
        net_salary=%s,
        salary_month=%s
    WHERE employee_id=%s
    """

    values = (
        data['basic_salary'],
        data['bonus'],
        data['deduction'],
        data['net_salary'],
        data.get('salary_month', ''),
        employee_id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Salary Updated Successfully"})


# ==========================================================
# DELETE SALARY
# ==========================================================

@app.route('/salary/<int:employee_id>', methods=['DELETE'])
def delete_salary(employee_id):

    cursor.execute("DELETE FROM salaries WHERE employee_id=%s", (employee_id,))
    db.commit()

    return jsonify({"message": "Salary Deleted Successfully"})


# ==========================================================
# ATTENDANCE API
# ==========================================================

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():

    if request.method == 'POST':

        data = request.json

        query = """
        INSERT INTO attendance
        (
            employee_id,
            attendance_date,
            check_in_time,
            check_out_time,
            status,
            leave_type,
            leave_reason,
            leave_days,
            total_present_days,
            total_absent_days,
            total_leave_days
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data['employee_id'],
            data['attendance_date'],
            data['check_in_time'],
            data['check_out_time'],
            data['status'],
            data.get('leave_type', ''),
            data.get('leave_reason', ''),
            data.get('leave_days', 0),
            data.get('total_present_days', 0),
            data.get('total_absent_days', 0),
            data.get('total_leave_days', 0)
        )

        cursor.execute(query, values)
        db.commit()

        return jsonify({"message": "Attendance Added Successfully"})

    cursor.execute("SELECT * FROM attendance")
    return jsonify({"data": cursor.fetchall()})


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
        status=%s,
        leave_type=%s,
        leave_reason=%s,
        leave_days=%s,
        total_present_days=%s,
        total_absent_days=%s,
        total_leave_days=%s
    WHERE employee_id=%s
    """

    values = (
        data['attendance_date'],
        data['check_in_time'],
        data['check_out_time'],
        data['status'],
        data.get('leave_type', ''),
        data.get('leave_reason', ''),
        data.get('leave_days', 0),
        data.get('total_present_days', 0),
        data.get('total_absent_days', 0),
        data.get('total_leave_days', 0),
        employee_id
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Attendance Updated Successfully"})


# ==========================================================
# DELETE ATTENDANCE
# ==========================================================

@app.route('/attendance/<int:employee_id>', methods=['DELETE'])
def delete_attendance(employee_id):

    cursor.execute("DELETE FROM attendance WHERE employee_id=%s", (employee_id,))
    db.commit()

    return jsonify({"message": "Attendance Deleted Successfully"})


# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == '__main__':
    app.run(debug=True, port=5001)
