# Constructors help to make objects by passing arguments
class greetings:
    def __init__(self): # default constructor
        print("hey, how are you")
a = greetings() # whenever an objects of class is made, constructor is called

class Person:
    def __init__(self, name, occ): # Parameterized constructor
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a/an {self.occ}")
a = Person("habiba", "AI engineer")
b = Person("hunain", "doctor")
a.info()
b.info()