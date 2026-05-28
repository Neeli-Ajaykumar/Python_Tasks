from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)
app.secret_key = "ems_secret"

API_URL = "http://127.0.0.1:5001"


# ==========================================================
# LOGIN
# ==========================================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        data = {
            "username": request.form['username'],
            "password": request.form['password']
        }

        try:
            res = requests.post(f"{API_URL}/login", json=data)
            result = res.json()
        except:
            return render_template("login.html", error="Server error")

        if result.get("status") == "success":
            session["user"] = data["username"]
            return redirect("/")

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# ==========================================================
# LOGOUT
# ==========================================================

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")


# ==========================================================
# AUTH CHECK
# ==========================================================

def login_required(func):
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


# ==========================================================
# DASHBOARD
# ==========================================================

@app.route('/')
@login_required
def dashboard():
    return render_template("dashboard.html")


# ==========================================================
# EMPLOYEES
# ==========================================================

@app.route('/employees', methods=['GET', 'POST'])
@login_required
def employees():

    departments = requests.get(f"{API_URL}/departments").json()["data"]

    if request.method == 'POST':

        data = {
            "id": int(request.form['id']),
            "department_id": int(request.form['department_id']),  # FIXED
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

    return render_template("employees.html", departments=departments)


# ==========================================================
# UPDATE EMPLOYEE
# ==========================================================

@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
@login_required
def update_employee(id):

    # GET employee data
    res = requests.get(f"{API_URL}/employees/{id}")

    try:
        employee = res.json()
    except:
        return "Error: Cannot fetch employee data from API"

    if request.method == 'POST':

        data = {
            "name": request.form['name'],
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form.get('address', ''),
            "designation": request.form['designation'],
            "joining_date": request.form.get('joining_date', ''),
            "department_id": int(request.form['department_id'])
        }

        requests.put(f"{API_URL}/employees/{id}", json=data)

        return redirect('/details')

    return render_template("update_employee.html", employee=employee)


# ==========================================================
# DELETE EMPLOYEE
# ==========================================================

@app.route('/delete_employee/<int:id>')
@login_required
def delete_employee(id):

    requests.delete(f"{API_URL}/employees/{id}")

    return redirect('/details')

# ==========================================================
# DEPARTMENTS PAGE
# ==========================================================

@app.route('/departments', methods=['GET', 'POST'])
@login_required
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
@login_required
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

        requests.put(f"{API_URL}/departments/{id}", json=data)

        return redirect('/details')

    return render_template("update_department.html", department=department)


# ==========================================================
# DELETE DEPARTMENT
# ==========================================================

@app.route('/delete_department/<int:id>')
@login_required
def delete_department(id):

    requests.delete(f"{API_URL}/departments/{id}")

    return redirect('/details')


# ==========================================================
# SALARY PAGE
# ==========================================================

@app.route('/salary', methods=['GET', 'POST'])
@login_required
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
@login_required
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

        requests.put(f"{API_URL}/salary/{employee_id}", json=data)

        return redirect('/details')

    return render_template("update_salary.html", salary=salary)


# ==========================================================
# DELETE SALARY
# ==========================================================

@app.route('/delete_salary/<int:employee_id>')
@login_required
def delete_salary(employee_id):

    requests.delete(f"{API_URL}/salary/{employee_id}")

    return redirect('/details')


# ==========================================================
# ATTENDANCE PAGE
# ==========================================================

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():

    if request.method == 'POST':

        # SAFE INT CONVERTER (prevents empty string crash)
        def safe_int(value):
            return int(value) if value not in [None, ""] else 0

        data = {
            "employee_id": int(request.form['employee_id']),
            "attendance_date": request.form['attendance_date'],
            "check_in_time": request.form['check_in_time'],
            "check_out_time": request.form['check_out_time'],
            "status": request.form['status'],

            "leave_type": request.form.get('leave_type', ''),
            "leave_reason": request.form.get('leave_reason', ''),

            # FIXED LINES (NO CRASH)
            "leave_days": safe_int(request.form.get('leave_days')),
            "total_present_days": safe_int(request.form.get('total_present_days')),
            "total_absent_days": safe_int(request.form.get('total_absent_days')),
            "total_leave_days": safe_int(request.form.get('total_leave_days'))
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
@login_required
def update_attendance(employee_id):

    attendance_data = requests.get(f"{API_URL}/attendance").json()["data"]

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

        requests.put(f"{API_URL}/attendance/{employee_id}", json=data)

        return redirect('/details')

    return render_template("update_attendance.html", attendance=attendance)


# ==========================================================
# DELETE ATTENDANCE
# ==========================================================

@app.route('/delete_attendance/<int:employee_id>')
@login_required
def delete_attendance(employee_id):

    requests.delete(f"{API_URL}/attendance/{employee_id}")

    return redirect('/details')


# ==========================================================
# DETAILS PAGE
# ==========================================================

@app.route('/details')
@login_required
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
