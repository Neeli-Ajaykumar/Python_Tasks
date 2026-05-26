// ==========================================================
// EMPLOYEE MANAGEMENT SYSTEM - MAIN JS
// ==========================================================

console.log("Employee Management System Loaded");

// ==========================================================
// PAGE LOADED MESSAGE
// ==========================================================

window.onload = function () {

    console.log("All Pages Loaded Successfully");
};

// ==========================================================
// SHOW ALERT MESSAGE
// ==========================================================

function showMessage(message) {

    alert(message);
}

// ==========================================================
// CONFIRM DELETE
// ==========================================================

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this record?"
    );
}

// ==========================================================
// AUTO CALCULATE NET SALARY
// ==========================================================

function calculateSalary() {

    let basicSalary =
        parseFloat(
            document.getElementById("basic_salary")?.value
        ) || 0;

    let bonus =
        parseFloat(
            document.getElementById("bonus")?.value
        ) || 0;

    let deduction =
        parseFloat(
            document.getElementById("deduction")?.value
        ) || 0;

    let netSalary =
        basicSalary + bonus - deduction;

    let netSalaryField =
        document.getElementById("net_salary");

    if (netSalaryField) {

        netSalaryField.value = netSalary;
    }
}

// ==========================================================
// EMPLOYEE FORM VALIDATION
// ==========================================================

function validateEmployeeForm() {

    let name =
        document.getElementById("name")?.value;

    let email =
        document.getElementById("email")?.value;

    let phone =
        document.getElementById("phone")?.value;

    if (name === "") {

        alert("Employee Name is required");

        return false;
    }

    if (email === "") {

        alert("Email is required");

        return false;
    }

    if (phone === "") {

        alert("Phone Number is required");

        return false;
    }

    return true;
}

// ==========================================================
// DEPARTMENT FORM VALIDATION
// ==========================================================

function validateDepartmentForm() {

    let departmentName =
        document.getElementById("department_name")?.value;

    let departmentHead =
        document.getElementById("department_head")?.value;

    if (departmentName === "") {

        alert("Department Name is required");

        return false;
    }

    if (departmentHead === "") {

        alert("Department Head is required");

        return false;
    }

    return true;
}

// ==========================================================
// ATTENDANCE FORM VALIDATION
// ==========================================================

function validateAttendanceForm() {

    let employeeId =
        document.getElementById("employee_id")?.value;

    let status =
        document.getElementById("status")?.value;

    if (employeeId === "") {

        alert("Employee ID is required");

        return false;
    }

    if (status === "") {

        alert("Attendance Status is required");

        return false;
    }

    return true;
}

// ==========================================================
// SALARY FORM VALIDATION
// ==========================================================

function validateSalaryForm() {

    let employeeId =
        document.getElementById("employee_id")?.value;

    let basicSalary =
        document.getElementById("basic_salary")?.value;

    if (employeeId === "") {

        alert("Employee ID is required");

        return false;
    }

    if (basicSalary === "") {

        alert("Basic Salary is required");

        return false;
    }

    return true;
}

// ==========================================================
// HIGHLIGHT CARDS ON CLICK
// ==========================================================

let cards = document.querySelectorAll(".card");

cards.forEach(function(card) {

    card.addEventListener("click", function() {

        card.style.transform = "scale(1.03)";
    });
});

// ==========================================================
// LIVE DATE & TIME
// ==========================================================

function updateDateTime() {

    let dateTimeElement =
        document.getElementById("datetime");

    if (dateTimeElement) {

        let now = new Date();

        dateTimeElement.innerHTML =
            now.toLocaleString();
    }
}

setInterval(updateDateTime, 1000);

// ==========================================================
// SEARCH FILTER FOR DETAILS PAGE
// ==========================================================

function searchTable() {

    let input =
        document.getElementById("searchInput");

    if (!input) return;

    let filter =
        input.value.toUpperCase();

    let table =
        document.getElementById("employeeTable");

    if (!table) return;

    let tr =
        table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {

        let td =
            tr[i].getElementsByTagName("td")[0];

        if (td) {

            let txtValue =
                td.textContent || td.innerText;

            if (
                txtValue.toUpperCase().indexOf(filter)
                > -1
            ) {

                tr[i].style.display = "";
            }

            else {

                tr[i].style.display = "none";
            }
        }
    }
}

// ==========================================================
// SUCCESS POPUP AFTER FORM SUBMIT
// ==========================================================

function formSuccess() {

    alert("Form Submitted Successfully");
}