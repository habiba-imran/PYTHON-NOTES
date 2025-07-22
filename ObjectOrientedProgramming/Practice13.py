# METHOD OVERRIDING 
class Animal:
    def make_sound(self):
        print("Some sound")
    def eat(self):
        print("Some food")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
    # how to still use parent method:
    def eat(self):
        super().eat()
# both parent and child class have same method
d1 = Dog()
d1.make_sound() # prints bark
d1.eat() # prints some food