# Multiple Inheritance in Python
class Father:
    def __init__(self, profession):
        self.profession = profession
    def show(self):
        print(f"Father's sprofession: {self.profession}")
class Mother:
    def __init__(self, age):
        self.age = age
    def show(self):
        print(f"Mother's age: {self.age}")
class Child(Father, Mother):
    def __init__(self, name, profession, age):
        Father.__init__(self, profession)
        Mother.__init__(self, age) # super not used here
        self.name = name
    def show(self):
        print(f"Child's name: {self.name}")
        Father.show(self)
        Mother.show(self)
c1 = Child("ali", "Doctor", "21")
c1.show()
print(Child.mro())
# [<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
# means every function will be first searched in child -> father -> mother
# due to order given while initializing Child class


