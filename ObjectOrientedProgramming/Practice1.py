# The programmng done up till is procedural programming, using functions
class Person:
    name = "Habiba"
    age = 21
    CGPA = 3.84
    def info(self): # we add self to evry function which has no parameters
        '''self is reference to current instance of class,'''
        print(f"{self.name} has a CGPA of {self.CGPA}")
# self: object for which method is called, e.g., for a info() was called, self = a
a = Person() # a is an object
print(a.name) # prints habiba
a.info() # prints habiba has a CGPA of 3.84
a.name = "hunain"
a.info() # prints hunainn has a CGPA of 3.84





