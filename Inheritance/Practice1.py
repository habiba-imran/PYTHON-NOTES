# Single Inheritance in Python
# a class (child/derived class) inherits from one parent (base) class.
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")
# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")
# Create object of child class
d = Dog()
d.speak()  # inherited from Animal
d.bark()   # defined in Dog
