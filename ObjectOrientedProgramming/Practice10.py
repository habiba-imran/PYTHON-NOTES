#-----dir method -----
x = [1, 2, 3] # in python every data type is an object
print(dir(x)) # prints all method that can be associated with x 
# prints ['__add__', '__class__', '__class_getitem__', '__contains__', ...

print(x.__add__) # tells whether is it a method or not 
# prints <method-wrapper '__add__' of list object at 0x00000191981760C0>

# -----dict method-----
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 21
    def show(self):
        print(self.name)
p = Person("habiba")
print(p.__dict__) # prints all the attributes/variables of the class, not the functions
# prints {'name': 'habiba', 'age': 21}

# -----help method-----
print(help(Person)) # # prints everything about class Person
print(help(str)) # # prints everything about string
print(help(int)) # prints everything about int



