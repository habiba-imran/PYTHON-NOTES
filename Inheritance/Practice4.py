# Hybrid Inheritance
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name: {self.name}")
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id
    def show_employee(self):
        print(f"Employee ID: {self.emp_id}")
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def show_student(self):
        print(f"Student ID: {self.student_id}")
class WorkingStudent(Employee, Student):
    def __init__(self, name, emp_id, student_id, hours):
        # Explicitly call both parent initializers using class names
        Employee.__init__(self, name, emp_id)
        Student.__init__(self, name, student_id)
        self.hours = hours
    def show_details(self):
        self.show()
        self.show_employee()
        self.show_student()
        print(f"Working Hours/Week: {self.hours}")
ws = WorkingStudent("Habiba", "E102", "S987", 20)
ws.show_details()



