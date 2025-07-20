# Instance variables vs class variables
class Employee:
    # class variable
    company_name = "Google" # given to all instances/objects
    no_of_employees = 0
    def __init__(self, name):
        # instance variable
        self.name = name
        self.raise_amount = 0.02
        Employee.no_of_employees += 1 # when an obj is made , no of employees increased
        # but you need to make it without self (used for object), so use class name
    def showDetails(self):
        print(f"The name is: {self.name} and works in {self.company_name} with raise amount: {self.raise_amount}")
a = Employee("habiba") # prints The name is: habiba
a.showDetails()
# or Employee.showDetails(a) # prints The name is: habiba

b = Employee("hunain")
b.showDetails()
b.company_name = "RailwayHospital"
b.showDetails() 
# IMPORTANT: if a variable is called using an object, instance variables are checked
# if an instance variable is present, okay, otherwise, class variable is choosen
print(Employee.no_of_employees)


