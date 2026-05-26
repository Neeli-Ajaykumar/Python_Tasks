from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# ==========================================================
# FASTAPI SERVER URL
# ==========================================================

API_URL = "http://127.0.0.1:5001"

# ==========================================================
# DASHBOARD
# ==========================================================

@app.route('/')
def dashboard():
    return render_template("dashboard.html")


# ==========================================================
# EMPLOYEES PAGE
# ==========================================================

@app.route('/employees', methods=['GET', 'POST'])
def employees():

    if request.method == 'POST':

        data = {
            "id": int(request.form['id']),
            "name": request.form['name'],
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form.get('address', ''),
            "designation": request.form['designation'],
            "joining_date": request.form.get('joining_date', '')
        }

        requests.post(f"{API_URL}/employees", json=data)

        return render_template(
            "success.html",
            message="Employee Added Successfully",
            back_url="/employees"
        )

    return render_template("employees.html")


# ==========================================================
# UPDATE EMPLOYEE
# ==========================================================

@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):

    employee = requests.get(f"{API_URL}/employees/{id}").json()

    if request.method == 'POST':

        data = {
            "id": id,
            "name": request.form['name'],
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form.get('address', ''),
            "designation": request.form['designation'],
            "joining_date": request.form.get('joining_date', '')
        }

        requests.put(
            f"{API_URL}/employees/{id}",
            json=data
        )

        return redirect('/details')

    return render_template(
        "update_employee.html",
        employee=employee
    )


# ==========================================================
# DELETE EMPLOYEE
# ==========================================================

@app.route('/delete_employee/<int:id>')
def delete_employee(id):

    requests.delete(f"{API_URL}/employees/{id}")

    return redirect('/details')


# ==========================================================
# DEPARTMENTS PAGE
# ==========================================================

@app.route('/departments', methods=['GET', 'POST'])
def departments():

    if request.method == 'POST':

        data = {
            "department_name": request.form['department_name'],
            "department_head": request.form['department_head'],
            "department_location": request.form['department_location'],
            "total_employees": int(request.form['total_employees'])
        }

        requests.post(f"{API_URL}/departments", json=data)

        return render_template(
            "success.html",
            message="Department Added Successfully",
            back_url="/departments"
        )

    return render_template("departments.html")


# ==========================================================
# UPDATE DEPARTMENT
# ==========================================================

@app.route('/update_department/<int:id>', methods=['GET', 'POST'])
def update_department(id):

    departments = requests.get(f"{API_URL}/departments").json()["data"]

    department = None

    for dept in departments:
        if dept["id"] == id:
            department = dept
            break

    if request.method == 'POST':

        data = {
            "department_name": request.form['department_name'],
            "department_head": request.form['department_head'],
            "department_location": request.form['department_location'],
            "total_employees": int(request.form['total_employees'])
        }

        requests.put(
            f"{API_URL}/departments/{id}",
            json=data
        )

        return redirect('/details')

    return render_template(
        "update_department.html",
        department=department
    )


# ==========================================================
# DELETE DEPARTMENT
# ==========================================================

@app.route('/delete_department/<int:id>')
def delete_department(id):

    requests.delete(f"{API_URL}/departments/{id}")

    return redirect('/details')


# ==========================================================
# SALARY PAGE
# ==========================================================

@app.route('/salary', methods=['GET', 'POST'])
def salary():

    if request.method == 'POST':

        data = {
            "employee_id": int(request.form['employee_id']),
            "basic_salary": float(request.form['basic_salary']),
            "bonus": float(request.form['bonus']),
            "deduction": float(request.form['deduction']),
            "net_salary": float(request.form['net_salary']),
            "salary_month": request.form.get('salary_month', '')
        }

        requests.post(f"{API_URL}/salary", json=data)

        return render_template(
            "success.html",
            message="Salary Added Successfully",
            back_url="/salary"
        )

    return render_template("salary.html")


# ==========================================================
# UPDATE SALARY
# ==========================================================

@app.route('/update_salary/<int:employee_id>', methods=['GET', 'POST'])
def update_salary(employee_id):

    salaries = requests.get(f"{API_URL}/salary").json()["data"]

    salary = None

    for sal in salaries:
        if sal["employee_id"] == employee_id:
            salary = sal
            break

    if request.method == 'POST':

        data = {
            "employee_id": employee_id,
            "basic_salary": float(request.form['basic_salary']),
            "bonus": float(request.form['bonus']),
            "deduction": float(request.form['deduction']),
            "net_salary": float(request.form['net_salary']),
            "salary_month": request.form.get('salary_month', '')
        }

        requests.put(
            f"{API_URL}/salary/{employee_id}",
            json=data
        )

        return redirect('/details')

    return render_template(
        "update_salary.html",
        salary=salary
    )


# ==========================================================
# DELETE SALARY
# ==========================================================

@app.route('/delete_salary/<int:employee_id>')
def delete_salary(employee_id):

    requests.delete(f"{API_URL}/salary/{employee_id}")

    return redirect('/details')


# ==========================================================
# ATTENDANCE PAGE
# ==========================================================

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():

    if request.method == 'POST':

        data = {
            "employee_id": int(request.form['employee_id']),
            "attendance_date": request.form['attendance_date'],
            "check_in_time": request.form['check_in_time'],
            "check_out_time": request.form['check_out_time'],
            "status": request.form['status'],
            "leave_type": request.form.get('leave_type', ''),
            "leave_reason": request.form.get('leave_reason', ''),
            "leave_days": int(request.form.get('leave_days', 0)),
            "total_present_days": int(request.form.get('total_present_days', 0)),
            "total_absent_days": int(request.form.get('total_absent_days', 0)),
            "total_leave_days": int(request.form.get('total_leave_days', 0))
        }

        requests.post(f"{API_URL}/attendance", json=data)

        return render_template(
            "success.html",
            message="Attendance Added Successfully",
            back_url="/attendance"
        )

    return render_template("attendance.html")


# ==========================================================
# UPDATE ATTENDANCE
# ==========================================================

@app.route('/update_attendance/<int:employee_id>', methods=['GET', 'POST'])
def update_attendance(employee_id):

    attendance_data = requests.get(
        f"{API_URL}/attendance"
    ).json()["data"]

    attendance = None

    for att in attendance_data:
        if att["employee_id"] == employee_id:
            attendance = att
            break

    if request.method == 'POST':

        data = {
            "employee_id": employee_id,
            "attendance_date": request.form['attendance_date'],
            "check_in_time": request.form['check_in_time'],
            "check_out_time": request.form['check_out_time'],
            "status": request.form['status'],
            "leave_type": request.form.get('leave_type', ''),
            "leave_reason": request.form.get('leave_reason', ''),
            "leave_days": int(request.form.get('leave_days', 0)),
            "total_present_days": int(request.form.get('total_present_days', 0)),
            "total_absent_days": int(request.form.get('total_absent_days', 0)),
            "total_leave_days": int(request.form.get('total_leave_days', 0))
        }

        requests.put(
            f"{API_URL}/attendance/{employee_id}",
            json=data
        )

        return redirect('/details')

    return render_template(
        "update_attendance.html",
        attendance=attendance
    )


# ==========================================================
# DELETE ATTENDANCE
# ==========================================================

@app.route('/delete_attendance/<int:employee_id>')
def delete_attendance(employee_id):

    requests.delete(f"{API_URL}/attendance/{employee_id}")

    return redirect('/details')


# ==========================================================
# DETAILS PAGE
# ==========================================================

@app.route('/details')
def details():

    employees = requests.get(f"{API_URL}/employees").json()
    departments = requests.get(f"{API_URL}/departments").json()
    salaries = requests.get(f"{API_URL}/salary").json()
    attendance = requests.get(f"{API_URL}/attendance").json()

    return render_template(
        "details.html",
        employees=employees["data"],
        departments=departments["data"],
        salaries=salaries["data"],
        attendance=attendance["data"]
    )


# ==========================================================
# RUN FLASK
# ==========================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)
