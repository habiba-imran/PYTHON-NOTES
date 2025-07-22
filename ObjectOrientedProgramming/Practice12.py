# DUNDER METHODS: start and end with __
# used to give more information about the object
class Employee:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return (f"The name of employee is {self.name} ")
    def __call__(self):
        print("The object is callable")
a = Employee("habiba")
print(a) # prints: the name of employee is habiba
print(str(a)) # prints: the name of employee is habiba
print(len(a)) # prints 6
a() # __call__method makes the object callable
# explore oter methods yourself

