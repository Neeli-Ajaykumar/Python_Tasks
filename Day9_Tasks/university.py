"""University Staff Management (Hierarchical Inheritance) 
A university has different staff types such as Professor, LabAssistant, and 
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
to manage and display their information."""

class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def display_staff(self):
        print("Name:", self.name)
        print("Staff ID:", self.staff_id)

class Professor(Staff):
    def __init__(self, name, staff_id, subject):
        super().__init__(name, staff_id)
        self.subject = subject

    def display_professor(self):
        self.display_staff()
        print("Subject:", self.subject)

class LabAssistant(Staff):
    def __init__(self, name, staff_id, lab):
        super().__init__(name, staff_id)
        self.lab = lab

    def display_lab_assistant(self):
        self.display_staff()
        print("Lab:", self.lab)

class Administrator(Staff):
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def display_administrator(self):
        self.display_staff()
        print("Department:", self.department)

p = Professor("Dr. kamal", 6939, "Computer Science")
l = LabAssistant("Anil", 6940, "Physics Lab")
a = Administrator("Sita", 6941, "Accounts")

print("Professor Details are:")
p.display_professor()

print("\nLab Assistant Details are:")
l.display_lab_assistant()

print("\nAdministrator Details are:")
a.display_administrator()
