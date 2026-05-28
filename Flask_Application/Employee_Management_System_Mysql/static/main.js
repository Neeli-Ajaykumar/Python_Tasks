// ==========================================================
// EMPLOYEE MANAGEMENT SYSTEM - MAIN JS (FIXED VERSION)
// ==========================================================

console.log("Employee Management System Loaded");

// ==========================================================
// PAGE LOAD
// ==========================================================

window.addEventListener("load", function () {

    console.log("Page Loaded Successfully");

    calculateSalary();
    calculateAttendanceDays();
    updateDateTime();

    startClock();
});

// ==========================================================
// SAFE MESSAGE ALERT
// ==========================================================

function showMessage(message) {
    alert(message);
}

// ==========================================================
// CONFIRM DELETE
// ==========================================================

function confirmDelete() {
    return confirm("Are you sure you want to delete this record?");
}

// ==========================================================
// SALARY CALCULATION (REAL TIME READY)
// ==========================================================

function calculateSalary() {

    let basicSalary = parseFloat(document.getElementById("basic_salary")?.value) || 0;
    let bonus = parseFloat(document.getElementById("bonus")?.value) || 0;
    let deduction = parseFloat(document.getElementById("deduction")?.value) || 0;

    let netSalary = basicSalary + bonus - deduction;

    let netField = document.getElementById("net_salary");

    if (netField) {
        netField.value = netSalary;
    }
}

// ==========================================================
// ATTENDANCE CALCULATION (FIXED LOGIC)
// ==========================================================

function calculateAttendanceDays() {

    let status = document.getElementById("status")?.value || "";
    let leaveDays = parseInt(document.getElementById("leave_days")?.value) || 0;

    let totalWorkingDays = 30;

    let presentField = document.getElementById("total_present_days");
    let absentField = document.getElementById("total_absent_days");
    let leaveField = document.getElementById("total_leave_days");

    if (!presentField || !absentField || !leaveField) return;

    let present = 0;
    let absent = 0;
    let leave = 0;

    if (status === "present") {

        leave = leaveDays;
        absent = 0;
        present = totalWorkingDays - leaveDays;
    }

    else if (status === "absent") {

        absent = leaveDays || 1;
        present = totalWorkingDays - absent;
        leave = 0;
    }

    else if (status === "leave") {

        leave = leaveDays || 1;
        present = totalWorkingDays - leave;
        absent = 0;
    }

    presentField.value = present;
    absentField.value = absent;
    leaveField.value = leave;
}

// ==========================================================
// EMPLOYEE FORM VALIDATION
// ==========================================================

function validateEmployeeForm() {

    let employeeId = document.getElementById("id")?.value;
    let departmentId = document.getElementById("department_id")?.value;
    let name = document.getElementById("name")?.value;
    let email = document.getElementById("email")?.value;
    let phone = document.getElementById("phone")?.value;

    if (!employeeId) return alert("Employee ID is required"), false;
    if (!departmentId) return alert("Department ID is required"), false;
    if (!name) return alert("Employee Name is required"), false;
    if (!email) return alert("Email is required"), false;
    if (!phone) return alert("Phone Number is required"), false;

    return true;
}

// ==========================================================
// DEPARTMENT FORM VALIDATION
// ==========================================================

function validateDepartmentForm() {

    let departmentName = document.getElementById("department_name")?.value;
    let departmentHead = document.getElementById("department_head")?.value;

    if (!departmentName) return alert("Department Name is required"), false;
    if (!departmentHead) return alert("Department Head is required"), false;

    return true;
}

// ==========================================================
// ATTENDANCE FORM VALIDATION
// ==========================================================

function validateAttendanceForm() {

    let employeeId = document.getElementById("employee_id")?.value;
    let status = document.getElementById("status")?.value;

    if (!employeeId) return alert("Employee ID is required"), false;
    if (!status) return alert("Attendance Status is required"), false;

    return true;
}

// ==========================================================
// SALARY FORM VALIDATION
// ==========================================================

function validateSalaryForm() {

    let employeeId = document.getElementById("employee_id")?.value;
    let basicSalary = document.getElementById("basic_salary")?.value;

    if (!employeeId) return alert("Employee ID is required"), false;
    if (!basicSalary) return alert("Basic Salary is required"), false;

    return true;
}

// ==========================================================
// CARD CLICK EFFECT (FIXED RESET)
// ==========================================================

document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("click", function () {

        card.style.transform = "scale(1.03)";

        setTimeout(() => {
            card.style.transform = "scale(1)";
        }, 200);
    });
});

// ==========================================================
// LIVE DATE TIME (SAFE START)
// ==========================================================

function updateDateTime() {

    let el = document.getElementById("datetime");

    if (el) {
        el.innerHTML = new Date().toLocaleString();
    }
}

function startClock() {

    if (document.getElementById("datetime")) {
        setInterval(updateDateTime, 1000);
    }
}

// ==========================================================
// SEARCH TABLE (SAFE VERSION)
// ==========================================================

function searchTable() {

    let input = document.getElementById("searchInput");
    if (!input) return;

    let filter = input.value.toUpperCase();
    let table = document.getElementById("employeeTable");
    if (!table) return;

    let tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {

        let td = tr[i].querySelector("td");

        if (td) {

            let txtValue = td.textContent || td.innerText;

            tr[i].style.display =
                txtValue.toUpperCase().indexOf(filter) > -1
                    ? ""
                    : "none";
        }
    }
}

// ==========================================================
// SUCCESS MESSAGE
// ==========================================================

function formSuccess() {
    alert("Form Submitted Successfully");
}

// ==========================================================
// PASSWORD TOGGLE (SAFE VERSION)
// ==========================================================

function togglePassword() {

    let password = document.getElementById("password");
    let eye = document.getElementById("eye");

    if (!password || !eye) {
        console.log("Elements not found");
        return;
    }

    if (password.type === "password") {

        password.type = "text";

        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");

    } else {

        password.type = "password";

        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");
    }
}

// ==========================================================
// REAL-TIME INPUT LISTENERS (IMPORTANT FIX)
// ==========================================================

document.addEventListener("input", function (e) {

    if (
        e.target.id === "basic_salary" ||
        e.target.id === "bonus" ||
        e.target.id === "deduction"
    ) {
        calculateSalary();
    }

    if (
        e.target.id === "status" ||
        e.target.id === "leave_days"
    ) {
        calculateAttendanceDays();
    }
});