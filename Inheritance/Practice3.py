# Multilevel Inheritance in Python : hierarchy of classes
# when a derived class inherits from another derived class
# Each child class inherits all accessible features of its parent and grandparent.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Student ID: {self.student_id}")

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def display_info(self):
        Person.display_info(self)
        Student.display_info(self)
        print(f"Thesis Title: {self.thesis_title}")

grad = GraduateStudent("Habiba", 22, "BSCS2025", "AI in Healthcare")
grad.display_info()       # from Person

