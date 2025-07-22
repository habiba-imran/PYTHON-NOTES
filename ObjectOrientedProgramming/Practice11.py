# SUPER KEYWORD IN PYTHON
# used to call parent constructor
class Parent:
    def __init__(self):
        print("Parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()  # Call Parent constructor
        print("Child constructor")
c = Child() # printsParent constructor Child constructor

# used to call parent method
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")
b = B()
b.greet() # prints Hello from A Hello from B
# b.greet() will search for greet method in B class(since b is obj of B)
# if found will run that, if not found, will search in parent class

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
a = Employee("hunain", 51)
b = Programmer("habiba", "48", "C++")
print(b.name)

