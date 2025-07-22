# split function:
x = "Code-with-Harry"
print(x.split("-")) # prints ['Code', 'with', 'Harry']
print(x.split("-")[0]) # prints code
print(x.split("-")[2]) # prints Harry
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal
str = "Habiba-120000"
a = Employee(str.split("-")[0],str.split("-")[1])
# Class Methods as Alternative Constructors
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @ classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age) # return statement should be there to return constructor parameters
p1 = Person("Habiba", 21) # constructor: calls __init__
p2 = Person.from_birth_year("Habiba", 2004) # alternative constructor: calls class method
print(p1.name, p1.age)  # Habiba 21
print(p2.name, p2.age)  # Habiba 21



