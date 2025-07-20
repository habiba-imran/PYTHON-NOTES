# ACCESS MODIFIERS IN PYTHON
class Employee:
    def __init__(self, n, id, cgpa):
        self.name = n  # public
        self.id = id
        self._CGPA = cgpa
    def show(self):
        print(f"Employee {self.name} has ID: {self.id} and CGPA: {self._CGPA}")

class Programmer(Employee):
    def __init__(self, n, id, cgpa, lang, sem):
        super().__init__(n, id, cgpa)  # call parent constructor
        self.lang = lang
        self.sem = sem
    def show_info(self):
        print(f"Programmer {self.name} (ID: {self.id}) is in {self.sem} semester,", end = " ")
        print("and knows {self.lang} and CGPA: {self._CGPA}.)")
a = Programmer("habiba", 48, 3.84, "C++", "3rd")
print(a._CGPA) # protected member, can be accessed directly but not recommended
a.show_info()
a.show()

# Creating an Employee object
b = Employee("Imran", 101, 3.84)
b.show()












