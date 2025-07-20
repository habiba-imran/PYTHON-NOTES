# ACCESS MODIFIERS IN PYTHON
# there is no concept of public, private and protected in python
# we use it as convention
# we already did
# private members of a class can be accessed indireclty
print("Hello")
class Employee:
    def __init__(self):
        self.__salary = 45000
        self._name = "habiba"
a = Employee()
print(a._name) # protected member : prints habiba
# print(a.__salary) # gives error # private member can't be accessed directly
# but can be accessed indirectly by:
print(a._Employee__salary) # prints 45000


